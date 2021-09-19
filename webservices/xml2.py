# XML 
import xml.etree.cElementTree as ET # REQUIRED

# Retrieving data from XML file (hard coded in this example)
data = '''<person>
    <name>Derrick</name>
    <phone> type="intl">
        +1 234 456 7899
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data) # Returns an object
print('Name:', tree.find('name').text) # Returns query
print('Attr:', tree.find('email').get('hide'))  # Returns query

print('\n\n')

# Retrieving data from XML file (hard coded in this example)
data = '''<database>
<users>
    <user>
         <id>001</id>
        <name>Derrick</name>
        <email hide="yes" />
    </user>
    <user>
        <id>002</id>
        <name>Malone</name>
        <email hide="no" />
    </user>
    </users>
</database>'''

tree = ET.fromstring(data)  # Returns an object
lst = tree.findall('users/user')
print('No. items in list:', len(lst)) # 2
for item in lst:    
    print('ID:', item.find('id').text)  # Returns query
    print('Name:', item.find('name').text)  # Returns query
    print('Attr:', item.find('email').get('hide'))  # Returns query
