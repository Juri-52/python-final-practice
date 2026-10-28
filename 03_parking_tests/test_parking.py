from parking import ParkingLot, calculate_fee

class NewParkingLot:
    def __init__(self, capacity:int) -> None:
        self.capacity = capacity
        self.cars:list[str] = []
        self.revenue = 0
    def enter(self, car_number:str) -> bool:
        if self.capacity > len(self.cars):
            if car_number not in self.cars:
                self.cars.append(car_number)
                return True
        return False
    def leave(self, car_number:str, hours:int) -> int | None:
        if car_number in self.cars:
            amount = calculate_fee(hours)
            self.cars.remove(car_number)
            self.revenue += amount
            return amount
        return None

# 各テストで準備・操作・確認を行います。passだけでは何も確認できません。

def test_visit_records_payment_and_frees_space() -> None:
    # TODO: 入庫、3時間後の出庫、別の車の入庫を順に行い、各段階の状態を確認してください。
    parking = NewParkingLot(1)
    result = parking.enter("A-001")
    assert result == True
    assert parking.cars == ["A-001"]
    assert parking.revenue == 0

    result = parking.leave("A-001", 3)
    assert result == 500
    assert parking.cars == []
    assert parking.revenue == 500

    result = parking.enter("B-002")
    assert result == True
    assert parking.cars == ["B-002"]
    assert parking.revenue == 500

def test_full_parking_rejects_another_car() -> None:
    # TODO: 2台入庫した後に3台目を入庫させ、失敗しても状態が変わらないことを確認してください。
    parking = NewParkingLot(2)
    parking.enter("A-001")
    parking.enter("B-002")
    copy = parking.cars
    result = parking.enter("C-003")
    assert result == False
    assert parking.cars is copy
    assert parking.revenue == 0

def test_duplicate_entry_does_not_use_another_space() -> None:
    # TODO: 空きがある状態で同じ車を再入庫させ、重複しないことを確認してください。
    parking = NewParkingLot(3)
    parking.enter("A-001")
    result = parking.enter("A-001")
    assert result == False
    assert parking.cars == ["A-001"]
    assert parking.revenue == 0

def test_unknown_car_cannot_leave() -> None:
    # TODO: 別の車が駐車中の状態で未登録の車を出庫させ、戻り値と状態を確認してください。
    parking = NewParkingLot(2)
    parking.enter("A-001")
    result = parking.leave("Z-999", 3)
    assert result is None
    assert parking.cars == ["A-001"]
    assert parking.revenue == 0

def test_free_exit_cannot_be_charged_again() -> None:
    # TODO: 0時間で出庫した車を再度出庫させ、無料の成功と失敗を区別してください。
    parking = NewParkingLot(1)
    parking.enter("A-001")
    result = parking.leave("A-001", 0)
    assert result == 0
    assert result is not None
    assert parking.cars == []
    assert parking.revenue == 0
    result = parking.leave("A-001", 3)
    assert result is None
    assert parking.cars == []
    assert parking.revenue == 0

def test_parking_lots_have_independent_state() -> None:
    # TODO: 2つの駐車場を作り、一方の操作がもう一方に影響しないことを確認してください。
    parking1 = NewParkingLot(1)
    parking2 = NewParkingLot(1)
    parking1.enter("A-001")
    assert parking2.cars == []
    assert parking2.revenue == 0
    parking2.enter("B-002")
    result = parking1.leave("A-001",1)
    assert result == 300
    assert parking1.cars == []
    assert parking1.revenue == 300
    assert parking2.cars == ["B-002"]
    assert parking2.revenue == 0