--use master
DROP DATABASE footballLeague;
CREATE DATABASE footballLeague;
GO
USE footballLeague;
GO

-- Table Creation --
CREATE TABLE Team(TeamID INT PRIMARY KEY NOT NULL, Name VARCHAR(50), Location VARCHAR(50));
CREATE TABLE Stadium(StadiumID INT PRIMARY KEY NOT NULL, StadiumName VARCHAR(50), Address VARCHAR(50));
CREATE TABLE Player(PlayerID INT PRIMARY KEY NOT NULL, FirstName VARCHAR(25) NOT NULL, LastName VARCHAR(25) 
			NOT NULL, MiddleInitial VARCHAR(1), Height INT, Weight INT, DateOfBirth DATE);
CREATE TABLE Matchup(MatchupID INT PRIMARY KEY NOT NULL, StadiumID INT FOREIGN KEY REFERENCES Stadium(StadiumID),
			HomeTeamID INT FOREIGN KEY REFERENCES Team(TeamID), AwayTeamID INT FOREIGN KEY REFERENCES Team(TeamID))

CREATE TABLE Stats(MatchupID INT FOREIGN KEY REFERENCES Matchup(MatchupID), TeamID INT FOREIGN KEY REFERENCES 
			Team(TeamID), OffensiveYards INT, Turnovers INT, PRIMARY KEY (MatchupID, TeamID))
CREATE TABLE Roster(BeginDate DATE NOT NULL, PlayerID INT FOREIGN KEY REFERENCES Player(PlayerID), TeamID INT
			FOREIGN KEY REFERENCES Team(TeamID),Position VARCHAR(25), Number INT, EndDate DATE, PRIMARY KEY
			(BeginDate, PlayerID))

CREATE TABLE Score(MatchupID INT FOREIGN KEY REFERENCES Matchup(MatchupID), TeamID INT FOREIGN KEY REFERENCES Team(TeamID),
			Score INT NOT NULL, PRIMARY KEY (MatchupID, TeamID))

-- Users, logins, and roles --

CREATE LOGIN rgoodell WITH PASSWORD = 'password123',
	DEFAULT_DATABASE = footballLeague;

CREATE ROLE commissioner;

GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, ALTER
ON DATABASE::footballLeague
TO commissioner;

CREATE USER rgoodell FOR LOGIN rgoodell;

ALTER ROLE commissioner ADD MEMBER rgoodell;

CREATE ROLE coach;

GRANT SELECT
ON Roster
TO coach;

GRANT SELECT, UPDATE
ON [Stats]
TO coach;

CREATE ROLE teamOwner;

GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, ALTER
ON Team
TO teamOwner;

GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, ALTER
ON Roster
TO teamOwner;