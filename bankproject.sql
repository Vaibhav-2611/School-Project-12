-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 01, 2020 at 09:41 AM
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
-- Database: `bankproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `acno` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(30) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `aadhar_no` varchar(20) DEFAULT NULL,
  `acc_type` varchar(20) DEFAULT NULL,
  `status` char(15) DEFAULT NULL,
  `balance` float(15,2) DEFAULT NULL,
  PRIMARY KEY (`acno`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`acno`, `name`, `address`, `phone`, `email`, `aadhar_no`, `acc_type`, `status`, `balance`) VALUES
(1, 'rakesh kumar', 'cf-4 surya nagar', '987181818', 'support@cbsetoday.com', '1234-1243-4545', 'saving', 'active', 12200.00),
(2, 'raju vashistha', 'A-75-B Brij vihar', '96734344318', 'raju@cbsetoday.com', '4545-1243-4545', 'current', 'active', 10000.00),
(3, 'archana', 'cf04 ', '4545456', 'archana@bianrynote.com', '1234-5656-4545', 'saving', 'active', 10000.00),
(4, 'ashutosh', 'd-100 brij vihar', '1122334455', 'ashu@gmail.com', '1124-5656-6576', 'saving', 'close', 56000.00),
(5, 'raman singh', 'e-40 radha bihar', '3344556677', 'raman@yahoo.com', '4455-5656-4545', 'saving', 'close', 20000.00),
(6, 'sam', 'f-12 surya nagar', '1234', 'sam@gmail.com', '1234-4556-5656', 'saving', 'active', 22000.00);

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `dot` date DEFAULT NULL,
  `amount` int(10) DEFAULT NULL,
  `type` char(20) DEFAULT NULL,
  `acno` int(10) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`tid`, `dot`, `amount`, `type`, `acno`) VALUES
(1, '2020-10-16', 2000, 'deposit', 1),
(2, '2020-10-15', 2000, 'deposit', 2),
(3, '2020-10-18', 1200, 'withdraw', 1),
(4, NULL, 2000, 'deposit', 1),
(5, '2020-11-30', 200, 'deposit', 1),
(6, '2020-11-30', 2000, 'withdraw', 1),
(7, '2020-11-30', 200, 'withdraw', 1),
(8, '2020-12-01', 2000, 'deposit', 6);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
