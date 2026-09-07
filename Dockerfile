# 1. Gunakan Official Playwright Image (Semua dependensi & browser sudah terinstal sempurna!)
FROM mcr.microsoft.com/playwright/python:v1.41.0-jammy

# 2. Buat folder bernama /app di dalam kontainer virtual
WORKDIR /app

# 3. Masukkan file daftar belanjaan ke dalam kontainer
COPY requirements.txt .

# 4. Instal library QA kita (Tidak perlu lagi 'playwright install' karena sudah bawaan pabrik)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Salin seluruh framework Titan milikmu ke dalam kontainer
COPY . .

# 6. Perintah default saat menyalakan kontainer ini
CMD ["python", "-m", "pytest", "-s", "-v", "--alluredir=allure-results", "tests/"]