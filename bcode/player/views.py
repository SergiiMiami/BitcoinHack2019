from django.shortcuts import render

from gameplay.models import Game


def home(request):
    games_first_player = Game.objects.filter(
        first_player = request.user,
        status='F'
    )
    games_second_player = Game.objects.filter(
        second_player=request.user,
        status='S'
    )
    all_my_games = list(games_first_player) + list(games_second_player)


    #    .games_for_user(request.user)
    #active_games = my_games.active()

    return render(request, "player/home.html",
                  {'games': all_my_games,
                   'num_games': Game.objects.count(),
                   'n_games': len(all_my_games)})

