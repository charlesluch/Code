************************************************************************
* CPT223 - Scripting Language Programming
* Study Period 1 2018 Assignment #2 (Python)
* Full Name        : Charles Luchetti
* Student Number   : s3612293
************************************************************************

                    PROGRAM : IF-THIS-THEN-THAT CLONE

ifttt.com is a program that uses third party APIs to deliver functionality to its users in the form of small, customizable widgets. In this assignment our cohort has been asked to clone the functionality of ifttt.com to a set of specifications provided by Dale Stanbrough at RMIT.

In order to run this program, it is important to make sure that the JSON configuration file exists in the same directory as the extracted files and that it contains the mandatory components for the called application to run: a service name, a program directory and a service description.

******************** what to expect from the program ********************

The program functions as follows:

 1.

 2.

****************** what to enter into the command line ******************

 * to run the configuration settings written by the student, enter the following into the command line at the directory of the extracted files:

> python  ./[filename of service].py "[output file].[file type]"

                                    OR

> python  ./morning.py "output.txt"

* if the configuration file you desire to use with this program is different to the one provided (ifttt.json) and you have made sure that it contains all the mandatory components (name, program, description) as mentioned earlier in this readme, you may redirect the configuration file by using the following commands:

> python  ./[filename of service].py "[output file].[file type]" "[alternate configuration file filename].json"

                                    OR

> python  ./append.py "output.txt" altConfigFile.json


************************ what errors are handled ************************



******* the possible extensions and applications for this program *******



******************** change log and outstanding work ********************

OUTSTANDING SPECS NOT REALISED:

 * Each service should return a status value, flow continues if 0 and stops if flow is 1

 * Each program should continually process all flows (attempt once per second)

 * Part 1 - Services to create:
    1. Morning, Afternoon, Evening
    2. Quit if false
    3. Not
   (4.)Service only continues if run every hour, every n mins or secs
   (5.)Service that returns sunrise time, sunset time
   (6.)Service that savs the time to a file, but only in the evening

===

   create a file with some data in it (i've got ones named true.txt, false.txt that just contain "True" and "False").
   Then I can run it against my service (I was testing my "not.py" service today) with...

   ./not.py < true.txt

   which says "run the program ./not.py, and have standard input read from the file true.txt, not the keyboard".

===

NOT.py

1. test interactively:
programInput = input("True or False?")

2.
 p = run(command, stdout=PIPE, input=programInput, encoding='utf-8')
which meant I could see my keyboard input (stdin) show up in every program as required.

programInput = p.stdout     #The output of the past program

FROM THE SPECS

command = ['date', '+%d/%m/%Y %H:%M:%S']
p = run(command, stdout=PIPE, input='', encoding='utf-8')
print(p.returncode)
print(p.stdout)

===

VERY IMPORTANT! If you want to communicate with the next process you -have- to write it to standard output with a print statement

===

Quit if false should return a "fail" error code so that your interpreter knows to stop that workflow.

===

 * Part 2 - what to do NB seperate submission!:
    1. each service has a configuration file CONFIG.JSON, types verified when flow is running, parameters section used to specify required values

> ./evening.py "any parameters you need for the program" -any "ke
y value pairs you need"

CHANGE LOG:

* configparser deleted, not using

* forecast is not required, time is.

OUTSTANDING WORK:

 * write a script to get the current time.

 * get time zone from geolocation provided and compute current time in that location based on a calculation

 * write: morning.py, afternoon.py, evening.py

 * clarify what is typed into the command line: LAT,LNG is not required, it is an API

 * http://ip-api.com/json for a much simpler geolocation API from google - "a preceding service that makes use of a geolocation API"

 * sys.exit(1) whenever something goes wrong, sys.exit(0) for exit:success

 * .json for geolocation needs changing - no long lat and fields are 3

 * confirm that the json keys for sunrise and sunset are correctly named in the fields part of the config file

 * optional: sundown
