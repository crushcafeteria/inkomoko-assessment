-- Adminer 4.8.1 MySQL 11.5.2-MariaDB-ubu2404 dump

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
  `sec_a_unique_id` varchar(254) DEFAULT NULL,
  `sec_a_cd_biz_country_name` varchar(254) DEFAULT NULL,
  `sec_a_cd_biz_region_name` varchar(254) DEFAULT NULL,
  `sec_b_bda_name` varchar(254) DEFAULT NULL,
  `sec_b_cd_cohort` varchar(254) DEFAULT NULL,
  `sec_b_cd_program` varchar(254) DEFAULT NULL,
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
  `group_mx5fl16_cd_biz_status` varchar(254) DEFAULT NULL,
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

INSERT INTO `dataset` (`id`, `external_id`, `formhub_uuid`, `starttime`, `endtime`, `cd_survey_date`, `sec_a_unique_id`, `sec_a_cd_biz_country_name`, `sec_a_cd_biz_region_name`, `sec_b_bda_name`, `sec_b_cd_cohort`, `sec_b_cd_program`, `sec_c_cd_client_name`, `sec_c_cd_client_id_manifest`, `sec_c_cd_location`, `sec_c_cd_clients_phone`, `sec_c_cd_phoneno_alt_number`, `sec_c_cd_clients_phone_smart_feature`, `sec_c_cd_gender`, `sec_c_cd_age`, `sec_c_cd_nationality`, `sec_c_cd_strata`, `sec_c_cd_disability`, `sec_c_cd_education`, `sec_c_cd_client_status`, `sec_c_cd_sole_income_earner`, `sec_c_cd_howrespble_pple`, `group_mx5fl16_cd_biz_status`, `version`, `meta_instanceID`, `xform_id_string`, `uuid`, `attachments`, `status`, `geolocation`, `submission_time`, `tags`, `notes`, `validation_status`, `submitted_by`) VALUES
(5,	376888360,	'a7eb959ada4c485b8334ee761ab1e4a7',	'2024-08-29 02:06:06',	'2024-08-29 02:08:29',	'2024-08-29',	'SS01406240716145458',	'Kenya',	'Dadaab',	'Yunis Abdirahman',	'Cohort 2',	'Livelihood',	'NETSANET ADENE GEBREHIWET',	'106-00010320',	'Juba urban refugees',	'925956160',	NULL,	'Smart phone',	'Female',	32,	'Ethiopian',	'Urban Based Refugee',	'No',	'Attended high school',	'New clients',	'Yes',	3,	'Idea stage',	'vBfco72yRxvHQun3cF8HPK',	'uuid:e7b88b99-c2cb-4a08-bac8-681c54686be8',	'aW9w8jHjn4Cj8SSQ5VcojK',	'e7b88b99-c2cb-4a08-bac8-681c54686be8',	'[]',	'submitted_via_web',	'\"[null, null]\"',	'2024-08-28 23:08:32',	'[]',	'[]',	'\"{}\"',	NULL),
(6,	376888732,	'a7eb959ada4c485b8334ee761ab1e4a7',	'2024-08-29 02:08:29',	'2024-08-29 02:10:46',	'2024-08-29',	'SS01406240716100553',	'Ethiopia',	'Addis Ababa',	'Estalu Baye',	'Cohort 2',	'Livelihood',	'NDIKURIYO EGIDE',	'106-00002884',	'Juba urban refugees',	'921814730',	'927360888',	'Smart phone Feature phone',	'Male',	33,	'Burundian',	'Urban Based Refugee',	'No',	'Attended high school',	'New clients',	'Yes',	5,	'Idea stage',	'vBfco72yRxvHQun3cF8HPK',	'uuid:d512b0d5-b1af-43ac-b3cf-00618215c51f',	'aW9w8jHjn4Cj8SSQ5VcojK',	'd512b0d5-b1af-43ac-b3cf-00618215c51f',	'[]',	'submitted_via_web',	'\"[null, null]\"',	'2024-08-28 23:10:50',	'[]',	'[]',	'\"{}\"',	NULL),
(7,	376889084,	'a7eb959ada4c485b8334ee761ab1e4a7',	'2024-08-29 02:10:46',	'2024-08-29 02:14:03',	'2024-08-31',	'SS01406240716100553',	'Ethiopia',	'Addis Ababa',	'Ahmed Mohammed',	'Cohort 2',	'Livelihood',	'NDIKURIYO EGIDE',	'106-00002884',	'Juba urban refugees',	'921814730',	'927360888',	'Smart phone Feature phone',	'Male',	33,	'Burundian',	'Urban Based Refugee',	'No',	'Attended high school',	'New clients',	'Yes',	5,	'Idea stage',	'vBfco72yRxvHQun3cF8HPK',	'uuid:049d4ec5-23fc-41cd-8415-6d5d7be20bcc',	'aW9w8jHjn4Cj8SSQ5VcojK',	'049d4ec5-23fc-41cd-8415-6d5d7be20bcc',	'[]',	'submitted_via_web',	'\"[null, null]\"',	'2024-08-28 23:14:05',	'[]',	'[]',	'\"{}\"',	NULL),
(8,	376889725,	'a7eb959ada4c485b8334ee761ab1e4a7',	'2024-08-29 02:14:03',	'2024-08-29 02:19:50',	'2024-08-29',	'SS01406240717130102',	'Ethiopia',	'Addis Ababa',	'Ahmed Mohammed',	'Cohort 2',	'Livelihood',	'SUWAD OMAR KUKU',	'243-00002864',	'Juba urban refugees',	'915137484',	NULL,	'Feature phone',	'Female',	51,	'Sudanese',	'Urban Based Refugee',	'No',	'Attended primary school',	'New clients',	'Yes',	8,	'Idea stage',	'vBfco72yRxvHQun3cF8HPK',	'uuid:f34a0c18-bb8a-44be-940d-da19266614da',	'aW9w8jHjn4Cj8SSQ5VcojK',	'f34a0c18-bb8a-44be-940d-da19266614da',	'[]',	'submitted_via_web',	'\"[null, null]\"',	'2024-08-28 23:19:52',	'[]',	'[]',	'\"{}\"',	NULL),
(9,	376889869,	'a7eb959ada4c485b8334ee761ab1e4a7',	'2024-08-29 02:19:50',	'2024-08-29 02:20:57',	'2024-08-30',	'SS01406240717130102',	'South Sudan',	'Juba',	'Atong Grace Akuot',	'Cohort 2',	'Livelihood',	'SUWAD OMAR KUKU',	'243-00002864',	'Juba urban refugees',	'915137484',	NULL,	'Feature phone',	'Female',	51,	'Sudanese',	'Urban Based Refugee',	'No',	'Attended primary school',	'New clients',	'Yes',	8,	'Idea stage',	'vBfco72yRxvHQun3cF8HPK',	'uuid:03386603-52c4-4e79-9264-ea96b78eee3a',	'aW9w8jHjn4Cj8SSQ5VcojK',	'03386603-52c4-4e79-9264-ea96b78eee3a',	'[]',	'submitted_via_web',	'\"[null, null]\"',	'2024-08-28 23:20:59',	'[]',	'[]',	'\"{}\"',	NULL);

-- 2024-08-28 23:23:42
