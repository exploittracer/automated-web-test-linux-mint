import os

class Config:
    BASE_URL = "http://localhost:9392"
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    TIMEOUT = 10