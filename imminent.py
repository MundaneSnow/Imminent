import csv

### database management
def write_csv(data, arg2, arg3):
    """write data to csv file"""

    with open("data.csv", newline='') as csvfile:
        # csv writer object
        writer = csv.writer(csvfile)

        # to write to file: writer.writerow([thing1, thing2, ...])

### main
def main():
    """This is the main function"""

    # check database for tracking options
    # if empty prompt to add subject

    # present tracking options

    # calculate timedelta

    # printing/updating the time
