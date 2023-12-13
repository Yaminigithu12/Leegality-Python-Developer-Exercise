class ParkingLot:
    def __init__(self):
        self.levels = {'A': {}, 'B': {}}
        self.available_spots = set()

        for level in 'AB':
            for spot_number in range(1, 21):
                spot_id = f"{level}{spot_number}"
                self.available_spots.add(spot_id)
                self.levels[level][spot_id] = None

    def assign_parking_spot(self, vehicle_number):
        if not self.available_spots:
            return "Parking lot is full."

        spot_id = self.available_spots.pop()
        level, spot_number = spot_id[0], int(spot_id[1:])
        self.levels[level][spot_id] = vehicle_number
        return {"level": level, "spot": spot_number}

    def retrieve_parking_spot(self, vehicle_number):
        for level in 'AB':
            for spot_id, parked_vehicle in self.levels[level].items():
                if parked_vehicle == vehicle_number:
                    return {"level": level, "spot": int(spot_id[1:])}

        return "Vehicle not found in the parking lot."

    def unpark_vehicle(self, vehicle_number):
        for level in 'AB':
            for spot_id, parked_vehicle in self.levels[level].items():
                if parked_vehicle == vehicle_number:
                    self.available_spots.add(spot_id)
                    self.levels[level][spot_id] = None
                    return f"Vehicle {vehicle_number} has been unparked from {level}{int(spot_id[1:])}."

        return "Vehicle not found in the parking lot."

    def retrieve_nearest_parking_location(self):
        if not self.available_spots:
            return "Parking lot is full."

        nearest_spot = min(self.available_spots, key=lambda x: int(x[1:]))
        level, spot_number = nearest_spot[0], int(nearest_spot[1:])
        return {"level": level, "spot": spot_number}



parking_lot = ParkingLot()

# 1. Assign a parking space to a new vehicle
assignment_result = parking_lot.assign_parking_spot("ABC123")
print(assignment_result)

# 2. R'[tetrieve parking spot number of a particular vehicle
retrieval_result = parking_lot.retrieve_parking_spot("ABC123")
print(retrieval_result)

# 3. Unpark the vehicle
unpark_result = parking_lot.unpark_vehicle("ABC123")
print(unpark_result)

# 4. Retrieve the nearest parking location
nearest_location = parking_lot.retrieve_nearest_parking_location()
print(nearest_location)
