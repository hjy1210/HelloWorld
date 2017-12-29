select radius,t_eff from Star where radius>1;

/* A range of hot stars */
select kepler_id, t_eff 
from Star
where t_eff between 5000 and 6000

/* Confirmed exoplanets */
select kepler_name,radius 
from Planet 
where not kepler_name is NULL and radius between 1 and 3;

/* Planet statistics */
select min(radius),max(radius),avg(radius),stddev(radius)
from Planet 
where kepler_name is  NULL;

/* Planets in multi-planet systems */
select kepler_id,count(*)
from Planet
group by kepler_id
having count(*)>1
order by count(*) desc;

/* Systems with small planets */
select s.radius as sun_radius, p.radius as planet_radius
from Star as s, Planet as p
where s.kepler_id=p.kepler_id and s.radius>p.radius 
order by s.radius desc;

/* How many planets for big stars? */
select s.radius as radius, count(*) as count
from Star as s
join Planet as p on s.radius>1 and s.kepler_id = p.kepler_id
group by s.kepler_id
having count(*)>1
order by s.radius desc;

/* Lonely stars */
select s.kepler_id as kepler_id, s.t_eff as t_eff, s.radius as radius
from Star s
left outer join Planet p
on s.kepler_id=p.kepler_id
where p.kepler_id is NULL
group by s.kepler_id
order by s.t_eff desc;

/* Subquery joint stars and planets */
select round(avg(p.t_eq),1) , min(s.t_eff), max(s.t_eff)
from Star s, Planet p
where s.t_eff > (select avg(t_eff) from Star) and s.kepler_id=p.kepler_id

/* Correlated sizes? */
select p.koi_name as koi_name, p.radius as radius, s.radius as radius
from Star s, Planet p
where p.kepler_id= s.kepler_id and p.kepler_id in 
(
  select s.kepler_id
  from Star s
  order by s.radius desc
  limit 5
)

/* Adding Stars */
insert into Star (kepler_id,t_eff,radius) 
values (7115384,	3789,	27.384),
       (8106973,	5810,	0.811),
        (9391817,	6200,	0.958);

/* A messed up table */
\d Planet
select * from Planet;

delete from Planet
where radius< 0;

update Planet
set kepler_name=NULL
where not status='CONFIRMED';

/*  Make your own table */
create table Planet
  (kepler_id integer not NULL,
    koi_name varchar(15) not null unique,
    kepler_name varchar(15),
    status varchar(20) not null,
    radius float not null);
\d Planet
insert into Planet
(kepler_id, koi_name, kepler_name,status, radius)
values
(6862328,	'K00865.01',null,'CANDIDATE',	119.021),
(10187017,	'K00082.05',	'Kepler-102 b',	'CONFIRMED',	5.286),
(10187017,	'K00082.04',	'Kepler-102 c',	'CONFIRMED',	7.071);

/* DIY exoplanet archive */
CREATE TABLE Star (
  kepler_id INTEGER PRIMARY KEY,
  t_eff INTEGER not null,
  radius FLOAT not null
);
create table Planet(
  kepler_id integer references Star(kepler_id),
  koi_name varchar(20) primary key,
  kepler_name varchar(20),
  status varchar(20) not null,
  period float,
  radius float,
  t_eq integer
  );
  
COPY Star (kepler_id, t_eff, radius) 
  FROM 'stars.csv' CSV;
COPY Planet (kepler_id, koi_name, kepler_name, status, period, radius, t_eq) 
  FROM 'planets.csv' CSV;
SELECT * FROM Star;
select * from Planet;

/* Star coordinates */
alter table Star
add column ra float;
alter table Star
add column decl float;

delete from Star;

COPY Star (kepler_id, t_eff, radius,ra,decl) 
  FROM 'stars_full.csv' CSV;

/* Taking it all in */
/* package psycopg2 */
import psycopg2

# Establish the connection
conn = psycopg2.connect(dbname='db', user='grok')
cursor = conn.cursor()

def select_all(tablename):
  cursor.execute('select * from '+tablename+';')
  records=cursor.fetchall()
  return records

/* A proper median */
import psycopg2
import numpy as np
# Establish the connection
conn = psycopg2.connect(dbname='db', user='grok')
cursor = conn.cursor()

def column_stats(table,column):
  cursor.execute('select {0} from {1};'.format(column,table))
  records=cursor.fetchall()
  data=np.array(records)
  return np.mean(data),np.median(data)

/* Simple queries in Python 1/3 */
import psycopg2
import numpy as np
# mimic following sql statement in python
# SELECT kepler_id, radius
# FROM Star
# WHERE radius > 1.0;
def query(csvfile):
  data=np.loadtxt(csvfile,usecols=[0,2],delimiter=',')
  return data[data[:,1]>1.0,:]

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  print(query('stars.csv'))

/* Simple queries in Python 2/3 */
# Write your query function here
# SELECT kepler_id, radius
# FROM Star
# WHERE radius > 1.0
# ORDER BY radius ASC;

import numpy as np
def query(csvfile):
  data=np.loadtxt(csvfile,usecols=[0,2],delimiter=',')
  data=data[data[:,1]>1.0,:]
  return data[np.argsort(data[:,1]),:]



# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  print(query('stars.csv'))

/* Simple queries in Python 3/3 */
# SELECT p.radius/s.radius AS radius_ratio
# FROM Planet AS p
# INNER JOIN star AS s USING (kepler_id)
# WHERE s.radius > 1.0 *
# ORDER BY p.radius/s.radius ASC;
import numpy as np
def query(starfile, planetfile):
  stars=np.loadtxt(starfile,usecols=[0,2],delimiter=',')
  planets=np.loadtxt(planetfile,usecols=[0,5],delimiter=',')
  stars=stars[stars[:,1]>1.0,:]
  res=[]
  for i in range(stars.shape[0]):
    for j in range(planets.shape[0]):
      if planets[j,0]==stars[i,0]:
        res.append(planets[j,1]/[stars[i,1]])
  res=np.array(res)
  return res[np.argsort(res[:,0])]

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')
  print(result)
  print(np.sort(np.array([1,5,3,2])))
