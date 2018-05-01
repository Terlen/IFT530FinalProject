--Table Backup Stored Procedure

USE footballLeague;
GO

CREATE PROC Table_Backup 
@tbname AS varchar(MAX) --Input variable to specify which table to backup
AS 
BEGIN
	BEGIN
		DECLARE @drop as VARCHAR(MAX)
		SET @drop = 'IF OBJECT_ID('+@tbname+'_Backup) IS NOT NULL DROP TABLE '+@tbname+'_Backup';
		EXEC (@drop)
	END
	SET nocount ON;
	BEGIN
		DECLARE @query AS VARCHAR(MAX)
		SET @query = 'SELECT * INTO '+@tbname+'_Backup FROM '+@tbname+''; 
		EXEC (@query)
	END 
	SET nocount OFF; 
END

--Exec statements for all tables
EXEC Table_Backup Team;
EXEC Table_Backup Stadium;
EXEC Table_Backup Player;
EXEC Table_Backup Matchup;
EXEC Table_Backup Stats;
EXEC Table_Backup Roster;
