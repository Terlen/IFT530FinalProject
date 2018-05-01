from django import forms
from backend.models import *

class register_player_form(forms.ModelForm):
	
	mName = forms.CharField(required=False)

	class Meta:
		model = Player
		fields = ('__all__')
		labels = {
			"fName": "First Name",
			"lName" : "Last Name",
			"mName": "Middle Name"
			}

	def save(self, commit=True):
		player = super(register_player_form, self).save(commit=False)
		player.fName = self.cleaned_data['fName']
		player.lName = self.cleaned_data['lName']

		if commit:
			player.save()

		return player


class register_team_form(forms.ModelForm):
	class Meta:
		model = Team
		fields = ('__all__')


class register_stadium_form(forms.ModelForm):
	class Meta:
		model = Stadium
		fields = ('__all__')
		labels = {'stadiumName': 'Stadium Name'}


class register_match_form(forms.ModelForm):
	class Meta:
		model = Matchup
		fields = ('__all__')


class register_roster_form(forms.ModelForm):
	class Meta:
		model = Stat
		fields = ('__all__')


class register_stat_form(forms.ModelForm):
	class Meta: 
		model = Roster
		fields = ('__all__')


class register_score_form(forms.ModelForm):
	class Meta:
		model = Score
		fields = ('__all__')

