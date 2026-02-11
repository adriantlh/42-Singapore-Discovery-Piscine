first_name = input("Hey, what's your first name? : ")
last_name = input("And your last name? : ")
name = first_name + " " + last_name
print ("Well, pleased to meet you, " + name)

# --- Improvement Recommendations ---
# 1. Add a shebang line at the top: #!/usr/bin/env python3
# 2. Remove the space before parenthesis in print() and input().
# 3. Use an f-string for the final print for cleaner formatting:
#    print(f"Well, pleased to meet you, {first_name} {last_name}")