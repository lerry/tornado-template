DROP TABLE IF EXISTS `Session`;
CREATE TABLE `Session` (
  `id` int(12)  unsigned NOT NULL AUTO_INCREMENT,
  `value` char(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `Tag`;
CREATE TABLE `Tag` (
  `id` int(12)  unsigned NOT NULL AUTO_INCREMENT,
  `value` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `Relationship`;
CREATE TABLE `Relationship` (
  `id` int(12)  unsigned NOT NULL AUTO_INCREMENT,
  `tag_id` int(12) NOT NULL,
  `entry_id` int(12) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


-- CREATE TABLE IF NOT EXISTS `Comment` (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `uid` int(11) DEFAULT NULL,
--   `post_id` int(11) DEFAULT NULL,
--   `email` varchar(20) DEFAULT NULL,
--   `url` varchar(50) DEFAULT NULL,
--   `content` text,
--   `time` datetime DEFAULT NULL,
--   `ip` varchar(15) DEFAULT NULL,
--   `ua` varchar(128) DEFAULT NULL,
--   `parent` int(11) DEFAULT NULL,
--   `status` smallint(6) DEFAULT NULL,
--   PRIMARY KEY (`id`)
-- ) ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `Entry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `slug` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` text,
  `post_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `allow_comment` smallint(6) DEFAULT 1,
  `view_times` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;



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
INSERT INTO `User` (`id`, `name`, `nickname`, `password`, `addtime`, `lastlogin`, `lastip`, `logintimes`) VALUES (1, 'lerry', 'lerry', '9f5a1c4d9af5076dc3f24a9240d6fff85b1e78cb', '2013-05-12 05:40:32', '2013-05-12 05:40:32', NULL, 0);


CREATE TABLE IF NOT EXISTS `PostCard` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `address` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `postcode` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `msg` varchar(256) COLLATE utf8_bin DEFAULT NULL,
  `time` int(10) unsigned DEFAULT NULL,
  `state` tinyint(3) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


DROP TABLE IF EXISTS `Oauth2`;
CREATE TABLE `Oauth2` (
  `id` int(12)  unsigned NOT NULL AUTO_INCREMENT,
  `oauth_type` varchar(16) NOT NULL,
  `oauth_id` int(12)  unsigned NOT NULL,
  `token` varchar(100) NOT NULL,
  `refresh_token` varchar(100),
  `expires_at` int(12)  unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;