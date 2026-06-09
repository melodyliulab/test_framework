from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login():
    # 1. 初始化浏览器驱动 (以 Edge 为例)
    # Selenium 4 会自动管理底层驱动，无需指定 executable_path
    driver = webdriver.Edge()
    
    try:
        # 2. 访问目标 URL
        print("正在打开登录页面...")
        driver.get("http://the-internet.herokuapp.com/login")
        
        # 3. 设置显式等待 (最大等待时间 10 秒)
        # 这是面试的加分项：绝对不要在生产代码中使用 time.sleep()
        wait = WebDriverWait(driver, 10)
        
        # 4. 定位并输入用户名
        # 使用 ID 定位是最快且最稳定的方式
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("tomsmith")
        
        # 5. 定位并输入密码
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        
        # 6. 定位并点击登录按钮
        # 当没有 ID 或 Name 时，可以使用 CSS Selector 或 XPath
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_button.click()
        
        # 7. 核心环节：断言 (Assertion)
        # 验证是否出现了具有特定 ID 的成功提示元素，并读取其文本
        success_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        
        assert "You logged into a secure area!" in success_message.text
        print("测试通过：成功登录并捕获到成功提示！")

    except Exception as e:
        print(f"测试失败: {e}")
        
    finally:
        # 8. 无论测试成功与否，都要确保关闭浏览器释放资源
        driver.quit()

# 运行测试
if __name__ == "__main__":
    test_successful_login()
