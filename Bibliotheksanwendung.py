import json
class ContactManager:
    def __init__(self,path="-"):
        self.contact_list=[]
        if path != "-" :
            print("loading previos contacts..")
            with open(path,"r") as f:
                data=f.read()
                self.contact_list=json.loads(data)
            print("loaded...")

    def add(self,name,number):
        self.contact_list.append({"name":name,
         "number": number})
        return self.contact_list
    
    def search(self,name):
        result=[]
        for item in self.contact_list:
            if name.lower()in item["name"].lower():
                result.append(item)
        print(result)
    
    def backup(self):
        with open("./contact_list.json","w")as f:
            f.write(json.dumps(self.contact_list))

    def print(self):
        print(f"your contact:{self.contact_list}")

my_contact=ContactManager()
my_contact.add("mary","11111")
#my_contact.add("ali","11112")
#my_contact.add("maryam","11113")
print(my_contact)
#my_contact.search("al")
#my_contact.backup()