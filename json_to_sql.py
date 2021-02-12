from sys import argv

import json
import os

# Get path to the location of this file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Open config.json file in location of this file
config = json.load(open(os.path.join(__location__, 'config.json')))

# Open .json to be parsed from cmd params
try:
    json_to_parse = json.load(open(argv[1]))
except FileNotFoundError:
    print('Wrong file or file path.')

# Replace illegal characters defined in config
# Cycle through the json objects
for dictionary in json_to_parse:
    # Check the desired json fields
    for key in config['json_keys_to_parse']:
        # Check for illegal characters and replace them by those defined in config
        for illegal_character in config['illegal_characters_to_replace']:
            dictionary[key] = dictionary[key].replace(illegal_character, 
                                                config['illegal_characters_to_replace'][illegal_character])

# Get the starting index of the table from config
id_seq = config['sql_id_start']

# Start building the query
sql_query = 'INSERT INTO ' + config['table_name'] + ' ('

# Add the desired collumns to the query
for column in config['sql_columns']:
    sql_query += column + ', '

sql_query += ') VALUES\n'

sql_query = sql_query.replace(', ) VALUES', ') VALUES')

# Add the data from formated json to query
for dictionary in json_to_parse:
    sql_query += '(' + str(id_seq)
    # Add the desired data
    for key in config['json_keys_to_parse']:
        sql_query += ', \'' + dictionary[key] + '\''
    sql_query += '),\n'
    id_seq += 1

sql_query += ';'

sql_query = sql_query.replace('),\n;', ');')

# Generate the sql file
write_file = open(os.path.join(__location__, 'formated_json.sql'), 'w')
write_file.write(sql_query)
write_file.close()










