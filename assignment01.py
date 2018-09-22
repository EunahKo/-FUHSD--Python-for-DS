"""
Create dictionary for profile
by Eunah Ko
date Apr., 10, '18
for assignment01 - Vijay
"""

import pprint
import collections

#def pprint_OrderedDict():
#    pp_orig = pprint._sorted
#    od_orig = OrderedDict.__repr__
#    try:
#        pprint._sorted = lambda x:x
#        OrderedDict.__repr__ = dict.__repr__
#        yield
#    finally:
#        pprint._sorted = pp_orig
#        OrderedDict.__repr__ = od_orig

## Create profile dictionary
profile = {"NAME": 'Mildred D. Robertson',
           "ADDRESS":
           [{"Street": '438 Redbud Drive',
            "State": 'New York, NY',
            "Zipcode": 10011}],
           "Mother's maiden name": 'McBride',
           "SSN": '114-38-XXXX',
           "Geo coordinates": [40.679748, -74.076426],
           "PHONE":
           [{"Home Phone number": '347-683-3961',
            "Country code": '+1'},
            {"Work Phone number": '347-683-3961',
            "Country code": '+1'}],
           "BIRTHDAY":
           [{"Birthdday": 'September 13, 1963',
            "Age": 54,
            "Tropical zodiac": 'Virgo'}],
           "ONLINE":
           [{"Email Address": 'MildredDRobertson@armyspy.com',
            "Username": 'Obtainted',
            "Password": 'Tha3uiy5aegh',
            "Website": 'sanrioworld.com'}],
           "FINANCE":
           [{"Visa": "4539 9676 7752 6065",
            "Expires": '6/2021',
            "CVV2": '735'}],
           "EMPLOYMENT":
           [{"Company": 'Total Yard Management',
            "Occupation": 'Electrical power line installer'}],
           "PHYSICAL CHARACTERISTICS":
           [{"Height": '5\' 6" (167 centimeters)',
            "Weight": '213.6 pounds (97.1 kilograms)',
            "Blood type": 'O+'}],
           "TRACKING NUMBERS":
           [{"UPS tracking number": '1Z 85W 247 00 1102 229 8',
            "Western Union MTCN": '1387471482',
            "MoneyGram MTCN": '56949852'}],
           "OTHER":
           [{"Favorite color": 'Purple',
            "Vehicle": '2000 Holden HRT',
            "GUID": '78d4c7c6-5d4d-497e-8cb1-1448534f79a9'}]
           }

## print profile with pprint
#profile = collections.OrderedDict(profil1)
pp = pprint.PrettyPrinter(width = 20, indent = 4)
pprint.pprint(profile)

#with pprint_OrderedDict():
#    pprint.pprint(profile, width = 20, indent = 4)
