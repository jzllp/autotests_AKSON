# Akson website design test 
Contains automated tests to check the functionality of the site https://akson.ru/.

Autotests use PyTest, Selenium and PageObjec tools.

Tests are designed for educational purposes, they test only part of the functionality, and, of course, can be improved.

How to run:
1) Autotests are located in the tests folder.
2) Download driver for Chrome:
https://chromedriver.chromium.org/downloads
3) Install all required python packages library
4) Run in terminal with line:
python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/"enter the name of the file with autotests".py
