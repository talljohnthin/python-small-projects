from bs4 import BeautifulSoup
import aiohttp

# scrape with the following conditions
# 1. remote jobs
# 2. has salary provided


async def scraper(skill):
    async with aiohttp.ClientSession() as session:
        url = f'https://www.indeed.com/jobs?as_and={skill}&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=b4d4ed7cd136f07d'
        async with session.get(url) as response:
            request = await response.text()
            print("request:", request)
            soup = BeautifulSoup(request, 'lxml')
            job_list = []
            jobs = soup.find_all('a', class_="tapItem")

            for job in jobs:
                title_wrapper = job.find('h2', class_="jobTitle")
                title = title_wrapper.find('span').text
                company_location = job.find(
                    'div', class_="companyLocation").text
                salary = job.find('span', class_="salary-snippet")
                salary_text = ""

                if salary is None:
                    salary_text = "Not provided"
                else:
                    salary_text = salary.text

                obj = {
                    "title": title,
                    "company_location": company_location,
                    "salary": salary_text,
                    "link": 'https://www.indeed.com' + job['href']
                }

                if not salary is None:
                    if "remote" in obj["company_location"].lower():
                        job_list.append(obj)

            return job_list
