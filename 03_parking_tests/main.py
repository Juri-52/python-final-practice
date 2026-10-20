from parking import ParkingLot


def main() -> None:
    parking = ParkingLot(1)
    result = parking.enter("A-001")
    print(f"A-001入庫: {result}, 駐車中={parking.cars}")
    result = parking.enter("B-002")
    print(f"満車時のB-002入庫: {result}, 駐車中={parking.cars}")
    fee = parking.leave("A-001", 3)
    print(f"A-001出庫: {fee}円, 駐車中={parking.cars}, 売上={parking.revenue}円")
    result = parking.enter("B-002")
    print(f"出庫後のB-002入庫: {result}, 駐車中={parking.cars}")
    fee = parking.leave("A-001", 3)
    print(f"A-001再出庫: {fee}, 売上={parking.revenue}円")


if __name__ == "__main__":
    main()
