# CC_HW4

## Git URL
<br>
https://github.uc.edu/dobh/CC_HW4
## To run hadoop mapreduce script
<br>
hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/$USER/mapper.py    -mapper /home/$USER/mapper.py -file /home/$USER/reducer.py   -reducer /home/$USER/reducer.py -input /data/nyc/nyc-traffic.csv -output /user/$USER/outputfile
<br>
## Get output file from above which is "outputfile"
<br>
hadoop fs -cat /user/tatavag/outputfile/*  2> /dev/null | head -10 
<br>
## Output 
<br>
> 
<br>AMBULANCE       3713
<br>BICYCLE 24153
<br>BUS     25871
<br>FIRE TRUCK      1333
<br>LARGE COM VEH(6 OR MORE TIRES)  27981
<br>LIVERY VEHICLE  17775
<br>MOTORCYCLE      10029
<br>OTHER   51360
<br>PASSENGER VEHICLE       1005162
<br>PEDICAB 123
<br>PICK-UP TRUCK   26281
<br>SCOOTER 534
<br>SMALL COM VEH(4 TIRES)  30048
<br>SPORT UTILITY / STATION WAGON   363209
<br>TAXI    63892
<br>UNKNOWN 105481
<br>VAN     51666
