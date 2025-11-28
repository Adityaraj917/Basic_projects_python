from twilio .rest import Client

ACCOUNT_SID = "ACc5ba5390f94.........3ec9492"
AUTH_TOKEN = "9af2824fe35de.........906157af"
TWILIO_NUMBER = "+1510.......4"
RECEIVER_NUM  = "+918  ......6"  
Client = Client(ACCOUNT_SID,AUTH_TOKEN)
messages = Client.messages.create(
    body = "kya haal h bhaiyia ji",
    from_ = TWILIO_NUMBER,
to = RECEIVER_NUM)
