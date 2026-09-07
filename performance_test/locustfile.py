from locust import HttpUser, task, between

class PenggunaTokoOnline(HttpUser):
    # Waktu jeda (berpikir) antar klik, agar simulasi serealistis manusia (1 sampai 3 detik)
    wait_time = between(1, 3)

    @task(1)
    def buka_halaman_utama(self):
        with self.client.get("/", catch_response=  True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"gagal memuta response : {response.status_code}")

    @task(3)
    def buka_halaman_inventaris(self):
        """Mensimulasikan user yang berusaha melihat daftar barang (Bobot 3x lebih sering)"""
        # Dalam skenario asli, kita akan mengirim token login di sini. 
        # Untuk demo keamanan, kita hanya menembak endpoint-nya secara langsung.
        with self.client.get("/inventaris", catch_response= True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"gagal memuat response : {response.status_code}")