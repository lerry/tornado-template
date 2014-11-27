CREATE TABLE IF NOT EXISTS `Session` (
  `id` int(12)  unsigned NOT NULL AUTO_INCREMENT,
  `value` char(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


CREATE TABLE IF NOT EXISTS `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `nickname` varchar(20) DEFAULT NULL,
  `password` varchar(50) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `lastlogin` datetime DEFAULT NULL,
  `lastip` varchar(20) DEFAULT NULL,
  `logintimes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
# INSERT INTO `User` (`id`, `name`, `nickname`, `password`, `addtime`, `lastlogin`, `lastip`, `logintimes`) VALUES (1, 'lerry', 'lerry', 'aaaaaaaaaaf5076dc3f24a9240d6fff85b1e78cb', '2013-05-12 05:40:32', '2013-05-12 05:40:32', NULL, 0);

DROP TABLE IF EXISTS `Log`;
CREATE TABLE IF NOT EXISTS `Log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source` TINYINT NOT NULL,
  `create_time` int(11),
  `txt` TEXT,
  `author` TINYINT,
  `remark` TEXT,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
