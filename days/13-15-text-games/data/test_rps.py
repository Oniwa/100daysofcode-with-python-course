from unittest.mock import patch
import random
from random import choice

import pytest

from .rps import Roll, Player, header


def test_rock():
    p1 = Roll()
    p1.throw = 'Rock'
    assert not p1.can_defeat('Paper')
    assert p1.can_defeat('Scissors')


def test_paper():
    p1 = Roll()
    p1.throw = 'Paper'
    assert p1.can_defeat('Rock')
    assert not p1.can_defeat('Scissors')


def test_scissors():
    p1 = Roll()
    p1.throw = 'Scissors'
    assert p1.can_defeat('Paper')
    assert not p1.can_defeat('Rock')


@patch.object(random, 'choice')
def test_random_throw(m):
    m.return_value = 'Paper'
    p1 = Roll()
    p1.random_throw()
    assert p1.throw == 'Paper'


@patch("builtins.input", side_effect=['John'])
def test_player_name(inp):
    p1 = Player()
    p1.get_name()
    assert p1.name == 'John'


def test_track_record():
    p1 = Player()
    p1.update_record(True)
    assert p1.record == {'Wins': 1, 'Losses': 0, 'Ties': 0}
    p1.update_record(False)
    assert p1.record == {'Wins': 1, 'Losses': 1, 'Ties': 0}
    p1.update_record(False)
    assert p1.record == {'Wins': 1, 'Losses': 2, 'Ties': 0}
    p1.update_record(None)
    assert p1.record == {'Wins': 1, 'Losses': 2, 'Ties': 1}
    p1.update_record(True)
    assert p1.record == {'Wins': 2, 'Losses': 2, 'Ties': 1}
    p1.update_record(None)
    assert p1.record == {'Wins': 2, 'Losses': 2, 'Ties': 2}
    p1.update_record(True)
    assert p1.record == {'Wins': 3, 'Losses': 2, 'Ties': 2}
    p1.update_record(False)
    assert p1.record == {'Wins': 3, 'Losses': 3, 'Ties': 2}
    p1.update_record(None)
    assert p1.record == {'Wins': 3, 'Losses': 3, 'Ties': 3}


def test_header(capfd):
    header()
    out = capfd.readouterr()[0]
    assert out == 'Get ready to play Rock, Paper, Scissors!  First player to ' \
                  'two wins is the winner!\n'


@patch("builtins.input", side_effect=['r', 'p', 's', 'R', 'S', 'P'])
def test_get_roll(inp, capfd):
    roll = Roll()
    roll.get_roll()
    assert roll.throw == 'Rock'
    roll.get_roll()
    assert roll.throw == 'Paper'
    roll.get_roll()
    assert roll.throw == 'Scissors'
    roll.get_roll()
    assert roll.throw == 'Rock'
    roll.get_roll()
    assert roll.throw == 'Scissors'
    roll.get_roll()
    assert roll.throw == 'Paper'



