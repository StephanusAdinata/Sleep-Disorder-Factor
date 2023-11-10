create table table_g7(
id serial primary key,
"Person ID" int,
"Gender" varchar(50),
"Age" int,
"Occupation" varchar(50),
"Sleep Duration" Float,
"Quality of Sleep" int,
"Physical Activity Level" int,
"Stress Level" int,
"BMI Category" Varchar(50),
"Blood Pressure" Varchar(50),
"Heart Rate" int,
"Daily Steps" int,
"Sleep Disorder" varchar(50));

copy table_g7("Person ID", "Gender", "Age", "Occupation", "Sleep Duration", "Quality of Sleep", "Physical Activity Level",
             "Stress Level", "BMI Category", "Blood Pressure", "Heart Rate", "Daily Steps", "Sleep Disorder")
FROM 'C:\tmp\P2G7_Stephanus_raw.csv'
DELIMITER ','
CSV HEADER;