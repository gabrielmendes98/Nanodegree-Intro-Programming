from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "xxx" # Your Account SID from www.twilio.com/console
auth_token  = "xxx"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)


message = client.messages.create(
    body="Hello from Python",
    to="+xxx",    # Replace with your phone number
    from_="+xxx") # Replace with your Twilio number

print message.sid