from core.models import db, Invention


def test_get_inventions(client):
    rs = client.get("api/v0/inventions")
    assert rs.status_code == 200
    ret_dict = rs.json  # gives you a list
    assert ret_dict["success"] == True

