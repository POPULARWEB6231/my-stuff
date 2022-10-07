import os
from datetime import date

def rename_file():
    # Find today's date to name the file.
    today = date.today().strftime("%m_%d_%Y_")

    # Find the file and rename it.
    old_name = r'C:/Users/slpol/python_work/fltp_files/downloads/DoeCommitteeList.txt'
    new_name = f"C:/Users/slpol/python_work/fltp_files/downloads/{today}DoeCommitteeList.txt"

    # Make sure not to overwrite if we already changed it.
    if os.path.isfile(new_name):
        print("The file already exists.")
    # Rename that sucker.
    else:
        os.rename(old_name, new_name)

rename_file()