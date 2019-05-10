-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 24, 2018 at 03:47 PM
-- Server version: 5.7.23-0ubuntu0.16.04.1
-- PHP Version: 5.6.37-1+ubuntu16.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `code_coverage`
--
CREATE DATABASE IF NOT EXISTS `code_coverage` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `code_coverage`;

-- --------------------------------------------------------

--
-- Table structure for table `covered_files`
--

CREATE TABLE `covered_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(400) NOT NULL,
  `fk_test_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `covered_lines`
--

CREATE TABLE `covered_lines` (
  `id` int(11) NOT NULL,
  `line_number` int(11) NOT NULL,
  `run` int(11) NOT NULL,
  `fk_file_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `included_files`
--

CREATE TABLE `included_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(400) CHARACTER SET utf8 NOT NULL,
  `fk_test_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `software`
--

CREATE TABLE `software` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `software_files`
--

CREATE TABLE `software_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(400) CHARACTER SET utf8 NOT NULL,
  `line_count` int(11) DEFAULT '-1',
  `removed` tinyint(4) DEFAULT NULL,
  `fk_software_files_description` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `software_files_description`
--

CREATE TABLE `software_files_description` (
  `id` int(11) NOT NULL,
  `description` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `fk_software_id` int(11) NOT NULL,
  `fk_software_version_id` int(11) NOT NULL,
  `software_files_descriptioncol` varchar(45) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `software_functions`
--

CREATE TABLE `software_functions` (
  `id` int(11) NOT NULL,
  `fk_software_file` int(11) DEFAULT '-1',
  `function_name` varchar(150) DEFAULT NULL,
  `line_number` int(11) DEFAULT NULL,
  `line_count` int(11) DEFAULT '-1',
  `removed` tinyint(4) NOT NULL DEFAULT '-1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `software_version`
--

CREATE TABLE `software_version` (
  `id` int(11) NOT NULL,
  `version` varchar(100) NOT NULL,
  `fk_software_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tests`
--

CREATE TABLE `tests` (
  `id` int(11) NOT NULL,
  `test_name` varchar(100) DEFAULT 'unnamed',
  `test_group` varchar(250) NOT NULL DEFAULT 'default',
  `test_date` datetime DEFAULT NULL,
  `fk_software_id` int(11) DEFAULT '0',
  `fk_software_version_id` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `vulnerabilities`
--

CREATE TABLE `vulnerabilities` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `cve` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `fk_software_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vulnerability_software`
--

CREATE TABLE `vulnerability_software` (
  `id` int(11) NOT NULL,
  `fk_version_id` int(11) NOT NULL,
  `fk_vulnerability_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vulnerable_files`
--

CREATE TABLE `vulnerable_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(250) NOT NULL,
  `fk_vulnerability_software` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vulnerable_functions`
--

CREATE TABLE `vulnerable_functions` (
  `id` int(11) NOT NULL,
  `function_name` varchar(150) COLLATE utf8_bin DEFAULT NULL,
  `line_number` int(11) NOT NULL,
  `fk_vulnerable_file` int(11) NOT NULL,
  `fk_vulnerability_software` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `vulnerable_lines`
--

CREATE TABLE `vulnerable_lines` (
  `id` int(11) NOT NULL,
  `line_number` int(11) NOT NULL,
  `fk_vulnerability_software` int(11) NOT NULL,
  `fk_vulnerable_file` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `covered_files`
--
ALTER TABLE `covered_files`
  ADD PRIMARY KEY (`id`,`file_name`),
  ADD KEY `fk_test_id_idx` (`fk_test_id`),
  ADD KEY `file_name` (`file_name`);

--
-- Indexes for table `covered_lines`
--
ALTER TABLE `covered_lines`
  ADD PRIMARY KEY (`id`,`line_number`),
  ADD KEY `fk_file_id_idx` (`fk_file_id`),
  ADD KEY `line_number` (`line_number`);

--
-- Indexes for table `included_files`
--
ALTER TABLE `included_files`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_test_id` (`fk_test_id`),
  ADD KEY `file_name` (`file_name`);

--
-- Indexes for table `software`
--
ALTER TABLE `software`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `software_files`
--
ALTER TABLE `software_files`
  ADD PRIMARY KEY (`id`),
  ADD KEY `file_name` (`file_name`),
  ADD KEY `fk_software_files_description` (`fk_software_files_description`);

--
-- Indexes for table `software_files_description`
--
ALTER TABLE `software_files_description`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_software_id` (`fk_software_id`),
  ADD KEY `fk_software_version_id` (`fk_software_version_id`);

--
-- Indexes for table `software_functions`
--
ALTER TABLE `software_functions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `software_version`
--
ALTER TABLE `software_version`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_software_id` (`fk_software_id`);

--
-- Indexes for table `tests`
--
ALTER TABLE `tests`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_2` (`id`),
  ADD KEY `test_date` (`test_date`),
  ADD KEY `fk_tests_software_idx` (`fk_software_id`),
  ADD KEY `fk_tests_software_version_idx` (`fk_software_version_id`),
  ADD KEY `test_group` (`test_group`);

--
-- Indexes for table `vulnerabilities`
--
ALTER TABLE `vulnerabilities`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_software_id` (`fk_software_id`);

--
-- Indexes for table `vulnerability_software`
--
ALTER TABLE `vulnerability_software`
  ADD PRIMARY KEY (`id`,`fk_vulnerability_id`,`fk_version_id`);

--
-- Indexes for table `vulnerable_files`
--
ALTER TABLE `vulnerable_files`
  ADD PRIMARY KEY (`id`,`file_name`,`fk_vulnerability_software`);

--
-- Indexes for table `vulnerable_functions`
--
ALTER TABLE `vulnerable_functions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_vulnerable_file` (`fk_vulnerable_file`),
  ADD KEY `fk_vulnerability_software` (`fk_vulnerability_software`);

--
-- Indexes for table `vulnerable_lines`
--
ALTER TABLE `vulnerable_lines`
  ADD PRIMARY KEY (`id`,`line_number`,`fk_vulnerable_file`,`fk_vulnerability_software`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `covered_files`
--
ALTER TABLE `covered_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1909981;

--
-- AUTO_INCREMENT for table `covered_lines`
--
ALTER TABLE `covered_lines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=146459523;

--
-- AUTO_INCREMENT for table `included_files`
--
ALTER TABLE `included_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1904217;

--
-- AUTO_INCREMENT for table `software`
--
ALTER TABLE `software`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `software_files`
--
ALTER TABLE `software_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10518;

--
-- AUTO_INCREMENT for table `software_files_description`
--
ALTER TABLE `software_files_description`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `software_functions`
--
ALTER TABLE `software_functions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `software_version`
--
ALTER TABLE `software_version`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tests`
--
ALTER TABLE `tests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18604;

--
-- AUTO_INCREMENT for table `vulnerabilities`
--
ALTER TABLE `vulnerabilities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `vulnerability_software`
--
ALTER TABLE `vulnerability_software`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `vulnerable_files`
--
ALTER TABLE `vulnerable_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=120;

--
-- AUTO_INCREMENT for table `vulnerable_functions`
--
ALTER TABLE `vulnerable_functions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=136;

--
-- AUTO_INCREMENT for table `vulnerable_lines`
--
ALTER TABLE `vulnerable_lines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=379;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tests`
--
ALTER TABLE `tests`
  ADD CONSTRAINT `fk_tests_software` FOREIGN KEY (`fk_software_id`) REFERENCES `software` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_tests_software_version` FOREIGN KEY (`fk_software_version_id`) REFERENCES `software_version` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
