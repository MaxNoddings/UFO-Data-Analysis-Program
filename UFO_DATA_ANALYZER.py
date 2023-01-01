#Max Noddings, CS21 - Final Project Program - DATA Collector!
#This is a program that will first provide some sort of user interface where they can select different options
#as to what function they would like to perform. Each function will do some sort of searching through the UFO
#TXT file and will return a result! The functions will be like a bunch of different factoids that you can choose
#from!

#First start the main function that will break up each UFO-report into categories. Each category will have its own list.
#The categories will be - date posted, city, state, shape of UFO, duration of sighting, description of sighting, and date uploaded!
def main():
    #Introduce the program!
    print("Hello, welcome to the UFO data analysis program!")
    print("\n")
    
    #Initialize 7 lists - one for each UFO report category.
    event_date = []
    city = []
    state = []
    shape = []
    duration = []
    description = []
    upload_date = []
    
    #Open the TXT file for reading.
    readfile_UFO = open("UFO_data.txt","r")

    #Assign a variable to line1 to start the while loop which will iterate through the data set and store each data catergory into
    #a list
    line1 = readfile_UFO.readline()

    while line1 != "":
        #Each report is broken up into 7 lines. Read each of the seven lines, strip the end of line characters, and append
        #them into their specified lists.
        line1_strip = line1.rstrip("\n")
        event_date.append(line1_strip)

        line2 = readfile_UFO.readline()
        line2_strip = line2.rstrip("\n")
        city.append(line2_strip)

        line3 = readfile_UFO.readline()
        line3_strip = line3.rstrip("\n")
        state.append(line3_strip)

        line4 = readfile_UFO.readline()
        line4_strip = line4.rstrip("\n")
        shape.append(line4_strip)
    
        line5 = readfile_UFO.readline()
        line5_strip = line5.rstrip("\n")
        duration.append(line5_strip)

        line6 = readfile_UFO.readline()
        line6_strip = line6.rstrip("\n")
        description.append(line6_strip)

        line7 = readfile_UFO.readline()
        line7_strip = line7.rstrip("\n")
        upload_date.append(line7_strip)

        #Read two more lines to reach the next UFO report.
        readfile_UFO.readline()
        readfile_UFO.readline()

        #Read the next line to begin the while loop again.
        line1 = readfile_UFO.readline()

    #Close the TXT file!
    readfile_UFO.close()

    #To signify that all the UFO data has been stored in lists, write a conformation message regarding how many UFO reports there are!
    print("There are a total of",len(event_date),"UFO reports in the database.")
    print("\n")

    #Display list of functions for the user.
    list_options(event_date,city,state,shape,duration,description,upload_date)

    #End of program.
    print("Shutting down program.")








#Make a function that will take in the state list and will determine how many reports there were in each state and then print that
#total for each state in a nice format!
def reports_by_state(state_list):
    #First, create an empty dictionary.
    states_dictionary = {}
    
    #Perform the word counter algorithm to determine how many times a specific state appears!
    for index_state in state_list:
        #If the state is already in the dictonary, add one to it's count!
        if index_state in states_dictionary:
            count = states_dictionary[index_state]
            count += 1
            states_dictionary[index_state] = count

        #If the state is not already in the dictionary, add it with a value, or count, of 1!
        else:
            states_dictionary[index_state] = 1
            
    #Format the results of the states and their number of reports in a table form!
    print("    State    Number of Reports")
    print("----------------------------------")

    #Make new dictionary that can be altered!
    mock_dictionary = states_dictionary.copy()
    
    #Display the results by looping through each key/state in the states-dictionary and it's assigned value or number of times that it
    #was reported!
    for rank in range(1,len(states_dictionary) + 1):
        #Find the key with the maximum value in the dictionary.
        max_key = max(mock_dictionary, key = mock_dictionary.get)

        #If rank is less than 10!
        if rank < 10:
            #If the state is blank:
            if max_key == "":
                print(rank,".","    ","  ","         ",mock_dictionary[max_key],sep = "")
            else:
                print(rank,".","    ",max_key,"         ",mock_dictionary[max_key],sep = "")
        else:
            print(rank,".","   ",max_key,"         ",mock_dictionary[max_key],sep = "")
            
        #Pop the specific key out of the dictionary so the  next highest city will be  printed diuring the next iteration.
        mock_dictionary.pop(max_key)








        

