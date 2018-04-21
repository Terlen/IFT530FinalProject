from django.db import models


# Create your models here.

# class User(models.Model):
#     # these names are the columns
#     username = models.CharField(max_length=100)
#     fname = models.CharField(max_length=100)
#     lname = models.CharField(max_length=100)
#     mname = models.CharField(max_length=100)
#     address = models.TextField()
#     officenum = models.CharField(max_length=15)
#     cellnum = models.CharField(max_length=15)
#     email = models.EmailField()
	
# 	def __str__(self):
# 		return ("Username: %s, First Name: %s, Mididle Name: %s, Last Name: %s, Address: %s, Office Number: %s, Cell Number: %s, Email: %s " % (self.username, self.fname, self.mname, self.lname, self.address, self.officenum, self.cellnum, self.email))


class Team(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return ("Team Name: %s") % self.name


class Stadium(models.Model):
	stadiumName = models.CharField(max_length=50)
	address = models.CharField(max_length=50)


class Player(models.Model):
	fName = models.CharField(max_length=50)
	lName = models.CharField(max_length=50)
	mName = models.CharField(max_length=1)

	def __str__(self):
		return( "%s, %s") % (self.fName, self.lName)


class Matchup(models.Model):
	stadiumID = models.ForeignKey(Stadium, on_delete=models.CASCADE, default=None)
	homeTeamID = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team', default=None)
	awayTeamID = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team', default=None)


class Stat(models.Model):
	matchID = models.ForeignKey(Matchup, on_delete=models.CASCADE, default=None)
	teamID = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
	offensiveYards = models.DecimalField(max_digits=10, decimal_places=2, default=None)
	turnOvers = models.IntegerField(default=None)

	class Meta:
		unique_together = (("matchID", "teamID"))


class Roster(models.Model):
	beginDate = models.DateField(default=None)
	playerID =  models.ForeignKey(Player, on_delete=models.CASCADE, default=None)
	teamID = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
	position = models.CharField(max_length=20, default=None)
	number = models.IntegerField(default=None)
	endDate = models.DateField(default=None)

	class Meta:
		unique_together = (("beginDate", "playerID"))


class Score(models.Model):
	matchID = models.ForeignKey(Matchup, on_delete=models.CASCADE, default=None)
	teamID = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
	score = models.CharField(max_length=10, default=None)
	
	class Meta:
		unique_together = (("matchID", "teamID"))