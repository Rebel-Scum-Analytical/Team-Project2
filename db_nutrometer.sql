USE nutrometer;
DROP TABLE user_account;
CREATE TABLE user_account (account_number INTEGER PRIMARY KEY, Username VARCHAR(50), password VARCHAR(50), first_name VARCHAR(50), last_name VARCHAR(50), gender CHAR(1), date_of_birth DATE, height FLOAT(5,1), 
Weight	FLOAT(5,1), physical_activity_level	SET("Sedentary", "Lightly active", "Moderately active", " Very active", "Extra active"));

DROP TABLE meal_record;
CREATE TABLE meal_record (id INTEGER PRIMARY KEY, account_number INTEGER, meal_category	SET("Breakfast", "Lunch", "Dinner", "Snack"), meal_date	DATE, meal_time	TIME,
meal_item SET("carrot", "egg", "apple"), meal_item_code	INTEGER, amount	FLOAT(5,1), measure_unit SET("ml", "oz", "g"), measure_unit_id	CHAR(10), magnesium	float(5,1),
calcium	FLOAT(5,1), potassium FLOAT(5,1), sodium FLOAT(5,1), phosphorus FLOAT(5,1), chloride FLOAT(5,1), sulphur FLOAT(5,1), chromium FLOAT(5,1), copper FLOAT(5,1),
fluoride FLOAT(5,1), iodine FLOAT(5,1), iron FLOAT(5,1), manganese FLOAT(5,1), molybdenum FLOAT(5,1), selenium FLOAT(5,1), zinc FLOAT(5,1), vitamin_c FLOAT(5,1), 
cobalamin FLOAT(5,1), vitamin_b_12 FLOAT(5,1), thiamine	FLOAT(5,1), riboflavin FLOAT(5,1), niacin FLOAT(5,1), pantothenic_acid FLOAT(5,1), pyridoxine FLOAT(5,1), 
biotin FLOAT(5,1), folate FLOAT(5,1), vitamin_d FLOAT(5,1), vitamin_k FLOAT(5,1), vitamin_e FLOAT(5,1), vitamin_a FLOAT(5,1));