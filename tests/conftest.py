import pytest
from brownie import interface

@pytest.fixture(autouse=True)
def setup(fn_isolation):
    """
    Isolation setup fixture.

    This ensures that each test runs against the same base environment.
    """
    pass


@pytest.fixture(scope="module")
def aave_lending_pool_v2(Contract):
    """
    Yield a `Contract` object for the Aave lending pool address provider.
    """
    yield interface.ILendingPoolV2("0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5")


@pytest.fixture(scope="module")
def leverager(Leverager, aave_lending_pool_v2, accounts):
    """
    Deploy a `Flashloan` contract from `web3.eth.accounts[0]` and yields the
    generated object.
    """
    yield Leverager.deploy(aave_lending_pool_v2, {"from": accounts[0]})


# Mainnet reserve token fixtures - addresses are taken from
# https://docs.aave.com/developers/v/1.0/deployed-contracts/deployed-contract-instances#reserves-assets


@pytest.fixture(scope="module")
def WETH(Contract):
    yield interface.ERC20("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")


@pytest.fixture(scope="module")
def AWETH(Contract):
    yield interface.IAToken("0x030bA81f1c18d280636F32af80b9AAd02Cf0854e")


@pytest.fixture(scope="module")
def ETH():
    yield "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"


@pytest.fixture(scope="module")
def DAI(Contract):
    yield interface.ERC20("0x6B175474E89094C44Da98b954EedeAC495271d0F")


@pytest.fixture(scope="module")
def USDC(Contract):
    yield interface.ERC20("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")


@pytest.fixture(scope="module")
def VDUSDC(Contract):
    yield interface.IVariableDebtToken("0x619beb58998eD2278e08620f97007e1116D5D25b")


@pytest.fixture(scope="module")
def SUSD(Contract):
    yield interface.ERC20("0x57Ab1ec28D129707052df4dF418D58a2D46d5f51")


@pytest.fixture(scope="module")
def TUSD(Contract):
    yield interface.ERC20("0x0000000000085d4780B73119b644AE5ecd22b376")


@pytest.fixture(scope="module")
def USDT(Contract):
    yield interface.ERC20("0xdAC17F958D2ee523a2206206994597C13D831ec7")


@pytest.fixture(scope="module")
def BUSD(Contract):
    yield interface.ERC20("0x4Fabb145d64652a948d72533023f6E7A623C7C53")


@pytest.fixture(scope="module")
def BAT(Contract):
    yield interface.ERC20("0x0D8775F648430679A709E98d2b0Cb6250d2887EF")


@pytest.fixture(scope="module")
def KNC(Contract):
    yield interface.ERC20("0xdd974D5C2e2928deA5F71b9825b8b646686BD200")


@pytest.fixture(scope="module")
def LEND(Contract):
    yield interface.ERC20("0x80fB784B7eD66730e8b1DBd9820aFD29931aab03")


@pytest.fixture(scope="module")
def LINK(Contract):
    yield interface.ERC20("0x514910771AF9Ca656af840dff83E8264EcF986CA")


@pytest.fixture(scope="module")
def MANA(Contract):
    yield interface.ERC20("0x0F5D2fB29fb7d3CFeE444a200298f468908cC942")


@pytest.fixture(scope="module")
def MKR(Contract):
    yield interface.ERC20("0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2")


@pytest.fixture(scope="module")
def REP(Contract):
    yield interface.ERC20("0x1985365e9f78359a9B6AD760e32412f4a445E862")


@pytest.fixture(scope="module")
def SNX(Contract):
    yield interface.ERC20("0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F")


@pytest.fixture(scope="module")
def WBTC(Contract):
    yield interface.ERC20("0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599")


@pytest.fixture(scope="module")
def ZRX(Contract):
    yield interface.ERC20("0xE41d2489571d322189246DaFA5ebDe1F4699F498")
