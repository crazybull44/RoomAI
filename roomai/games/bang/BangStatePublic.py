#!/bin/python

from roomai.games.common import AbstractStatePublic

class PhaseInfo(object):
    ChancePlay  = "ChancePlay"
    Draw        = "Draw"
    Play        = "Play"
    Discard     = "Discard"
    def __init__(self):
        self.__playid__ = -1
        self.__phase__  = self.ChancePlay

    def __get_playerid__(self): return self.__playid__
    playerid = property(__get_playerid__, doc="Now the game is in the players[playerid]'s turn")

    def __get_phase__(self):    return self.__phase__
    phase = property(__get_phase__, doc = "Now the game is in the players[playerid]'s turn's phase. The phases are ChancePlay, Draw, Play, Discard")


class PublicPersonInfo(object):
    def __init__(self):
        self.__num_hand_cards__  = 0
        self.__character_card__  = None
        self.__equipment_cards__ = []

    def __get_num_hand_cards__(self):   return self.__num_hand_cards__
    num_hand_cards = property(__get_num_hand_cards__,doc="The number of hand cards")

    def __get_character_card__(self):   return self.__character_card__
    character_card = property(__get_character_card__, doc="The character card")

    def __get_equipment_cards__(self):  return tuple(self.__equipment_cards__)
    get_equipment_cards = property(__get_equipment_cards__, doc="The equipment cards")


class BangStatePublic(AbstractStatePublic):

    def __init__(self):
        self.__public_person_infos__  = []
        self.__phase_info__           = PhaseInfo()
        self.__sheriff_id__           = -1
        self.__discard_pile__         = []


    def __get_public_person_infos__(self):   return tuple(self.__public_person_infos__)
    public_person_infos = property(__get_public_person_infos__, doc="The person info in public")

    def __get_phase_info__(self):   return self.__phase_info__
    phase_info = property(__get_phase_info__, doc="The phase info indicates in which phase is the game")

    def __get_sheriff_id__(self):   return self.__sheriff_id__
    sheriff_id = property(__get_sheriff_id__, doc="The id of the sheriff")

    def __get_discard_pile__(self): return tuple(self.__discard_pile__)
    discard_pile = property(__get_discard_pile__, doc="The discard pile of this game")
