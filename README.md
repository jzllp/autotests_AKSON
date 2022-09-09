# Akson website design test 
Contains automated tests to check the functionality of the site.
.Autotests use PyTest, Selenium and PageObjec tools.

How to run:
1) Autotests are located in the tests folder.
2) Download driver for Chrome:
https://chromedriver.chromium.org/downloads
3) Install all required python packages library
4) Run in terminal with line:
python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/"enter the name of the file with autotests".py
