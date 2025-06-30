import os
from dotenv import load_dotenv

load_dotenv()

EASYPOST_PRODUCTION_KEY = os.getenv("EASYPOST_PRODUCTION_KEY")
EASYPOST_TEST_KEY = os.getenv("EASYPOST_TEST_KEY")
PERSONAL_PRODUCTION_KEY = os.getenv("PERONSAL_PRODUCTION_KEY")
ENVIRONMENT = "test"

carriers = {
    "AMAZON": os.getenv("AMAZON"),
    "ASENDIA": os.getenv("ASENDIA"),
    "AUSTRALIA_POST": os.getenv("AUSTRALIA_POST"),
    "CANADA_POST": os.getenv("CANADA_POST"),
    "DHL_EXPRESS": os.getenv("DHL_EXPRESS"),
    "DHL_PAKET": os.getenv("DHL_PAKET"),
    "DOORDASH": os.getenv("DOORDASH"),
    "DPD": os.getenv("DPD"),
    "FEDEX": os.getenv("FEDEX"),
    "FEDEX_DEFAULT": os.getenv("FEDEX_DEFAULT"),
    "FEDEX_MAILVIEW": os.getenv("FEDEX_MAILVIEW"),
    "LASERSHIP": os.getenv("LASERSHIP"),
    "ONTRAC": os.getenv("ONTRAC"),
    "PUROLATOR": os.getenv("PUROLATOR"),
    "ROYAL_MAIL": os.getenv("ROYAL_MAIL"),
    "SENDLE": os.getenv("SENDLE"),
    "UPS": os.getenv("UPS"),
    "UPS_MAILINNOVATIONS": os.getenv("UPS_MAILINNOVATIONS"),
    "USPS": os.getenv("USPS"),
}
