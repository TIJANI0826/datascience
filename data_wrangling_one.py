import gzip
import simplejson as json
import statistics

with gzip.open('./pw-data/201701scripts_sample.json.gz', 'rb') as f:
    scripts = json.load(f)

with gzip.open('./pw-data/practices.json.gz', 'rb') as f:
    practices = json.load(f)



def describe(key):
    scripts_item = sorted([scripts[x][key] for x in range(len(scripts))])
    total = sum([scripts[x]['items'] for x in range(len(scripts))])
    avg = sum([scripts[x]['items'] for x in range(len(scripts))])/len(scripts)
    s = (sum([((scripts[x]['items'] - avg) ** 2) for x in range(len(scripts))]) / len(scripts)) ** 0.5
    q25 = scripts_item[(len(scripts_item)//4)]

    med = scripts_item[len(scripts_item)//2]
    q75 = scripts_item[(3 * len(scripts_item)//4)]

    return (total, avg, s, q25, med, q75)

summary = [('items', describe('items')),
           ('quantity', describe('quantity')),
           ('nic', describe('nic')),
           ('act_cost', describe('act_cost'))]

bnf_names = {x['bnf_name'] for x in scripts}

"""
We want to construct "groups" identified by 'bnf_name', where each group is a collection of prescriptions (i.e. dictionaries from scripts). We'll construct a dictionary called groups, using bnf_names as the keys. We'll represent a group with a list, since we can easily append new members to the group. To split our scripts into groups by 'bnf_name', we should iterate over scripts, appending prescription dictionaries to each group as we encounter them.
"""
groups = {name: [] for name in bnf_names}
for script in scripts:
    if script['bnf_name'] in groups.keys():
        groups[script['bnf_name']].append(script)
"""
Now that we've constructed our groups we should sum up 'items' in each group and find the 'bnf_name' with the largest sum. The result, max_item, should have the form [(bnf_name, item total)], e.g. [('Foobar', 2000)].

"""
max_item = []
a = len(groups.keys())
for bnf_name,value in groups.items():
    items = []
    for group in value:
        items.append(group['items'])
    max_item.append((bnf_name,sum(items)))


# max_item = sorted(max_item ,key=lambda x : x[0], reverse=False)
max_item = [max(max_item,key=lambda x: x[1])]
# print(max_item)


"""
Our data set is broken up among different files. This is typical for tabular data to reduce redundancy. Each table typically contains data about a particular type of event, processes, or physical object. Data on prescriptions and medical practices are in separate files in our case. If we want to find the total items prescribed in each postal code, we will have to join our prescription data (scripts) to our clinic data (practices).

Find the total items prescribed in each postal code, representing the results as a list of tuples (post code, total items prescribed). Sort your results ascending alphabetically by post code and take only results from the first 100 post codes. Only include post codes if there is at least one prescription from a practice in that post code.

NOTE: Some practices have multiple postal codes associated with them. Use the alphabetically first postal code.

We can join scripts and practices based on the fact that 'practice' in scripts matches 'code' in practices. However, we must first deal with the repeated values of 'code' in practices. We want the alphabetically first postal codes.
"""
print(scripts[1])
print(practices[1])

practice_postal = {}
for practice in practices:
    if practice['code'] in practice_postal:
        practice_postal[practice['code']] = scripts['practice']
    else:
        practice_postal[practice['code']] = scripts['practice']

assert practice_postal['K82019'] == 'HP21 8TR'