#Make a function that will take in the state and city list and will determine how many reports there were in each city. It will then
#ask the user to enter in the name of a city and will search the list. If that city is in the list it will print how many times a
#UFO was reported in that city. The program will keep looping until the user decides to stop.
def reports_by_city(state_list,city_list):
    #Create a new empty list for the city/state combination.
    city_state = []
    
    #Perform an operation that combines the state_list to the city_list into a new list of the format "Burlinton,VT".
    for index in range(0,len(state_list)):
        city_state.append(city_list[index] + "," + state_list[index])

    #Create an empty dictionary.
    city_dictionary = {}

    #Perform the word counter algorithm to determine how many times a specific element in city_state occurs.
    for city in city_state:
        #If the state is already in the dictonary, add one to it's count!
        if city in city_dictionary:
            count = city_dictionary[city]
            count += 1
            city_dictionary[city] = count

        #If the state is not already in the dictionary, add it with a value, or count, of 1!
        else:
            city_dictionary[city] = 1

    #Have the user input a city/state combination to start the loop.
    print("If you would like to search for city, enter the city followed by it's state with a comma in between.")
    print("(Ex - 'Burlington,VT').")
    print("If you would like to see the top 50 cities with the most UFO reports enter '50'.")
    print("\n")
    user_city = input("Input: ")
    print("\n")

    #Start a while loop the will keep asking the user for a city and displaying it's corresponding amount of reports until the user enters "q".
    while user_city != "b" and user_city != "B":
        #If user_city equals "5". Print the top 5 cities with the most UFO reports.
        if user_city == "50":
            #Print a nicely formatted header.
            print("    Reports         City")
            print("-----------------------------")

            #Make a new dictionary that can be altered by copying the old one!
            mock_dictionary = city_dictionary.copy()
            
            #Start a loop that will run 51 times to get the top 50 cities.
            for rank in range(1,51):
                #Find the key with the maximum value in the dictionary.
                max_key = max(mock_dictionary, key = mock_dictionary.get)

                #Print the key with the maximum value along  with how many reports it has!
                if rank < 10:
                    print(rank,".","   ",format(float(mock_dictionary[max_key]),"4.0f"),"          ", max_key, sep = "")
                else:
                    print(rank,".","   ",format(float(mock_dictionary[max_key]),"3.0f"),"          ", max_key, sep = "")

                #Pop the specific key out of the dictionary so the  next highest city will be  printed diuring the next iteration.
                mock_dictionary.pop(max_key)

            print("\n")
            
        #Enter how many times that city had a UFO report!
        elif user_city in city_dictionary:
            print("UFO reports in",user_city,":",city_dictionary[user_city])
            print("\n")

            #Ask the user if they would like to see all of the reports from that given city! If they want to display the reports!
            print("Would you like to see all the reports for ",user_city,"?",sep = "")
            user_descision = input("Enter 'y' for yes or 'n' for no. : ")
            print("\n")
            
            while user_descision != "n":
                if user_descision == "y" or user_descision == "Y":
                    #Seperate the user_city into a list with the 0 index being the city and the 1 index being the state.
                    user_city_split = user_city.split(",")

                    #Read through the text file. If the city and state match a spefic report then print that whole report!
                    #Open the TXT file for reading.
                    readfile_UFO = open("UFO_data.txt","r")

                    #Read the first line of the text file to start the loop.
                    line1 = readfile_UFO.readline()

                    while line1 != "":
                        #Each report is broken up into 7 lines. Read each of the seven lines and strip the end of line characters.
                        line1_strip = line1.rstrip("\n")

                        line2 = readfile_UFO.readline()
                        line2_strip = line2.rstrip("\n")

                        line3 = readfile_UFO.readline()
                        line3_strip = line3.rstrip("\n")

                        line4 = readfile_UFO.readline()
                        line4_strip = line4.rstrip("\n")

                        line5 = readfile_UFO.readline()
                        line5_strip = line5.rstrip("\n")

                        line6 = readfile_UFO.readline()
                        line6_strip = line6.rstrip("\n")

                        line7 = readfile_UFO.readline()
                        line7_strip = line7.rstrip("\n")

                        #If line 2 and line 3 equal user_city_split[0] and user_city_split[1] then print lines 1 through 7.
                        if line2_strip == user_city_split[0] and line3_strip == user_city_split[1]:
                            print(line1_strip)
                            print(line2_strip)
                            print(line3_strip)
                            print(line4_strip)
                            print(line5_strip)
                            print(line6_strip)
                            print(line7_strip)
                            print("\n")
                        
                        #Read two more lines to reach the next UFO report.
                        readfile_UFO.readline()
                        readfile_UFO.readline()

                        #Read the next line to begin the while loop again.
                        line1 = readfile_UFO.readline()

                    #Close the TXT file.
                    readfile_UFO.close()

                    #Make user descision equal to 'n' to stop the loop.
                    user_descision = "n"

                else:
                    print("Invalid input. Try Again.")
                    print("Would you like to see all the reports for ",user_city,"?",sep = "")
                    user_descision = input("Enter 'y' for yes or 'n' for no. : ")
                    print("\n")
                    
        else:
            print("There have been no UFO reports in",user_city)
            print("\n")

        #Ask the user for the name of a new city!
        user_city = input("Enter the city name to search for a city, enter 'b' to go back to the main menu , enter '50' for the top 50: ")
        print("\n")








