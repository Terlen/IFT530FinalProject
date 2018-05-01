use footballLeague;
GO;
CREATE VIEW upcomingGames
AS
SELECT Date as 'Date', Home.Name as 'Home Team', Away.Name as 'Away Team', Loc.StadiumName as 'Location'
FROM Matchup
JOIN Team as Home
ON Matchup.HomeTeamID = Home.TeamID
JOIN Team as Away
ON Matchup.AwayTeamID = Away.TeamID
JOIN Stadium as Loc
ON Matchup.StadiumID = Loc.StadiumID
WHERE Date > GETDATE()
GO;

CREATE VIEW winLoss
AS
WITH MatchesPlayed AS
(SELECT TeamID as ID, MatchupID FROM Team
 JOIN Matchup as t ON TeamID = t.HomeTeamID
 UNION
 SELECT TeamID as ID, MatchupID FROM Team
 JOIN Matchup as t ON TeamID = t.AwayTeamID)
,
MatchesWon AS
(SELECT t.TeamID,COUNT(t.TeamID)AS Wins
 FROM
(SELECT a.TeamID,a.MatchupID, a.Score
 FROM Score a
 INNER JOIN
(SELECT MatchupID, MAX(Score) Score
 FROM Score
 Group BY MatchupID) b
 ON a.MatchupID = b.MatchupID AND a.Score = b.Score) AS t
 GROUP BY TeamID
)
SELECT Name,COUNT(ID)AS "Games Played", ISNULL(Wins,0) as Wins, (COUNT(ID)-ISNULL(Wins,0)) AS Losses,
		(Count(ID)-(ISNULL(Wins,0)+(COUNT(ID)-ISNULL(Wins,0)))) AS Ties
FROM MatchesPlayed
Left JOIN MatchesWon ON TeamID = ID
JOIN Team ON Team.TeamID = ID
GROUP BY Name, Wins
ORDER BY Name

