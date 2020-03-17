from selenium import webdriver
import time

# 구글 지도 검색하여 크롱링
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://www.google.com/maps/'
driver.get(url)
driver.implicitly_wait(3)

# 지도 검색
driver.find_element_by_id('searchboxinput').send_keys('서울대입구 맛집')
driver.find_element_by_id('searchbox-searchbutton').click()
time.sleep(3)
# 한번 클릭
# # driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[1]').click()
# box = driver.find_element_by_xpath('//div[@role="listbox"]/div[@data-result-index="1"]').click()
# print("썸네일 정보 \n",box.text)
# # title = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h1')
# title = driver.find_element_by_xpath('//div[@class="section-hero-header-title-description"]')
# time.sleep(3)
# add = driver.find_element_by_xpath('//div[@data-section-id="ad"]')
# ph = driver.find_element_by_xpath('//div[@data-section-id="pn0"]')
#
# print(title.text)
# print("주소 : " ,add.text)
# print("전화번호 : ",ph.text)
# driver.back()

# 여러개 찾아서 가져오기
for i in range(1,21):
    driver.implicitly_wait(3)
    box = driver.find_element_by_xpath('//div[@role="listbox"]/div[@data-result-index="%d"]'%i).click()
    # 썸네일 정보
    try:
        title = driver.find_element_by_xpath('//div[@class="section-hero-header-title-description"]')
        time.sleep(2)
        print(title.text)
    except Exception:
        pass
    try:
        add = driver.find_element_by_xpath('//div[@data-section-id="ad"]')
        time.sleep(2)
        print("주소 : ", add.text)
    except Exception:
        pass
    try:
        ph = driver.find_element_by_xpath('//div[@data-section-id="pn0"]')
        print("전화번호 : ", ph.text)
        time.sleep(3)
    except Exception:
        pass
    # 브라우저 뒤로 돌아가기
    # back_button = driver.find_element_by_xpath('//button[@jsaction="pane.place.backToList"]')
    # driver.implicitly_wait(3)
    # back_button.click()
    driver.back()

from selenium import webdriver
import time

# 구글 지도 검색하여 크롱링
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://www.google.com/maps/'
driver.get(url)
driver.implicitly_wait(3)

# 지도 검색
driver.find_element_by_id('searchboxinput').send_keys('서울대입구 맛집')
driver.find_element_by_id('searchbox-searchbutton').click()
time.sleep(3)
# 한번 클릭
# # driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[1]').click()
# box = driver.find_element_by_xpath('//div[@role="listbox"]/div[@data-result-index="1"]').click()
# print("썸네일 정보 \n",box.text)
# # title = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h1')
# title = driver.find_element_by_xpath('//div[@class="section-hero-header-title-description"]')
# time.sleep(3)
# add = driver.find_element_by_xpath('//div[@data-section-id="ad"]')
# ph = driver.find_element_by_xpath('//div[@data-section-id="pn0"]')
#
# print(title.text)
# print("주소 : " ,add.text)
# print("전화번호 : ",ph.text)
# driver.back()

# 여러개 찾아서 가져오기
for i in range(1,21):
    driver.implicitly_wait(3)
    box = driver.find_element_by_xpath('//div[@role="listbox"]/div[@data-result-index="%d"]'%i).click()
    # 썸네일 정보
    try:
        title = driver.find_element_by_xpath('//div[@class="section-hero-header-title-description"]')
        time.sleep(2)
        print(title.text)
    except Exception:
        pass
    try:
        add = driver.find_element_by_xpath('//div[@data-section-id="ad"]')
        time.sleep(2)
        print("주소 : ", add.text)
    except Exception:
        pass
    try:
        ph = driver.find_element_by_xpath('//div[@data-section-id="pn0"]')
        print("전화번호 : ", ph.text)
        time.sleep(3)
    except Exception:
        pass
    # 브라우저 뒤로 돌아가기
    # back_button = driver.find_element_by_xpath('//button[@jsaction="pane.place.backToList"]')
    # driver.implicitly_wait(3)
    # back_button.click()
    driver.back()