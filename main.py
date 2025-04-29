import requests
from bs4 import BeautifulSoup

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

print(jobListings.prettify())

#--------STEP 4--------
#iscolate jobs
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

#iterate over each developerJob to get elements w/ relevant info
for devJob in developerJobCards:
    devJobTitle = devJob.find("h2", class_="title")
    devJobCompany = devJob.find("h3", class_="company")
    devJobLocation = devJob.find("p", class_="location")
    
    linkURL = devJob.find_all("a")[1]["href"]
    
    
    print("---")
    print(devJobTitle.text.strip(), "\n")
    print(devJobCompany.text.strip(), "\n")
    print(devJobLocation.text.strip(), "\n")
    print(f"Apply here: {linkURL}\n")
    print("---")
    
#---STEP 8----
#get the urls associated with each job because this is kind of useless otherwise
#This site has 2 links for each job posting. We only need the second one so we have to do a little thing with an array
