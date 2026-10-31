facts = {
    "marks_above_80",
    "attendance_above_90"
}

rules = [
    (["marks_above_80"], "academically_eligible"),
    (["attendance_above_90"], "attendance_eligible"),
    (["academically_eligible", "attendance_eligible"], "scholarship_eligible")
]

def forward_chaining(facts, rules):
    facts = set(facts)
    while True:
        new_fact = False
        for conditions, conclusion in rules:
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("Derived:", conclusion)
                    new_fact = True
        if not new_fact:
            break
    return facts

final_facts = forward_chaining(facts, rules)
print("\nFinal facts:")
for fact in final_facts:
    print("-", fact)
