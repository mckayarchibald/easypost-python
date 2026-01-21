import dad_tool
import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)
if settings.ENVIRONMENT == "personal":
    client = easypost.EasyPostClient(settings.PERSONAL_PRODUCTION_KEY)
if settings.ENVIRONMENT == "personalTest":
    client = easypost.EasyPostClient(settings.PERSONAL_TEST_KEY)

# SHIPMENT PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////
# ADDRESSES:

custom_recepient_address = {
    "name": "David Hughes",
    "company": "C/O Test",
    "street1": "29 Shady Lane #100",
    "street2": "",
    "city": "ROSS",
    "state": "CA",
    "zip": "94957-9676",
    "country": "US",
    "phone": "4152154760",
    "email": "3264760@gmail.com",
    "residential": True,
}
custom_sender_address = {
    "name": "Shipping Manager",
    "company": "Sun Home Saunas",
    "street1": "1634 Turrill Ave",
    "street2": "",
    "city": "San Bernardino",
    "state": "CA",
    "zip": "92411",
    "country": "US",
    "phone": "5552221111",
    "email": "example@example.com",
    "residential": False,
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

destination = france_address_1
buyer = france_address_1
origin = utah_address
return_destination = utah_address


to_address = {
    "name": "Gob Bluth",
    "street1": destination["street1"],
    "street2": destination["street2"],
    "city": destination["city"],
    "state": destination["state"],
    "zip": destination["zip"],
    "country": destination["country"],
    # "phone": destination["phone"],
    "phone": "4352326896",
    # "email": destination["email"],
    "email": "marchibald@easypost.com",
    # "residential": True,
    # "federal_tax_id": "federal_tax_id",
}

buyer_address = {
    "name": "Michael Bluth",
    "street1": buyer["street1"],
    "street2": buyer["street2"],
    "city": buyer["city"],
    "state": buyer["state"],
    "zip": buyer["zip"],
    "country": buyer["country"],
    "phone": "415-456-7890",
}

from_address = {
    "name": "Tobias Fünke",
    "company": "Test",
    "street1": origin["street1"],
    "street2": origin["street2"],
    "city": origin["city"],
    "state": origin["state"],
    "zip": origin["zip"],
    "country": origin["country"],
    "phone": "4352326896",
    "email": "marchibald@easypost.com",
    # "phone": origin["phone"],
    # "email": origin["email"],
}

return_address = {
    "name": "Buster Bluth",
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
            "currency": "CAD",
            "hs_tariff_number": "654321",
            "origin_country": "US",
            "code": "1234",
        }
    ],
}

parcel = {"weight": 32}
# CREATE SHIPMENT ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    shipment = client.shipment.create_and_buy_luma(
        carrier_accounts=[settings.carriers["FEDEX"]],
        to_address={
            "name": "Dr. Steve Brule",
            "street1": "5744 Silverton Ave",
            "city": "McKinney",
            "state": "TX",
            "zip": "75070",
            "country": "US",
            "phone": "8573875756",
            "email": "dr_steve_brule@gmail.com",
        },
        from_address={
            "name": "EasyPost",
            "street1": "417 Montgomery Street",
            "street2": "5th Floor",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94104",
            "country": "US",
            "phone": "4153334445",
            "email": "support@easypost.com",
        },
        parcel={
            "length": 20.2,
            "width": 10.9,
            "height": 5,
            "weight": 65.9,
        },
        options={
            "label_format": "PDF",
            "label_size": "4x6",
        },
        ruleset_name="cheapest_delivery",
        planned_ship_date="2026-01-24",
    )

    print(shipment)
except Exception as error:
    print("...uh oh: ", error)
