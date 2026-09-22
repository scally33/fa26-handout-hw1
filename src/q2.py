"""HW1 Question 2

Please implement the following function according to the provided documentation.
Tests are provided for this question in the file tests/test_q2.py."""

def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """

    isValidPassword = False

    if password.length() >= 8:
        if not (password.isUpper() and password.isLower()):
            if ('1' in password) or ('2' in password) or ('3' in password) or ('4' in password) or ('5' in password) or ('6' in password) or ('7' in password) or ('8' in password) or ('9' in password) or ('0' in password):
                if ('!' in password) or ('@' in password) or ('#' in password) or ('$' in password) or ('%' in password) or ('^' in password) or ('&' in password) or ('*' in password):
                    isValidPassword = True










    pass