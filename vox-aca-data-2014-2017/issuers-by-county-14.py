from python_lib_util import csvtools as c
from operator import itemgetter
import collections


# STEP ONE: Read in needed data as a list of dicts
data = c.read_as_dict('raw-csvs/2014-combined.csv')

issuers_by_county = list()
for row in data:
    att = dict()
    att ['i'] = row['Issuer Name']
    att['s'] = row['State']
    att['c'] = row['County'].title()

    # and
    if att['c'] == 'King And Queen':
        att['c'] = 'King and Queen'
    if att['c'] == 'Lake And Peninsula':
        att['c'] = 'Lake and Peninsula'
    if att['c'] == 'Lewis And Clark':
        att['c'] = 'Lewis and Clark'

    # census areas
    if att['c'] == 'Aleutians West':
        att['c'] = 'Aleutians West Census'
    if att['c'] == 'Dillingham':
        att['c'] = 'Dillingham Census'
    if att['c'] == 'Wade Hampton':
        att['c'] = 'Wade Hampton Census'
    if att['c'] == 'Bethel':
        att['c'] = 'Bethel Census'
    if att['c'] == 'Hoonah-Angoon':
        att['c'] = 'Hoonah-Angoon Census'
    if att['c'] == 'Petersburg':
        att['c'] = 'Petersburg Census'
    if att['c'] == 'Southeast Fairbanks':
        att['c'] = 'Southeast Fairbanks Census'
    if att['c'] == 'Yukon-Koyukuk':
        att['c'] = 'Yukon-Koyukuk Census'
    if att['c'] == 'Prince Of Wales-Hyder':
        att['c'] = 'Prince of Wales-Hyder Census'
    if att['c'] == 'Valdez-Cordova':
        att['c'] = 'Valdez-Cordova Census'
    if att['c'] == 'Bristol Bay Borough':
        att['c'] = 'Bristol Bay'


    if att['c'] == 'Matanuska Susitna':
        att['c'] = 'Matanuska-Susitna'
    if att['c'] == 'Fond Du Lac':
        att['c'] = 'Fond du Lac'
    if att['c'] == 'Isle Of Wight':
        att['c'] = 'Isle of Wight'
    if att['c'] == 'Obrien':
        att['c'] = "O'Brien"

    # city
    if 'City' in att['c']:
        att['c'] = att['c'].replace('City', 'city')
    if att['c'] == 'Radford':
        att['c'] = 'Radford city'
    if att['c'] == 'Yakutat Borough':
        att['c'] = 'Yakutat City and'
    if att['c'] == 'Wrangell city And Borough':
        att['c'] = 'Wrangell City and'
    if att['c'] == 'Sitka':
        att['c'] = 'Sitka City and'
    if att['c'] == 'Nome':
        att['c'] = 'Nome Census'
    if att['s'] == 'AK' and att['c'] == 'Juneau':
        att['c'] = 'Juneau City and'
    if att['s'] == 'VA' and att['c'] == 'Salem':
        att['c'] = 'Salem city'
    if att['s'] == 'VA' and att['c'] == 'Bristol':
        att['c'] = 'Bristol city'
    if att['c'] == 'Carson city':
        att['c'] = 'Carson'
    if att['c'] == 'James city':
        att['c'] = 'James City'
    if att['c'] == 'Charles city':
        att['c'] = 'Charles City'
    if att['c'] == 'Poquoson':
        att['c'] = 'Poquoson city'

    # compound names
    if att['c'] == 'Du Page':
        att['c'] = 'DuPage'
    if att['s'] == 'TX' and att['c'] == 'De Witt':
        att['c'] = 'DeWitt'
    if att['s'] == 'IL' and att['c'] == 'Dewitt':
        att['c'] = 'De Witt'
    if att['c'] == 'De Kalb':
        att['c'] = 'DeKalb'
    if att['c'] == 'Dekalb':
        att['c'] = 'DeKalb'
    if att['c'] == 'Lagrange':
        att['c'] = 'LaGrange'
    if att['c'] == 'La Porte':
        att['c'] = 'LaPorte'
    if att['c'] == 'La Salle':
        att['c'] = 'La Salle'
    if att['c'] == 'La Salle' and att['s'] == 'IL':
        att['c'] = 'LaSalle'
    if att['c'] == 'La Moure':
        att['c'] = 'LaMoure'
    if att['c'] == 'De Soto' and att['s'] == 'MS':
        att['c'] = 'DeSoto'
    if att['c'] == 'De Soto' and att['s'] == 'FL':
        att['c'] = 'DeSoto'
    if att['c'] == 'De Soto' and att['s'] == 'LA':
        att['c'] = 'De Soto'
    if att['c'] == 'Mccone':
        att['c'] = 'McCone'
    if att['c'] == 'Mc Mullen':
        att['c'] = 'McMullen'
    if att['c'] == 'Mc Minn':
        att['c'] = 'McMinn'
    if att['c'] == 'Mc Kean':
        att['c'] = 'McKean'
    if att['c'] == 'Mc Cook':
        att['c'] = 'McCook'
    if att['c'] == 'Mc Duffie':
        att['c'] = 'McDuffie'
    if att['c'] == 'Mc Dowell':
        att['c'] = 'McDowell'
    if att['c'] == 'Mc Pherson':
        att['c'] = 'McPherson'
    if att['c'] == 'Mcpherson':
        att['c'] = 'McPherson'
    if att['c'] == 'Mckinley':
        att['c'] = 'McKinley'
    if att['c'] == 'Mckenzie':
        att['c'] = 'McKenzie'
    if att['c'] == 'Mc Henry':
        att['c'] = 'McHenry'
    if att['c'] == 'Mchenry':
        att['c'] = 'McHenry'
    if att['c'] == 'Mc Nairy':
        att['c'] = 'McNairy'
    if att['c'] == 'Mc Culloch':
        att['c'] = 'McCulloch'
    if att['c'] == 'Mccormick':
        att['c'] = 'McCormick'
    if att['c'] == 'Mcintosh':
        att['c'] = 'McIntosh'
    if att['c'] == 'Mc Intosh':
        att['c'] = 'McIntosh'
    if att['c'] == 'Mc Donough':
        att['c'] = 'McDonough'
    if att['c'] == 'Mc Lean':
        att['c'] = 'McLean'
    if att['c'] == 'Mclean':
        att['c'] = 'McLean'
    if att['c'] == 'Mcclain':
        att['c'] = 'McClain'
    if att['c'] == 'Mc Lennan':
        att['c'] = 'McLennan'
    if att['c'] == 'Mc Donald':
        att['c'] = 'McDonald'
    if att['c'] == 'Mccurtain':
        att['c'] = 'McCurtain'
    if att['c'] == 'W. Baton Rouge':
        att['c'] = 'West Baton Rouge'
    if att['c'] == 'E. Baton Rouge':
        att['c'] = 'East Baton Rouge'

    # misspellings
    if att['c'] == 'Scott Bluff':
        att['c'] = 'Scotts Bluff'
    if att['c'] == 'Menomonee':
        att['c'] = 'Menominee'
    if att['c'] == 'Northumberlnd':
        att['c'] = 'Northumberland'
    if att['c'] == 'Lapaz':
        att['c'] = 'La Paz'
    if att['c'] == 'Manassus Park city':
        att['c'] = 'Manassas Park city'
    if att['c'] == 'Manassus city':
        att['c'] = 'Manassas city'
    if att['c'] == 'Northwest Artic':
        att['c'] = 'Northwest Arctic'

    # the saints
    if att['c'] == 'St Joseph':
        att['c'] = 'St. Joseph'
    if att['c'] == 'St. John Baptist':
        att['c'] = 'St. John the Baptist'
    if 'Sainte' in att['c']:
        att['c'] = att['c'].replace('Sainte', 'Ste.')
    if 'Saint' in att['c']:
        att['c'] = att['c'].replace('Saint', 'St.')

    att['id'] = att['c'] + ', ' + att['s']
    issuers_by_county.append(att)
