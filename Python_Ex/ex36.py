def common_skills():
    set1 = {"Python", "Java", "SQL", "AI"}
    set2 = {"Python", "C++", "SQL", "ML"}

    if not set1 or not set2:
        return "Invalid input"

    return set1 & set2   

print("Common Skills:", common_skills())