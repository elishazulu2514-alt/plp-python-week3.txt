count = 1
total = 0

# BUG: Missing colon (:) at the end of the while header. Added : after 5.
# BUG: Loop condition 'count < 5' stopped before adding 5 (sum was 10 instead of 15). Changed condition to 'count <= 5'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Cannot concatenate string with int using '+'. Used f-string formatting instead.
print(f"Sum of 1 to 5 is: {total}")
