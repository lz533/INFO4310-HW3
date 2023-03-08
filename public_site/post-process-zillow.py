import csv


def passes_filter(row):
    # Filter criteria:
    if len(row['Bathroom']) < 1: # Keep only listings that have bathroom data
        return False
    else:
        return True


# import and run passes_filter
data = []
header = []

with open('zillow_pittsburgh.csv', 'r') as f:
    reader = csv.DictReader(f)

    header = reader.fieldnames
    for row in reader:
        if passes_filter(row):
            # TODO: additional processing here
            data.append(row)

# name the output file
with open('zillow_pittsburgh_filtered.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
    print('processed')
