CREATE DATABASE IF NOT EXISTS `pythonlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pythonlogin`;

CREATE TABLE IF NOT EXISTS `accounts`(
`username` varchar(50) NOT NULL,
`email` varchar(100) NOT NULL,
`password` varchar(255) NOT NULL,
`confirmpassword` varchar(100) NOT NULL,
PRIMARY KEY(`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `accounts` (`username`,`email`,`password`,`confirmpassword`) VALUES ('test','test@test.com','test','test');



CREATE TABLE IF NOT EXISTS `recipes`(
`chef_name` varchar(50) NOT NULL default 'botrini',
`recipe_name` varchar(50) NOT NULL,
`cookware` SET('pot','pan','stock-pot','grill-pan','casserole','baking-sheet') NOT NULL,
`type_of_meal` SET('breakfast','branch','lunch','snack','dinner') NOT NULL,
`vegetables` SET('cabbage','tomato','cucumber','potato','carrot') default null ,
`meat` SET('chicken','lamb','beef','pork','shrimps','tuna') default null ,
`dairy` SET('milk','cheese','yogurt','butter','soft-cheese') default null,
`fruit` SET('apple','banana','strawberry','avocado','peach') default null,
`recipe_image` BLOB,
`your_instructions` TEXT(100) NOT NULL,
PRIMARY KEY(`recipe_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `recipes` (`chef_name`,`recipe_name`,`cookware`,`type_of_meal`,`vegetables`,`meat`,`dairy`,`fruit`,`recipe_image`,`your_instructions`) VALUES ('botrini','tost','pan','breakfast',NULL,NUll,'cheese',NULL,NULL,'Extra cheese');
INSERT INTO `recipes` (`chef_name`,`recipe_name`,`cookware`,`type_of_meal`,`vegetables`,`meat`,`dairy`,`fruit`,`recipe_image`,`your_instructions`) VALUES ('botrini','tortillas','pan','breakfast',NULL,NUll,'cheese',NULL,NULL,'Extra cheese');
INSERT INTO `recipes` (`chef_name`,`recipe_name`,`cookware`,`type_of_meal`,`vegetables`,`meat`,`dairy`,`fruit`,`recipe_image`,`your_instructions`) VALUES ('botrini','salad','pan','breakfast',NULL,NUll,'cheese',NULL,NULL,'Extra cheese');

CREATE TABLE `nutriappointments`(
`userPatiencename` varchar(50) NOT NULL,
`Date` DATE NOT NULL,
`hour` TIME NOT NULL,
`nutritionist` varchar(50) DEFAULT 'DrPhill',
PRIMARY KEY(`userPatiencename`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `nutriappointments` VALUES ('ilias','2020-07-13','16:00','DrPhill');
INSERT INTO `nutriappointments` VALUES ('mariada','2020-07-12','16:30','DrPhill');

CREATE TABLE `pendingappointments`(
`userPatiencename` varchar(50) NOT NULL,
`Date` DATE NOT NULL,
`hour` TIME NOT NULL,
`nutritionist` varchar(50) DEFAULT 'DrPhill',
PRIMARY KEY(`userPatiencename`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `pendingappointments` VALUES ('makis','2020-06-28','16:00','DrPhill');
INSERT INTO `pendingappointments` VALUES ('mariada','2020-06-29','16:30','DrPhill');


CREATE TABLE IF NOT EXISTS `nutri`(
`drname` varchar(50) NOT NULL,
`stars` varchar(100) NOT NULL,
PRIMARY KEY(`drname`)
);

INSERT INTO `nutri` (`drname`,`stars`) VALUES ('DrPhill','3');
INSERT INTO `nutri` (`drname`,`stars`) VALUES ('DrWho','4');

CREATE TABLE IF NOT EXISTS `recipesnot`(
`dr_name` varchar(50) NOT NULL,
`stars` varchar(50) NOT NULL,
PRIMARY KEY(`dr_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `recipesnot` (`dr_name`,`stars`) VALUES ('DrPhill','5stars');
INSERT INTO `recipesnot` (`dr_name`,`stars`) VALUES ('DrMaria','4stars');
INSERT INTO `recipesnot` (`dr_name`,`stars`) VALUES ('DrJohn','3stars');

CREATE TABLE IF NOT EXISTS personal (
age ENUM ('0-10','11-15','16-18','19-22','23-27','28-40','41-50','51+'),
height ENUM ('<150','150-160','161-170','171-180','181-190','190+'),
wieght ENUM ('<40','41-60','61-80','81-100','101-120','121+')
);

CREATE TABLE IF NOT EXISTS medicalcon (
medical ENUM ('leukaemia','cholecystitis','addison disease','anaphylaxis','asbestosis','lactose','kidney stones','lyme disease','osteoporosis'),
allergies ENUM ('milk','egg','peanut','tree nut','soy','wheat','fin fish','sesame')
);

CREATE TABLE IF NOT EXISTS FavoriteCuisines (
favcuisines ENUM ('mexican','italian','greek','chinese','spanish','mediterranean','american')
);
