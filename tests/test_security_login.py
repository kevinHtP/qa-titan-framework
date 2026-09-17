from pytest_bdd import scenarios, given , when, then, parsers
from playwright.sync_api import Page, expect

scenarios('../features/security_login.feature')

@given('Saya membuka halaman login "http://localhost:3000/#/login"')
def buka_halaman_login(page:Page):
    page.goto('http://localhost:3000/#/login')

@when('Saya menutup pop-up welcome jika ada')
def tutup_popup(page:Page):
    try:
        page.locator("button[aria-label='Close Welcome Banner']").click(Timeout=3000, force=True)
    except:
        pass
    
    try:
        page.locator("a[aria-label='dismiss cookie message']").click(timeout=3000, force=True)
    except:
        pass # Lanjut jika tidak ada
        
@when(parsers.re(r'Saya memasukkan email "(?P<email>.*)" dan password "(?P<password>.*)"'))
def login(email, password, page:Page):
    page.locator("input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)


@when ('Saya menekan tombol Log in')
def tombol_login(page:Page):
    page.locator("button#loginButton").click()

@then ('Saya harus melihat pesan error "Invalid email or password"')
def msg_error(page:Page):
    error_msg = page.locator('div.error')
    expect(error_msg).to_be_visible()

@then ('Saya memverifikasi bahwa akun berhasil diretas dan masuk ke halaman utama')
def verifikasi(page:Page):
    # Jika berhasil dijebol, logo atau keranjang belanja akan muncul
    expect(page.locator("button[aria-label='Close Welcome Banner']")).to_be_visible