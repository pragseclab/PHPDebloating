-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Mar 25, 2019 at 01:38 PM
-- Server version: 5.7.23
-- PHP Version: 7.1.27-1+ubuntu16.04.1+deb.sury.org+1

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
CREATE DATABASE IF NOT EXISTS `code_coverage` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `code_coverage`;

-- --------------------------------------------------------

--
-- Table structure for table `covered_files`
--

DROP TABLE IF EXISTS `covered_files`;
CREATE TABLE `covered_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(400) NOT NULL,
  `fk_test_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `covered_lines`
--

DROP TABLE IF EXISTS `covered_lines`;
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

DROP TABLE IF EXISTS `included_files`;
CREATE TABLE `included_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(400) CHARACTER SET utf8 NOT NULL,
  `fk_test_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `software`
--

DROP TABLE IF EXISTS `software`;
CREATE TABLE `software` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `software`
--

INSERT INTO `software` (`id`, `name`) VALUES
(1, 'phpMyAdmin'),
(2, 'MediaWiki'),
(3, 'Magento'),
(4, 'Wordpress');

-- --------------------------------------------------------

--
-- Table structure for table `software_files`
--

DROP TABLE IF EXISTS `software_files`;
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

DROP TABLE IF EXISTS `software_files_description`;
CREATE TABLE `software_files_description` (
  `id` int(11) NOT NULL,
  `description` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `fk_software_version_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `software_functions`
--

DROP TABLE IF EXISTS `software_functions`;
CREATE TABLE `software_functions` (
  `id` int(11) NOT NULL,
  `fk_software_file` int(11) DEFAULT '-1',
  `function_name` varchar(150) DEFAULT NULL,
  `line_number` int(11) DEFAULT NULL,
  `line_count` int(11) DEFAULT '-1',
  `removed` tinyint(4) NOT NULL DEFAULT '-1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `software_version`
--

DROP TABLE IF EXISTS `software_version`;
CREATE TABLE `software_version` (
  `id` int(11) NOT NULL,
  `version` varchar(100) NOT NULL,
  `fk_software_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `software_version`
--

INSERT INTO `software_version` (`id`, `version`, `fk_software_id`) VALUES
(1, '4.0.0', 1),
(2, '4.4.0', 1),
(3, '4.6.0', 1),
(4, '4.7.0', 1),
(5, '1.19.1', 2),
(6, '1.21.1', 2),
(7, '1.23.0', 2),
(8, '1.24.0', 2),
(9, '1.28.0', 2),
(10, '1.9.0', 3),
(11, '2.0.5', 3),
(12, '2.0.9', 3),
(13, '2.2', 3),
(14, '3.3', 4),
(15, '3.9', 4),
(16, '4.0', 4),
(17, '4.2.3', 4),
(18, '4.6', 4),
(19, '4.7', 4),
(20, '4.7.1', 4);

-- --------------------------------------------------------

--
-- Table structure for table `tests`
--

DROP TABLE IF EXISTS `tests`;
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

DROP TABLE IF EXISTS `vulnerabilities`;
CREATE TABLE `vulnerabilities` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `cve` varchar(50) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `fk_software_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vulnerabilities`
--

INSERT INTO `vulnerabilities` (`id`, `name`, `cve`, `description`, `fk_software_id`) VALUES
(1, 'vulnerability in preg_replace', 'CVE-2016-5734', 'The table searching feature is relatively common, however, this vulnerability takes effect under specific PHP version.', 1),
(2, '', 'CVE-2013-3238', 'This allows remote code execution and performing attack is easy.', 1),
(3, '', 'CVE-2016-6620', 'The tracking feature, the extra feature provided by phpMyAdmin, is inactive by default.', 1),
(4, '', 'CVE-2016-5703', '', 1),
(5, '', 'CVE-2016-6616', 'This allows remote code execution and performing attack is easy.', 1),
(6, '', 'CVE-2016-6631', 'It is triggered by specific configurations.', 1),
(7, '', 'CVE-2016-9865', 'This is about export/import feature. It is not seem to be high since we usually use SQL to export/import database, rarely to use PHP codes.', 1),
(8, '', 'CVE-2016-6629', 'This vulnerability is extremely dangerous, however, the related feature is inactive by default. For most users, especially whose database is located at the same web server, this feature is useless.', 1),
(9, '', 'CVE-2016-6606', 'This vulnerability is related to auth.', 1),
(10, '', 'CVE-2016-9849', '', 1),
(11, '', 'CVE-2016-6617', '', 1),
(12, '', 'CVE-2016-6628', '', 1),
(13, '', 'CVE-2016-6633', '', 1),
(14, '', 'CVE-2016-9866', '', 1),
(15, '', 'CVE-2016-6609', '', 1),
(16, '', 'CVE-2016-6619', '', 1),
(17, 'test', 'test', 'test', 1),
(18, '', 'CVE-2017-1000499', '', 1),
(19, '', 'CVE-2013-3240', '', 1),
(20, '', 'CVE-2014-8959', '', 1),
(21, '', 'CVE-2017-1000017', '', 1),
(22, '', 'CVE-2017-8809', '', 2),
(23, '', 'CVE-2015-6728', '', 2),
(24, '', 'CVE-2014-9277', '', 2),
(25, '', 'CVE-2013-6453', '', 2),
(26, '', 'CVE-2015-2937', '', 2),
(27, '', 'CVE-2015-2936', '', 2),
(28, '', 'CVE-2017-0362', '', 2),
(29, '', 'CVE-2015-8624', '', 2),
(30, '', 'CVE-2015-8623', '', 2),
(31, '', 'CVE-2015-8003', '', 2),
(32, '', 'CVE-2015-8002', '', 2),
(33, '', 'CVE-2014-5241', '', 2),
(34, '', 'CVE-2013-2114', '', 2),
(35, '', 'CVE-2017-0367', '', 2),
(36, '', 'CVE-2014-1610', '', 2),
(37, '', 'CVE-2017-0364', '', 2),
(38, '', 'CVE-2017-0363', '', 2),
(39, '', 'CVE-2014-2243', '', 2),
(40, '', 'CVE-2014-9276', '', 2),
(41, '', 'CVE-2017-0370', '', 2),
(42, '', 'CVE-2017-0368', '', 2),
(43, '', 'CVE-2018-5301', 'Magento Community Edition and Enterprise Edition before 2.0.10 and 2.1.x before 2.1.2 have CSRF resulting in deletion of a customer address from an address book, aka APPSEC-1433.', 3),
(44, '', 'CVE-2016-6485', 'The __construct function in Framework/Encryption/Crypt.php in Magento 2 uses the PHP rand function to generate a random number for the initialization vector, which makes it easier for remote attackers to defeat cryptographic protection mechanisms by guessing the value.', 3),
(45, '', 'CVE-2016-4010', 'Magento CE and EE before 2.0.6 allows remote attackers to conduct PHP objection injection attacks and execute arbitrary PHP code via crafted serialized shopping cart data.', 3),
(46, '', 'CVE-2016-2212', 'The getOrderByStatusUrlKey function in the Mage_Rss_Helper_Order class in app/code/core/Mage/Rss/Helper/Order.php in Magento Enterprise Edition before 1.14.2.3 and Magento Community Edition before 1.9.2.3 allows remote attackers to obtain sensitive order information via the order_id in a JSON object in the data parameter in an RSS feed request to index.php/rss/order/status.', 3),
(47, '', 'CVE-2015-8707', 'Password reset tokens in Magento CE before 1.9.2.2, and Magento EE before 1.14.2.2 are passed via a GET request and not canceled after use, which allows remote attackers to obtain user passwords via a crafted external service with access to the referrer field.', 3),
(48, '', 'CVE-2015-1399', 'PHP remote file inclusion vulnerability in the fetchView function in the Mage_Core_Block_Template_Zend class in Magento Community Edition (CE) 1.9.1.0 and Enterprise Edition (EE) 1.14.1.0 allows remote administrators to execute arbitrary PHP code via a URL in unspecified vectors involving the setScriptPath function. NOTE: it is not clear whether this issue crosses privilege boundaries, since administrators might already have privileges to include arbitrary files.', 3),
(49, '', 'CVE-2015-1398', 'Multiple directory traversal vulnerabilities in Magento Community Edition (CE) 1.9.1.0 and Enterprise Edition (EE) 1.14.1.0 allow remote authenticated users to include and execute certain PHP files via (1) .. (dot dot) sequences in the PATH_INFO to index.php or (2) vectors involving a block value in the ___directive parameter to the Cms_Wysiwyg controller in the Adminhtml module, related to the blockDirective function and the auto loading mechanism. NOTE: vector 2 might not cross privilege boundaries, since administrators might already have the privileges to execute code and upload files.', 3),
(50, '', 'CVE-2015-1397', 'SQL injection vulnerability in the getCsvFile function in the Mage_Adminhtml_Block_Widget_Grid class in Magento Community Edition (CE) 1.9.1.0 and Enterprise Edition (EE) 1.14.1.0 allows remote administrators to execute arbitrary SQL commands via the popularity[field_expr] parameter when the popularity[from] or popularity[to] parameter is set.', 3),
(51, '', 'CVE-2014-5203', '', 4),
(52, '', 'CVE-2015-2213', '', 4),
(53, '', 'CVE-2017-5611', '', 4),
(54, '', 'CVE-2017-14723', '', 4),
(55, '', 'CVE-2017-16510', '', 4),
(56, '', 'CVE-2014-5204', '', 4),
(57, '', 'CVE-2014-5205', '', 4),
(58, '', 'CVE-2014-9033', '', 4),
(59, '', 'CVE-2014-9037', '', 4),
(60, '', 'CVE-2015-5731', '', 4),
(61, '', 'CVE-2016-6635', '', 4),
(62, '', 'CVE-2017-5492', '', 4),
(63, '', 'CVE-2017-9064', '', 4),
(64, '', 'CVE-2016-7169', '', 4),
(65, '', 'CVE-2017-17091', '', 4),
(66, '', 'CVE-2018-12895', '', 4),
(67, '', 'CVE-2017-6815', '', 4),
(68, '', 'CVE-2018-10100', '', 4),
(69, '', 'CVE-2018-10101', '', 4),
(70, '', 'CVE-2014-9038', '', 4);

-- --------------------------------------------------------

--
-- Table structure for table `vulnerability_software`
--

DROP TABLE IF EXISTS `vulnerability_software`;
CREATE TABLE `vulnerability_software` (
  `id` int(11) NOT NULL,
  `fk_version_id` int(11) NOT NULL,
  `fk_vulnerability_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vulnerability_software`
--

INSERT INTO `vulnerability_software` (`id`, `fk_version_id`, `fk_vulnerability_id`) VALUES
(1, 2, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 4),
(5, 2, 5),
(6, 1, 6),
(8, 1, 8),
(9, 3, 9),
(10, 3, 10),
(11, 3, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(18, 3, 1),
(19, 3, 4),
(20, 3, 5),
(21, 2, 6),
(22, 3, 6),
(23, 3, 7),
(24, 2, 8),
(25, 3, 8),
(26, 2, 13),
(27, 3, 13),
(28, 2, 14),
(29, 3, 14),
(30, 2, 15),
(31, 3, 15),
(32, 2, 16),
(33, 3, 16),
(34, 4, 18),
(35, 1, 19),
(36, 1, 20),
(37, 2, 21),
(38, 9, 22),
(39, 8, 23),
(41, 6, 25),
(42, 8, 26),
(43, 8, 27),
(44, 9, 28),
(45, 8, 29),
(46, 8, 30),
(47, 8, 31),
(48, 8, 32),
(49, 6, 33),
(50, 5, 34),
(51, 9, 35),
(52, 6, 36),
(53, 9, 37),
(54, 9, 38),
(55, 6, 39),
(56, 7, 40),
(57, 8, 41),
(58, 9, 42),
(59, 6, 24),
(60, 11, 43),
(61, 11, 44),
(62, 11, 45),
(63, 10, 46),
(64, 10, 47),
(65, 10, 48),
(66, 10, 49),
(67, 10, 50),
(68, 15, 51),
(69, 16, 52),
(70, 20, 53),
(71, 16, 54),
(72, 20, 55),
(73, 15, 56),
(74, 15, 57),
(75, 16, 58),
(76, 16, 59),
(77, 17, 60),
(78, 16, 61),
(79, 19, 62),
(80, 19, 63),
(81, 18, 64),
(83, 18, 65),
(84, 15, 66),
(85, 19, 67),
(86, 19, 68),
(87, 19, 69),
(88, 16, 70);

-- --------------------------------------------------------

--
-- Table structure for table `vulnerable_files`
--

DROP TABLE IF EXISTS `vulnerable_files`;
CREATE TABLE `vulnerable_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(250) NOT NULL,
  `fk_vulnerability_software` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vulnerable_files`
--

INSERT INTO `vulnerable_files` (`id`, `file_name`, `fk_vulnerability_software`) VALUES
(1, 'libraries/controllers/table/TableSearchController.php', 18),
(2, 'libraries/TableSearch.class.php', 1),
(3, 'libraries/mult_submits.inc.php', 2),
(4, 'tbl_tracking.php', 3),
(5, 'libraries/central_columns.lib.php', 4),
(6, 'libraries/server_user_groups.lib.php', 5),
(7, 'libraries/db_designer.lib.php', 5),
(8, 'libraries/plugins/export/ExportSql.php', 20),
(9, 'libraries/plugins/schema/ExportRelationSchema.php', 20),
(10, 'libraries/pmd_common.php', 5),
(11, 'libraries/plugins/transformations/generator_plugin.sh', 6),
(12, 'libraries/core.lib.php', 23),
(13, 'config.inc.php', 8),
(14, 'libraries/plugins/auth/AuthenticationCookie.php', 9),
(15, 'libraries/plugins/auth/AuthenticationCookie.php', 10),
(16, 'libraries/plugins/auth/AuthenticationHttp.php', 10),
(17, 'libraries/display_export.lib.php', 11),
(18, 'file_echo.php', 12),
(19, 'libraries/plugins/import/ImportShp.class.php', 13),
(20, 'libraries/zip_extension.lib.php', 13),
(21, 'prefs_manage.php', 14),
(22, 'libraries/plugins/export/ExportPhparray.class.php', 15),
(23, 'libraries/RecentFavoriteTable.php', 33),
(24, 'libraries/Table.class.php', 16),
(25, 'libraries/central_columns.lib.php', 19),
(26, 'libraries/server_user_groups.lib.php', 20),
(27, 'libraries/db_designer.lib.php', 20),
(28, 'libraries/pmd_common.php', 20),
(29, 'libraries/plugins/transformations/generator_plugin.sh', 21),
(30, 'libraries/plugins/transformations/generator_plugin.sh', 22),
(31, 'config.inc.php', 24),
(32, 'config.inc.php', 25),
(33, 'libraries/plugins/import/ImportShp.class.php', 26),
(34, 'libraries/plugins/import/ImportShp.php', 27),
(35, 'libraries/zip_extension.lib.php', 26),
(36, 'libraries/zip_extension.lib.php', 27),
(37, 'prefs_manage.php', 28),
(38, 'prefs_manage.php', 29),
(39, 'libraries/plugins/export/ExportPhparray.class.php', 30),
(40, 'libraries/plugins/export/ExportPhparray.class.php', 31),
(41, 'libraries/RecentFavoriteTable.class.php', 32),
(42, 'libraries/Table.class.php', 32),
(43, 'libraries/Table.php', 33),
(44, 'libraries/URL.php', 34),
(45, 'libraries/common.inc.php', 34),
(46, 'libraries/navigation/nodes/NodeColumn.php', 34),
(47, 'libraries/navigation/nodes/NodeColumnContainer.php', 34),
(48, 'libraries/navigation/nodes/NodeDatabase.php', 34),
(49, 'libraries/navigation/nodes/NodeEvent.php', 34),
(50, 'libraries/navigation/nodes/NodeEventContainer.php', 34),
(51, 'libraries/navigation/nodes/NodeFunction.php', 34),
(52, 'libraries/navigation/nodes/NodeFunctionContainer.php', 34),
(53, 'libraries/navigation/nodes/NodeIndex.php', 34),
(54, 'libraries/navigation/nodes/NodeIndexContainer.php', 34),
(55, 'libraries/navigation/nodes/NodeProcedure.php', 34),
(56, 'libraries/navigation/nodes/NodeProcedureContainer.php', 34),
(57, 'libraries/navigation/nodes/NodeTable.php', 34),
(58, 'libraries/navigation/nodes/NodeTableContainer.php', 34),
(59, 'libraries/navigation/nodes/NodeTrigger.php', 34),
(60, 'libraries/navigation/nodes/NodeTriggerContainer.php', 34),
(61, 'libraries/navigation/nodes/NodeView.php', 34),
(62, 'libraries/navigation/nodes/NodeViewContainer.php', 34),
(63, 'libraries/plugin_interface.lib.php', 35),
(64, 'libraries/gis/pma_gis_factory.php', 36),
(65, 'libraries/replication_gui.lib.php', 37),
(66, 'api.php', 38),
(67, 'includes/api/ApiFormatBase.php', 38),
(68, 'includes/Feed.php', 38),
(69, 'includes/api/ApiBase.php', 39),
(70, 'includes/OutputHandler.php', 40),
(71, 'includes/api/ApiFormatPhp.php', 40),
(72, 'includes/api/ApiFormatJson.php', 40),
(73, 'includes/upload/UploadBase.php', 41),
(74, 'includes/media/XMP.php', 42),
(75, 'includes/User.php', 43),
(76, 'includes/specials/SpecialUserlogin.php', 43),
(77, 'includes/specials/SpecialWatchlist.php', 44),
(78, 'includes/user/User.php', 45),
(79, 'includes/user/User.php', 46),
(80, 'includes/api/ApiUpload.php', 47),
(81, 'includes/specials/SpecialUpload.php', 47),
(82, 'includes/api/ApiUpload.php', 48),
(83, 'includes/api/ApiFormatJson.php', 49),
(84, 'includes/api/ApiUpload.php ', 50),
(85, 'includes/upload/UploadBase.php', 50),
(86, 'includes/upload/UploadFromChunks.php', 50),
(87, 'includes/upload/UploadFromStash.php', 50),
(88, 'includes/upload/UploadStash.php', 50),
(89, 'includes/cache/localisation/LocalisationCache.php', 51),
(90, 'includes/media/Bitmap.php', 52),
(91, 'includes/media/DjVu.php', 52),
(92, 'includes/media/ImageHandler.php', 52),
(93, 'includes/OutputPage.php', 53),
(94, 'includes/specials/SpecialChangeCredentials.php', 53),
(95, 'includes/specials/SpecialChangeEmail.php', 53),
(97, 'includes/specials/SpecialPageLanguage.php', 53),
(98, 'includes/specials/SpecialPreferences.php', 53),
(99, 'includes/specials/SpecialSearch.php', 53),
(100, 'includes/specials/helpers/LoginHelper.php', 53),
(101, 'includes/specialpage/RedirectSpecialPage.php', 53),
(102, 'includes/OutputPage.php', 54),
(103, 'includes/specials/SpecialChangeCredentials.php', 54),
(104, 'includes/specials/SpecialChangeEmail.php', 54),
(105, 'includes/specials/SpecialPageLanguage.php', 54),
(106, 'includes/specials/SpecialPreferences.php', 54),
(107, 'includes/specials/SpecialSearch.php', 54),
(108, 'includes/specials/helpers/LoginHelper.php', 54),
(109, 'includes/specialpage/RedirectSpecialPage.php', 54),
(110, 'includes/User.php', 55),
(111, 'includes/specials/SpecialExpandTemplates.php', 56),
(112, 'includes/parser/Parser.php', 57),
(113, 'includes/parser/ParserOutput.php', 57),
(114, 'includes/cache/MessageCache.php', 58),
(115, 'includes/parser/CoreTagHooks.php', 58),
(116, 'includes/OutputPage.php', 58),
(117, 'includes/OutputHandler.php', 59),
(118, 'includes/api/ApiFormatPhp.php', 59),
(119, 'includes/api/ApiFormatJson.php', 59),
(120, 'app/code/Magento/Customer/Controller/Address/Delete.php', 60),
(121, 'lib/internal/Magento/Framework/Encryption/Crypt.php', 61),
(122, 'lib/internal/Magento/Framework/Model/ResourceModel/AbstractResource.php', 62),
(123, 'app/code/core/Mage/Rss/Helper/Order.php', 63),
(124, 'app/code/core/Mage/Customer/controllers/AccountController.php', 64),
(125, 'app/design/frontend/base/default/template/customer/form/resetforgottenpassword.phtml', 64),
(126, 'app/design/frontend/rwd/default/template/customer/form/resetforgottenpassword.phtml', 64),
(127, 'app/code/core/Mage/Admin/Model/Observer.php', 65),
(128, 'app/code/core/Mage/Oauth/controllers/Adminhtml/Oauth/AuthorizeController.php', 66),
(129, 'app/code/core/Mage/XmlConnect/Model/Observer.php', 66),
(130, 'lib/Varien/Db/Adapter/Pdo/Mysql.php', 67),
(131, 'wp-includes/class-wp-customize-widgets.php', 68),
(132, 'wp-includes/post.php', 69),
(133, 'wp-includes/class-wp-query.php', 70),
(134, 'wp-includes/wp-db.php', 71),
(135, 'wp-includes/meta.php', 72),
(136, 'wp-includes/post.php', 72),
(137, 'wp-includes/pluggable.php', 73),
(138, 'wp-includes/pluggable.php', 74),
(139, 'wp-login.php', 75),
(140, 'wp-includes/class-phpass.php', 76),
(141, 'wp-admin/includes/post.php', 77),
(142, 'wp-admin/includes/ajax-actions.php', 78),
(143, 'wp-admin/includes/template.php', 78),
(144, 'wp-admin/includes/class-wp-screen.php', 79),
(145, 'wp-admin/includes/file.php', 80),
(146, 'wp-admin/includes/class-file-upload-upgrader.php', 81),
(147, 'wp-admin/user-new.php', 83),
(148, 'wp-includes/post.php', 84),
(149, 'wp-includes/pluggable.php', 85),
(150, 'wp-login.php', 86),
(151, 'wp-includes/http.php', 87),
(152, 'wp-includes/http.php', 88),
(153, 'wp-includes/wp-db.php', 72),
(154, 'wp-admin/post.php', 77),
(155, 'wp-admin/widgets.php', 79);

-- --------------------------------------------------------

--
-- Table structure for table `vulnerable_functions`
--

DROP TABLE IF EXISTS `vulnerable_functions`;
CREATE TABLE `vulnerable_functions` (
  `id` int(11) NOT NULL,
  `function_name` varchar(150) COLLATE utf8_bin DEFAULT NULL,
  `line_number` int(11) NOT NULL,
  `fk_vulnerable_file` int(11) NOT NULL,
  `fk_vulnerability_software` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `vulnerable_functions`
--

INSERT INTO `vulnerable_functions` (`id`, `function_name`, `line_number`, `fk_vulnerable_file`, `fk_vulnerability_software`) VALUES
(3, '_getRegexReplaceRows', 1390, 2, 1),
(4, '_getRegexReplaceRows', 711, 1, 18),
(5, 'PMA_getColumnsList', 56, 5, 4),
(6, 'PMA_getCentralColumnsCount', 88, 5, 4),
(7, 'PMA_findExistingColNames', 119, 5, 4),
(8, 'PMA_deleteColumnsFromList', 324, 5, 4),
(9, 'PMA_getCentralColumnsListRaw', 881, 5, 4),
(10, 'PMA_editUserGroup', 331, 26, 20),
(11, 'PMA_editUserGroup', 330, 6, 5),
(12, 'PMA_getPageIdsAndNames', 123, 7, 5),
(13, 'PMA_getPageIdsAndNames', 81, 27, 20),
(14, '_exportMetadata', 1041, 8, 20),
(15, 'setPageNumber', 56, 9, 20),
(16, 'PMA_getTablePositions', 251, 10, 5),
(17, 'PMA_getPageName', 285, 10, 5),
(18, 'PMA_deletePage', 313, 10, 5),
(19, 'PMA_getTablePositions', 251, 28, 20),
(20, 'PMA_getPageName', 285, 28, 20),
(21, 'PMA_deletePage', 313, 28, 20),
(22, 'PMA_getDefaultPage', 347, 28, 20),
(23, 'PMA_getLoadingPage', 382, 28, 20),
(24, 'authCheck', 280, 14, 9),
(25, 'storeUserCredentials', 532, 14, 9),
(26, 'cookieEncrypt', 728, 14, 9),
(27, 'cookieDecrypt', 755, 14, 9),
(28, 'createIV', 805, 14, 9),
(29, 'authCheck', 280, 15, 10),
(30, 'authCheck', 127, 16, 10),
(31, 'PMA_getOptionsForExportTemplates', 243, 17, 11),
(32, 'doImport', 81, 19, 13),
(33, 'doImport', 69, 33, 26),
(34, 'doImport', 66, 34, 27),
(35, 'PMA_zipExtract', 154, 36, 27),
(36, 'PMA_zipExtract', 155, 35, 26),
(37, 'PMA_zipExtract', 148, 20, 13),
(38, 'getCommonRaw', 206, 44, 34),
(39, '__construct', 29, 46, 34),
(40, '__construct', 26, 47, 34),
(41, '__construct', 37, 48, 34),
(42, '__construct', 29, 49, 34),
(43, '__construct', 25, 50, 34),
(44, '__construct', 29, 51, 34),
(45, '__construct', 25, 52, 34),
(46, '__construct', 29, 53, 34),
(47, '__construct', 25, 54, 34),
(48, '__construct', 29, 55, 34),
(49, '__construct', 25, 56, 34),
(50, '__construct', 29, 57, 34),
(51, '__construct', 25, 58, 34),
(52, '__construct', 29, 59, 34),
(53, '__construct', 25, 60, 34),
(54, '__construct', 29, 61, 34),
(55, '__construct', 25, 62, 34),
(56, 'exportDBHeader', 121, 22, 15),
(57, 'exportData', 166, 22, 15),
(58, 'exportDBHeader', 109, 39, 30),
(59, 'exportData', 160, 39, 30),
(60, 'exportDBHeader', 106, 40, 31),
(61, 'exportData', 164, 40, 31),
(62, 'getFromDb', 102, 41, 32),
(63, 'saveToDb', 124, 41, 32),
(64, 'getFromDb', 97, 23, 33),
(65, 'saveToDb', 119, 23, 33),
(66, 'getUiPrefsFromDb', 1337, 24, 16),
(67, 'getUiPrefsFromDb', 1493, 42, 32),
(68, 'saveUiPrefsToDb', 1518, 42, 32),
(69, 'getUiPrefsFromDb', 1491, 43, 33),
(70, 'saveUiPrefsToDb', 1516, 43, 33),
(71, 'PMA_getPlugin', 26, 63, 35),
(72, 'factory', 33, 64, 36),
(73, 'PMA_handleControlRequest', 909, 65, 37),
(74, 'initPrinter', 155, 67, 38),
(75, 'httpHeaders', 229, 68, 38),
(76, 'getWatchlistUser', 1071, 69, 39),
(77, 'wfOutputHandler', 31, 70, 40),
(78, 'execute', 38, 71, 40),
(79, 'execute', 59, 72, 40),
(80, 'detectScriptInSvg', 1151, 73, 41),
(81, 'parse', 263, 74, 42),
(82, 'checkPasswordValidity', 784, 75, 43),
(83, 'setPassword', 2294, 75, 43),
(84, 'checkPassword', 3789, 75, 43),
(85, 'addNewAccountInternal', 437, 76, 43),
(86, 'execute', 48, 77, 44),
(87, 'matchEditToken', 3922, 78, 45),
(88, 'matchEditToken', 3922, 79, 46),
(89, 'getContextResult', 129, 80, 47),
(90, 'processUpload', 410, 81, 47),
(91, 'getChunkResult', 196, 82, 48),
(92, 'selectUploadModule', 320, 82, 48),
(93, 'execute', 59, 83, 49),
(94, 'getChunkResult', 171, 84, 50),
(95, 'verifyMimeType', 306, 85, 50),
(96, 'verifyFile', 343, 85, 50),
(97, 'stashFile', 48, 86, 50),
(98, 'concatenateChunks', 86, 86, 50),
(99, 'addChunk', 151, 86, 50),
(100, 'verifyFile', 118, 87, 50),
(101, 'getExtensionForPath', 397, 88, 50),
(102, '__construct', 194, 89, 51),
(103, 'transformImageMagick', 266, 90, 52),
(104, 'transformCustom', 442, 90, 52),
(105, 'doTransform', 117, 91, 52),
(106, 'normaliseParams', 87, 92, 52),
(107, 'returnToMain', 2640, 102, 53),
(108, 'getReturnUrl', 230, 94, 53),
(109, 'onSuccess', 129, 95, 53),
(110, 'onSubmit', 117, 97, 53),
(111, 'submitReset', 140, 98, 53),
(112, 'goResult', 214, 99, 53),
(113, 'showReturnToPage', 64, 100, 53),
(114, 'execute', 40, 101, 53),
(115, 'returnToMain', 2640, 102, 54),
(116, 'getReturnUrl', 230, 103, 54),
(117, 'onSuccess', 129, 104, 54),
(118, 'onSubmit', 117, 105, 54),
(119, 'submitReset', 140, 106, 54),
(120, 'goResult', 214, 107, 54),
(121, 'showReturnToPage', 64, 108, 54),
(122, 'execute', 40, 109, 54),
(123, 'loadFromSession', 924, 110, 55),
(124, 'makeForm', 139, 111, 56),
(125, 'showHtmlPreview', 245, 111, 56),
(126, 'makeFreeExternalLink', 1367, 112, 57),
(127, 'replaceExternalLinks', 1648, 112, 57),
(128, 'renderImageGallery', 5259, 112, 57),
(129, 'addExternalLink', 315, 113, 57),
(130, 'getParserOptions', 173, 114, 58),
(131, 'html', 85, 115, 58),
(132, 'parserOptions', 1513, 116, 58),
(133, 'wfOutputHandler', 31, 117, 59),
(134, 'execute', 38, 118, 59),
(135, 'execute', 59, 119, 59),
(136, 'execute()', 16, 120, 60),
(137, '__construct($key, $cipher, $mode, $initVector, $initVector)', 56, 121, 61),
(138, '_serializeField($object, $field, $defaultValue, $unsetEmpty)', 130, 122, 62),
(139, '_unserializeField(\\Magento\\Framework\\DataObject $object, $field, $defaultValue)', 157, 122, 62),
(140, 'getOrderByStatusUrlKey($key)', 85, 123, 63),
(141, 'resetPasswordPostAction()', 765, 124, 64),
(142, 'actionPreDispatchAdmin($observer)', 45, 127, 65),
(143, 'preDispatch()', 58, 128, 66),
(144, 'actionFrontPreDispatchXmlAdmin($event)', 144, 129, 66),
(145, 'actionPreDispatchXmlAdmin($event)', 159, 129, 66),
(146, 'prepareSqlCondition($fieldName, $condition)', 2813, 130, 67),
(147, 'sanitize_widget_js_instance', 1190, 131, 68),
(148, 'sanitize_widget_instance', 1153, 131, 68),
(149, 'wp_untrash_post_comments', 2864, 132, 69),
(150, 'get_posts', 1668, 133, 70),
(151, 'prepare', 1155, 134, 71),
(152, 'delete_metadata', 310, 135, 72),
(153, 'get_page_by_path', 4226, 136, 72),
(154, '_real_escape', 1169, 135, 72),
(155, 'prepare', 1292, 135, 72),
(156, 'wp_validate_auth_cookie', 597, 137, 73),
(157, 'wp_verify_nonce', 1643, 138, 73),
(158, 'wp_verify_nonce', 1643, 138, 74),
(159, 'HashPassword', 217, 140, 76),
(160, 'CheckPassword', 252, 140, 76),
(161, 'redirect_post', 42, 154, 77),
(162, 'wp_ajax_wp_compression_test', 159, 142, 78),
(163, 'compression_test', 1713, 143, 78),
(164, 'show_screen_options', 909, 144, 79),
(165, 'request_filesystem_credentials', 1078, 145, 80),
(166, '__construct', 59, 146, 81),
(167, 'wp_delete_attachment', 4623, 148, 84),
(169, 'wp_http_validate_url', 515, 151, 87),
(170, 'wp_http_validate_url', 447, 152, 88),
(171, 'wp_validate_redirect', 1286, 149, 85);

-- --------------------------------------------------------

--
-- Table structure for table `vulnerable_lines`
--

DROP TABLE IF EXISTS `vulnerable_lines`;
CREATE TABLE `vulnerable_lines` (
  `id` int(11) NOT NULL,
  `line_number` int(11) NOT NULL,
  `fk_vulnerability_software` int(11) NOT NULL,
  `fk_vulnerable_file` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vulnerable_lines`
--

INSERT INTO `vulnerable_lines` (`id`, `line_number`, `fk_vulnerability_software`, `fk_vulnerable_file`) VALUES
(1, 1409, 1, 2),
(2, 730, 0, 1),
(3, 427, 2, 3),
(4, 316, 3, 4),
(5, 66, 4, 5),
(6, 69, 4, 5),
(7, 97, 4, 5),
(8, 128, 4, 5),
(9, 136, 4, 5),
(10, 382, 4, 5),
(11, 888, 4, 5),
(12, 900, 4, 5),
(13, 354, 5, 6),
(14, 93, 5, 7),
(15, 1115, 5, 8),
(16, 56, 5, 9),
(17, 264, 5, 10),
(18, 293, 5, 10),
(19, 320, 5, 10),
(20, 328, 5, 10),
(21, 367, 5, 10),
(22, 409, 5, 10),
(23, 1, 6, 11),
(24, 1091, 7, 12),
(25, 362, 9, 14),
(26, 363, 9, 14),
(27, 364, 9, 14),
(28, 488, 9, 14),
(29, 681, 9, 14),
(30, 682, 9, 14),
(31, 683, 9, 14),
(32, 684, 9, 14),
(34, 685, 9, 14),
(35, 686, 9, 14),
(36, 687, 9, 14),
(37, 688, 9, 14),
(38, 689, 9, 14),
(39, 690, 9, 14),
(40, 691, 9, 14),
(41, 692, 9, 14),
(42, 693, 9, 14),
(43, 694, 9, 14),
(44, 695, 9, 14),
(45, 696, 9, 14),
(46, 697, 9, 14),
(47, 698, 9, 14),
(48, 699, 9, 14),
(49, 700, 9, 14),
(50, 707, 9, 14),
(51, 708, 9, 14),
(52, 709, 9, 14),
(53, 710, 9, 14),
(54, 711, 9, 14),
(55, 712, 9, 14),
(56, 713, 9, 14),
(57, 714, 9, 14),
(58, 715, 9, 14),
(59, 716, 9, 14),
(60, 717, 9, 14),
(61, 718, 9, 14),
(62, 719, 9, 14),
(63, 720, 9, 14),
(64, 721, 9, 14),
(65, 722, 9, 14),
(66, 723, 9, 14),
(67, 724, 9, 14),
(68, 725, 9, 14),
(69, 726, 9, 14),
(70, 727, 9, 14),
(71, 728, 9, 14),
(72, 729, 9, 14),
(73, 730, 9, 14),
(74, 731, 9, 14),
(75, 732, 9, 14),
(76, 733, 9, 14),
(77, 757, 9, 14),
(78, 758, 9, 14),
(79, 759, 9, 14),
(80, 760, 9, 14),
(81, 761, 9, 14),
(82, 762, 9, 14),
(83, 763, 9, 14),
(84, 764, 9, 14),
(85, 765, 9, 14),
(86, 766, 9, 14),
(87, 767, 9, 14),
(88, 768, 9, 14),
(89, 769, 9, 14),
(90, 770, 9, 14),
(91, 771, 9, 14),
(92, 772, 9, 14),
(93, 366, 10, 15),
(94, 183, 10, 16),
(95, 253, 11, 17),
(96, 15, 12, 18),
(97, 16, 12, 18),
(98, 17, 12, 18),
(99, 18, 12, 18),
(100, 19, 12, 18),
(101, 20, 12, 18),
(102, 21, 12, 18),
(103, 22, 12, 18),
(104, 23, 12, 18),
(105, 24, 12, 18),
(106, 25, 12, 18),
(107, 26, 12, 18),
(108, 27, 12, 18),
(109, 28, 12, 18),
(110, 29, 12, 18),
(111, 30, 12, 18),
(112, 31, 12, 18),
(113, 32, 12, 18),
(114, 33, 12, 18),
(115, 34, 12, 18),
(116, 35, 12, 18),
(117, 36, 12, 18),
(118, 37, 12, 18),
(119, 38, 12, 18),
(120, 39, 12, 18),
(121, 40, 12, 18),
(122, 41, 12, 18),
(123, 42, 12, 18),
(124, 43, 12, 18),
(125, 44, 12, 18),
(126, 45, 12, 18),
(127, 46, 12, 18),
(128, 47, 12, 18),
(129, 48, 12, 18),
(130, 49, 12, 18),
(131, 50, 12, 18),
(132, 51, 12, 18),
(133, 52, 12, 18),
(134, 53, 12, 18),
(135, 54, 12, 18),
(136, 55, 12, 18),
(137, 56, 12, 18),
(138, 57, 12, 18),
(139, 58, 12, 18),
(140, 59, 12, 18),
(141, 60, 12, 18),
(142, 61, 12, 18),
(143, 62, 12, 18),
(144, 63, 12, 18),
(145, 97, 13, 19),
(146, 98, 13, 19),
(147, 99, 13, 19),
(148, 100, 13, 19),
(149, 101, 13, 19),
(150, 102, 13, 19),
(151, 103, 13, 19),
(152, 104, 13, 19),
(153, 105, 13, 19),
(154, 106, 13, 19),
(155, 107, 13, 19),
(156, 108, 13, 19),
(157, 109, 13, 19),
(158, 110, 13, 19),
(159, 111, 13, 19),
(160, 112, 13, 19),
(161, 113, 13, 19),
(162, 152, 13, 20),
(163, 153, 13, 20),
(164, 154, 13, 20),
(165, 155, 13, 20),
(166, 156, 13, 20),
(167, 157, 13, 20),
(168, 158, 13, 20),
(169, 159, 13, 20),
(170, 160, 13, 20),
(171, 161, 13, 20),
(172, 176, 14, 21),
(173, 109, 15, 22),
(174, 110, 15, 22),
(175, 111, 15, 22),
(176, 112, 15, 22),
(177, 113, 15, 22),
(178, 210, 15, 22),
(179, 211, 15, 22),
(180, 212, 15, 22),
(181, 97, 16, 23),
(182, 98, 16, 23),
(183, 99, 16, 23),
(184, 120, 16, 23),
(185, 121, 16, 23),
(186, 121, 16, 23),
(187, 122, 16, 23),
(188, 123, 16, 23),
(189, 124, 16, 23),
(190, 125, 16, 23),
(191, 1496, 16, 24),
(192, 1497, 16, 24),
(193, 1498, 16, 24),
(194, 1499, 16, 24),
(195, 1523, 16, 24),
(196, 1524, 16, 24),
(197, 1525, 16, 24),
(198, 1526, 16, 24),
(199, 1527, 16, 24),
(200, 999969, 17, 25),
(201, 8, 10, 15),
(202, 730, 18, 1),
(203, 731, 18, 1),
(204, 732, 18, 1),
(205, 733, 18, 1),
(206, 734, 18, 1),
(207, 1410, 1, 2),
(208, 1411, 1, 2),
(209, 1412, 1, 2),
(210, 1413, 1, 2),
(211, 915, 37, 65),
(212, 37, 36, 64),
(213, 33, 35, 63),
(214, 29, 34, 62),
(215, 31, 34, 62),
(216, 45, 34, 62),
(217, 47, 34, 62),
(218, 33, 34, 61),
(219, 29, 34, 60),
(220, 31, 34, 60),
(221, 43, 34, 60),
(222, 45, 34, 60),
(223, 33, 34, 59),
(224, 35, 34, 59),
(225, 29, 34, 58),
(226, 31, 34, 58),
(227, 45, 34, 58),
(228, 47, 34, 58),
(229, 56, 34, 57),
(230, 63, 34, 57),
(231, 69, 34, 57),
(232, 32, 34, 56),
(233, 34, 34, 56),
(234, 47, 34, 56),
(235, 49, 34, 56),
(236, 37, 34, 55),
(237, 40, 34, 55),
(238, 29, 34, 54),
(239, 31, 34, 54),
(240, 45, 34, 54),
(241, 48, 34, 54),
(242, 33, 34, 53),
(243, 35, 34, 53),
(244, 32, 34, 52),
(245, 34, 34, 52),
(246, 37, 34, 52),
(247, 49, 34, 52),
(248, 34, 34, 51),
(249, 37, 34, 51),
(250, 29, 34, 50),
(251, 31, 34, 50),
(252, 43, 34, 50),
(253, 45, 34, 50),
(254, 33, 34, 49),
(255, 35, 34, 49),
(256, 50, 34, 48),
(257, 52, 34, 48),
(258, 30, 34, 47),
(259, 32, 34, 47),
(260, 46, 34, 47),
(261, 49, 34, 47),
(262, 34, 34, 46),
(263, 37, 34, 46),
(264, 375, 34, 45),
(265, 386, 34, 45),
(266, 387, 34, 45),
(267, 79, 13, 19),
(268, 43, 38, 66),
(269, 44, 38, 66),
(270, 45, 38, 66),
(271, 48, 38, 66),
(272, 155, 38, 67),
(273, 229, 38, 68),
(274, 1077, 39, 69),
(275, 31, 59, 117),
(276, 32, 59, 117),
(277, 38, 59, 118),
(278, 67, 59, 119),
(279, 69, 59, 119),
(280, 1152, 41, 73),
(281, 308, 42, 74),
(282, 801, 43, 75),
(283, 2303, 43, 75),
(284, 542, 43, 76),
(285, 78, 44, 77),
(286, 80, 44, 77),
(287, 3923, 45, 78),
(288, 3923, 46, 79),
(289, 143, 47, 80),
(290, 455, 47, 81),
(291, 204, 48, 82),
(292, 213, 48, 82),
(293, 224, 48, 82),
(294, 372, 48, 82),
(295, 64, 49, 83),
(296, 178, 50, 84),
(297, 315, 50, 85),
(298, 316, 50, 85),
(299, 317, 50, 85),
(300, 393, 50, 85),
(301, 394, 50, 85),
(302, 395, 50, 85),
(303, 396, 50, 85),
(304, 397, 50, 85),
(305, 398, 50, 85),
(306, 399, 50, 85),
(307, 400, 50, 85),
(308, 401, 50, 85),
(309, 402, 50, 85),
(310, 403, 50, 85),
(311, 404, 50, 85),
(312, 405, 50, 85),
(313, 406, 50, 85),
(314, 407, 50, 85),
(315, 48, 50, 86),
(316, 110, 50, 86),
(317, 160, 50, 86),
(318, 118, 50, 87),
(319, 415, 50, 88),
(320, 216, 51, 89),
(321, 217, 51, 89),
(322, 218, 51, 89),
(323, 219, 51, 89),
(324, 277, 52, 90),
(325, 282, 52, 90),
(326, 286, 52, 90),
(327, 290, 52, 90),
(328, 300, 52, 90),
(329, 304, 52, 90),
(330, 308, 52, 90),
(331, 320, 52, 90),
(332, 321, 52, 90),
(333, 324, 52, 90),
(334, 325, 52, 90),
(335, 326, 52, 90),
(336, 327, 52, 90),
(337, 331, 52, 90),
(338, 334, 52, 90),
(339, 335, 52, 90),
(340, 336, 52, 90),
(341, 337, 52, 90),
(342, 449, 52, 90),
(343, 450, 52, 90),
(344, 150, 52, 91),
(345, 151, 52, 91),
(346, 152, 52, 91),
(347, 96, 52, 92),
(348, 2657, 53, 93),
(349, 239, 53, 94),
(350, 139, 53, 95),
(351, 144, 53, 97),
(352, 151, 53, 98),
(353, 231, 53, 99),
(354, 92, 53, 100),
(355, 44, 53, 101),
(356, 2657, 54, 102),
(357, 239, 54, 103),
(358, 139, 54, 104),
(359, 144, 54, 105),
(360, 151, 54, 106),
(361, 231, 54, 107),
(362, 92, 54, 108),
(363, 44, 54, 109),
(364, 987, 55, 110),
(365, 194, 56, 111),
(366, 22, 56, 111),
(367, 1405, 57, 112),
(368, 1406, 57, 112),
(369, 1713, 57, 112),
(370, 1714, 57, 112),
(371, 5383, 57, 112),
(372, 315, 57, 113),
(373, 182, 58, 114),
(374, 189, 58, 114),
(375, 87, 58, 115),
(376, 1535, 58, 116),
(377, 1545, 58, 116),
(378, 1547, 58, 116),
(379, 18, 60, 120),
(380, 78, 61, 121),
(381, 136, 62, 122),
(382, 141, 62, 122),
(383, 161, 62, 122),
(384, 93, 63, 123),
(385, 94, 63, 123),
(386, 95, 63, 123),
(387, 96, 63, 123),
(388, 797, 64, 124),
(389, 798, 64, 124),
(390, 799, 64, 124),
(391, 814, 64, 124),
(392, 815, 64, 124),
(393, 816, 64, 124),
(394, 31, 64, 125),
(395, 31, 64, 126),
(396, 72, 65, 127),
(397, 58, 66, 128),
(398, 146, 66, 129),
(399, 163, 66, 129),
(400, 2837, 67, 130),
(401, 2838, 67, 130),
(402, 2839, 67, 130),
(403, 1174, 68, 131),
(404, 1175, 68, 131),
(405, 1176, 68, 131),
(406, 1197, 68, 131),
(407, 2893, 69, 132),
(408, 2894, 69, 132),
(409, 2258, 70, 133),
(410, 2261, 70, 133),
(411, 2263, 70, 133),
(412, 1166, 71, 134),
(413, 369, 72, 135),
(414, 372, 72, 135),
(415, 4244, 72, 136),
(416, 4247, 72, 136),
(417, 1171, 72, 153),
(418, 1173, 72, 153),
(419, 1184, 72, 153),
(420, 1307, 72, 153),
(421, 1308, 72, 153),
(422, 1310, 72, 153),
(423, 650, 73, 137),
(424, 1661, 73, 137),
(425, 1664, 73, 137),
(426, 1661, 74, 138),
(427, 1664, 74, 138),
(428, 573, 75, 139),
(429, 217, 76, 140),
(430, 252, 76, 140),
(431, 1545, 77, 141),
(432, 163, 77, 154),
(433, 194, 78, 142),
(434, 196, 78, 142),
(435, 1732, 78, 143),
(436, 918, 79, 144),
(437, 25, 79, 155),
(439, 1095, 80, 145),
(440, 1096, 80, 145),
(441, 1097, 80, 145),
(442, 1100, 80, 145),
(443, 1101, 80, 145),
(444, 1118, 80, 145),
(445, 1119, 80, 145),
(446, 1125, 80, 145),
(447, 1129, 80, 145),
(448, 103, 81, 146),
(449, 73, 83, 147),
(450, 4686, 84, 148),
(451, 4687, 84, 148),
(452, 4694, 84, 148),
(453, 4695, 84, 148),
(454, 4702, 84, 148),
(455, 4703, 84, 148),
(456, 1286, 85, 149),
(459, 17, 86, 150),
(460, 533, 87, 151),
(461, 448, 88, 152),
(462, 458, 88, 152),
(463, 476, 88, 152),
(464, 477, 88, 152),
(465, 20, 86, 150);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `covered_files`
--
ALTER TABLE `covered_files`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `file_name` (`file_name`,`fk_test_id`);

--
-- Indexes for table `covered_lines`
--
ALTER TABLE `covered_lines`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `line_number` (`line_number`,`fk_file_id`);

--
-- Indexes for table `included_files`
--
ALTER TABLE `included_files`
  ADD PRIMARY KEY (`id`);

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
  ADD UNIQUE KEY `test_group` (`test_group`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `covered_lines`
--
ALTER TABLE `covered_lines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `included_files`
--
ALTER TABLE `included_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `software`
--
ALTER TABLE `software`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `software_files`
--
ALTER TABLE `software_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `software_files_description`
--
ALTER TABLE `software_files_description`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `software_functions`
--
ALTER TABLE `software_functions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `software_version`
--
ALTER TABLE `software_version`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `tests`
--
ALTER TABLE `tests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vulnerabilities`
--
ALTER TABLE `vulnerabilities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT for table `vulnerability_software`
--
ALTER TABLE `vulnerability_software`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `vulnerable_files`
--
ALTER TABLE `vulnerable_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=156;

--
-- AUTO_INCREMENT for table `vulnerable_functions`
--
ALTER TABLE `vulnerable_functions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=172;

--
-- AUTO_INCREMENT for table `vulnerable_lines`
--
ALTER TABLE `vulnerable_lines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=466;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
