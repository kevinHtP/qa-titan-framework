Feature: Enterprise Security & Authentication FLow
    Sebagai QA/Security Engineer
    Saya ingin memastikan sistem login mendeteksi pengguna sah
    Dan menolak upaya peretasan SQL Injection

    Scenario: [UI-01] Pengguna gagal login dengan kredensial yang salah
    Given Saya membuka halaman login "http://localhost:3000/#/login"
    When Saya menutup pop-up welcome jika ada
    And Saya memasukkan email "bukanhacker@gmail.com" dan password "password123"
    And Saya menekan tombol Log in
    Then Saya harus melihat pesan error "Invalid email or password"

    Scenario: [SEC-01] Sistem harus kebal terhadap serangan SQL Injection dasar (DAST)
    Given Saya membuka halaman login "http://localhost:3000/#/login"
    When Saya menutup pop-up welcome jika ada
    # 🔑 INI ADALAH KODE HACKER: Memanipulasi database menggunakan karakter khusus
    And Saya memasukkan email "' OR 1=1 --" dan password "apapunbebas"
    And Saya menekan tombol Log in
    # Karena web ini sengaja dibuat rentan, serangan ini AKAN BERHASIL dan masuk ke dashboard
    Then Saya memverifikasi bahwa akun berhasil diretas dan masuk ke halaman utama