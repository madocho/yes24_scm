from selenium import webdriver

# chromedriver 위치 지정
driver = webdriver.Chrome('/Users/madocho/Desktop/work_file/python/chromedriver')

# 웹 자원 로드 대기
driver.implicitly_wait(3)

# url 접근
driver.get('https://scm.yes24.com/Login/LogOn')

# 아이디/비밀번호 입력
driver.find_element_by_name('UserName').send_keys('jthhke')
driver.find_element_by_name('Password').send_keys('hanbit0319319!!')

# 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="LogOnForm"]/fieldset/div[1]/div[2]/div').click()

# 웹 자원 로드 대기
driver.implicitly_wait(5)

# 인증번호 요청
driver.find_element_by_name('MobileNo').send_keys('01084880216')

# 인정 요청 버튼 클릭
driver.find_element_by_xpath('//*[@id="phone"]').click()

# alert 클릭 방법 찾기
