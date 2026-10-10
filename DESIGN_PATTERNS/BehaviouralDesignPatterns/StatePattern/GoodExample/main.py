from TransportService import TransportService

from WalkMode import WalkMode

from BikeMode import BikeMode

bike_mode = BikeMode()
transport_service = TransportService(bike_mode)
transport_service.eta()
transport_service.direction()

walk_mode = WalkMode()
transport_service.set_mode(walk_mode)
transport_service.eta()
transport_service.direction()


