pragma solidity ^0.6.6;

import "./aave/FlashLoanReceiverBaseV2.sol";
import "../../interfaces/v2/ILendingPoolAddressesProviderV2.sol";
import "../../interfaces/v2/ILendingPoolV2.sol";
import "../../interfaces/IUniswap.sol";

contract Leverager is FlashLoanReceiverBaseV2, Withdrawable {

    using SafeMath for uint256;

    address public uniswap = address(0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D);

    constructor(address _addressProvider) FlashLoanReceiverBaseV2(_addressProvider) public {}

    /**
     * @dev This function must be called only be the LENDING_POOL and takes care of repaying
     * active debt positions, migrating collateral and incurring new V2 debt token debt.
     *
     * @param assets The array of flash loaned assets used to repay debts.
     * @param amounts The array of flash loaned asset amounts used to repay debts.
     * @param premiums The array of premiums incurred as additional debts.
     * @param initiator The address that initiated the flash loan, unused.
     * @param params The byte array containing, in this case, the arrays of aTokens and aTokenAmounts.
     */
    function executeOperation(
        address[] calldata assets,
        uint256[] calldata amounts,
        uint256[] calldata premiums,
        address initiator,
        bytes calldata params
    )
        external
        override
        returns (bool)
    {

        //
        // This contract now has the funds requested.
        // Your logic goes here.
        //
        
        // At the end of your logic above, this contract owes
        // the flashloaned amounts + premiums.
        // Therefore ensure your contract has enough to repay
        // these amounts.
        
        (address _caller, address _asset) = abi.decode(params, (address, address));

        // Approve the LendingPool contract allowance to *pull* the owed amount
        for (uint i = 0; i < assets.length; i++) {
            // uint amountOwing = amounts[i].add(premiums[i]);
            // IERC20(assets[i]).approve(address(LENDING_POOL), amountOwing);

            address[] memory path = new address[](2);
            path[0] = address(assets[i]);
            path[1] = address(_asset);
            IERC20(assets[i]).approve(uniswap, amounts[i]);
            uint out = IUniswapV2Router02(uniswap).swapExactTokensForTokens(amounts[i], 0, path, address(this), uint(-1))[1];
            IERC20(_asset).approve(address(LENDING_POOL), out);
            LENDING_POOL.deposit(_asset, out, _caller, 0);

        }
        
        return true;
    }

    // function _flashloan(address[] memory assets, uint256[] memory amounts) internal {
    //     address receiverAddress = address(this);

    //     address onBehalfOf = address(this);
    //     bytes memory params = "";
    //     uint16 referralCode = 0;

    //     uint256[] memory modes = new uint256[](assets.length);

    //     // 0 = no debt (flash), 1 = stable, 2 = variable
    //     for (uint256 i = 0; i < assets.length; i++) {
    //         modes[i] = 0;
    //     }

    //     LENDING_POOL.flashLoan(
    //         receiverAddress,
    //         assets,
    //         amounts,
    //         modes,
    //         onBehalfOf,
    //         params,
    //         referralCode
    //     );
    // }

    // /*
    //  *  Flash multiple assets 
    //  */
    // function flashloan(address[] memory assets, uint256[] memory amounts) public onlyOwner {
    //     _flashloan(assets, amounts);
    // }

    /*
     *  Leverge to `amtout` of `_asset` with `amtin` of `_asset` using `_debtasset` as debt
     */
    function doleverage(address _asset, uint amtin, uint amtout, address _debtasset) public {

        address[] memory path = new address[](2);
        path[0] = address(_debtasset);
        path[1] = address(_asset); 

        // bytes memory data = _asset;
        uint amount = IUniswapV2Router02(uniswap).getAmountsIn(amtout.sub(amtin), path)[0];

        IERC20(_asset).transferFrom(msg.sender, address(this), amtin);
        IERC20(_asset).approve(address(LENDING_POOL), amtin);
        LENDING_POOL.deposit(_asset, amtin, msg.sender, 0);

        address[] memory assets = new address[](1);
        assets[0] = _debtasset;

        uint256[] memory amounts = new uint256[](1);
        amounts[0] = amount;

        address receiverAddress = address(this);
        address onBehalfOf = msg.sender;
        bytes memory params = abi.encode(msg.sender, _asset);

        uint256[] memory modes = new uint256[](assets.length);

        // 0 = no debt (flash), 1 = stable, 2 = variable
        for (uint256 i = 0; i < assets.length; i++) {
            modes[i] = 2;
        }

        LENDING_POOL.flashLoan(
            receiverAddress,
            assets,
            amounts,
            modes,
            onBehalfOf,
            params,
            0
        );

    }
}