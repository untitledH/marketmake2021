def test_weth_usdc_leverager(accounts, WETH, leverager, USDC, VDUSDC, AWETH):
    """
    Borrows USDC to create WETH leverage
    """

    deposit = "10 ether"
    leveraged = "20 ether"

    print('Leveraging %s in WETH to %s in WETH by borrowing against USDC' % (deposit, leveraged))

    accounts[0].transfer(WETH, deposit)

    WETH.approve(leverager, deposit, {"from": accounts[0]})
    VDUSDC.approveDelegation(leverager, 115792089237316195423570985008687907853269984665640564039457584007913129639935, {"from": accounts[0]})

    leverager.doleverage(WETH, deposit, leveraged, USDC, {"from": accounts[0]})

    print('\033[92m%f AETH, %d VDUSDC\033[0m' % (AWETH.balanceOf(accounts[0])/1e18, VDUSDC.balanceOf(accounts[0])/1e6))