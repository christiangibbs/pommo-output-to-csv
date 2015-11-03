# pommo-output-to-csv
PoMMo output to csv is a simple script that takes the default subscriber export from PoMMo and converts the file to .csv format so the list can be used in other applications.

##1 - Requirements
Python must be installed on your Operating System

##2 - How to

Ensure that the file containing your subscribers is in the same directory as this python script and run the following command:

    $ python convert.py filename

filename examples: input.txt, this.rtf

##3 - Examples

A file named input.txt has the following data:

    email@example.com email2@example.com email3@example.com

Running the command:

    $ python convert.py input.txt
    
A file named output.csv is created:

    email@example.com
    email2@example.com
    email3@example.com
