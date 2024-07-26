-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 10, 2020 at 07:37 AM
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
-- Database: `report_card`
--

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

DROP TABLE IF EXISTS `marks`;
CREATE TABLE IF NOT EXISTS `marks` (
  `admno` int(11) DEFAULT NULL,
  `term` varchar(20) DEFAULT NULL,
  `session` varchar(20) DEFAULT NULL,
  `phy` int(3) DEFAULT NULL,
  `chem` int(3) DEFAULT NULL,
  `math` int(3) DEFAULT NULL,
  `eng` int(3) DEFAULT NULL,
  `comp` int(3) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `marks`
--

INSERT INTO `marks` (`admno`, `term`, `session`, `phy`, `chem`, `math`, `eng`, `comp`) VALUES
(101, 'UT-1', '2020-21', 67, 89, 90, 67, 90),
(102, 'UT-1', '2020-21', 67, 78, 56, 34, 45),
(103, 'UT-1', '2020-21', 78, 78, 90, 56, 67),
(104, 'UT-2', '2020-21', 67, 65, 4, 67, 67),
(105, 'UT-1', '2020-21', 56, 78, 90, 45, 67),
(106, 'UT-2', '2020-21', 58, 78, 90, 45, 67),
(107, 'UT-1', '2020-21', 52, 75, 97, 75, 77),
(108, 'UT-1', '2020-21', 98, 98, 97, 97, 98),
(109, 'UT-2', '2020-21', 99, 67, 78, 67, 67),
(109, 'UT-2', '2020-21', 99, 89, 78, 89, 56),
(111, 'UT-2', '2020-21', 99, 12, 11, 13, 14);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `admno` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `fname` varchar(30) DEFAULT NULL,
  `class` varchar(15) DEFAULT NULL,
  `section` varchar(10) DEFAULT NULL,
  `status` char(15) DEFAULT NULL,
  PRIMARY KEY (`admno`)
) ENGINE=MyISAM AUTO_INCREMENT=113 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`admno`, `name`, `fname`, `class`, `section`, `status`) VALUES
(101, 'rakesh', 'jagdish', '12', 'A', 'active'),
(102, 'unnati', 'ramesh saxena', '12', 'C', 'active'),
(103, 'mannat Bhatia', 'Mr Bhatia', '12', 'B', 'active'),
(104, 'pushkar', 'Ramji', '12', 'A', 'active'),
(105, 'vishank', 'sudesh raina', '11', 'C', 'active'),
(106, 'nikunj tyagi', 'Subodh Tyagi', '12', 'A', 'active'),
(107, 'pratham chauhan', 'chauhan sir', '12', 'C', 'active'),
(108, 'swarnima', 'rakesh ji', '12', 'A', 'active'),
(109, 'gopal ji', 'sameer pandey', '10', 'a', 'active'),
(110, 'swarnima', 'ramesh', '12-B', '2020-21', 'active'),
(111, 'Kuldeep Sharma', 'satish sharma', '10', 'D', 'active'),
(112, 'sudha gupta', 'ramesh chandra', '11', 'B', 'active');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
