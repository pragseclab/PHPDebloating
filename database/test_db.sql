-- phpMyAdmin SQL Dump
-- version 4.0.0
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2018 at 12:02 PM
-- Server version: 5.7.22-0ubuntu0.16.04.1
-- PHP Version: 5.6.36-1+ubuntu16.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

use test_db;


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `test_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl1`
--

CREATE TABLE IF NOT EXISTS `tbl1` (
  `col1` int(10) NOT NULL AUTO_INCREMENT,
  `col2` varchar(50) NOT NULL DEFAULT 'a',
  `col3` date NOT NULL,
  `col4` int(11) NOT NULL,
  `col5` int(11) NOT NULL,
  PRIMARY KEY (`col1`),
  KEY `col2` (`col2`),
  KEY `col2_2` (`col2`),
  KEY `col4` (`col4`),
  KEY `col4_2` (`col4`),
  KEY `col4_3` (`col4`),
  KEY `col4_4` (`col4`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `tbl1`
--

INSERT INTO `tbl1` (`col1`, `col2`, `col3`, `col4`, `col5`) VALUES
(10, '1', '2018-06-04', 1, 1),
(20, '1', '2018-06-04', 1, 1),
(30, '1', '2018-06-04', 1, 1),
(40, '2', '2018-06-04', 4, 5),
(50, '2', '2018-06-04', 4, 5),
(60, '2', '2018-06-04', 4, 5),
(70, 'b', '2018-06-05', 4, 6),
(80, 'b', '2018-06-04', 4, 6);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
