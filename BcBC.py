facts = {
    "marks_above_80",
    "attendance_above_90"
}

rules = {
    "academically_eligible": [
        "marks_above_80"
    ],
    "attendance_eligible": [
        "attendance_above_90"
    ],
    "scholarship_eligible": [
        "academically_eligible",
        "attendance_eligible"
    ]
}

def backward_chaining(goal):
    if goal in facts:
        print("Fact found:", goal)
        return True

    if goal in rules:
        print("Trying to prove:", goal)
        for condition in rules[goal]:
            if not backward_chaining(condition):
                return False

        print("Therefore:", goal)
        return True

    print("Cannot Prove:", goal)
    return False

goal = "scholarship_eligible"

print("Goal:", goal)

if backward_chaining(goal):
    print("\nResult: Goal is True")
else:
    print("\nResult: Goal is False")
