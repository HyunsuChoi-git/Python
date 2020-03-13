# from indeed import extract_indeed_pages, extract_indeed_jobs

# last_indeed_pages = extract_indeed_pages()
# indeed_jobs = extract_indeed_jobs(last_indeed_pages)

# print(indeed_jobs)


# 위 indeed에서 긁어온 정보들 메소드로 묶어
# 임포트 해주기
from crawling.jobCrawling.Test01.indeed import get_jobs as get_jobs_in
from crawling.jobCrawling.Test01.jobKorea import get_jobs as get_jobs_jo
from crawling.jobCrawling.Test01.saveJobs import save_file


indeed_jobs = get_jobs_in()
jobKorea_jobs = get_jobs_jo()

jobs = indeed_jobs + jobKorea_jobs
save_file(jobs)
