import os
from pathlib import Path
import allure 
import pytest
from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import Page

BASE_DIR = Path(__file__).parent.parent
FEATURE_FILE = BASE_DIR / "features" / "login.feature"

# ====================================================================
# 1. STEP DEFINITIONS (Kita taruh di atas agar memori mendaftarkannya)
# ====================================================================

# Kita gunakan parsers.parse untuk SEMUA langkah agar pencocokannya lebih kuat
@given(parsers.parse('Saya berada di halaman Saucedemo'))
def buka_halaman_utama(page: Page):
    print("\n[BDD] GIVEN: Membuka Saucedemo...")
    page.goto("https://www.saucedemo.com/")

    # Bonus: Ambil screenshot otomatis dan lampirkan ke Allure Report!
    allure.attach(page.screenshot(full_page = True), name="Halaman Login", attachment_type= allure.attachment_type.PNG)

@when(parsers.parse('Saya login menggunakan {username} dan {password}'))
def proses_login(page: Page, username, password):
    print(f"[BDD] WHEN: Login dengan user '{username}'...")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")

@then(parsers.parse('Harga {nama_produk} adalah {harga_harapan}'))
def validasi_harga(page: Page, nama_produk, harga_harapan):
    print(f"[BDD] THEN: Memvalidasi harga '{nama_produk}'...")
    teks_harga = page.locator(f".inventory_item:has-text('{nama_produk}') .inventory_item_price").inner_text()

    allure.attach(page.screenshot(full_page = True), name = "Halaman Inventarsis", attachment_type= allure.attachment_type.PNG)
    
    assert teks_harga == harga_harapan, f"Gagal! Diharapkan {harga_harapan}, tapi muncul {teks_harga}"
    print(f"       ✅ Sukses: Harga sesuai!")


# ====================================================================
# 2. DEKLARASI SKENARIO (Kita panggil secara spesifik di bawah)
# ====================================================================

@scenario(FEATURE_FILE, 'Login sukses dan verifikasi harga barang')
def test_login_bdd_eksplisit():
    # Pytest akan otomatis mencocokkan skenario ini dengan step di atas
    pass