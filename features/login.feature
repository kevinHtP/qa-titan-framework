Feature: Validasi E2E Pembelian Barang di Toko

  Scenario: Login sukses dan verifikasi harga barang
    Given Saya berada di halaman Saucedemo
    When Saya login menggunakan standard_user dan secret_sauce
    Then Harga Sauce Labs Backpack adalah $29.99