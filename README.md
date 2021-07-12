# Smart_License_Check
This scripts connects to networks devices using Scrapli, executes a show version command and captures the Smart licensing status.

# Requirements
scrapli
Due to scrapli´´s compalitibilty, this scrips runs on mac or linux OS

# Run the Script
python smart_license_status.py

# Inputs
CSV host file with Hostname, IP Address, SSH port

# Sample execution
![image](https://user-images.githubusercontent.com/80859980/125355047-242d1d00-e32a-11eb-916e-30a3dd9f2671.png)

# Output
You get a CSV file, "Smart_License_Status.csv", with the Hostname, IP Address and the Status.
If there are connectivity errors or credentials are invalid, the status field will read "Unauthorized/Unreachalbe"
