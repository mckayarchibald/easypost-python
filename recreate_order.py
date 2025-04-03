import easypost
import settings
import json

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

with open("recreate_data.json") as recreate_data:
    order_data = json.load(recreate_data)

# ORDER PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////
# ADDRESSES:
to_address = {
    "name": order_data["to_address"]["name"],
    "company": order_data["to_address"]["company"],
    "street1": order_data["to_address"]["street1"],
    "street2": order_data["to_address"]["street2"],
    "city": order_data["to_address"]["city"],
    "state": order_data["to_address"]["state"],
    "zip": order_data["to_address"]["zip"],
    "country": order_data["to_address"]["country"],
    "phone": order_data["to_address"]["phone"],
}

buyer_address = {
    "name": order_data["buyer_address"]["name"],
    "company": order_data["buyer_address"]["company"],
    "street1": order_data["buyer_address"]["street1"],
    "street2": order_data["buyer_address"]["street2"],
    "city": order_data["buyer_address"]["city"],
    "state": order_data["buyer_address"]["state"],
    "zip": order_data["buyer_address"]["zip"],
    "country": order_data["buyer_address"]["country"],
    "phone": order_data["buyer_address"]["phone"],
}

from_address = {
    "name": order_data["from_address"]["name"],
    "company": order_data["from_address"]["company"],
    "street1": order_data["from_address"]["street1"],
    "street2": order_data["from_address"]["street2"],
    "city": order_data["from_address"]["city"],
    "state": order_data["from_address"]["state"],
    "zip": order_data["from_address"]["zip"],
    "country": order_data["from_address"]["country"],
    "phone": order_data["from_address"]["phone"],
}

# SHIPMENTS:

# Copy all shipments
shipments = order_data["shipments"]

# Delete the unessecary keys in each shipment
for shipment in shipments:
    del shipment["id"]
    del shipment["mode"]
    del shipment["created_at"]
    del shipment["order_id"]
    del shipment["rates"]
    del shipment["object"]
    del shipment["from_address"]["id"]
    del shipment["from_address"]["object"]
    del shipment["from_address"]["created_at"]
    del shipment["from_address"]["updated_at"]
    del shipment["from_address"]["mode"]
    del shipment["to_address"]["id"]
    del shipment["to_address"]["object"]
    del shipment["to_address"]["created_at"]
    del shipment["to_address"]["updated_at"]
    del shipment["to_address"]["mode"]
    del shipment["return_address"]["id"]
    del shipment["return_address"]["object"]
    del shipment["return_address"]["created_at"]
    del shipment["return_address"]["updated_at"]
    del shipment["return_address"]["mode"]
    del shipment["buyer_address"]["id"]
    del shipment["buyer_address"]["object"]
    del shipment["buyer_address"]["created_at"]
    del shipment["buyer_address"]["updated_at"]
    del shipment["buyer_address"]["mode"]

# CREATE ORDER ////////////////////////////////////////////////////////////////////////////////////////////////////////
order = client.order.create(
    to_address=to_address,
    from_address=from_address,
    shipments=shipments,
)

print("The order was successfully created: ", order.id)

# ORDER BUY ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# LOWEST RATE:
try:
    bought_order = client.order.buy(order.id, rate=order.lowest_rate())
    print("The order was successfully purchased: ", bought_order.id)
except Exception as error:
    print("...uh oh. The purchase request failed: ", error)

# SPECIFIC CARRIER AND SERVICE:
# try:
#     bought_order = client.order.buy(
#         order.id,
#         rate=shipment.lowest_rate(["USPS"], ["PriorityMailInternational"])
#     )
#     print(bought_order.id)
# except Exception as error:
#      print("...uh oh: ", error)
