import dad_tool
import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# ADDRESSES:
utah_address = dad_tool.random_address('US_UT')
california_address = dad_tool.random_address('US_CA')
canada_address = dad_tool.random_address('CA_BC')

destination = canada_address
buyer = canada_address
origin = utah_address
return_destination = utah_address

to_address = {
    "name": "EasyPost",
    "street1": destination['street1'],
    "street2": destination['street2'],
    "city": destination['city'],
    "state": destination['state'],
    "zip": destination['zip'],
    "country": destination['country'],
    "phone": "415-456-7890",
}

buyer_address = {
    "name": "EasyPost",
    "street1": buyer['street1'],
    "street2": buyer['street2'],
    "city": buyer['city'],
    "state": buyer['state'],
    "zip": buyer['zip'],
    "country": buyer['country'],
    "phone": "415-456-7890",
}

from_address = {
    "name": "EasyPost",
    "street1": origin['street1'],
    "street2": origin['street2'],
    "city": origin['city'],
    "state": origin['state'],
    "zip": origin['zip'],
    "country": origin['country'],
    "phone": "415-456-7890",
}

return_address = {
    "name": "EasyPost",
    "street1": return_destination['street1'],
    "street2": return_destination['street2'],
    "city": return_destination['city'],
    "state": return_destination['state'],
    "zip": return_destination['zip'],
    "country": return_destination['country'],
    "phone": "415-456-7890",
}

# CUSTOMS INFORMATION:
customs_info = {
    "eel_pfc": "NOEEI 30.37(a)",
    "customs_certify": True,
    "customs_signer": "Steve Brule",
    "contents_type": "merchandise",
    "contents_explanation": "this is the general notes section",
    "restriction_type": "none",
    "restriction_comments": '',
    "non_delivery_option": "return",
    "customs_items": [
        {
            "description": "Sweet shirts",
            "quantity": 12,
            "weight": 5,
            "value": 222,
            "hs_tariff_number": "654321",
            "origin_country": "US",
            "code": "1234",
        },
    ],
}
try:
    order = client.order.create(
        to_address = to_address,
        from_address = from_address,
        shipments = [
            {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
            {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },            {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
                        {
                "parcel": {
                    # "predefined_package": "FedExBox",
                    "weight": 30,
                },
                "customs_info": customs_info
            },
        ],
    )
except:
    print("...uh oh") 

# BUY SPECIFIC CARRIER AND SERVICE:
try:
    bought_order = client.order.buy(
        order.id,
        carrier="FedEx",
        service="INTERNATIONAL_ECONOMY"
    )
    print(bought_order)
except: 
    print("It did not work")