from selenium import webdriver

def login_auto():
    wp_login = 'https://adboub.internet-sicherheit.de/wp-login.php'
    wp_admin = 'https://adboub.internet-sicherheit.de/wp-admin/'
    username = 'ifis2'
    password = 'tRjo%EEwzZ81jY&2ZesSLY87'

    with requests.Session() as s:
        headers1 = { 'Cookie':'wordpress_test_cookie=WP Cookie check' }
        datas={ 
            'log':username, 'pwd':password, 'wp-submit':'Log In', 
            'redirect_to':wp_admin, 'testcookie':'1'  
        }
        s.post(wp_login, headers=headers1, data=datas)
        resp = s.get(wp_admin)
        print(resp.text)


def login_automation():

    username = 'ifis2'
    password = 'tRjo%EEwzZ81jY&2ZesSLY87'
    driver = webdriver.chrome('chromedriver.exe')
    driver.get('https://adboub.internet-sicherheit.de/wp-login.php')

    user_input = driver.find_element_by_id('user_login')
    user_input.send_keys(username)

    passwort_input = driver.find_element_by_id('user_pass')
    passwort_input.send_keys(password)

    login_button = driver.find_element_by_id('wp-submit')
    login_button.click()


def main():
    login_automation()
    

if __name__ == "__main__":
    main()