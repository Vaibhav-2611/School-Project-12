-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 15, 2020 at 02:14 PM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alumni`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumni`
--

DROP TABLE IF EXISTS `alumni`;
CREATE TABLE IF NOT EXISTS `alumni` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` char(30) DEFAULT NULL,
  `fname` char(30) DEFAULT NULL,
  `phone` char(30) DEFAULT NULL,
  `email` char(30) DEFAULT NULL,
  `stream` char(30) DEFAULT NULL,
  `pass_year` char(4) DEFAULT NULL,
  `hqualification` char(40) DEFAULT NULL,
  `current_position` char(30) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `c_city` char(20) DEFAULT NULL,
  `c_country` char(30) DEFAULT NULL,
  `employement` char(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `alumni`
--

INSERT INTO `alumni` (`id`, `name`, `fname`, `phone`, `email`, `stream`, `pass_year`, `hqualification`, `current_position`, `dob`, `c_city`, `c_country`, `employement`) VALUES
(3, 'rakesh kumar', 'jagdish', '9871816901', 'rakesh@mail.com', 'commerce', '1991', 'Msc', 'Web Designer', '2010-03-20', 'Haridwar', 'china', 'Business'),
(4, 'SAMRIDDHI', 'RAKESH KUMAR', '564564564', 'samriddhi@company.com', 'COMM', '2024', 'PHD', 'CEO', '2011-10-14', 'DELHI', 'INDIA', 'Business');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
