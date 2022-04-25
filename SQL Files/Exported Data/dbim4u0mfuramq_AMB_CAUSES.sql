-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 35.213.140.165    Database: dbim4u0mfuramq
-- ------------------------------------------------------
-- Server version	5.7.32-35-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AMB_CAUSES`
--

DROP TABLE IF EXISTS `AMB_CAUSES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AMB_CAUSES` (
  `CAUSE_ID` varchar(20) NOT NULL,
  `CAUSE_TYPE` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AMB_CAUSES`
--

LOCK TABLES `AMB_CAUSES` WRITE;
/*!40000 ALTER TABLE `AMB_CAUSES` DISABLE KEYS */;
INSERT INTO `AMB_CAUSES` VALUES ('AMBCASID001','Accident'),('AMBCASID002','Heart Stroke /chest pain'),('AMBCASID003','Brain stroke'),('AMBCASID004','Fire '),('AMBCASID005','chocking'),('AMBCASID006','severe bleeding'),('AMBCASID007','Amputation'),('AMBCASID008','Miscarraige'),('AMBCASID009','Diabetic Coma'),('AMBCASID010','Seizure'),('AMBCASID011','Loss of Consciuosness'),('AMBCASID012','Allergic Reaction'),('AMBCASID013','Severe Abdominal pain'),('AMBCASID014','swallowe poison or Tablets'),('AMBCASID015','difficult breathing'),('AMBCASID016','lips and face turning blue'),('AMBCASID017','severe burns'),('AMBCASID018','coughing or vomting blood'),('AMBCASID019','severe pain'),('AMBCASID020','severe headache'),('AMBCASID021','stroke symptoms'),('AMBCASID022','drowning'),('AMBCASID023','vision problems'),('AMBCASID024','High fever'),('AMBCASID025','confusion or trouble speaking'),('AMBCASID026','broken bones'),('AMBCASID027','suicidal or homicidal feelings'),('AMBCASID028','Fits'),('AMBCASID029','head injury'),('AMBCASID030','severe dehydration');
/*!40000 ALTER TABLE `AMB_CAUSES` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-25 16:19:14
