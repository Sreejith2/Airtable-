import requests
AIRTABLE_API_KEY = "keyenr0EY01E1JA0g"
AIRTABLE_BASE_ID="appUvjxvwzFGaempx"

airtable_endpoint=f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/table-1"
def add_to_airtable(email=None,name="",mobile_no="",attendance=None):
    if email is None:
        return
    headers={
        "Authorization":f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    data={
      "records": [
        {
          "fields": {
            "name": name,
            "email": email,
            "mobile no":mobile_no,
            "attendance":attendance
          }
        }
      ]
        }
    r = requests.post(airtable_endpoint,json=data,headers=headers)
    #print(r.json())

print(""" _________________________ 
|  _____________________  |
| |     WELCOME TO
    Attendance analysor | |
| |_____________________| |
|_________________________|""")



name=input("\nWhat is your name?\n")
email=input("\nWhat is your email?\n")
mobileno=input("\nEnter your mobile No:\n")
attend=float(input("\nEnter the attendence (percentage):\n"))

add_to_airtable(email,name,mobileno,attend)

headers={
       "Authorization":F"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

total=int(input("Total no of students in class:\n"))
response=requests.get(airtable_endpoint,headers=headers)
data=response.json()

print("""(¯`·¯`·.¸¸.·´¯`·.¸¸.·´¯·´¯)
( \                     / )
 ( ) Attendance Report ( ) 
  (/                   \)  
   (.·´¯`·.¸¸.·´¯`·.¸¸.)   """)

for i in range(0,total):
    attendance=data['records'][i]['fields']['attendance']
    if attendance<65:
        print(f"\n❗❗Warning {data['records'][i]['fields']['name']} doesnt have required attendance")
    else:
        print(f"\n{data['records'][i]['fields']['name']} : {attendance}% Good ✅ ")