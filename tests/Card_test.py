from Card import Card
from datetime import date, datetime
def test_Card():
    dishes = Card("dishes", "do the dishes!", date.today, "Upcomming")
    assert dishes.title == "dishes"
    assert dishes.description == "do the dishes!"
    assert dishes.deadline == date.today
    assert dishes.status == "Upcomming"

def test_update_status():
    dishes = Card("dishes", "do the dishes!", date.today, "Upcomming")
    dishes.update_status("Doing") 
    assert dishes.status == "Doing"

    