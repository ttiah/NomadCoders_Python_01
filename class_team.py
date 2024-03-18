class Player:

    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
    
    def introduce(self):
        print(f'Hi! I\'m {self.name} and I play for {self.team}.')


class Team:

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, name):
        names = [player.name for player in self.players]
        if name not in names:
            new_player = Player(name, self.team_name)
            self.players.append(new_player)
            print(f'{name} 등록 완료')
        else:
            print(f'{name} 중복')

    def remove_player(self, name):
        for player in self.players:
            if name == player.name:
                self.players.remove(player)
                print(f'{name} 삭제 완료')

    def total_xp(self):
        sum = 0
        for player in self.players:
            sum += player.xp
        print(f'XP 총합: {sum}')

    def show_players(self):
        for player in self.players:
            player.introduce()


# dk = Player(name='DK', team='Team X')
# dk.introduce()

# cy = Player(name='CY', team='Team Blue')
# cy.introduce()

team_x = Team('Team X')
team_x.add_player('DK')
team_x.add_player('DK')
team_x.add_player('Shin')
team_x.add_player('Eun')
team_x.add_player('Yeon')
team_x.remove_player('DK')
team_x.show_players()
team_x.total_xp()

team_blue = Team('Team Blue')
team_blue.add_player('CY')
team_blue.add_player('CY')
team_blue.show_players()
team_blue.total_xp()
