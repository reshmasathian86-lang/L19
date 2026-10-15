county_code = {' India' : '0091',
               'Australia' : '0025',
               'Nepal' : '00977'}

# search dictionary for country code of India
print("country code of India -")
print(county_code.get('India', 'Not found'))

# search dictionary for country code of Japan
print("country code of Japan -")
print(county_code.get('Japan', 'Not found'))