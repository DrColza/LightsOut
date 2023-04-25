import pytest
from src.lightsout import LightsOut
from src.levels import STARTING_MATRIX
from copy import deepcopy

@pytest.fixture()
def game_object():
    game = object.__new__(LightsOut)
    return game


class TestLightsOut:

    @pytest.mark.button_toggling
    def test_handle_button_click_with_no_lights_on(self, game_object):
        game_object.grid = deepcopy(STARTING_MATRIX[0])
        expected_response = [
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,1,1,1,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
        ]

        game_object.handle_button_click(2, 2)
        assert game_object.grid == expected_response


    @pytest.mark.button_toggling
    def test_handle_button_click_with_bottom_lights_on(self, game_object):
        game_object.grid = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,1,0,0,0],
            [1,1,1,0,0],
        ]
        game_object.handle_button_click(4, 1)
        assert game_object.grid == STARTING_MATRIX[0]


    @pytest.mark.button_toggling
    def test_handle_button_click_level_1_move_1(self, game_object):
        game_object.grid = deepcopy(STARTING_MATRIX[1])
        expected_response = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,1],
            [1,1,0,0,0],
            [1,0,0,0,0],
        ]
        game_object.handle_button_click(3, 0)
        assert game_object.grid == expected_response


    @pytest.mark.pass_level
    def test_level_1_can_be_passed(self, game_object):
        game_object.grid = deepcopy(STARTING_MATRIX[1])

        game_object.handle_button_click(3, 0)
        game_object.handle_button_click(3, 2)
        game_object.handle_button_click(3, 4)
        game_object.handle_button_click(4, 0)
        game_object.handle_button_click(4, 2)
        game_object.handle_button_click(4, 4)

        assert game_object.grid == STARTING_MATRIX[0]


    @pytest.mark.pass_level
    def test_level_2_can_be_passed(self, game_object):
        game_object.grid = STARTING_MATRIX[2]

        game_object.handle_button_click(4, 2)
        game_object.handle_button_click(3, 2)
        game_object.handle_button_click(2, 0)
        game_object.handle_button_click(2, 4)
        game_object.handle_button_click(1, 2)
        game_object.handle_button_click(0, 2)

        assert game_object.grid == STARTING_MATRIX[0]


    @pytest.mark.pass_level
    def test_level_3_can_be_passed(self, game_object):
        game_object.level = 3
        game_object.grid = STARTING_MATRIX[game_object.level]

        game_object.handle_button_click(0, 0)
        game_object.handle_button_click(0, 4)
        game_object.handle_button_click(4, 0)
        game_object.handle_button_click(4, 4)
        game_object.handle_button_click(2, 2)

        assert game_object.grid == STARTING_MATRIX[0]