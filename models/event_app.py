from models.event import Event

event1 = Event("15/09/2021", "Cheese Festival", "100", "Courtyard", "A Celebration of Local Handmade Cheeses")
event2= Event("17/10/2021", "Jam Competition", "30", "Garden Room", "Mary Berry guest judges. First Prize = £100")
event3 = Event("20/11/2021", "Weaving Class", "10", "Arts and Crafts Space", "Learn how to make your own wicker trousers and more.")
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)

