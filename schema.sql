-- Adminer 4.8.1 MySQL 11.4.2-MariaDB-ubu2404 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `dataset`;
CREATE TABLE `dataset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `external_id` int(11) DEFAULT NULL,
  `formhub_uuid` varchar(254) DEFAULT NULL,
  `starttime` datetime DEFAULT NULL,
  `endtime` datetime DEFAULT NULL,
  `cd_survey_date` varchar(254) DEFAULT NULL,
  `cd_biz_status` varchar(254) DEFAULT NULL,
  `bd_biz_operating` varchar(254) DEFAULT NULL,
  `version` varchar(254) DEFAULT NULL,
  `meta_instanceID` varchar(254) DEFAULT NULL,
  `xform_id_string` varchar(254) DEFAULT NULL,
  `uuid` varchar(254) DEFAULT NULL,
  `attachments` varchar(254) DEFAULT NULL,
  `status` varchar(254) DEFAULT NULL,
  `geolocation` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`geolocation`)),
  `submission_time` datetime DEFAULT NULL,
  `tags` varchar(254) DEFAULT NULL,
  `notes` varchar(254) DEFAULT NULL,
  `validation_status` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`validation_status`)),
  `submitted_by` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_dataset_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `section_a`;
CREATE TABLE `section_a` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sec_a_unique_id` varchar(254) DEFAULT NULL,
  `sec_a_cd_biz_country_name` varchar(254) DEFAULT NULL,
  `sec_a_cd_biz_region_name` varchar(254) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`),
  KEY `ix_section_a_id` (`id`),
  CONSTRAINT `section_a_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `dataset` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `section_b`;
CREATE TABLE `section_b` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sec_b_bda_name` varchar(254) DEFAULT NULL,
  `sec_b_cd_cohort` varchar(254) DEFAULT NULL,
  `sec_b_cd_program` varchar(254) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`),
  KEY `ix_section_b_id` (`id`),
  CONSTRAINT `section_b_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `dataset` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


DROP TABLE IF EXISTS `section_c`;
CREATE TABLE `section_c` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sec_c_cd_client_name` varchar(254) DEFAULT NULL,
  `sec_c_cd_client_id_manifest` varchar(254) DEFAULT NULL,
  `sec_c_cd_location` varchar(254) DEFAULT NULL,
  `sec_c_cd_clients_phone` varchar(254) DEFAULT NULL,
  `sec_c_cd_phoneno_alt_number` varchar(254) DEFAULT NULL,
  `sec_c_cd_clients_phone_smart_feature` varchar(254) DEFAULT NULL,
  `sec_c_cd_gender` varchar(254) DEFAULT NULL,
  `sec_c_cd_age` int(11) DEFAULT NULL,
  `sec_c_cd_nationality` varchar(254) DEFAULT NULL,
  `sec_c_cd_strata` varchar(254) DEFAULT NULL,
  `sec_c_cd_disability` varchar(254) DEFAULT NULL,
  `sec_c_cd_education` varchar(254) DEFAULT NULL,
  `sec_c_cd_client_status` varchar(254) DEFAULT NULL,
  `sec_c_cd_sole_income_earner` varchar(254) DEFAULT NULL,
  `sec_c_cd_howrespble_pple` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`),
  KEY `ix_section_c_id` (`id`),
  CONSTRAINT `section_c_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `dataset` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;


-- 2024-08-30 12:42:09