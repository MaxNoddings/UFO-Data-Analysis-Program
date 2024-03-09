# <u>UFO Data Analysis Program</u>

This is a program that I made to analyze a large amount of data from NUFORC (National UFO Reporting Center). 

I've always been fascinated by the idea of UFO's and extraterrestial life (conspiracies aside), and there is a ton of UFO reporting data on NUFORC.org, so this was a fun opportunity to scrape 
all of the data on NUFORC perform some different forms on analysis on it. 

For this project, I first utilized the BeautifulSoup python library to download all of the UFO report data and organize it into a txt file (only txt file with all UFO reports data included in GitHub. Next, I built a python script 
that the user could interact with via the command line. 

The main python script gives the user the ability to (1) view the amount of UFO reports by USA state, (2) view the amount of UFO reports in each USA city, or see the top 50 most reported USA cities, (3) view instances of reports that 
were made in the same city on the same day, and (4) do a word search and view all reports that included a specific word or phrase in the report descripiton.

To run the program, download the UFO_DATA_ANALYZER.py and UFO_data.txt into the same folder and then run the UFO_DATA_ANALYZER.py program through the comman line. 
