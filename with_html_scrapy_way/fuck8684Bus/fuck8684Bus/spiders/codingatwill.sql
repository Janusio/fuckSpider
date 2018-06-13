/*
Navicat MySQL Data Transfer

Source Server         : Localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : codingatwill

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-05-28 17:58:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for area
-- ----------------------------
DROP TABLE IF EXISTS `area`;
CREATE TABLE `area` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cityId` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `16` (`cityId`),
  CONSTRAINT `16` FOREIGN KEY (`cityId`) REFERENCES `city` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of area
-- ----------------------------
INSERT INTO `area` VALUES ('1', '武侯区', '1');
INSERT INTO `area` VALUES ('2', '龙泉驿区', '1');
INSERT INTO `area` VALUES ('3', '高新区', '1');

-- ----------------------------
-- Table structure for busesef
-- ----------------------------
DROP TABLE IF EXISTS `busesef`;
CREATE TABLE `busesef` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `busName` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `busType` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `busTime` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `busPrice` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `busCompany` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `busUpdateTime` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `busUrl` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of busesef
-- ----------------------------

-- ----------------------------
-- Table structure for city
-- ----------------------------
DROP TABLE IF EXISTS `city`;
CREATE TABLE `city` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `privinceId` int(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `161` (`privinceId`),
  CONSTRAINT `161` FOREIGN KEY (`privinceId`) REFERENCES `privince` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of city
-- ----------------------------
INSERT INTO `city` VALUES ('1', '成都', '1');
INSERT INTO `city` VALUES ('2', '北京', '2');
INSERT INTO `city` VALUES ('3', '眉山', '1');

-- ----------------------------
-- Table structure for country
-- ----------------------------
DROP TABLE IF EXISTS `country`;
CREATE TABLE `country` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of country
-- ----------------------------
INSERT INTO `country` VALUES ('1', '中国');
INSERT INTO `country` VALUES ('2', '加拿大');
INSERT INTO `country` VALUES ('3', '美国');

-- ----------------------------
-- Table structure for interestlist
-- ----------------------------
DROP TABLE IF EXISTS `interestlist`;
CREATE TABLE `interestlist` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `interestTypeId` int(50) NOT NULL,
  KEY `iid` (`id`),
  KEY `1` (`interestTypeId`),
  CONSTRAINT `1` FOREIGN KEY (`interestTypeId`) REFERENCES `interesttype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of interestlist
-- ----------------------------
INSERT INTO `interestlist` VALUES ('1', 'java', '1');
INSERT INTO `interestlist` VALUES ('2', 'python', '1');
INSERT INTO `interestlist` VALUES ('3', 'Ajax', '2');

-- ----------------------------
-- Table structure for interesttype
-- ----------------------------
DROP TABLE IF EXISTS `interesttype`;
CREATE TABLE `interesttype` (
  `id` int(50) NOT NULL,
  `name` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of interesttype
-- ----------------------------
INSERT INTO `interesttype` VALUES ('1', '后端');
INSERT INTO `interesttype` VALUES ('2', '前端');

-- ----------------------------
-- Table structure for interest_user
-- ----------------------------
DROP TABLE IF EXISTS `interest_user`;
CREATE TABLE `interest_user` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `userid` int(50) NOT NULL,
  `interestid` int(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `12` (`interestid`),
  KEY `121` (`userid`),
  CONSTRAINT `12` FOREIGN KEY (`interestid`) REFERENCES `interestlist` (`id`),
  CONSTRAINT `121` FOREIGN KEY (`userid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of interest_user
-- ----------------------------
INSERT INTO `interest_user` VALUES ('1', '1', '1');

-- ----------------------------
-- Table structure for iprecord
-- ----------------------------
DROP TABLE IF EXISTS `iprecord`;
CREATE TABLE `iprecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `userId` int(11) DEFAULT NULL,
  `BeginTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `17` (`userId`),
  CONSTRAINT `17` FOREIGN KEY (`userId`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of iprecord
-- ----------------------------
INSERT INTO `iprecord` VALUES ('1', '1.1.1.1', '1', '2018-05-23 17:54:12');

-- ----------------------------
-- Table structure for jodlist
-- ----------------------------
DROP TABLE IF EXISTS `jodlist`;
CREATE TABLE `jodlist` (
  `id` int(50) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `interestId` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `18` (`interestId`),
  CONSTRAINT `18` FOREIGN KEY (`interestId`) REFERENCES `interestlist` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of jodlist
-- ----------------------------
INSERT INTO `jodlist` VALUES ('1', '后端开发工程师', '1');

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `content` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `userid` int(50) DEFAULT NULL,
  `interestId` int(50) DEFAULT NULL,
  `begintime` datetime DEFAULT NULL,
  `level` int(10) DEFAULT NULL,
  `previosId` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `13` (`userid`),
  KEY `131` (`interestId`),
  KEY `132` (`previosId`),
  CONSTRAINT `13` FOREIGN KEY (`userid`) REFERENCES `user` (`id`),
  CONSTRAINT `131` FOREIGN KEY (`interestId`) REFERENCES `interestlist` (`id`),
  CONSTRAINT `132` FOREIGN KEY (`previosId`) REFERENCES `post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES ('1', '这是一个测试标题', '你们好，我开始讲述java后端了', '1', '3', '2018-05-08 17:57:46', '0', null);
INSERT INTO `post` VALUES ('2', '再次标题', '你们好，再次上课了', '1', '2', '2018-05-08 17:58:22', '0', null);
INSERT INTO `post` VALUES ('3', '第一次回复', '我是一楼', '1', null, '2018-05-23 17:58:53', '1', '1');

-- ----------------------------
-- Table structure for privince
-- ----------------------------
DROP TABLE IF EXISTS `privince`;
CREATE TABLE `privince` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `countryId` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `15` (`countryId`),
  CONSTRAINT `15` FOREIGN KEY (`countryId`) REFERENCES `country` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of privince
-- ----------------------------
INSERT INTO `privince` VALUES ('1', '四川', '1');
INSERT INTO `privince` VALUES ('2', '北京', '1');

-- ----------------------------
-- Table structure for roadrun
-- ----------------------------
DROP TABLE IF EXISTS `roadrun`;
CREATE TABLE `roadrun` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stationName` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `busUrl` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `stationSorted` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `stationUrl` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of roadrun
-- ----------------------------
INSERT INTO `roadrun` VALUES ('1', '天府软件园公交站', null, null, '/z_5ef31aa4');
INSERT INTO `roadrun` VALUES ('2', '天府软件园东侧', null, null, '/z_398eaf6e');
INSERT INTO `roadrun` VALUES ('3', '天华路', null, null, '/z_733ec84f');
INSERT INTO `roadrun` VALUES ('4', '新会展中心南侧', null, null, '/z_0d241189');
INSERT INTO `roadrun` VALUES ('5', '新会展中心东侧', null, null, '/z_f14c866d');
INSERT INTO `roadrun` VALUES ('6', '新会展北侧世纪城路口', null, null, '/z_fd9b0e96');
INSERT INTO `roadrun` VALUES ('7', '新会展中心北侧', null, null, '/z_d8218467');
INSERT INTO `roadrun` VALUES ('8', '天府大道世纪城路口北', null, null, '/z_a71df416');
INSERT INTO `roadrun` VALUES ('9', '天府大道北段', null, null, '/z_1938f779');
INSERT INTO `roadrun` VALUES ('10', '天府大道锦尚东路口', null, null, '/z_7b13fe52');
INSERT INTO `roadrun` VALUES ('11', '天府长城', null, null, '/z_55a16c97');
INSERT INTO `roadrun` VALUES ('12', '人南立交桥南', null, null, '/z_a0dae2db');
INSERT INTO `roadrun` VALUES ('13', '人南立交桥北', null, null, '/z_1b4ccc58');
INSERT INTO `roadrun` VALUES ('14', '倪家桥', null, null, '/z_099da369');
INSERT INTO `roadrun` VALUES ('15', '人民南路四段北', null, null, '/z_009e46bf');
INSERT INTO `roadrun` VALUES ('16', '地铁省体育馆站', null, null, '/z_836907a2');
INSERT INTO `roadrun` VALUES ('17', '人民南路三段中(华西第二、第四医院)', null, null, '/z_f5b5536a');
INSERT INTO `roadrun` VALUES ('18', '华西坝', null, null, '/z_d8858f9e');
INSERT INTO `roadrun` VALUES ('19', '锦江宾馆', null, null, '/z_612ce26a');
INSERT INTO `roadrun` VALUES ('20', '人民南路一段', null, null, '/z_f7cf8722');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(50) NOT NULL AUTO_INCREMENT COMMENT '用户名称',
  `nickname` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '用户昵称',
  `email` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '邮箱',
  `type` tinyint(1) DEFAULT NULL COMMENT '2: 随机账户; 1: 注册账号',
  `address` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `jobId` int(50) DEFAULT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `passwordBeginTime` datetime DEFAULT NULL,
  `passwordLossTotalTime` datetime DEFAULT NULL,
  `areaId` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `19` (`jobId`),
  KEY `191` (`areaId`),
  CONSTRAINT `19` FOREIGN KEY (`jobId`) REFERENCES `jodlist` (`id`),
  CONSTRAINT `191` FOREIGN KEY (`areaId`) REFERENCES `area` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'Janus', 'neng_qi_2018@163.com', '1', '航天丙区', '1', '1314', '2018-05-23 17:53:12', null, '1');
