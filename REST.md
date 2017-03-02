# CC_HW2
#Cloud Computing homework2

#Call to weather data

##Getting Historical Dates
* **Description:**
You can call all dates that have data. API responds with a list of json results that includes all the dates.
* **URL:** /historical/
* **Method:** GET
* **Parameters**: None
* **Examples of API calls:** <br>
  * GET | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/historical/*
* **Success Response:** 
 * **Code:** 200
* **Error Response:**
 * **Code:** 404

##Getting weather data **by Date**:
###Description:
You can get the weather data by date. API will responds with exact result.
* **URL:** /historical/<dateYYYYMMDD>
* **Method:** GET
* **Parameters**: 
 * **id**  Date
 * **type** DateTime(YYYYMMDD)
* **Examples of API calls:** <br>
  * GET | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/historical/20130102/*
* **Success Response:** 
 * **Code:** 200
* **Error Response:**
 * **Code:** 404

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
 * **Code:** 201
* **Error Response:**
 * **Code:** 404

##Deleting weather data by Date:
###Description:
You can **delete** the weather data for a specific date. API will update the results.
* **URL:** /historical/<dateYYYYMMDD>
* **Method:** DELETE
* **Parameters**: 
 * **id**  date
 * **type** DateTime(YYYYMMDD)
* **Examples of API calls:** <br>
  * DELETE | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/historical/<dateYYYYMMDD>* 
* **Success Response:** 
 * **Code:** 200
* **Error Response:**
 * **Code:** 404


##Getting weather forecast data by Date:
###Description:
You can **get** the weather data by date for the next 7 days. API will responds with exact results.
* **URL:** /forecast/<dateYYYYMMDD>
* **Method:** GET
* **Parameters**: 
 * **id**  Date
 * **type** DateTime(YYYYMMDD)
* **Examples of API calls:** <br>
  * GET | *ec2-52-37-173-114.us-west-2.compute.amazonaws.com/forecast/20130102/*
* **Success Response:** 
 * **Code:** 200
* **Error Response:**
 * **Code:** 404
