# This is the final project for the 2018 MIDS course W209 #
The project intends to provide useful insights into the New York city traffic collisions.

* Website - http://people.ischool.berkeley.edu/~ellyrath/

* Source Code - https://github.com/ellyrath/MIDSVizFinalProject

* Preprocessing - https://github.com/ellyrath/MIDSVizFinalProject/tree/master/preprocessing

* Tableau Workbooks - https://github.com/ellyrath/MIDSVizFinalProject/tree/master/tableau

# Description:
New York City is divided into 5 boroughs (districts). New York city is one of the busiest city in US and has very heavy traffic. The winter weather also creates treacherous traffic conditions. New York Police department publishes the traffic accident report on the New York city  website (https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95) as part of public safety initiative. The data is listed by date, time, intersection, geo coordinates and number of injuries and death of pedestrians, cyclists and motorists. The data set contains 1.23 M incidents from 2012 to 2018.
The purpose of this project is to provide a visualization of the traffic data to understand the intersections and areas where there have been repeated accidents. 
We also integrated the weather data from NOAA (https://www.ncdc.noaa.gov/data-access) to understand the impact of weather on traffic incidents. This site provides hourly data for the weather and includes precipitation and temperature based on the sensor locations. There are 109163 records in the weather dataset. 

# Preprocessing:

## Merging Weather Data:

Unzip the datafile NYPD_Motor_Vehicle_Collisions.csv.zip to get the csv data. This gets the csv file. 


The following program appends the weather information in the traffic data. 

python appendWeather.py NYP_Motor_Vehicle_Collisions.csv NYPD_Weather_Collisions_with_Weather.csv.  

It also filters rows that have missing latitude and longitude information.

The file weather_final.txt contains the weather data for New York City. The temperature and precipitation information is arranged by sensor locations. For each row in the traffic file, the program finds the nearest sensor location and gets the temperature and precipitation for that location and appends it as two columns in the traffic file. 

## Extracting top 50 fatal accidents:

The python program topaccidents.py extracts relevant data from the modified traffic file and creates a geojscon file. It extracts the n fatal accidents where n is a commandline parameter (50). 

python topaccidents.py NYPD_Motor_Vehicle_Collions_with_Weather.csv topaccidentsbyyear.js 50

## Correlation between temperature and number of accidents:

The python program tempcorr.py is used to extract the temperature and number of accidents.

python tempcorr.py tempcorr.csv

# Map rendering:

The geojson files for the Newyork borroughs were generate by converting the shape files from the website of New York City. 

@ Main Page:
The index.html is the main entry point to the website. 
