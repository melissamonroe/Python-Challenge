# Dependencies
import os
import csv
import datetime
# from Resources import us_state_abbrev
# could not get it to run by importing

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


input_path = "PyBoss\Resources\employee_data.csv"

# Specify the file to write to
output_path = "PyBoss\Output\employee_data.csv"

names = []

with open(input_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',',)

    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    with open(output_path, 'w', newline='') as csvfile:
        i = 0
        for row in csvreader:

            newrow = []

            if i == 0:
                newheaders = ["Emp ID", "First Name",
                              "Last Name", "DOB", "SSN", "State"]
            else:
                # Emp ID
                newrow.append(row[0])

                names = row[1].split(' ')

                # First Name
                newrow.append(names[0])

                # Last Name
                newrow.append(names[1])

                # DOB
                dob_date = datetime.datetime.strptime(
                    row[2], "%Y-%m-%d")
                d = dob_date.strftime("%m/%d/%Y")
                newrow.append(d)

                # SSN
                ssn = row[3]
                formatted_ssn = "**-**-" + ssn[7:]
                newrow.append(formatted_ssn)

                # State
                # Exception has occurred: TypeError 'module' object is not subscriptable
                # could not get it to run by importing
                state = row[4]
                state = us_state_abbrev[state]

                newrow.append(state)

                print(row[0], names[0], names[1],
                      d, formatted_ssn, state)

            # Initialize csv.writer
            csvwriter = csv.writer(csvfile, delimiter=',')

            # write new header
            if i == 0:
                csvwriter.writerow(newheaders)
            else:
                # Write the first row (column headers)
                csvwriter.writerow(newrow)

            i += 1
            # break
