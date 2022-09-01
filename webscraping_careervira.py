#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


urls= ['https://talentedge.com/xlri-jamshedpur/financial-management-course/', 'https://talentedge.com/iiit-allahabad/big-data-analytics-machine-learning-course-iiit-allahabad/', 'https://talentedge.com/xlri-jamshedpur/talent-management-course/', 'https://talentedge.com/iim-kozhikode/professional-certificate-program-in-business-analytics/','https://talentedge.com/xlri-jamshedpur/executive-development-program-strategic-management-course/', 'https://talentedge.com/mica-ahmedabad/advertising-management-public-relations-course', 'https://talentedge.com/iim-lucknow/integrated-marketing-strategy-course/', 'https://talentedge.com/xlri-jamshedpur/business-analytics-courses/', 'https://talentedge.com/xlri-jamshedpur/business-analytics-courses/', 'https://talentedge.com/iim-kozhikode/professional-certificate-program-in-strategic-management/', 'https://talentedge.com/iim-kozhikode/applied-financial-risk-management-course/', 'https://talentedge.com/iim-kozhikode/supply-chain-strategy-management-course/', 'https://talentedge.com/iim-lucknow/advanced-program-leadership-digital-era/', 'https://talentedge.com/xlri-jamshedpur/project-management-course/', 'https://talentedge.com/xlri-jamshedpur/data-science-course-python/', 'https://talentedge.com/iim-kozhikode/professional-certificate-program-marketing-sales-management-iim-kozhikode/']


# In[3]:


partner_course_url = []
title = []
learn_type = []
description = []
cover_image = []
delievery_method = []
instruction_type = []
content = []
what_we_learn = []
prerequisites = []
instructor_names = []
accreditation_name = []
accreditation_logo = []
accreditation_description = []
level = []
language = []
subtitles_language = []
pricing_type =[]
currency = []
course_financing_available = []
institute = []
personalized_teaching = []
live_class = []
job_assistance = []
internship = []
capstone_project = []


# In[4]:


for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #printing  KPI's
    
    #partner course url
    partner_course_url.append(url)
    
    #title
    tit = soup.find('h1', class_="pl-title").text
    title.append(tit)
    
    #learn type
    search_word1 = "Certification"
    search_word2 = "Degree"
    if (search_word1 in soup.text):
        learn_type.append("Certification")
    elif (search_word2 in soup.text):
        learn_type.append("Degree")
    else:
        learn_type.append("Diploma")
    
    #description
    descrip = soup.find('div', class_="desc")
    description.append(descrip)
    
    #cover image
    cov_imag = soup.find('figure', class_="mb-0" )
    cover_image.append(cov_imag)

    #delievery method
    search_word3 = "In-Campus"
    if (search_word3 in soup.text):
        delievery_method.append("Online+Offline")
    else:
        delievery_method.append("Online")
    
    #instruction type
    search_word4 = "faculty"
    if (search_word4 in soup.text.lower()):
        instruction_type.append("Instructor Paced")
    else:
        instruction_type.append("Self Paced")
    
    #content
    cont = soup.find('div', class_= "sylab-tab-ul")
    content.append(cont)
    
    #what we learn
    what_we_lea = soup.find('div', class_="pl-deeper-undstnd to_flex_ul").text.replace('\n','|')
    what_we_learn.append(what_we_lea)
    
    #prerequisites
    prerequis = soup.find('div', class_= "eligible-right-top-list").text.replace('\n', '|')
    prerequisites.append(prerequis)
    
    #instructor names
    instructor_na = soup.find_all('h4', class_= "best-fname")
    instructor_names.append(instructor_na)
    
    #accreditation_name
    accred_name = soup.find('h4', class_= "about-ititle").text
    accreditation_name.append(accred_name)
    
    #accreditation_logo
    accred_logo = soup.find('div', class_= "ii-image-g")
    accreditation_logo.append(accred_logo)
    
    #accreditation_description
    accred_description = soup.find('div', class_= "about-theinstitute").text.replace('\n', ' ')
    accreditation_description.append(accred_description)

    #level
    search_word5 = "advanced"
    if (search_word5 in soup.text):
        level.append("Advanced")
    else:
        level.append("Intermediate")
      
    #language
    language.append("English")
    
    #subtitles
    subtitles_language.append("English")
    
    #pricing type
    search_word6 = "Fee Structure"
    if (search_word6 in soup.text):
        pricing_type.append("Paid")
    else:
        pricing_type.append("Free")
        
    #currency
    search_word7 = "INR"
    search_word8= "USD"
    if (search_word7 and search_word8) in soup.text:
        currency.append("INR, USD")
    else:
        currency.append("INR")
        
    #course financing available
    search_word9 = "Instalment"
    if (search_word9 in soup.text):
        course_financing_available.append("TRUE")
    else:
        course_financing_available.append("FALSE")
        
    #institute
    institute.append("Talentededge")
    
    #personalized_teaching
    search_word10 = "personalized teaching"
    if (search_word10 in soup.text):
        personalized_teaching.append("TRUE")
    else:
        personalized_teaching.append("FALSE")
        
    #live class
    search_word11 = "Live"
    if (search_word11 in soup.text):
        live_class.append("TRUE")
    else:
        live_class.append("FALSE")
        
    #job assistance
    search_word12 = "job assistance"
    if (search_word12  in soup.text.lower()):
        job_assistance.append("TRUE")
    else:
        job_assistance.append("FALSE")
    
    #internship
    search_word13 = "internship"
    if (search_word13  in soup.text.lower()):
        internship.append("TRUE")
    else:
        internship.append("FALSE")
        
    #capstone project
    search_word14 = "capstone project"
    if (search_word14 in soup.text.lower()):
        capstone_project.append("TRUE")
    else:
        capstone_project.append("FALSE")
    


# In[5]:


webscrap2 = pd.DataFrame({"partner_course_url": partner_course_url ,"title": title, "learn_type": learn_type, "description": description,  "cover_image": cover_image, "delievery_method": delievery_method, "instruction_type": instruction_type, "content": content, "what_we_learn": what_we_learn, "prerequisites": prerequisites,  "instructor_names": instructor_names, "accreditation_name":  accreditation_name, "accreditation_logo": accreditation_logo, "accreditation_description": accreditation_description, "level": level, "language" : language, "subtitles_language": subtitles_language, "pricing_type": pricing_type, "currency": currency, "course_financing_available": course_financing_available, "institute": institute, "personalized_teaching": personalized_teaching, "live_class": live_class, "job_assistance": job_assistance, "internship": internship, "capstone_project": capstone_project})
webscrap2


# In[6]:


webscrap2.to_csv('webscrapedtalentedge.csv')

