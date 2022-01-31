/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 10.6.3-MariaDB : Database - invitetracker
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`invitetracker` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;

USE `invitetracker`;

/*Table structure for table `invitecodes` */

DROP TABLE IF EXISTS `invitecodes`;

CREATE TABLE `invitecodes` (
  `uses` int(11) NOT NULL DEFAULT 0,
  `inviter_id` bigint(20) NOT NULL,
  `invite_code` varchar(12) NOT NULL,
  `srlno` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`invite_code`),
  KEY `srlno` (`srlno`)
) ENGINE=InnoDB AUTO_INCREMENT=11151 DEFAULT CHARSET=utf8mb3;

/*Table structure for table `invitecount` */

DROP TABLE IF EXISTS `invitecount`;

CREATE TABLE `invitecount` (
  `inviter_id` bigint(20) NOT NULL,
  `invited` int(11) DEFAULT 0,
  `leaved` int(11) DEFAULT 0,
  `fake` int(11) DEFAULT 0,
  PRIMARY KEY (`inviter_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

/*Table structure for table `invited_users` */

DROP TABLE IF EXISTS `invited_users`;

CREATE TABLE `invited_users` (
  `inviter_id` bigint(20) NOT NULL,
  `user_invited` bigint(20) NOT NULL,
  PRIMARY KEY (`user_invited`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
