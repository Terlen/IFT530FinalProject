from django.shortcuts import render, redirect, loader
from .forms import *

# Create your views here.

def home(request):
	return render(request, 'football/index.html')


def login(request):
	return render(request, 'football/login.html')


def register_player(request):
    if request.method == 'POST':
        player_form = register_player_form(request.POST)

        if player_form.is_valid():
            # allow when testing is finished
            player_form.save()
            return redirect('home')

    else:
        player_form = register_player_form()

    context = {'form': player_form}
    return render(request, 'football/registerplayer.html', context)


def register_team(request):
	if request.method == 'POST':
		team_form = register_team_form(request.POST)

		if team_form.is_valid():
			# allow when testing is finished
			team_form.save()
			return redirect('home')

	else:
		team_form = register_team_form()

	context = {'form': team_form}
	return render(request, 'football/registerteam.html', context)


def register_stadium(request):
	if request.method == 'POST':
		stadium_form = register_stadium_form(request.POST)

		if stadium_form.is_valid():
			# allow when testing is finished
			stadium_form.save()
			return redirect('home')

	else:
		stadium_form = register_stadium_form()

	context = {'form': stadium_form}
	return render(request, 'football/registerstadium.html', context)


def register_match(request):
	if request.method == 'POST':
		match_form = register_match_form(request.POST)

		if match_form.is_valid():
			# allow when testing is finished
			match_form.save()
			return redirect('home')

	else:
		match_form = register_match_form()

	context = {'form': match_form}
	return render(request, 'football/registermatch.html', context)


def register_roster(request):
	if request.method == 'POST':
		roster_form = register_roster_form(request.POST)

		if roster_form.is_valid():
			# allow when testing is finished
			roster_form.save()
			return redirect('home')

	else:
		roster_form = register_roster_form()

	context = {'form': roster_form}
	return render(request, 'football/registerroster.html', context)


def register_stat(request):
	if request.method == 'POST':
		stat_form = register_stat_form(request.POST)

		if stat_form.is_valid():
			# allow when testing is finished
			stat_form.save()
			return redirect('home')

	else:
		stat_form = register_stat_form()

	context = {'form': stat_form}
	return render(request, 'football/registerstat.html', context)


def register_score(request):
	if request.method == 'POST':
		score_form = register_score_form(request.POST)

		if score_form.is_valid():
			# allow when testing is finished
			score_form.save()
			return redirect('home')

	else:
		score_form = register_score_form()

	context = {'form': score_form}
	return render(request, 'football/registerscore.html', context)


def view_player(request):
	players = Player.objects.all()

	template = loader.get_template('football/viewplayer.html')
	context = {
		'players': players,
	}
	return render(request, 'football/viewplayer.html', context)


def view_team(request):
	teams = Team.objects.all()

	template = loader.get_template('football/viewteam.html')

	context = {
		'teams': teams,
	}
	return render(request,'football/viewteam.html', context)


def view_stadium(request):
	stadiums = Stadium.objects.all()

	template = loader.get_template('football/viewstadium.html')

	context = {
		'stadiums': stadiums,
	}
	return render(request,'football/viewstadium.html', context)


def view_match(request):
	matches = Matchup.objects.all()

	template = loader.get_template('football/viewmatchup.html')

	context = {
		'matches': matches,
	}
	return render(request,'football/viewmatchup.html', context)


def view_roster(request):
	rosters = Roster.objects.all()

	template = loader.get_template('football/viewroster.html')

	context = {
		'rosters': rosters,
	}
	return render(request,'football/viewroster.html', context)


def view_stat(request):
	stats = Stat.objects.all()

	template = loader.get_template('football/viewstat.html')

	context = {
		'stats': stats,
	}
	return render(request,'football/viewstat.html', context)


def view_score(request):
	scores = Score.objects.all()

	template = loader.get_template('football/viewscore.html')

	context = {
		'scores': scores,
	}
	return render(request,'football/viewscore.html', context)
