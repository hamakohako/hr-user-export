import json
import csv

def export_json(exportfile, users):
    json.dump(users, exportfile, indent=4)
    exportfile.close()

def export_csv(exportfile, users):
    exportfile.write('name,id,home,shell\n')
    writer = csv.writer(exportfile)
    rows = []
    for user in users:
        rows.append([user['name'], user['id'], user['home'], user['shell']])
    # shorthand
    # rows = [[user['name'], user['id'], user['home'], user['shell']] for user in users]
    writer.writerows(rows)
    exportfile.close()