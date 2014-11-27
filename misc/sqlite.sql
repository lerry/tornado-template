CREATE TABLE log (
    id INTEGER PRIMARY KEY,
    source NUMERIC, 
    create_time NUMERIC,
    txt TEXT, 
    author NUMERIC,
    remark TEXT
);


-- DROP TABLE IF EXISTS `log`;
-- CREATE TABLE `log` (
--   `id` int(12)  unsigned NOT NULL AUTO_INCREMENT,
--   `source` tinyint NOT NULL,
--   `create_time` int(12) NOT NULL,
--   `txt` text NOT NULL,
--   `author` tinyint NOT NULL,
--   `remark` text, 
--   PRIMARY KEY (`id`)
-- ) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;