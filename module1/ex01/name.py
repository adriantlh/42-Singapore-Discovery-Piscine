first_name = "Adrian"
last_name = "Tan"
whole_name = first_name +" "+ last_name

print (whole_name)

# --- Improvement Recommendations ---
# 1. Add a shebang line at the top: #!/usr/bin/env python3
# 2. Remove the space before parenthesis in print().
# 3. Fix inconsistent spacing around the + operator on line 3.
#    Current:  first_name +" "+ last_name
#    Better:   first_name + " " + last_name   (spaces on both sides of +)
#    Or use an f-string: whole_name = f"{first_name} {last_name}"