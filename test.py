from selenium import webdriver

driver = webdriver.Chrome('H:\python\Dlib_test\chromedriver.exe')

url = "https://www.giantcyclingworld.com/travel/travel.php?f%5Blevel%5D%5B%5D=10000569&f%5Bprice%5D%5B%5D=3000&f%5Bprice%5D%5B%5D=300000&f%5Bcat%5D=10000579&f%5BbeginDate%5D%5B%5D=1660406400&f%5BbeginDate%5D%5B%5D=1660924800&t=1&o=bgd"
driver.get(url)
num = driver.find_element_by_css_selector('.number').text
print(num)
driver.close()
