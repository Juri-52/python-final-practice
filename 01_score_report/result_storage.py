import json
from student_result import StudentResult

def load_results(filename: str) -> list[StudentResult]:
    # TODO: JSONから読み込んだデータをStudentResultのリストに変換してください。
    results = []
    with open(filename, "r", encoding="utf-8") as f:
        items = json.load(f)
    for item in items:
        result = StudentResult(item["name"], item["score"])
        results.append(result)
    return results