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