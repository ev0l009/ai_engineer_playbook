"""
    Contains tests on all academy and player methods. All tests return None. 
"""

# required to run tests
import pytest

# required to create academy and player objects
from models.player import Player
from models.academy import Academy

# required to test exceptions
from exceptions import InvalidPlayerError
from exceptions import PlayerAlreadyExistsError
from exceptions import PlayerNotFoundError
from exceptions import AcademyError

@pytest.fixture
def academy():
    return Academy("My Football Academy")

@pytest.fixture
def academy_with_players(academy):
    (
        academy
            .add_player(Player("Val",27,"CDM",7.8))
            .add_player(Player("Jude",23,"CAM",8.0))
            .add_player(Player("Joe",21,"CM",6.5))
            .add_player(Player("Philip",30,"ST",8.0))
    )
    return academy

def test_player_is_valid():
    """Tests whether a successful player initialization."""
    val = Player("Val",27,"CDM",7.8)
    assert val.name == "Val"
    assert val.age == 27
    assert val.position == "CDM"
    assert val.rating == 7.8

@pytest.mark.parametrize(
    "value, error",
    [
        ("", InvalidPlayerError),
        (" ", InvalidPlayerError)
    ]
)
def test_empty_player_name_raises_invalid_player_error(value,error):
    """Tests whether `InvalidPlayerError` is called on an empty name field."""
    with pytest.raises(error):
        Player(value,27,"CDM",7.8)


def test_invalid_player_age_raises_invalid_player_error():
    """Tests whether `InvalidPlayerError` is called on negative age values."""
    with pytest.raises(InvalidPlayerError):
        Player("Val",-1,"CDM",7.8)

@pytest.mark.parametrize(
    "value, error",
    [
        ("", InvalidPlayerError),
        (" ", InvalidPlayerError)
    ]
)
def test_player_empty_position_raises_invalid_player_error(value,error):
    """Tests whether `InvalidPlayerError` is called on empty position field."""
    with pytest.raises(error):
        Player("Val",27,value,7.8)

@pytest.mark.parametrize(
    "value, error",
    [
        (-0.01, InvalidPlayerError),
        (10.01, InvalidPlayerError)
    ]
)
def test_player_rating_out_of_valid_range_raises_invalid_player_error(value,error):
    """Tests whether `InvalidPlayerError` is called on rating values out of valid range(see MIN_RATING/MAX_RATING in helpers module)"""
    with pytest.raises(error):
        Player("Val",27,"CDM",value)

def test_academy_add_player(academy):
    """Tests successful player registration for single player"""
    academy.add_player(Player("Val",27,"CDM",7.8))
    assert len(academy) == 1

def test_add_player_multiple_players(academy_with_players):
    """Tests successful player registration for multiple players"""
    assert len(academy_with_players) == 4

@pytest.mark.parametrize(
    "player_name,age,position,rating", 
    [
        ("Val",27,"CDM",7.8), 
        ("Jude",23,"CAM",8.0)
        ]
)
def test_add_player_retrieve_added_player(academy, player_name,age,position,rating):
    """Tests whether successfully added players are stored and accessable"""
    academy.add_player(Player(player_name,age,position,rating))
    player = academy.find_player(player_name)
    assert player.name == player_name
    assert player.age == age
    assert player.position == position
    assert player.rating == rating

def test_add_player_raises_player_already_exists_error_for_duplicate_registration_attempt(academy):
    """Tests whether PlayerAlreadyExistsError is raised for duplicate registration attempt"""
    with pytest.raises(PlayerAlreadyExistsError):
        (
            academy
                .add_player(Player("Val",27,"CDM",7.8))
                .add_player(Player("Val",27,"CDM",7.8))
        )

def test_find_player_when_player_exists(academy):
    """Tests if existing player can be found."""
    academy.add_player(Player("Val",27,"CDM",7.8))
    player = academy.find_player("Val")
    assert player.name == "Val"

def test_find_player_raises_player_not_found_error_for_missing_player(academy):
    """Tests whether PlayerNotFoundError is raised when player does not exist."""
    academy.add_player(Player("Val",27,"CDM",7.8))
    with pytest.raises(PlayerNotFoundError):
        academy.find_player("Jinx")

def test_remove_player_when_player_exists(academy):
    """Tests whether existing player can be removed"""
    (
        academy
            .add_player(Player("Val",27,"CDM",7.8))
            .add_player(Player("Jude",23,"CAM",8.0))
    )
    academy.remove_player("Val")
    assert len(academy) == 1
    with pytest.raises(PlayerNotFoundError):
        academy.find_player("Val")

def test_remove_player_raises_player_not_found_error_for_missing_player(academy):
    """Tests whether PlayerNotFoundError is raised when player to be remove does not exist."""
    academy.add_player(Player("Val",27,"CDM",7.8))
    with pytest.raises(PlayerNotFoundError):
        academy.remove_player("Jinx")

@pytest.mark.parametrize(
    "value, expected",
    [
        (0.0, 0.0),
        (5.0, 5.0),
        (10.0,10.0),
        (1, 1.0),
        (5, 5.0),
        (10, 10.0)
    ]
)
def test_update_rating(academy, value, expected):
    """Tests whether player rating is updated."""
    academy.add_player(Player("Val",27,"CDM",7.8))
    academy.update_rating("Val",value)
    assert academy.find_player('Val').rating == expected
    assert isinstance(academy.find_player('Val').rating, float)

@pytest.mark.parametrize(
    "value, error",
    [
        (-0.01, InvalidPlayerError),
        (10.01, InvalidPlayerError),
        (-1, InvalidPlayerError),
        (-11, InvalidPlayerError)
    ]
)
def test_update_rating_raises_invalid_player_error_for_rating_value_out_of_valid_range(academy, value, error):
    """Tests whether InvalidPlayerError is raised for rating values out of valid range(see MIN_RATING/MAX_RATING in helpers module)"""
    academy.add_player(Player("Val",27,"CDM",7.8))
    with pytest.raises(error):
        academy.update_rating("Val",value)

def test_update_rating_raises_player_not_found_error_for_missing_player(academy):
    """Tests whether PlayerNotFoundError is raised for non-existent players"""
    academy.add_player(Player("Val",27,"CDM",7.8))
    with pytest.raises(PlayerNotFoundError):
        academy.update_rating("Jinx",5.9)

def test_average_rating(academy_with_players):
    """Tests for average rating of all players in the academy"""
    average_rating = academy_with_players.average_rating()
    assert average_rating == pytest.approx(7.575)

def test_average_rating_raises_academy_error_for_empty_academy(academy):
    """Tests whether AcademyError is raised when no player is registered in the academy."""
    with pytest.raises(AcademyError):
        academy.average_rating()

def test_top_player_single_player(academy):
    """Tests for academy's top player where one player has the highest rating"""
    (
        academy
            .add_player(Player("Val",27,"CDM",7.8))
            .add_player(Player("Jude",23,"CAM",8.0))
            .add_player(Player("Joe",21,"CM",6.5))
            .add_player(Player("Philip",30,"ST",5.5))
    )
    top_player = academy.top_player()
    assert top_player.name == "Jude"

def test_top_player_multiple_players(academy_with_players):
    """Tests for academy's top player where multiple players have the same top rating
    
    Returns the first player with the highest rating"""
    top_player = academy_with_players.top_player()
    assert top_player.name == "Jude"

def test_top_player_raises_academy_error_for_empty_academy(academy):
    """Tests whether AcademyError is raised when no player is registered in the academy."""
    with pytest.raises(AcademyError):
        academy.top_player()