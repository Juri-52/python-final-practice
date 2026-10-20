from parking import ParkingLot


# 各テストで準備・操作・確認を行います。passだけでは何も確認できません。

def test_visit_records_payment_and_frees_space() -> None:
    # TODO: 入庫、3時間後の出庫、別の車の入庫を順に行い、各段階の状態を確認してください。
    pass


def test_full_parking_rejects_another_car() -> None:
    # TODO: 2台入庫した後に3台目を入庫させ、失敗しても状態が変わらないことを確認してください。
    pass


def test_duplicate_entry_does_not_use_another_space() -> None:
    # TODO: 空きがある状態で同じ車を再入庫させ、重複しないことを確認してください。
    pass


def test_unknown_car_cannot_leave() -> None:
    # TODO: 別の車が駐車中の状態で未登録の車を出庫させ、戻り値と状態を確認してください。
    pass


def test_free_exit_cannot_be_charged_again() -> None:
    # TODO: 0時間で出庫した車を再度出庫させ、無料の成功と失敗を区別してください。
    pass


def test_parking_lots_have_independent_state() -> None:
    # TODO: 2つの駐車場を作り、一方の操作がもう一方に影響しないことを確認してください。
    pass

