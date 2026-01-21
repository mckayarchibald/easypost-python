import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

try:
    address = client.address.create_and_verify(
        street1="Av Del Ejército 1180, Of. 1501",
        street2="",
        city="Magdalena Del Mar",
        state="",
        zip="15000",
        country="PE",
        company="Energuias Perú Sac",
        name="Enrique Cornejo",
        phone="51998676870",
        email="enrique@energuias.com",
        # verify=True,
        verify_carrier="fedex",
    )

    print(address.id)

except Exception as error:
    print("...uh oh: ", error)
