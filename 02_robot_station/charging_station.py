from robot import Robot

class ChargingStation:
    def __init__(self, energy: int) -> None:
        # TODO: ステーションのエネルギー残量を保存してください。
        self.energy = energy

    def charge(self, robot: Robot, amount: int) -> bool:
        # TODO: 条件を確認し、充電できる場合だけ両方のオブジェクトを変更してください。
        if amount > 0:
            if self.energy >= amount:
                if amount + robot.battery <= 100:
                    self.energy -= amount
                    robot.battery += amount
                    return True
        return False