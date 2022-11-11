#The Data We Need To Receive
    #the path to the CSV 
        #Resources/election_results.csv
    #DEPENDENCIES
        #Dependencies are a programming script that someone else has written that increases the functional programming of the code
            #EXAMPLE - Datetime module
                #Datetime --> Datetime Classes --> Datetime Methods
                 #Import the datetime class from the datetime module
                    # import datetime
                 #Use the now() attribute on the datetime class to get the present time
                    # now = datetime.datetime.now()
                 #Print the present time
                    # print("The time right now is", now)
                #The output should be
                    #The time right now is 2019-09-18 14:11:42.394131
                #To reduce the confusion on importing a module with the same name as a class we can use an abbreviated alias dt for the datetime module
                    #Import the datetime class from the datetime module
                        # import datetime as dt
                    #Use the now() attribute on the datetime class to get the present line
                        # now = dt.datetime.now()
                    #Print the present time
                        # print("The time right now is ", now)

    #PACKAGES
        #Packages are folders that contain a set of python modules
        #folders in packages contain various subpackages or other folders
        #To import packages, we use the import statement, as we did with the datetime module

    #MODULES
        #Modules are a separate software component, usually python files with a .py extension
            #The name of the module will be the name of the file
            #Modules are easy and provide reusability with a simple statemet like import fatetime

    #THE CSV MODULE
        #the csv module is imported by using the import statement followed by the module name, csv
        #STEPS 
            #Launch the python inperpreter
            #Type import csv to import the module
            #Press Enter
            #Type dir(csv). The "dir" is short for "directory"
            #python interpreter should look like this
                # >>> import csv
                # >>> dir(csv)
            #output should look like 
                #['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', 'excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'reduce', 'register_dialect', 'unregister_dialect', 'writer']
#import csv
#dir(csv)
                    #If you look closely at the output theres a function called reader
                        #We'll use this function to read the CSV file that contains the election data
                        #Using the dir() function, we can pass:
                            #A python module, like the csv module, THe dir() function will return all the functions available in the csv module
                            #A variable, like a dictionary {'key':'value'}, for example the counties_dict dictionary
                                #The dir() function will return all the functions available on that variable
                        #A data type, like str. The dir() function will return all the attributes and methods that can be used with the str date type
        #FILE TYPES
            # a text file can be opened in a text editor like VS Code, TextEdit on Mac
                # a CSV file is a text file 
                # the data in a text file is encoded as text using ASCII or Unicode
            # a binary file contains data that has not been converted to text. Binary files cannot be opened with a text editor
                # Binary numbers, or base-2 numbers, are numbers that are written with only ones and zeros
                # In binary, we use the digits 0 and 1 to represent how many times a power of 2 is included in a number
        
        #OPEN A FILE
            #you can access a file in a folder on the computer if  you know the direct file path
            #The general format for opening a file is
                #file_variable = open(filename, mode)
                    #file_variable is the name of the variable that will reference the file object
                    #filename is a string specifying the name of the file
                    #mode is a string specifying the mode for reading or writing the file object, The possible modes are:
                        # "r": Open a file to be read
                        # "w": Open a file to write to it 
                            #This will overwrite an existing file and create a file if one does not already exist
                        # "x": Open a file for exclusive creation. If the file does not exist, it will not create one
                        # "a": Open a file to append data to an existing file. 
                            # If a file does not exist, it creates one, if a file has been created the data will be added to the file
                        # "+": Open a file for reading and writing
        
# READ DATA FROM A FILE
#Direct Path to the File
#Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file
#election_data = open(file_to_load, 'r')

# To do: perform analysis

# Close the file
 #election_data.close()

#Closing a file disconnects the program from the file
    #It's important that you close the file after you read a file and write data to a file
        # When you read data from a file and it is not closed at the end of the operation, you can lose some of the data
        # When you write data to a file, the data is not stored in the file at first
        # It is written to a "buffer" in the computer memory and may be overwritten later if the file is not closed
        # Once you close the file, the data is stored in the file
# Python has a way to read and write to a file without needing to use the open() and close() functions every time
# We simply replace the open() function with the "with" statement
    # The with statement opens the file and ensures proper acquisition or release of any data without haveing to close the file
        # This ensure that the data isn't lost or corrupted
    # The format for the with statement is the following
            #with open(filename) as file_variable:
            #the file_variable is used to reference the file object throughout the script

#Editing the file assignment variable, file_to_load
    #Open the election results and read the file
#with open(file_to_load) as election_data:
    #The width statement ends with a colon, which means we need to indent on the next line, as we did with if-else statements and for loop

    #To do: perform analysis
    #print(election_data)

#The output should look like this
    # <_io.TextIOWrapper name='Resources/election_results.csv' mode='r' encoding='UTF-8'>
        # the _io.TextIOWrapper is a Python class that will allow us to read or write data to and from the file when we used the appropriate methods and attributes
        # The name represents the path of the file object, and the computer tells us that the file is open "read" mode with UTF-8 encoding

# INDIRECT PATH TO THE FILE
    # To access and open a file for which the direct path is unknown, we use the os module 
    # The os module allows us to interect with our operating system 
    # We can see all the different attributes and methods that the os module uses by importing the module and typing print(dir(os)) in the Python interpreter
        # import os
        # dir(os)
# CHAINING 
    # a programmatic style that is used for making multiple method calls on the same object 
    # This is a common practice that makes code look clean and concise 
        # to declare a variable for the file to load, connect the os.path submodule with the join()
        #inside the parentheses of the join() function, we will add the folder and file to join together
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file
#with open(file_to_load) as election_data:
    #print the file object
   #print(election_data)

