# Password
Description:

This project is my first venture into cybersecurity, focusing on the essential aspect of password security. I developed a simple yet effective **Password Strength Checker** that evaluates the robustness of passwords based on specific criteria such as length, the presence of lowercase and uppercase letters, digits, and special characters. The tool is designed to help users understand the strength of their passwords, guiding them to create more secure and resilient ones.

How It Works:

The Password Strength Checker analyzes a given password against five key criteria:
1. Length:** The password must be at least 8 characters long.
2. Lowercase Letters:** It should contain at least one lowercase letter (`a-z`).
3. Uppercase Letters:** It should include at least one uppercase letter (`A-Z`).
4. Digits:** The presence of at least one number (`0-9`) is required.
5. Special Characters:** It should have at least one special character from the set `!@#$%^&*()_+`.

Current Status:

At this stage, the tool successfully classifies passwords into two categories: "Moderate" and "Weak." A password meets the "Moderate" classification if it satisfies 3 or 4 out of the 5 criteria. If fewer than 3 criteria are met, the password is classified as "Weak."

Challenges and Next Steps:

One challenge I'm currently addressing is ensuring that a password can be classified as "Strong" when all five criteria are met. This will require refining the code and debugging the criteria checks to achieve the desired output.
