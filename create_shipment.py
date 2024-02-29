import settings
import script_functions
import easypost

environment = script_functions.get_environment()

if environment == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if environment == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)


shipment = client.shipment.create(
    from_address = {
        "name": "EasyPost",
        "street1": "118 2nd Street",
        "street2": "4th Floor",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94105",
        "country": "US",
        "phone": "415-456-7890",
    },
    to_address = {
        "name": "Dr. Steve Brule",
        "street1": "179 N Harbor Dr",
        "city": "Redondo Beach",
        "state": "CA",
        "zip": "90277",
        "country": "US",
        "phone": "310-808-5243",
    },
    parcel = {
        "length": 10.2,
        "width": 7.8,
        "height": 4.3,
        "weight": 21.2,
    },
)

bought_shipment = client.shipment.buy(shipment.id, rate=shipment.lowest_rate())

print(bought_shipment)