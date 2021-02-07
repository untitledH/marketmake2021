# Leverager

This project aim to allow user create leveraged position in AAVE v2 via flashloan

## How it works

1. User approve the leverage asset to Leverager contract
2. User delegate credit to Leverager contract
3. User call Leverager contract 
4. Leverager draw a flashloan onbehalf of user to buy the leverage asset
5. Leverager deposit the leverage asset onbehalf of user 

## Example

> tests/test_leverager.py::test_weth_usdc_leverager RUNNING

> Leveraging 10 ether in WETH to 20 ether in WETH by borrowing against USDC

> 20.000000 AETH, 15823 VDUSDC

> tests/test_leverager.py::test_weth_usdc_leverager PASSED


## Todo

1. Front-end UI
2. Test case for other token
3. Wrapper for ETH
4. 1inch integration
