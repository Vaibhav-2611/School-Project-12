-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 06, 2021 at 03:49 PM
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
-- Database: `crime`
--

-- --------------------------------------------------------

--
-- Table structure for table `crime_record`
--

DROP TABLE IF EXISTS `crime_record`;
CREATE TABLE IF NOT EXISTS `crime_record` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `c_date` date DEFAULT NULL,
  `offence_type` int(10) DEFAULT NULL,
  `complaint_by` char(30) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone_no` char(11) DEFAULT NULL,
  `status` char(15) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `crime_record`
--

INSERT INTO `crime_record` (`id`, `c_date`, `offence_type`, `complaint_by`, `address`, `phone_no`, `status`, `update_date`) VALUES
(1, '2021-02-04', 4, 'rakesh kumar', 'c-4 brij vihar', '9871816902', 'open', '2021-02-03'),
(2, '2021-02-03', 4, 'anuj bhati', 'b-100 surya nagar', '9565652302', 'open', '2021-02-04'),
(3, '2021-02-01', 8, 'amar singh', 'c-102 ramprastha', '9675652302', 'open', '2021-01-04'),
(4, '2021-03-05', 12, 'ramji', '100 shrestha vihar', '34534534', 'open', '2021-03-05'),
(5, '2021-03-05', 11, 'ramji', 'c-122 mayur vihar', '1122334455', 'open', '2021-03-05'),
(6, '2021-03-05', 13, 'suresh sharma', 'cf-5 vivek vihar delhi', '4433221111', 'open', '2021-03-05');

-- --------------------------------------------------------

--
-- Table structure for table `crime_type`
--

DROP TABLE IF EXISTS `crime_type`;
CREATE TABLE IF NOT EXISTS `crime_type` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `offence_name` char(50) DEFAULT NULL,
  `ipc_section` char(60) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `crime_type`
--

INSERT INTO `crime_type` (`id`, `offence_name`, `ipc_section`, `comment`) VALUES
(1, 'Attempt to Murder', '403', 'murder by parents'),
(2, 'Murder', '402', ''),
(3, 'Dacoity', '45-A', ''),
(4, 'Robbery', '564-B', ''),
(5, 'Stolen', '1243', 'When owner was away'),
(6, 'burgulary', '454-1234', 'sendhmaari'),
(7, 'sexual assult', '345-c', 'sexual assualt on adult woman'),
(8, 'sexual assult on minor', '66-A', 'sexual assualt on minor'),
(9, 'sexual assult on minor', 'POCSO', 'sexual assualt on minor'),
(10, 'EVE-Teasing', '254-B', 'Following or harassing adult woman'),
(11, 'Online Fraud', '68-A', 'Online fraud using spam phising or other means'),
(12, 'molestation', '3434-c', 'molastation by minor'),
(13, 'Financial Cheating', '420', 'simple financial cheating');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `id` int(11) DEFAULT NULL,
  `name` char(20) DEFAULT NULL,
  `pwd` char(30) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `name`, `pwd`) VALUES
(1, 'rakesh', 'ramji'),
(2, 'surya', 'singhji');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
