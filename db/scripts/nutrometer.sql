CREATE SCHEMA IF NOT EXISTS usda;
USE usda;
-- ALTER TABLE usda.user_account DROP CONSTRAINT username;
DROP TABLE IF EXISTS usda.user_account;
CREATE TABLE `user_account` (
  `username` varchar(10) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `gender` set('male','female') NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `height` float(5,1) DEFAULT NULL,
  `weight` float(5,1) DEFAULT NULL,
  `physical_activity_level` set('Sedentary','Lightly active','Moderately active',' Very active','Extra active') DEFAULT NULL,
  `confirm_password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
DROP TABLE IF EXISTS meal_record;
CREATE TABLE `meal_record` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `meal_date` date DEFAULT NULL,
  `meal_item_code` int(11) DEFAULT NULL,
  `meal_desc` varchar(256) DEFAULT NULL,
  `amount` float(5,1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `username_idx` (`username`),
  CONSTRAINT `username` FOREIGN KEY (`username`) REFERENCES `user_account` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;


