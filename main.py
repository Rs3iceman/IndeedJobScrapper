# imports
import requests
import time 
import pandas
import bs4
from bs4 import BeautifulSoup

#File Number
fileCount = 1

#Amount of jobs per city
maxResults = 100

#Job Titles
jobSet ['software+developer']

#Cities
citySet ['Sheffield']

#Loop through every city
for city in citySet:

    #Loop through every Job Title
    for job in jobSet:

        #Start a timer and reset the page count
        startTime = time.time()
        pageCount = 0
        
        # Create a dataframe to store our data
        dataFrame = pandas.DataFrame(columns = ['unique_id', 'city', 'job','job_title', 'company_name', 'location', 'summary', 'salary', 'link', 'date', 'full_text'])

        for start in range(0, maxResults, 10):

            page = requests.get('http://www.indeed.com/jobs?q=' + job +'&l=' + str(city) + '&start=' + str(start))
            soup = BeautifulSoup(page.text, "lxml", from_encoding = "utf-8")
            divs = soup.find_all(name = "div", attrs = {"class" : "row"})

            if not divs:
                break

            for div in divs:

                num = (len(dataFrame) + 1)
                pageCount += 1

                jobData = []

                jobData.append(div['id'])
                jobData.append(city)
                jobData.append(job)
                jobData.append(retrieveJobTitle(div))
                jobData.append(retrieveCompany(div))
                jobData.append(retrieveLocation(div))
                jobData.append(retrieveSummary(div))
                jobData.append(retrieveSalary(div))
                jobData.append(retrieveLink(div))
                jobData.append(retrieveDate(div))

                #appending list of job post info to dataframe at index num
                dataFrame.loc[num] = jobData

                                    
            #Write to debug log
            writeToLog(('Completed =>') + '\t' + city  + '\t' + job + '\t' + str(cnt) + '\t' + str(start) + '\t' + str(time.time() - startTime) + '\t' + ('file_' + str(file)))

        #Saving dataframe as a local csv file 
        dataFrame.to_csv('jobs_' + str(file) + '.csv', encoding = 'utf-8')
           
    # increment file
    fileCount += 1

def retrieveJobTitle(div):
    #TODO

def retrieveCompany(div):
    #TODO

def retrieveSummary(div):
    #TODO

def retrieveSalary(div):
    #TODO

def retrieveLink(div): 
    #TODO

def retrieveDate(div):
    #TODO

def writeToLog(text):
    f = open('log,txt', 'a')
    f.write(text + '\n')
    f.close()
