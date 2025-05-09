from selenium import webdriver
from selenium.webdriver.common.by import By

from modules.config import Config

import sys


def main():
    options = webdriver.FirefoxOptions()
    options.add_argument(f"-profile {Config().firefox_profile_path}")
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    driver.get(str(Config().mf_accounts_url))

    try:
        refresh_button = driver.find_element(By.XPATH, Config().mf_refresh_xpath)

        if refresh_button.text == Config().mf_refresh_button_text:
            refresh_button.click()
            print("更新要求に成功しました。")
    except Exception as e:
        print("更新要求に失敗しました。", file=sys.stderr)
        print(e, file=sys.stderr)

    # ブラウザを終了する
    driver.quit()


if __name__ == "__main__":
    main()
