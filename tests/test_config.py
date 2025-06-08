from src.config import MySQLConnection
import pytest

def test_get_engine(mocker):
    # created the engine mock
    mock_engine = mocker.MagicMock()
    mock_engine.__enter__.return_value = mock_engine
    mock_engine.__exit__.return_value = None

    # Patch sqlalchemy.create_engine to return mock_engine
    mock_connect =mocker.patch("src.config.create_engine", return_value=mock_engine)

    # run the code that uses sqlalchemy.create_engine
    connection = MySQLConnection(user="user", password="pass", host="localhost", port="3306", db_name="test")
    conn = connection.get_engine()

    # Verify that create_engine was called and that it returns the correct mock
    mock_connect.assert_called_once()

    assert conn == mock_engine


def test_get_engine_is_not_safe(mocker):
    # created the engine mock
    mock_engine = mocker.MagicMock()
    mock_engine.__enter__.return_value = mock_engine
    mock_engine.__exit__.return_value = None

    # Patch sqlalchemy.create_engine to return mock_engine
    mock_connect =mocker.patch("src.config.create_engine", return_value=mock_engine)

    # Catching SQL injection, the code that uses sqlalchemy.create_engine with sql injection
    with pytest.raises(ValueError, match="Invalid or suspicious value"):
        connection = MySQLConnection(user="user", password="select * from users", host="localhost", port="3306",
                                     db_name="test")
        connection.get_engine()

    # Verify that create_engine was called and that it returns the correct mock
    mock_connect.assert_not_called()