#WRITE TO FILES WITH PYTHON
    #Create a filename vaiable to a direct or indirect parth where the file is to be located
    #Use the open() function in the "w" mode to open a file and write data to the file
        #This creates an error
            #The error is an IOError, which is an "Input/Output" error, meaning that we used an output directory, 
                # 'analysis/election_analysis.txt', that doesn't exist with the given file path.
            #The error states that there is no file or directory 'analysis/election_analysis.txt'. 
                #This error occurs because we don't have a folder named "analysis" where the election_analysis.txt file should be saved.

    # Create a filename variable to a direct or indirect path to the file.
        #file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Using the open() function with the "w" mode we will write data to the file.
        #open(file_to_save, "w")

    # Use the open statement to open the file as a text file.
        #outfile = open(file_to_save, "w")

    # Write some data to the file.
        #outfile.write("Hello World")

    # Close the file
        #outfile.close()

#We can make this code cleaner and more precise using the with statements instead of open() and close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
    #with open(file_to_save, "w") as txt_file:

    # Write some data (three counties) to the file.
        #Dont forget to add coma and spaces so it doesnt look look like ArapahoeDenverJefferson
            #txt_file.write("Arapahoe, ")
            #txt_file.write("Denver, ")
            #txt_file.write("Jefferson, ")
        #Make it cleaner by adding it all to one line
            #txt_file.write("Arapahoe, Denver, Jefferson")
    #If you want to write the texts in separate lines
        #The newline escape sequence will create a newline, like pressing "return" when it is read. 
        #Everything after the \n will be on the next line.
        # Write three counties to the file.
        #txt_file.write("Counties in the Election\n_____________________________\nArapahoe\nDenver\nJefferson")

#Read and Analyze the data here
#Open the election results and read the file.
 #with open(file_to_load) as election_data:

    # Read the file object with the reader function.
     #file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

    # Print the header row.
     #headers = next(file_reader)
     #print(headers) 


#1. THE TOTAL NUMBER OF VOTES CAST
    #To count up all the votes, we need to initialize the variable
    # This is called the accumulator and increments by 1 as we read each row in the for lop
    # For convenience we will initialize a variable called total_votes to zero
        #total votes must be places above the code where we open the file
        #this is because the total_votes variable must be equal to zero
    #After the headers we can iterate through each row and increment a variable by 1 
    #Standard Python format to increment a variable is number = number + 1
        #This can be augmented to number += 1

#Initialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options = []
candidate_name = 0
# Candidate Votes
    # Declare the empty dictionary
candidate_votes = {}

#Vote percentage
vote_percentage = 0
votes = 0

# Winning Candidate
winning_candidate = ""
# Winning Count Tracker
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

#Print the total votes
#print(total_votes)

#2. A COMPLETE LIST OF CANDIDATES WHO RECIEVED THE VOTES
    #to get the candidate from each list when iterating through the row we can use indexing on the for loop variable, row
    #the Candidate column is the third column that has the second index
    #so we would use, row[2] to reference the Candidate column

#Print candidate name from each row
        candidate_name = row[2]

# Add the candidate_name to the candidate_options list using the append() method
# The append() method adds items to a list
        # candidate_options.append(candidate_name)

# Print the candidate list
# print(candidate_options)

# To get the unique names in the candidate_options list
    # we can use an if statement with the not in membership operator to check if the candidate has been added to the list. 
#If the candidate's name has been added to the list
    # then the next time the candidate's name is found in a row using the for loop, it will not be added to the list.
#The if statement needs to be nested inside the for loop while we are iterating through each row

# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
    # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
# print(candidate_options)

#3. THE TOTAL NUMBER OF VOTES EACH CANDIDATE WON
    # Best way to do this is to iterate a dictionary
        # The dictionary structure will look similar to this candidate_votes = {"candidate_name1": votes, "candidate_name2": votes, "candidate_name3": votes}
    # To create this dictionary, we first need to declare an empty dictionary, 
        # candidate_votes = {}, as we did with the empty candidate_options list. 
        # BEGIN TRACKING NUMBER OF VOTES
            candidate_votes[candidate_name] = 0
        # ADDING VOTES TO EACH CANDIDATE
           # The standard Python format to increment a variable is number = number + 1, which can be augmented to number += 1. 
        candidate_votes[candidate_name] += 1
            # This has to be out of the if statement but aligned with the for loop in order to track votes
# Print the candidate vote dictionary
print(candidate_votes)

# 3. THE PERCENTAGE OF VOTES EACH CANDIDATE HAS WON
    # vote_percentage = (votes / total_votes) * 100
        # The votes are the values of each candidate_name in the candidate_votes dictionary
        # To get a percentage
            # we need to convert votes and total_votes to floating-point decimal numbers 
                # This is because the votes in the dictionary and the total_votes are integers.

# Determine the percentage of votes for each candidate by looping through the counts.

# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

#5. THE WINNER OF THE ELECTION BASED ON POPULAR VOTE
    # Use an if statement in a for loop
        # Use an if statement to check if the first vote count for a candidate is greater than zero.
        # If the statement is true, then that vote count will be equal to the "winning count."
        # At the same time, we can set that candidate's percentage of the vote equal to the "winning percentage."
        # Then we can select the candidate as the "winning candidate" from the candidate_options list.
        
        #  Print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Determine winning vote count and candidate

            # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    
#  print out the winning candidate, vote count and percentage to terminal.       
winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")

print(winning_candidate_summary)