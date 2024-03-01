import settings
import easypost
import dad_tool

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

to_address = dad_tool.random_address('US_UT')
from_address = dad_tool.random_address('US_NY')

shipment = client.shipment.create(
    from_address = {
        "name": "EasyPost",
        "street1": from_address.street1,
        "street2": from_address.street2,
        "city": from_address.city,
        "state": from_address.state,
        "zip": from_address.zip,
        "country": from_address.country,
        "phone": "415-456-7890",
    },
    to_address = {
        "name": "EasyPost",
        "street1": to_address.street1,
        "street2": to_address.street2,
        "city": to_address.city,
        "state": to_address.state,
        "zip": to_address.zip,
        "country": to_address.country,
        "phone": "415-456-7890",
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