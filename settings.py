import os
from dotenv import load_dotenv
load_dotenv()

EASYPOST_PRODUCTION_KEY = os.getenv('EASYPOST_PRODUCTION_KEY')
EASYPOST_TEST_KEY = os.getenv('EASYPOST_TEST_KEY')
ENVIRONMENT = "test"

carriers = {
    "AUSTRALIA_POST": os.getenv("AUSTRALIA_POST"),
    "DHL_EXPRESS": os.getenv("DHL_EXPRESS"),
    "DHL_PAKET": os.getenv("DHL_PAKET"),
    "DPD": os.getenv("DPD"),
    "FEDEX": os.getenv("FEDEX"),
    "FEDEX_MAILVIEW": os.getenv("FEDEX_MAILVIEW"),
    "UPS": os.getenv("UPS"),
    "USPS": os.getenv("USPS"),
}
