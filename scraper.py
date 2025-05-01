#AITC 352 Tips & Tricks Presentation
#Eli Sauerwalt
#4.29.2025

#It's a simple webscraper for static websites. The example is built around a site used in a RealPython tutorial, but could be adapted to work for any static site. 
#If you want to work with a dynamic site use this library: https://pypi.org/project/requests-html/


import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path
from datetime import datetime

# Get user's desktop directory for later 
desktop = Path.home() / "Desktop"

# Define the JobPosting class
class JobPosting:
    def __init__(self, title, company, location, link):
        self.title = title
        self.company = company
        self.location = location
        self.link = link

#STEP 1----------
#Site to scrape
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

html_page = (page.text)

#print(html_page)


# create BS4 html object with scraped html as input. Second param specifies parser type
# parser options can be foung here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#differences-between-parsers
soup = BeautifulSoup(html_page, 'html.parser')

#-----STEP2------------
#Look for HTML element that contains job postings
#NOTE: can do this part in REPL env.
#NOTE: edit for alternative source demonstration
jobListings = soup.find(id="ResultsContainer")

#----STEP 3----------
#prettify() just dispalays all content within the class id

#print(jobListings.prettify())

#--------STEP 4--------
#isolate jobs
#find_all should return an array of relevant elements
jobCards = jobListings.find_all("div", class_="card-content")

# for job in jobCards:
#     print(job, end="\n")


#-------STEP 5---------
#Further isolate metadata
jobCards = jobListings.find_all("div", class_="card-content")

for job in jobCards:
   jobTitle = job.find("h2", class_="title")
   jobCompany = job.find("h3", class_="company")
   jobLocation = job.find("p", class_="location")
#    print("--------------------------------")
#    print(jobTitle.text.strip(), "\n")
#    print(jobCompany.text.strip(), "\n")
#    print(jobLocation.text.strip(), "\n")
#    print("--------------------------------")

#----STEP 7-------
#Filter for a specific job title
#Find parents of adribute used to filter
developerJobs = jobListings.find_all(
    "h2", string=lambda text: "developer" in text.lower())

#Create list of elements that include all info you want about each job
developerJobCards = [
    h2Element.parent.parent.parent for h2Element in developerJobs
]

#iterate over each developerJob to get elements w/ relevant info.
#add each listing as a JobPosting object to list

jobObjects = []
for devJob in developerJobCards:
    devJobTitle = devJob.find("h2", class_="title").text.strip()
    devJobCompany = devJob.find("h3", class_="company").text.strip()
    devJobLocation = devJob.find("p", class_="location").text.strip()
    
    #get the urls associated with each job because this is kind of useless otherwise
    #This site has 2 links for each job posting. We only need the second one so we have to do a little thing with an array
    linkURL = devJob.find_all("a")[1]["href"].strip()
    
    job = JobPosting(devJobTitle, devJobCompany, devJobLocation, linkURL)
    jobObjects.append(job)
    

    print(devJobTitle, "\n")
    print(devJobCompany, "\n")
    print(devJobLocation, "\n")
    print(f"Apply here: {linkURL}\n")
    
    
#---STEP 8----
#Save jobs to csv file 
#Save to desktop 
#Title csv file dynamically with file creation time stamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

fileName = f"developer_jobs_{timestamp}.csv"
output_file_path = desktop / fileName
with open(output_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Headers
    writer.writerow(["Title", "Company", "Location", "Apply Link"])  
    #Adding rows for each job
    for job in jobObjects:
        writer.writerow([job.title, job.company, job.location, job.link])
        
print(f"CSV saved to: {output_file_path}")