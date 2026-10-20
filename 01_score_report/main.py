from result_storage import load_results
from student_result import StudentResult


def get_passed_names(results: list[StudentResult], passing_score: int) -> list[str]:
    # TODO: 基準点以上の学生の名前を、元の順番で返してください。
    pass


def read_passing_score() -> int | None:
    # TODO: 「合格点（0〜100）: 」で入力を受け取り、整数に変換してください。
    # 整数にできない場合と範囲外の場合は、指定のメッセージを表示してNoneを返します。
    pass


def main() -> None:
    # 以下の表示処理は完成済みです。
    results = load_results("scores.json")
    passing_score = read_passing_score()
    if passing_score is None:
        return

    names = get_passed_names(results, passing_score)
    print(f"合格基準: {passing_score}点")
    if names:
        print(f"合格者: {', '.join(names)}")
    else:
        print("合格者: なし")
    print(f"合格者数: {len(names)}人")


if __name__ == "__main__":
    main()
