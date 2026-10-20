from charging_station import ChargingStation
from cleaning_robot import CleaningRobot
from robot import Robot


def main() -> None:
    # 動作確認の流れは完成済みです。各クラスを実装してから実行してください。
    robot = Robot("R1", 15)
    cleaner = CleaningRobot("C1", 15)
    station = ChargingStation(50)

    result = robot.work()
    print(f"R1: 作業={result}, バッテリー={robot.battery}")

    result = cleaner.work()
    print(f"C1: 作業={result}, バッテリー={cleaner.battery}")

    result = station.charge(cleaner, 20)
    print(f"C1へ20充電: 成功={result}, バッテリー={cleaner.battery}, ステーション={station.energy}")

    result = cleaner.work()
    print(f"C1: 作業={result}, バッテリー={cleaner.battery}")

    result = station.charge(robot, 40)
    print(f"R1へ40充電: 成功={result}, バッテリー={robot.battery}, ステーション={station.energy}")


if __name__ == "__main__":
    main()
