import os
from dotenv import load_dotenv

load_dotenv()

EASYPOST_PRODUCTION_KEY = os.getenv("EASYPOST_PRODUCTION_KEY")
EASYPOST_TEST_KEY = os.getenv("EASYPOST_TEST_KEY")
PERSONAL_PRODUCTION_KEY = os.getenv("PERSONAL_PRODUCTION_KEY")
PERSONAL_TEST_KEY = os.getenv("PERSONAL_TEST_KEY")
ENVIRONMENT = "production"
SERVICE = "lowest"

carriers = {
    "AMAZON": os.getenv("AMAZON"),
    "ASENDIA": os.getenv("ASENDIA"),
    "AUSTRALIA_POST": os.getenv("AUSTRALIA_POST"),
    "BETTER_TRUCKS": os.getenv("BETTER_TRUCKS"),
    "CANADA_POST": os.getenv("CANADA_POST"),
    "CIRRO": os.getenv("CIRRO"),
    "DAI_POST": os.getenv("DAI_POST"),
    "DHL_ECOMMERCE": os.getenv("DHL_ECOMMERCE"),
    "DHL_ECOMMERCE_WALLET": os.getenv("DHL_ECOMMERCE_WALLET"),
    "DHL_EXPRESS": os.getenv("DHL_EXPRESS"),
    "DHL_PAKET": os.getenv("DHL_PAKET"),
    "DOORDASH": os.getenv("DOORDASH"),
    "DPD": os.getenv("DPD"),
    "EVRI": os.getenv("EVRI"),
    "FEDEX": os.getenv("FEDEX"),
    "FEDEX_DEFAULT": os.getenv("FEDEX_DEFAULT"),
    "FEDEX_MAILVIEW": os.getenv("FEDEX_MAILVIEW"),
    "FIRST_MILE": os.getenv("FIRST_MILE"),
    "JITSU": os.getenv("JITSU"),
    "LASERSHIP": os.getenv("LASERSHIP"),
    "LOOMIS": os.getenv("LOOMIS"),
    "ONTRAC": os.getenv("ONTRAC"),
    "OPTIMA": os.getenv("OPTIMA"),
    "PUROLATOR": os.getenv("PUROLATOR"),
    "ROYAL_MAIL": os.getenv("ROYAL_MAIL"),
    "SENDLE": os.getenv("SENDLE"),
    "SF_EXPRESS": os.getenv("SF_EXPRESS"),
    "UPS": os.getenv("UPS"),
    "UPS_DAP": os.getenv("UPS_DAP"),
    "UPS_MAILINNOVATIONS": os.getenv("UPS_MAILINNOVATIONS"),
    "UPS_SUREPOST": os.getenv("UPS_SUREPOST"),
    "USA_EXPORT": os.getenv("USA_EXPORT"),
    "USPS": os.getenv("USPS"),
}
