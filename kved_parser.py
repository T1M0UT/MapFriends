"""
09.02.2022
"""
import json


def write(data):
    """
    Writes a json to a file
    """
    with open("kved_results.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=6, ensure_ascii=False)


def parse_kved(class_code):
    """
    returns a parsed json file
    >>> parse_kved("03.11")

    """
    with open("kved.json", "r") as file:
        data = json.load(file)
    for section in data["sections"][0]:
        for division in section["divisions"]:
            for group in division["groups"]:
                for class_ in group["classes"]:
                    if class_["classCode"] == class_code:
                        new_data = {
                              "name": class_["className"],
                              "type": "class",
                              "parent": {
                                "name": group["groupName"],
                                "type": "group",
                                "num_children": len(group["classes"]),
                                "parent": {
                                  "name": division["divisionName"],
                                  "type": "division",
                                  "num_children": len(division["groups"]),
                                  "parent": {
                                    "name": section["sectionName"],
                                    "type": "section",
                                    "num_children": len(section["divisions"])
                                  }
                                }
                              }
                            }
                        write(new_data)


if __name__ == "__main__":
    parse_kved("03.11")
    import doctest
    print(doctest.testmod())
