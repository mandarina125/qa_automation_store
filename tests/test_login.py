from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()

def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    assert "Automation Exercise" in page.get_title()

def test_login_fail(driver):
    page = LoginPage(driver)
    page.open()
    page.login("correo_malo@gmail.com", "clave_mala")
    assert "Automation Exercise" in page.get_title()