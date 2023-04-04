import json
import vobject

# Load the JSON data from the file
with open('data.json', 'r') as f:
    data = json.load(f)

# Create a new vCard object for each JSON object
vcards = []
for obj in data:
    # Create a new vCard object
    vcard = vobject.vCard()

    # Set the name and organization fields
    vcard.add('n')
    vcard.n.value = vobject.vcard.Name(family=obj['name'].split(';')[0], given=obj['name'].split(';')[1])
    vcard.add('org')
    vcard.org.value = [obj['organisation']]

    # Set the address field
    vcard.add('adr')
    vcard.adr.value = vobject.vcard.Address(street=obj['address'].split(';')[2], city=obj['address'].split(';')[3], region=obj['address'].split(';')[4], code=obj['address'].split(';')[5], country=obj['address'].split(';')[6])

    # Set the phone and email fields
    vcard.add('tel')
    vcard.tel.value = obj['telefon']
    vcard.add('email')
    vcard.email.value = obj['email']

    # Add the vCard object to the list
    vcards.append(vcard)

# Write the vCard objects to a file
with open('output.vcf', 'w') as f:
    for vcard in vcards:
        f.write(vcard.serialize())