#Make a function that will take in the event_date, city, state, and shape list. The function can then count all the times that the same shape was observed in the same city/state on the same day!
#The function can then ask the user if they would like to see all the reports, or just the reports in incriments of 20. 
def common_reports(event_date,city_list,state_list,shape_list,description_list):
    #Create two empty dictionaries.
    combination_dict = {}
    big_combination_dict = {}

    #Iterate through each item in list.
    for index in range(0,len(event_date)):
        #Modify the event date so it just displays the day and not the time as well.
        event_modify = event_date[index]
        modify_list = event_modify.split()
                
        #Assign two new variables, one is a combination of event,city,state,and shape the other is a combination of event,city,state,shape,and description.
        combination = modify_list[0] + "," + city_list[index] + "," + state_list[index] + "," + shape_list[index]
        big_combination = modify_list[0] + "," + city_list[index] + "," + state_list[index] + "," + shape_list[index] + "," + description_list[index] 

        #If combination is already in dictionary, add one to it's count!
        if combination in combination_dict:
            count = combination_dict[combination]
            count += 1
            combination_dict[combination] = count
        #if combination  isn't in the dictionary, add it with a value of 1.
        else:
            combination_dict[combination] = 1

        #If combination is already in dictionary, add one to it's count!
        if big_combination in big_combination_dict:
            count = big_combination_dict[big_combination]
            count += 1
            big_combination_dict[big_combination] = count
        #if combination  isn't in the dictionary, add it with a value of 1.
        else:
            big_combination_dict[big_combination] = 1

    #If a key in big combination occurs more than once, remove that key from the combination dictionary.
    for key in big_combination_dict:
        if big_combination_dict[key] > 1:
            modify_key = key.split(",")
            new_key = modify_key[0] + "," + modify_key[1] + "," + modify_key[2] + "," + modify_key[3]
            if new_key in combination_dict:
                combination_dict.pop(new_key)
                        
    #Initialize amount_multiple_reports variable and multiple_reports list.
    amount_multiple_reports = 0
    multiple_reports = []
            
    #For key in  dictionary, if it's value is more than one add to the "amount_multiple_reports" variable and append to the
    #multiple_reports list!
    for key in combination_dict:
        if combination_dict[key] > 1:
            amount_multiple_reports += 1
            multiple_reports.append(key)

    #Display how many times there were reports of the same shape on the same day in the same city.
    print("There were", amount_multiple_reports, "instances where there was a report of the same shape on the same day in the same city.")
    print("\n")

    #Ask the user if they would like to see all the reports of the same shape on the same day in the same city.
    user_decides = input("Would you like to see all of those reports? (Enter 'y' for yes 'n' for no): ")

    #While user_decides doesn't equal y or n.
    while user_decides != 'n' and user_decides != 'y':
        print("\n")
        print("Invalid input, try again.")
        print("\n")
        user_decides = input("Would you like to see all of those reports? (Enter 'y' for yes 'n' for no): ")
        print("\n")
    
    if user_decides == "y":
        #Initialize emtpy lists to append to.
        new_date_list = []
        new_city_list = []
        new_state_list = []
        new_shape_list = []
                
        #Split each item of the multiple_reports list up and add each to new state,city,shape, and time lists.
        for report in multiple_reports:
            fragment_report = report.split(",")
            new_date_list.append(fragment_report[0])
            new_city_list.append(fragment_report[1])
            new_state_list.append(fragment_report[2])
            new_shape_list.append(fragment_report[3])

        #Make a loop that iterates through the "new" list.
        for iteration in range(0,len(new_date_list)):
            #Open the TXT file for reading.
            readfile_UFO = open("UFO_data.txt","r")
                    
            #Read through the text file. If the date,city,state, and shape match a spefic report then print that whole report!
            #Read the first line of the text file to start the loop.
            line1 = readfile_UFO.readline()
                    
            while line1 != "":
                #Each report is broken up into 7 lines. Read each of the seven lines and strip the end of line characters.
                line1_strip = line1.rstrip("\n")
                line1_split = line1_strip.split()
                line1_final = line1_split[0]

                line2 = readfile_UFO.readline()
                line2_strip = line2.rstrip("\n")

                line3 = readfile_UFO.readline()
                line3_strip = line3.rstrip("\n")

                line4 = readfile_UFO.readline()
                line4_strip = line4.rstrip("\n")

                line5 = readfile_UFO.readline()
                line5_strip = line5.rstrip("\n")

                line6 = readfile_UFO.readline()
                line6_strip = line6.rstrip("\n")

                line7 = readfile_UFO.readline()
                line7_strip = line7.rstrip("\n")

                #If the lines match up, print the report!
                if line1_final == new_date_list[iteration] and line2_strip == new_city_list[iteration] and line3_strip == new_state_list[iteration] and line4_strip == new_shape_list[iteration]:
                    print(line1_final)
                    print(line2_strip)
                    print(line3_strip)
                    print(line4_strip)
                    print(line5_strip)
                    print(line6_strip)
                    print(line7_strip)
                    print("\n")

                #Read two more lines to reach the next UFO report.
                readfile_UFO.readline()
                readfile_UFO.readline()

                #Read the next line to begin the while loop again.
                line1 = readfile_UFO.readline()

            #Close the TXT file.
            readfile_UFO.close()









