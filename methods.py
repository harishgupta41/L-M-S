import hashlib
import vonage
import random

# password hashing
def sha256(data):
    data=bytes(data,'utf-8')
    sha=hashlib.sha256()
    sha.update(data)
    return sha.hexdigest()

#otp sending 
client = vonage.Client(key="7b8f120c", secret="OQK3YC47xY22jRYd")
sms = vonage.Sms(client)

def sendOTP(phone):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    responseData = sms.send_message(
        {
            "from": "LMS",
            "to": "919650859575",
            "text": "Your OTP for LMS registration is {0}.Do not share!".format(otp),
        }
    )
    if responseData["messages"][0]["status"] == "0":
        return otp

def verifyOTP(sOTP,rOTP):
    if (sOTP==rOTP):
        return True
    else:
        return False





# s='harish gupta'
# print(sha256(s))


