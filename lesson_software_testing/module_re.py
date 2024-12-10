# import re
# from selenium.webdriver.common.by import By
#
# font_campaign_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//strong[@class="campaign-price"]').value_of_css_property("font-size")
# font_regular_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//s[@class="regular-price"]').value_of_css_property('font-size')
# try:
#     font_campaign_price_product_page_list = re.findall(r'\d+', font_campaign_price_product_page)  # паттерн \d+ возвращает целые числа
#     font_regular_price_product_page_list = re.findall(r'\d+\.?\d', font_regular_price_product_page)  # паттерн \d+\.?\d возвращает дробные значения с разделителем точкой