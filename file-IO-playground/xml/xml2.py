# code to get the content and attributes in an xml document/tree and view in text format
import xml.etree.ElementTree as ET

data = """
<siblings>
   <users>
       <user x="2">
          <id>001</id>
          <name>Chinazo</name>
       </user>
       <user x="4">
          <id>002</id>
          <name>Genevieve</name>
       </user>
       <user x="6">
          <id>003</id>
          <name>Cabrini</name>
       </user>
       <user x="8">
          <id>004</id>
          <name>Carolus</name>
       </user>
   </users>
</siblings>
"""

tree = ET.fromstring(data)
my_list = tree.findall("users/user")
print("User Count: ", len(my_list))


for item in my_list:
    print("Name: ", item.find("name").text)
    print("Id: ", item.find("id").text)
    print("Attr: ", item.get("x"))

