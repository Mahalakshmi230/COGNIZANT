def split_bill(total_bill, people):
    if isinstance(total_bill, (int, float)) and isinstance(people, int) and people > 0:
        share = total_bill // people  # Floor division
        print(f"Individual Share: {share}")
    else:
        print("Invalid input")

total_bill = 1250
people = 4

split_bill(total_bill, people)