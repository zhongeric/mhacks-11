from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACcc3e85148706449da8e73f93cd26ece2'
auth_token = 'df02a06ee966b53fbe423bb0d815143d'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='bruh delete those damnnudes',
         to ='+12486355526',
         from_='+15862819961'
     )

print(message.sid)