#Make a function where the user can enter any word and the program will display in how many reports that word occurs in! The function
#will then prompt the user if they would like to see all the reports that the word occurs in. If they respond yes then the function
#will print all the reports that have the specified "word" in.
def word_search():
    #Ask user for a word.
    word = input("Enter a word or enter 'b' to go back to the menue: ")
    #Change the word to all undercase!
    word_u = word.lower()

    while word_u != 'b':
        #Initialize count.
        count = 0
    
        #Open the TXT file for reading.
        readfile_UFO = open("UFO_data.txt","r")

        #Read through the text file. 
        #Read the first line of the text file to start the loop.
        line1 = readfile_UFO.readline()

        while line1 != "":
            #Each report is broken up into 7 lines. Read each of the seven lines and strip the end of line characters.
            line1_strip = line1.rstrip("\n")

            line2 = readfile_UFO.readline()
            line2_strip = line2.rstrip("\n")

            line3 = readfile_UFO.readline()
            line3_strip = line3.rstrip("\n")

            line4 = readfile_UFO.readline()
            line4_strip = line4.rstrip("\n")

            line5 = readfile_UFO.readline()
            line5_strip = line5.rstrip("\n")

            #Perform operations on line 6, which is the description, to eliminate special characters or any uppercase letters.
            line6 = readfile_UFO.readline()
            line6_strip = line6.rstrip("\n")
            line6_lower = line6_strip.lower()
            line6_p = line6_lower.replace(".","")
            line6_c = line6_p.replace(",","")
            line6_e = line6_c.replace("!","")
            line6_q = line6_e.replace("?","")
            line6_replace5 = line6_q.replace("(","")
            line6_replace6 = line6_replace5.replace(")","")
            line6_replace7 = line6_replace6.replace("/"," ")
            description_list = line6_replace7.split() 

            line7 = readfile_UFO.readline()
            line7_strip = line7.rstrip("\n")

            #If word is in description list.
            if word_u in description_list:
                count += 1

            #Read two more lines to reach the next UFO report.
            readfile_UFO.readline()
            readfile_UFO.readline()

            #Read the next line to begin the while loop again.
            line1 = readfile_UFO.readline()

        #Close the TXT file.
        readfile_UFO.close()

        #Print results.
        print("\n")
        print('"',word,'"'," was found in ",count," reports.",sep = "")
        print("\n")

        #Ask user if they would like to see the reports if count is greater than 0.
        if count > 0:
            yesno = input("Would you like to see those reports? (enter 'y' for yes 'n' for no) ")
            print("\n")
            while yesno != 'n' and yesno != 'y':
                print("Invalid input, try again.")
                yesno = input("Would you like to see those reports? (enter 'y' for yes 'n' for no) ")
                print("\n")
            if yesno == 'y':
                #Open the TXT file for reading.
                readfile_UFO = open("UFO_data.txt","r")

                #Read through the text file. If the date,city,state, and shape match a spefic report then print that whole report!
                #Read the first line of the text file to start the loop.
                line1 = readfile_UFO.readline()

                while line1 != "":
                    #Each report is broken up into 7 lines. Read each of the seven lines and strip the end of line characters.
                    line1_strip = line1.rstrip("\n")

                    line2 = readfile_UFO.readline()
                    line2_strip = line2.rstrip("\n")

                    line3 = readfile_UFO.readline()
                    line3_strip = line3.rstrip("\n")

                    line4 = readfile_UFO.readline()
                    line4_strip = line4.rstrip("\n")

                    line5 = readfile_UFO.readline()
                    line5_strip = line5.rstrip("\n")

                    #Perform operations on line 6, which is the description, to eliminate special characters or any uppercase letters.
                    line6 = readfile_UFO.readline()
                    line6_strip = line6.rstrip("\n")
                    line6_lower = line6_strip.lower()
                    line6_p = line6_lower.replace(".","")
                    line6_c = line6_p.replace(",","")
                    line6_e = line6_c.replace("!","")
                    line6_q = line6_e.replace("?","")
                    line6_replace5 = line6_q.replace("(","")
                    line6_replace6 = line6_replace5.replace(")","")
                    line6_replace7 = line6_replace6.replace("/"," ")
                    description_list = line6_replace7.split()  

                    line7 = readfile_UFO.readline()
                    line7_strip = line7.rstrip("\n")

                    #If word is in description list.
                    if word_u in description_list:
                        print(line1_strip)
                        print(line2_strip)
                        print(line3_strip)
                        print(line4_strip)
                        print(line5_strip)
                        print(line6_strip)
                        print(line7_strip)
                        print("\n")
                
                    #Read two more lines to reach the next UFO report.
                    readfile_UFO.readline()
                    readfile_UFO.readline()

                    #Read the next line to begin the while loop again.
                    line1 = readfile_UFO.readline()

                #Close the TXT file.
                readfile_UFO.close()

        word = input("Enter a word or enter 'b' to go back to the menue: ")
        word_u = word.lower()
            
       

        
            
        



    


