from typing import List, Dict


def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    names_scores_map = {}
    for name, score in zip(names, scores):
        names_scores_map[name] = score

    return names_scores_map


# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
