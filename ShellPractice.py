# Overview: This program is being used as a proof of ability for the Python Programming language
# Author: Jacob Parker
# Objectives:
# 1. pass a string variable to the script as an argument.
# 2. produce a list of the individual characters in the passed string.
# 3. append the necessary components for a URL of the provided string (www, .com, etc.) unless those components already exist. make a get request and check status code.

# use the requests library for URL opening and HTTPS functionality.
import requests
# use the argparse library for parsing optional CLI arguments when executing script
import argparse

# create parser object
parser = argparse.ArgumentParser()
# add Echo functionality to repeat passed string back to SHELL
parser.add_argument("--echo", help="Echo back the string passed.")
# add Iteration functionality to print each character of a string to SHELL
parser.add_argument("--iterate", help="print a list of characters of the string passed.")
# add URL functionality which makes a string into a URL and opens the URL
parser.add_argument("--URL", help="Transform the provided string into a URL by appending 'https://www.' and '.com' to the ends of the string")
args = parser.parse_args()

if args.echo:
    # print the provided argument when Echo is called.
    print(args.echo)

elif args.iterate:
    # Attempt to iterate through the provided string as an array and print each index
    myString = args.iterate
    x = 0
    # iterate through string and print in formatting
    for i in myString:
        print("c[%d] = %s"%(x, i))
        x = x + 1

elif args.URL:
    # Transform a string to a URL.
    myDomain = args.URL
    # Make a full URL by concatenating the necessary components
    myURL = ("https://www." + myDomain + ".com")
    print(myURL)
    # Open the URL and report success or failure
    response = requests.get(myURL)
    # check response code and print it unless its not found
    if response.status_code != 404:
        print(response.status_code)
    else:
        print("404: Server not found.")
 
else:
    # no arguments passed to the script
    print("No arguments passed.")