# print issuers_by_county

# STEP TWO: Return a unique list of issuers for each county
# convert list of dictionaries to a list of tuples where the tuples contain dict items.
# b/c tuples can be hashed, you can remove duplicate entries using `set`
# and then re-create your list of dicts from tuples with `dict`.
unique_issuers_by_county = [dict(t) for t in set([tuple(d.items()) for d in issuers_by_county])]

# STEP THREE: Group data by state and county
# first group data by state into a list of list of dicts
# then for each state, sort by county
# lastly, flatten and write to file
state = collections.defaultdict(list)

for d in unique_issuers_by_county:
    state[d['s']].append(d)

state_list = state.values()

sorted_counties_list = list()
# a list of list of dicts
for row in state_list:
    # a list of dicts
    sorted_counties = sorted(row, key=itemgetter('c'))
    sorted_counties_list.append(sorted_counties)

# list of list of dicts
flattened = [val for sublist in sorted_counties_list for val in sublist]
sorted_issuers = sorted(flattened, key=itemgetter('s'))

# find the number of counties w/ only one insurance provider
# first group by county and tally count of insurers
data_grp = collections.defaultdict(list)

for row in sorted_issuers:
    data_grp[row['id']].append(row['i'])

issuers_count = list()
for k,v in data_grp.items():
    att = dict()
    att['Number of Issuers'] = len(v)
    att['Issuers'] = v
    att['County'] = k
    issuers_count.append(att)

# STEP FOUR: Write to file
c.write_dict(sorted_issuers, 'filtered-csvs/test14-issuers-filtered.csv')
c.write_dict(issuers_count, 'filtered-csvs/test14-count.csv')
