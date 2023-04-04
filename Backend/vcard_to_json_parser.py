def vcard_parser( file ):   
    
    import json

    INPUT_NAME = file
    OUTPUT_NAME = 'data.json'

    with open(INPUT_NAME, 'r') as f:
        text = f.read()

    contact_texts = text.split('END:VCARD\nBEGIN:VCARD')

    contact_texts[0] = contact_texts[0].replace('BEGIN:VCARD\n', '')
    contact_texts[-1] = contact_texts[-1].replace('END:VCARD\n', '')


    def fix_key(key):
        key_main = key.split(';')[0]
        return {
            'BDAY': 'birthday',
            'VERSION': 'version',
            'N': 'name',
            'FN': 'first name',
            'ORG': 'organisation',
            'ADR': 'address',
            'TEL': 'telefon',
            'EMAIL': 'email'
        }.get(key_main, key)


    contacts = []
    for contact_text in contact_texts:

        contact = {}
        lines = contact_text.split('\n')

        for line in lines:
            if len(line) < 1:
                continue

            key, *value = line.split(':')
            value = ':'.join(value)

            key = fix_key(key)

            contact[key] = value
        contacts.append(contact)

    json_text = json.dumps(contacts, indent=2)

    with open(OUTPUT_NAME, 'w') as f:
        f.write(json_text)
