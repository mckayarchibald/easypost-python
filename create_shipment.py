import dad_tool
import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# SHIPMENT PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////
# ADDRESSES:

custom_recepient_address = {
    "name": "NOT SUPPLIED",
    "company": "GEORGE KOREN",
    "email": "",
    "phone": "5037478381",
    "street1": "271 BLACKHEAD MOUNTAIN RD",
    "street2": "NY",
    "city": "ROUND TOP",
    "state": "NY",
    "zip": "12473-5308",
    "country": "US",
}
custom_sender_address = {
    "name": "Gabriel Espinola",
    "company": "",
    "street1": "4350 River Trail Way",
    "street2": "",
    "city": "The Dalles",
    "state": "OR",
    "zip": "97058",
    "country": "US",
    "phone": "48731385891",
}

# DOMESTIC:
california_address = dad_tool.random_address("US_CA")
texas_address = dad_tool.random_address("US_TX")
utah_address = dad_tool.random_address("US_UT")

# INTERNATIONAL:
australia_address_1 = dad_tool.random_address("AU_VT")
australia_address_2 = dad_tool.random_address("AU_VT")
canada_address = dad_tool.random_address("CA_BC")
france_address_1 = dad_tool.random_address("EU_FR")
france_address_2 = dad_tool.random_address("EU_FR")
uk_address = dad_tool.random_address("EU_UK")

destination = utah_address
buyer = utah_address
origin = california_address
return_destination = california_address


to_address = {
    "name": "McKay Archibald",
    "street1": destination["street1"],
    "street2": destination["street2"],
    "city": destination["city"],
    "state": destination["state"],
    "zip": destination["zip"],
    "country": destination["country"],
    "phone": "4352326896111",
    # "federal_tax_id": "federal_tax_id",
    "email": "mckay@example.com",
}

buyer_address = {
    "name": "EasyPost",
    "street1": buyer["street1"],
    "street2": buyer["street2"],
    "city": buyer["city"],
    "state": buyer["state"],
    "zip": buyer["zip"],
    "country": buyer["country"],
    "phone": "415-456-7890",
}

from_address = {
    "name": "EasyPost",
    "street1": origin["street1"],
    "street2": origin["street2"],
    "city": origin["city"],
    "state": origin["state"],
    "zip": origin["zip"],
    "country": origin["country"],
    "phone": "4352326896111",
    "email": "",
}

return_address = {
    "name": "EasyPost",
    "street1": return_destination["street1"],
    "street2": return_destination["street2"],
    "city": return_destination["city"],
    "state": return_destination["state"],
    "zip": return_destination["zip"],
    "country": return_destination["country"],
    "phone": "4154567890",
}

# CUSTOMS INFORMATION:
customs_info = {
    "eel_pfc": "NOEEI 30.37(a)",
    "declaration": "This is a declaration test",
    "customs_certify": True,
    "customs_signer": "Steve Brule",
    "contents_type": "merchandise",
    "contents_explanation": "This is a contents explanation test",
    "restriction_type": "none",
    "restriction_comments": "These are some additional comments",
    "non_delivery_option": "return",
    "customs_items": [
        {
            "description": "Sweat shirts",
            "quantity": 1,
            "weight": 32,
            "value": 500,
            "hs_tariff_number": "654321",
            "origin_country": "US",
            "code": "1234",
        }
    ],
}

# CREATE SHIPMENT ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    shipment = client.shipment.create(
        from_address=from_address,
        to_address=to_address,
        # return_address = return_address,
        # buyer_address = buyer_address,
        parcel={
            # "length": "27.01",
            # "width": "16.34",
            # "height": "25",
            "weight": "340",
            # "predefined_package": "FedExSmallBox",
        },
        options={},
        # customs_info=customs_info,
        carrier_accounts=[
            settings.carriers["UPS"],
            # settings.carriers["FEDEX_DEFAULT"],
        ],
        # service="Priority",
        # is_return=True,
    )

    print(shipment.id)
except Exception as error:
    print("...uh oh: ", error)

# SHIPMENT BUY ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# LOWEST RATE:
try:
    bought_shipment = client.shipment.buy(shipment.id, rate=shipment.lowest_rate())
    print(bought_shipment.id)
except Exception as error:
    print("...uh oh: ", error)

# SPECIFIC CARRIER AND SERVICE:
# try:
#     bought_shipment = client.shipment.buy(
#         shipment.id,
#         rate=shipment.lowest_rate(["USPS"], ["First"])
#     )
#     print(bought_shipment)
# except:
#     print("It did not work")
