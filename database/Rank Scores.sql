
-- failed, runtime error
--
select Score, @rank := @rank+ (@pre<>(@pre:=Score)) as Rank from
    Scores,
    (select @pre:=-1, @rank:=0) init
order by score desc

CREATE TABLE `scores2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` double NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
)