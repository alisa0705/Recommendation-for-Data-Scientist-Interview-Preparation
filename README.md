[![Python application test with Github Actions](https://github.com/nogibjj/Alisa_Project4/actions/workflows/build.yml/badge.svg)](https://github.com/nogibjj/Alisa_Project4/actions/workflows/build.yml)
# Alisa_Project4:Youtube Recommendation for Data Scientist Interview Preparation

<img width="274" alt="Screen Shot 2022-12-03 at 10 10 58 PM" src="https://user-images.githubusercontent.com/89174034/205472379-f00ee3d4-3d1c-4ed9-890f-828ea3d6ff85.png">
The aim of this project is to create a microservice that returns a JASON payload, and also performs continuous integration(CI) through Github actions as well as deploy change (CD) through Fast API. I used the example of getting youtube recommendation for data scientist interview preparation. 



Steps: 
 
1. Create a Microservice that returns a JSON payload and performs a Data Engineering related task
2. Push tested source code to Github and perform Continuous Integration with Github Actions (or similar SaaS Build service)
3. Configure Build Server to Deploy Changes on build (Continuous Delivery)
4. Create realistic API


* Install youtubesearchpython package: : `pip install youtubesearchpython`

# Output Example
<img width="1000" alt="Screen Shot 2022-12-03 at 10 12 38 PM" src="https://user-images.githubusercontent.com/89174034/205472458-90144b44-36ff-48c9-8242-3a38b289b165.png">

* When selecting `/video_suggestions` and then search 'data science intern interivew'

<img width="1240" alt="Screen Shot 2022-12-03 at 10 13 04 PM" src="https://user-images.githubusercontent.com/89174034/205472469-13918b5b-9051-4268-80f3-13cc4e6af2e0.png">


* When selecting `/channels_Search` and then search 'data science job interview preparation'

<img width="1261" alt="Screen Shot 2022-12-03 at 10 15 56 PM" src="https://user-images.githubusercontent.com/89174034/205472547-b070ea05-beed-4dc7-aa97-bc1db7d39725.png">

The output youtube channel: 

<img width="1258" alt="Screen Shot 2022-12-03 at 10 16 16 PM" src="https://user-images.githubusercontent.com/89174034/205472552-c862dd4b-9bd3-46f5-b684-c08143c033b2.png">


 




MakeFile
![image](https://user-images.githubusercontent.com/89174034/205471946-a78bb899-5cb5-4a71-af82-16c95d620f69.png)


<img width="1282" alt="Screen Shot 2022-12-03 at 10 18 11 PM" src="https://user-images.githubusercontent.com/89174034/205472600-c4777ad8-0d3d-42d2-95a2-ed43bd1b3a61.png">


# Result of CodeBuild

<img width="562" alt="Screen Shot 2022-11-30 at 6 58 38 PM" src="https://user-images.githubusercontent.com/89174034/204933519-76f6dc5b-ab21-497d-b4e8-539b052e42f8.png">
