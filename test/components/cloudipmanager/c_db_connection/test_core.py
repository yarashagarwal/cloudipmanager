from cloudipmanager.c_db_connection import db_connection


def test_sample():
    assert db_connection is not None
