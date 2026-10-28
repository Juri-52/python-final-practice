FIRST_HOUR_FEE = 300
ADDITIONAL_HOUR_FEE = 100
MAX_FEE = 1000

def calculate_fee(hours: int) -> int:
    if hours == 0:
        return 0
    fee = FIRST_HOUR_FEE + (hours - 1) * ADDITIONAL_HOUR_FEE
    return min(fee, MAX_FEE)

# このクラスには状態管理の誤りがあります。テストで確認してから修正してください。
class ParkingLot:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cars: list[str] = []
        self.revenue = 0

    def enter(self, car_number: str) -> bool:
        if len(self.cars) < self.capacity:
            if car_number not in self.cars:
                self.cars.append(car_number)
                return True
        return False

    def leave(self, car_number: str, hours: int) -> int | None:
        if car_number not in self.cars:
            return None
        fee = calculate_fee(hours)
        self.cars.remove(car_number)
        self.revenue += fee
        return fee