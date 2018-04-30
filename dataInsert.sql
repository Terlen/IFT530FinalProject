use footballLeague;

INSERT INTO Team
VALUES ('Sun Devils', 'Tempe', 'AZ'),('Buffalos', 'Boulder', 'CO'),('Aggies', 'Los Cruces', 'NM'),
		('Ducks', 'Eugene', 'OR'), ('Beavers', 'Corvallis', 'OR'),('Aztecs', 'San Diego', 'CA'),
		('Cardinals','Stanford','CA'),('Red Raiders', 'Lubboch','TX'),('Bruins','Passadena','CA'),
		('Wildcats','Tuscon','AZ'),('Trojans','Los Angeles','CA'),('Utes','Salt Lake City','UT'),
		('Huskies','Seattle','WA')

INSERT INTO Stadium
VALUES ('Sun Devil','Tempe','AZ'),('Folsom Field','Boulder','CO'),('Aggie Memorial','Los Cruces','NM'),
		('Autzen','Eugene','OR'),('Reser','Corvallis','OR'),('San Diego State','San Diego','CA'),
		('Stanford','Stanford','CA'),('Jones AT&T','Lubboch','TX'),('Rose Bowl','Pasadena','CA'),
		('Arizona','Tuscon','AZ'),('Los Angeles Memorial','Los Angeles','CA'),('Rice-Eccles','Salt Lake City','UT'),
		('Husky','Seattle','WA')

INSERT INTO Player
VALUES ('A.J.','McCollum',NULL,74,311,'1/1/1990'),('Abe','Thompson',NULL,74,230,'1/1/1990'),
		('Alani','Latu',NULL,74,248,'1/1/1990'),('Alex','Losoya',NULL,76,290,'1/1/1990'),
		('Alex','Perry',NULL,71,169,'1/1/1990'),('Alexander','Otero',NULL,76,263,'1/1/1990')

SELECT * FROM Matchup

INSERT INTO Matchup
VALUES (1,1,3,'08/31/17'),(1,1,6,'09/01/17'),(8,8,1,'09/16/17'),(1,1,4,'09/23/17'),(7,7,1,'09/30/17'),
		(1,1,13,'10/14/17'),(12,12,1,'10/21/17'),(1,1,11,'10/28/17'),(1,1,2,'11/04/17'),(9,9,1,'11/11/17'),
		(5,5,1,'11/18/17'),(1,1,10,'11/25/17')

INSERT INTO Stats
VALUES (1,1,53,4),(1,3,67,3),(2,1,89,2),(2,6,67,3),(3,8,120,5),(3,1,200,2),(4,1,220,1),(4,4,100,3),
		(5,7,45,1),(5,1,80,7),(6,1,47,2),(6,13,66,6),(7,12,300,2),(7,1,204,4),(8,1,230,3),(8,11,160,2),
		(9,1,400,7),(9,2,300,2),(10,9,700,5),(10,1,300,4),(11,5,200,4),(11,1,400,5),(12,1,340,4),(12,10,400,2)

INSERT INTO Roster
VALUES ('05/04/2016',1,1,'Wide Receiver',22,NULL),('05/04/2016',2,1,'Quarterback',1,NULL),
		('05/04/2012',3,1,'Safety',16,'05/04/2014'),('05/04/2014',3,2,'Safety',16,NULL),
		('02/13/2013',4,2,'Linebacker',28,NULL),('10/27/2017',5,3,'Centre',67,'12/20/2018')

INSERT INTO Score
VALUES (1,1,46),(1,3,34),(2,1,50),(2,6,60),(3,8,10),(3,1,20),(4,1,42),(4,4,14),(5,7,33),(5,1,12),(6,1,30),(6,13,20),
		(7,12,0),(7,1,12),(8,1,7),(8,11,15),(9,1,24),(9,2,26),(10,9,12),(10,1,14),(11,5,30),(11,1,0),(12,1,40),
		(12,10,33)
