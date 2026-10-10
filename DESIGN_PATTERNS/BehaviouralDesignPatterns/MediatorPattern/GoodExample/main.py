from ControlTower import ControlTower
from Airplane import Airplane


controlTower = ControlTower()
air_india = Airplane("AIR-234",controlTower)
spice_jet = Airplane("SPICE-234",controlTower)
indigo = Airplane("INDIGO-234",controlTower)

air_india.send_message("I am getting on runway")
spice_jet.send_message("I am getting on runway")

express = Airplane("EXPRESS-234",controlTower)

express.send_message("I am getting on runway")