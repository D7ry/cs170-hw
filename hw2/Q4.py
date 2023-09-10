class Player:
    def __init__(self, is_sus:bool = False):
        self.__is_sus:bool = is_sus
    def is_sus(self)->bool:
        return self.__is_sus
    
class ProblemState:
    def __init__(self):
        self.sus_players:set[Player]
    
def goto_mission(players:'list[Player]') -> bool:
    for player in players:
        if player.is_sus():
            return False
    return True


def find_sus(players:'list[Player]', state:ProblemState):
    if goto_mission(players) is True:
        return # mission success, no amongus
    
    num_players:int = len(players)
    if (num_players == 1):
        state.sus_players.add(players[0]) # found you
    
    split_point:int = num_players // 2
    first_group:'list[Player]' = players[split_point:]
    second_group:'list[Player]' = players[:split_point]
    
    find_sus(first_group, state)
    find_sus(second_group, state)