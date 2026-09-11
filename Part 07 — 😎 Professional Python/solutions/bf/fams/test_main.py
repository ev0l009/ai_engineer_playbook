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


def test_player_is_valid():
    """Tests whether a successful player initialization."""
    val = Player("Val",27,"CDM",7.8)
    assert val.name == "Val"
    assert val.age == 27
    assert val.position == "CDM"
    assert val.rating == 7.8

def test_empty_player_name_raises_invalid_player_error():
    """Tests whether `InvalidPlayerError` is called on an empty name field."""
    with pytest.raises(InvalidPlayerError):
        Player("",27,"CDM",7.8)

def test_invalid_player_age_raises_invalid_player_error():
    """Tests whether `InvalidPlayerError` is called on negative age values."""
    with pytest.raises(InvalidPlayerError):
        Player("Val",-1,"CDM",7.8)

def test_player_empty_position_raises_invalid_player_error():
    """Tests whether `InvalidPlayerError` is called on empty position field."""
    with pytest.raises(InvalidPlayerError):
        Player("Val",27," ",7.8)

def test_player_rating_below_zero_raises_invalid_player_error():
    """Tests whether `InvalidPlayerError` is called on rating values less than 0"""
    with pytest.raises(InvalidPlayerError):
        Player("Val",27,"CDM",-0.01)

def test_player_rating_above_ten_raises_invalid_player_error():
    """Tests whether `InvalidPlayerError` is called on rating values greater than 10"""
    with pytest.raises(InvalidPlayerError):
        Player("Val",27,"CDM",10.01)

@pytest.fixture
def academy():
    return Academy("My Football Academy")

def test_academy_add_player(academy):
    """Tests successful player registeration for single player"""
    academy.add_player(Player("Val",27,"CDM",7.8))
    assert len(academy.players) == 1

def test_add_player_multiple_players(academy):
    """Tests successful player registeration for multiple players"""
    (
        academy
            .add_player(Player("Val",27,"CDM",7.8))
            .add_player(Player("Jude",23,"CAM",8.0))
            .add_player(Player("Joe",21,"CM",7.5))
            .add_player(Player("Philip",30,"ST",6.5))
    )
    assert len(academy.players) == 4

def test_add_player_retrieve_added_player(academy):
    """Tests whether successfully added players are stored and accessable"""
    val = Player("Val",27,"CDM",7.8)
    jude = Player("Jude",23,"CAM",8.0)
    (
        academy
            .add_player(val)
            .add_player(jude)
    )
    # Every registered player is referenced by their name in lowercase
    val_key = val.name.lower()
    jude_key = jude.name.lower()
    assert academy.players[val_key].name == "Val"
    assert academy.players[val_key].age == 27
    assert academy.players[val_key].position == "CDM"
    assert academy.players[val_key].rating == 7.8

    assert academy.players[jude_key].name == "Jude"
    assert academy.players[jude_key].age == 23
    assert academy.players[jude_key].position == "CAM"
    assert academy.players[jude_key].rating == 8.0

def test_add_player_raises_player_already_exists_error_for_duplicate_registration_attempt(academy):
    """Tests whether PlayerAlreadyExistsError is raised for duplicate registeration attempt"""
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
    assert len(academy.players) == 1
    with pytest.raises(PlayerNotFoundError):
        academy.find_player("Val")

def test_remove_player_raises_player_not_found_error_for_missing_player(academy):
    """Tests whether PlayerNotFoundError is raised when player to be remove does not exist."""
    academy.add_player(Player("Val",27,"CDM",7.8))
    with pytest.raises(PlayerNotFoundError):
        academy.remove_player("Jinx")

def test_update_rating(academy):
    """Tests whether player rating is updated."""
    academy.add_player(Player("Val",27,"CDM",7.8))
    academy.update_rating("Val",9.0)
    assert academy.players['val'].rating == 9.0

def test_update_rating_raises_invalid_player_error_for_rating_value_below_zero(academy):
    """Tests whether InvalidPlayerError is raised for rating values below 0"""
    academy.add_player(Player("Val",27,"CDM",7.8))
    with pytest.raises(InvalidPlayerError):
        academy.update_rating("Val",-0.01)

def test_update_rating_raises_invalid_player_error_for_rating_value_above_ten(academy):
    """Tests whether InvalidPlayerError is raised for rating values above 10"""
    academy.add_player(Player("Val",27,"CDM",7.8))
    with pytest.raises(InvalidPlayerError):
        academy.update_rating("Val",10.01)

def test_update_rating_raises_player_not_found_error_for_missing_player(academy):
    """Tests whether PlayerNotFoundError is raised for non-existent players"""
    academy.add_player(Player("Val",27,"CDM",7.8))
    with pytest.raises(PlayerNotFoundError):
        academy.update_rating("Jinx",5.9)