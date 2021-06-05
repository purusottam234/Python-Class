import operator

PEOPLE = [{'first': "Lucky", 'last': 'Sharma'},
          {'first': "Rahul", 'last': 'Sharma'},
          {'first': "Hari", 'last': 'Sharma'},
          {'first': "Ram", 'last': 'Sharma'}
          ]


def alphabetinames(list_of_dicts):
    return sorted(list_of_dicts,
                  key=operator.itemgetter('last', 'first'))


print(alphabetinames(PEOPLE))
