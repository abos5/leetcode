

-- 168 ms
select
    Request_at as Day,
    round(avg(case when status = 'completed' then 0 else 1 end), 2) as `Cancellation Rate`
from Trips t
inner join Users u on t.client_id = u.users_id and u.banned='No'
where Request_at between '2013-10-01' and '2013-10-03'
group by Request_at;

-- 143 ms remove inner join
select
    Request_at as Day,
    round(avg(case when status = 'completed' then 0 else 1 end), 2) as `Cancellation Rate`
from Trips t, Users u
where t.client_id = u.users_id and u.banned='No'
and Request_at between '2013-10-01' and '2013-10-03'
group by Request_at;

-- 126 ms remove case 141 ms(2nd time)
select
    Request_at as Day,
    round(avg(IF (status = 'completed', 0, 1 )), 2) as `Cancellation Rate`
from Trips t, Users u
where t.client_id = u.users_id and u.banned='No'
and Request_at between '2013-10-01' and '2013-10-03'
group by Request_at;

-- 124 ms copy from discussion
select Day, round(avg(cnt), 2) as "Cancellation Rate"
from
(   select a.request_at as Day,
    @cnt := IF(a.Status = 'completed', 0, 1) as cnt
    from Trips a, Users b
    where a.Client_Id = b.Users_Id and b.Banned = 'No'
) c
where Day BETWEEN '2013-10-01' AND '2013-10-03'
group by Day

-- 143 ms copy from discussion and move up where
select Day, round(avg(cnt), 2) as "Cancellation Rate" from
(   select a.request_at as Day,
    @cnt := IF(a.Status = 'completed', 0, 1) as cnt
    from Trips a, Users b
    where a.Client_Id = b.Users_Id and b.Banned = 'No'
    and request_at BETWEEN '2013-10-01' AND '2013-10-03'
) c
group by Day;


-- data initialization

create table Trips(
Id int not null primary key auto_increment,
Client_Id int not null default 0 ,
Driver_Id int not null default 0 ,
City_Id int not null default 0 ,
Status enum('completed', 'cancelled_by_driver', 'cancelled_by_client') not null default 'completed',
Request_at varchar(10) not null default '2013-01-01'
);

create table Users(
Users_Id int not null primary key auto_increment,
Banned enum('No', 'Yes') not null default 'No' ,
Role enum('client', 'driver') not null default 'client'
);

insert into Trips values
 (1  ,     1     ,    10     ,    1    ,     'completed'      ,'2013-10-01'),
 (2  ,     2     ,    11     ,    1    , 'cancelled_by_driver','2013-10-01'),
 (3  ,     3     ,    12     ,    6    ,     'completed'      ,'2013-10-01'),
 (4  ,     4     ,    13     ,    6    , 'cancelled_by_client','2013-10-01'),
 (5  ,     1     ,    10     ,    1    ,     'completed'      ,'2013-10-02'),
 (6  ,     2     ,    11     ,    6    ,     'completed'      ,'2013-10-02'),
 (7  ,     3     ,    12     ,    6    ,     'completed'      ,'2013-10-02'),
 (8  ,     2     ,    12     ,    12   ,     'completed'      ,'2013-10-03'),
 (9  ,     3     ,    10     ,    12   ,     'completed'      ,'2013-10-03'),
 (10 ,     4     ,    13     ,    12   , 'cancelled_by_driver','2013-10-03');

insert into Users values
(1,'No', 'client'),
(2,'Yes', 'client'),
(3,'No', 'client'),
(4,'No', 'client'),
(10,'No', 'driver'),
(11,'No', 'driver'),
(12,'No', 'driver'),
(13,'No', 'driver');