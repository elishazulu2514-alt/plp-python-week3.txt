# List of student scores
scores = [72, 45, 90, 61, 38]

# Initialize tracking variables
passed_count = 0
failed_count = 0
total_score = 0

# Loop through each score
for score in scores:
    # Determine grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Print individual score and letter grade
    print(f"Score: {score} -> Grade: {grade}")

    # Track passed and failed counts
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

    # Add to total for average calculation
    total_score += score

# Calculate average and round to 1 decimal place
average = round(total_score / len(scores), 1)

# Print summary metrics
print("\n--- Summary ---")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average Score: {average}")
