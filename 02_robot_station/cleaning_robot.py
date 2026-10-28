from robot import Robot

class CleaningRobot(Robot):
    def get_work_cost(self) -> int:
        # TODO: super()で取得した消費量に、掃除用の消費量を加えて返してください。
        cost = super().get_work_cost()
        cost += 10
        return cost