from models.event import Event

event1 = Event("15th September", "Cheese Festival", "100", "Courtyard", "A Celebration of Local Handmade Cheeses")
event2= Event("17th October", "Jam Competition", "30", "Garden Room", "Mary Berry guest judges. First Prize = £100")
event3 = Event("20th November", "Weaving Class", "10", "Arts and Crafts Space", "Learn how to make your own wicker trousers and more.")
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)

