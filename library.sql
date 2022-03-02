-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 06, 2020 at 02:34 PM
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
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `title` char(60) DEFAULT NULL,
  `author` char(50) DEFAULT NULL,
  `pages` int(4) DEFAULT NULL,
  `price` float(6,2) DEFAULT NULL,
  `status` char(10) DEFAULT NULL,
  `publisher` char(60) DEFAULT NULL,
  `edition` char(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `title`, `author`, `pages`, `price`, `status`, `publisher`, `edition`) VALUES
(1, 'Let us Python', 'yashwant kanetkar', 879, 150.00, 'available', 'bpb', '10'),
(2, 'Let us Python', 'rakesh kumar', 350, 250.00, 'issue', 'Deewan international', '1'),
(3, 'Connect Dots', 'rashmi bansal', 256, 200.00, 'available', 'penguin india', '1'),
(4, 'Connect Dots', 'rashmi bansal', 256, 200.00, 'available', 'penguin india', '1'),
(5, 'Connect Dots', 'rashmi bansal', 256, 200.00, 'available', 'penguin india', '1'),
(6, 'Connect Dots', 'rashmi bansal', 256, 200.00, 'stolen', 'penguin india', '1'),
(7, 'Connect Dots', 'rashmi bansal', 256, 200.00, 'stolen', 'penguin india', '1'),
(8, 'Django 2 By Example', 'Mario Brothers', 565, 450.00, 'lost', 'BPB', '2'),
(9, 'Django 2 By Example', 'Mario Brothers', 565, 450.00, 'available', 'BPB', '2'),
(10, 'Django 2 By Example', 'Mario Brothers', 565, 450.00, 'weed-out', 'BPB', '2'),
(11, 'Bg Django 2.0 application', 'Tom Ayuth', 345, 450.00, 'available', 'Tata McGraw Hill', '2'),
(12, 'Bg Django 2.0 application', 'Tom Ayuth', 345, 450.00, 'available', 'Tata McGraw Hill', '2'),
(13, 'Bg Django 2.0 application', 'Tom Ayuth', 345, 450.00, 'available', 'Tata McGraw Hill', '2'),
(14, 'The lean startup', 'Peter thiel', 345, 190.00, 'lost', 'penguin india', '2'),
(15, 'The lean startup', 'Peter thiel', 345, 190.00, 'available', 'penguin india', '2'),
(16, 'The lean startup', 'Peter thiel', 345, 190.00, 'available', 'penguin india', '2'),
(17, 'The lean startup', 'Peter thiel', 345, 190.00, 'available', 'penguin india', '2'),
(18, 'The lean startup', 'Peter thiel', 345, 190.00, 'available', 'penguin india', '2');

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
CREATE TABLE IF NOT EXISTS `member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(30) DEFAULT NULL,
  `class` char(15) DEFAULT NULL,
  `address` char(100) DEFAULT NULL,
  `phone` char(15) DEFAULT NULL,
  `email` char(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`id`, `name`, `class`, `address`, `phone`, `email`) VALUES
(1, 'ram lal', '12 A', 'cf-4 brij vihar', '987177171', 'rakesh@cbsetoday.com'),
(2, 'samriddhi', '4 B', 'f-124 surya nagar', '2345677890', 'sam@gmail.com'),
(3, 'kamal aggarwal', '10 A', 'cf-9 brij vihar', '987383843', 'kamal@mail.com'),
(4, 'rakshit', '10-A', 'f-32 surya nagar', '65775575', 'rakshit@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `b_id` int(11) DEFAULT NULL,
  `m_id` int(11) DEFAULT NULL,
  `doi` date DEFAULT NULL,
  `dor` date DEFAULT NULL,
  `fine` float(5,2) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`tid`, `b_id`, `m_id`, `doi`, `dor`, `fine`) VALUES
(9, 1, 1, '2020-12-06', '2020-12-06', 0.01),
(10, 2, 2, '2020-12-06', '2020-12-06', 0.01),
(11, 1, 2, '2020-12-06', '2020-12-06', 0.01),
(12, 1, 1, '2020-12-06', '2020-12-06', 0.01),
(13, 1, 1, '2020-12-06', '2020-12-06', 0.01),
(14, 1, 1, '2020-12-06', '2020-12-06', 0.00),
(15, 1, 1, '2020-12-06', '2020-12-06', 0.00),
(16, 4, 4, '2020-12-06', '2020-12-06', 0.00);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