#Make a function that will take in all the lists from main and will display all the different UFO searching functions to the user.
#This funtion will loop until the user decides to quit the program!
def list_options(event_list,city_list,state_list,shape_list,duration_list,description_list,upload_date_list):
    print("What UFO data would you like to look at?")
    print("Enter '1' for the reports per state.")
    print("Enter '2' for the reports per city.")
    print("Enter '3' for reports with the same day, place, and shape.")
    print("Enter '4' to do a word search.")
    print("Enter 'quit' to shut down the program.")
    print("\n")
    user_option = input("Enter your input: ")

    #Start a loop, keep running as long as user doesn't want to quit.
    while user_option != "quit":
        if user_option == "1":
            print("\n")
            reports_by_state(state_list)
            print("\n")
        elif user_option == "2":
            print("\n")
            reports_by_city(state_list,city_list)
        elif user_option == "3":
            print("\n")
            common_reports(event_list,city_list,state_list,shape_list,description_list)
        elif user_option == "4":
            print("\n")
            word_search()
            print("\n")
        else:
            print("\n")
            print("Invalid input. Try again.")
            print("\n")

        #Re-iterate menue.
        print("What UFO data would you like to look at?")
        print("Enter '1' for the reports per state.")
        print("Enter '2' for the reports per city.")
        print("Enter '3' for instances of multiple reports on the same day.")
        print("Enter '4' to do a word search.")
        print("Enter 'quit' to shut down the program.")
        print("\n")
        user_option = input("Enter your input: ")
        


         
                      
main()









            

    
    
