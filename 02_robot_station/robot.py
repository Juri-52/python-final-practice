class Robot:
    def __init__(self, name: str, battery: int) -> None:
        # TODO: 名前とバッテリー残量を保存してください。
        self.name = name
        self.battery = battery

    def get_work_cost(self) -> int:
        # TODO: 通常のロボットの消費量を返してください。
        return 10

    def work(self) -> bool:
        # TODO: 消費量を確認し、作業できる場合だけバッテリーを減らしてください。
        cost = self.get_work_cost()
        if cost <= self.battery:
            self.battery -= cost
            return True
        return False