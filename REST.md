# CC_HW2
#Cloud Computing homework2

# RUN APP USING DOCKER IMAGE
###Load the docker image
[root]:docker load -i Bao_Do_Image.tar
<br> 
###Run image
[root]:docker run -d -p 8081:80 mydocker
<br>
###Website should be running on on port 8081

#Call to weather data
### Root URL: <br>
[**ec2-52-37-173-114.us-west-2.compute.amazonaws.com/**](http://ec2-52-37-173-114.us-west-2.compute.amazonaws.com/)
<br>
##On this page
* You can see the forecast for the next 10 days using the Yahoo Weather Service.

##Getting Historical Dates
* **Description:**
You can call all dates that have data. API responds with a list of json results that includes all the dates.
* **URL:** /historical/
* **Method:** GET
* **Parameters**: None
* **Examples of API calls:** <br>
  * GET | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/historical/*
* **Success Response:** 
 * **Code:** 200 OK
* **Error Response:**
 * **Code:** 404

##Getting weather data **by Date**:
###Description:
You can get the weather data by date. API will responds with exact result.
* **URL:** /historical/<*dateYYYYMMDD*>
* **Method:** GET
* **Parameters**: 
 * **id**  Date
 * **type** DateTime(YYYYMMDD)
* **Examples of API calls:** <br>
  * GET | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/historical/20130102/*
* **Success Response:** 
 * **Code:** 200 OK
* **Error Response:**
 * **Code:** 404 NOT FOUND

##Posting weather data:
###Description:
You can **add/update** the weather data for a specific date. API will update the results.
* **URL:** /historical/
* **Method:** POST
* **Parameters**: 
 * **id**  data {"DATE":"20130101","TMAX": 34.0,"TMIN":26.0}
 * **type** JSON(application/json)
* **Examples of API calls:** <br>
  * POST | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/historical/* | {"DATE":"20130101","TMAX": 34.0,"TMIN":26.0}
* **Success Response:** 
 * **Code:** 201 CREATED
* **Error Response:**
 * **Code:** 405 METHOD NOT ALLOWED

##Deleting weather data by Date:
###Description:
You can **delete** the weather data for a specific date. API will update the results.
* **URL:** /historical/<*dateYYYYMMDD*>
* **Method:** DELETE
* **Parameters**: 
 * **id**  date
 * **type** DateTime(YYYYMMDD)
* **Examples of API calls:** <br>
  * DELETE | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/historical/<dateYYYYMMDD>* 
* **Success Response:** 
 * **Code:** 200 OK
* **Error Response:**
 * **Code:** 404 NOT FOUND


##Getting weather forecast data by Date:
###Description:
You can **get** the weather data of by date of existing data for the next 7 days. API will responds with exact results.
* **URL:** /forecast/<*dateYYYYMMDD*>
* **Method:** GET
* **Parameters**: 
 * **id**  Date
 * **type** DateTime(YYYYMMDD)
* **Examples of API calls:** <br>
  * GET | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/forecast/20130102/*
* **Success Response:** 
 * **Code:** 200 OK
* **Error Response:**
 * **Code:** 404 NOT FOUND
