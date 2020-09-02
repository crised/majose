import csv

def parse(row, countries):
    """
    For each row it parses the data,
    and structures it into a dictionary.

    The dictionary keys are the country names.
    Nested in that, it is another dictionary per index.
    Again, nested in that there is a dictionary with the index value for each:
    TOT, WMN, MN, HGH, LW.

    :param row: Each row of the csv file
    :param countries: Master dictionary
    """
    country = row[1]
    index = row[2]
    sub_index = row[6]
    value = row[-3]
    if '.' in value:
        value = float(value)
    else:
        value = int(value)

    if country in countries:
        country_dict = countries[country]
    else:
        country_dict = {}
        countries[country] = {}

    if index in country_dict:
        index_dict = country_dict[index]
    else:
        index_dict = {}
        country_dict[index] = index_dict

    assert sub_index not in index_dict
    index_dict[sub_index] = float(value)


def get_countries_dict():
    """
    Build a master index with all the countries and their indexes.

    This master index can server to support to create new
    lists to create new indexes creations.
    :return: the master dictionary.
    """
    with open('data.csv') as csvfile:
        countryreader = csv.reader(csvfile)
        indexes = set()
        countries = dict()
        for i, row in enumerate(countryreader):
            if i == 0:
                continue
            parse(row, countries)
            indexes.add(row[6])
        return countries


def get_orderly_countries():
    """
    This methods get the satisfaction index
    with total inequality (SW_LIFS, TOT).

    In addition, it does not consider an entry
    which is not a country.

    The list is sorted in ascending order.
    :return:
    """
    countries = get_countries_dict()
    countries_list = []
    for country in countries.items():
        if 'OECD' in country[0]:
            continue  # OECD is not a country
        countries_list.append((country[1]['SW_LIFS']['TOT'], country[0]))
    countries_list.sort()  # binary search candidate.
    return countries_list


def get_filtered_countries(thres=7):
    """"
    Assumes the threshold is of type number.

    It returns a list of countries with an index
    above certain threshold.
    """
    countries_list = get_orderly_countries()
    for i, country_tuple in enumerate(countries_list):
        if country_tuple[0] > thres:
            return countries_list[i:]
