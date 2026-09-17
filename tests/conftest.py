import pytest
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") 
client = genai.Client(api_key=API_KEY)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome =yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        #ambil pesan error atau traceback
        error_msg = str(call.excinfo.getrepr())

        print("\n" "="*60)
        print("🤖 MENGIRIM ERROR KE AI UNTUK DIANALISIS... MOHON TUNGGU 🤖")
        print("="*60)

        try :
            #panggil ai
            client = genai.Client(api_key= API_KEY)
            prompt = f"""
            Kamu adalah seorang QA Automation Expert. Analisis error dari Pytest berikut ini. 
            Jelaskan dalam maksimal 3 kalimat mengapa tes ini gagal, dan berikan 1 rekomendasi singkat cara memperbaikinya.
            
            Error Log:
            {error_msg}
            """

            response = client.models.generate_content(
                model='gemini-3.8-flash',
                contents=prompt
            )
            # Cetak hasil analisis AI di terminal
            print("\n💡 [AI BUG ANALYZER REPORT] 💡")
            print(response.text)
            print("="*60 + "\n")

        except Exception as e:
            print(f"gagal menghubungi AI: {e} ")
