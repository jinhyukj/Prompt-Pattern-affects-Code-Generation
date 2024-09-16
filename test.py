import pytest
from SmartHomeGym import User, Feed, MembershipRegistration, LoginSystem, Calendar, ExerciseSystem, Ranking

##################
### class User ###
def test_user_creation_valid():
    # Valid User Creation
    user = User('johndoe', 'password123!', 'johndoe@example.com')
    assert user.username == 'johndoe'
    assert user.password == 'password123!'
    assert user.email == 'johndoe@example.com'
    assert user.calendar == {}
    assert user.exercises == []
    assert user.rank is None

#########################
### class MembershipRegistration ###
# __init__
def test_membership_initialization():
    membership = MembershipRegistration()
    assert membership.users == []

def test_membership_users_list_empty():
    membership = MembershipRegistration()
    assert len(membership.users) == 0

def test_membership_no_users_exist():
    membership = MembershipRegistration()
    assert not membership.users

def test_membership_users_type():
    membership = MembershipRegistration()
    assert isinstance(membership.users, list)

# General Case: register_user
def test_register_user_success():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    assert len(membership.users) == 1
    assert membership.users[0].username == 'johndoe'

# General Case: register_user
def test_register_user_success_2():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'password456!', 'johndoe@example.com')
    assert len(membership.users) == 2
    assert membership.users[0].username == 'johndoe'
    assert membership.users[1].username == 'janedoe'

# General Case: register_user
def test_register_user_success_3():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'password456!', 'johndoe@example.com')
    membership.register_user('jackdoe', 'password789!', 'jackdoe@example.com')
    assert len(membership.users) == 3
    assert membership.users[0].username == 'johndoe'
    assert membership.users[1].username == 'janedoe'
    assert membership.users[2].username == 'jackdoe'

# Edge Case: Duplicate username
def test_register_user_duplicate_username():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="Username already exists"):
        membership.register_user('johndoe', 'password456!', 'johndoe2@example.com')
    assert len(membership.users) == 1

# Edge Case: Invalid email
def test_register_user_invalid_email():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid email"):
        membership.register_user('janedoe', 'password123!', 'invalid_email')
    assert not any(user.email == 'invalid_email' for user in membership.users)

# Edge Case: Invalid password
def test_register_user_invalid_password():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid password"):
        membership.register_user('janedoe', 'short', 'janedoe@example.com')
    assert not any(user.username == 'janedoe' for user in membership.users)

# Edge Case: Username with special characters
def test_register_user_invalid_username_special_characters():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid username"):
        membership.register_user('john@doe', 'password123!', 'johndoe@example.com')
    assert not any(user.username == 'john@doe' for user in membership.users)

# Edge Case: Username with leading spaces
def test_register_user_invalid_username_leading_spaces():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid username"):
        membership.register_user(' johndoe', 'password123!', 'johndoe@example.com')
    assert not any(user.username == ' johndoe' for user in membership.users)

# Edge Case: Username with trailing spaces
def test_register_user_invalid_username_trailing_spaces():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid username"):
        membership.register_user('johndoe ', 'password123!', 'johndoe@example.com')
    assert not any(user.username == 'johndoe ' for user in membership.users)

# Edge Case: Username length too short
def test_register_user_invalid_username_length_short():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid username"):
        membership.register_user('jd', 'password123!', 'johndoe@example.com')
    assert not any(user.username == 'jd' for user in membership.users)

# Edge Case: Username length too long
def test_register_user_invalid_username_length_long():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid username"):
        membership.register_user('j' * 21, 'password123!', 'johndoe@example.com')
    assert not any(user.username == 'j' * 21 for user in membership.users)

# Edge Case: Username with different cases
def test_register_user_different_cases():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    membership.register_user('Johndoe', 'password456!', 'Johndoe@example.com')
    assert len(membership.users) == 2

# Edge Case: Password with only spaces
def test_register_user_invalid_password_only_spaces():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid password"):
        membership.register_user('janedoe', ' ' * 8, 'janedoe@example.com')
    assert not any(user.username == 'janedoe' for user in membership.users)

# Edge Case: Password with spaces (valid)
def test_register_user_password_with_spaces():
    membership = MembershipRegistration()
    membership.register_user('janedoe', 'pass word1!', 'janedoe@example.com')
    assert len(membership.users) == 1
    assert membership.users[0].username == 'janedoe'

# Edge Case: Password with no special characters
def test_register_user_invalid_password_no_special_characters():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid password"):
        membership.register_user('janedoe', 'password123', 'janedoe@example.com')
    assert not any(user.username == 'janedoe' for user in membership.users)

# Edge Case: Password with no numbers
def test_register_user_invalid_password_no_numbers():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid password"):
        membership.register_user('janedoe', 'password!', 'janedoe@example.com')
    assert not any(user.username == 'janedoe' for user in membership.users)

# Edge Case: Valid password with special characters at various positions
def test_register_user_valid_password_special_chars():
    membership = MembershipRegistration()
    membership.register_user('janedoe', 'pass!word1', 'janedoe@example.com')
    assert len(membership.users) == 1
    assert membership.users[0].username == 'janedoe'

# Edge Case: Valid email with subdomain
def test_register_user_valid_email_subdomain():
    membership = MembershipRegistration()
    membership.register_user('janedoe', 'password123!', 'user@sub.domain.com')
    assert len(membership.users) == 1
    assert membership.users[0].email == 'user@sub.domain.com'

# Edge Case: Valid email with different TLD
def test_register_user_valid_email_different_tld():
    membership = MembershipRegistration()
    membership.register_user('janedoe', 'password123!', 'user@domain.co.uk')
    assert len(membership.users) == 1
    assert membership.users[0].email == 'user@domain.co.uk'

# Edge Case: Invalid email missing '@'
def test_register_user_invalid_email_missing_at():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid email"):
        membership.register_user('janedoe', 'password123!', 'userdomain.com')
    assert not any(user.email == 'userdomain.com' for user in membership.users)

# Edge Case: Invalid email missing domain
def test_register_user_invalid_email_missing_domain():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid email"):
        membership.register_user('janedoe', 'password123!', 'user@.com')
    assert not any(user.email == 'user@.com' for user in membership.users)

# Edge Case: Invalid email with invalid characters
def test_register_user_invalid_email_invalid_characters():
    membership = MembershipRegistration()
    with pytest.raises(ValueError, match="Invalid email"):
        membership.register_user('janedoe', 'password123!', 'user@domain$.com')
    assert not any(user.email == 'user@domain$.com' for user in membership.users)

# Edge Case: Email with leading spaces
def test_register_user_email_with_leading_spaces():
    membership = MembershipRegistration()
    membership.register_user('janedoe', 'password123!', ' janedoe@example.com')
    assert len(membership.users) == 1
    assert membership.users[0].email == 'janedoe@example.com'

# Edge Case: Email with trailing spaces
def test_register_user_email_with_trailing_spaces():
    membership = MembershipRegistration()
    membership.register_user('janedoe', 'password123!', 'janedoe@example.com ')
    assert len(membership.users) == 1
    assert membership.users[0].email == 'janedoe@example.com'

# Edge Case: Very long email address (up to 254 characters)
def test_register_user_very_long_email():
    membership = MembershipRegistration()
    long_email = 'user' + 'a' * 240 + '@example.com'
    membership.register_user('janedoe', 'password123!', long_email)
    assert len(membership.users) == 1
    assert membership.users[0].email == long_email

# Edge Case: Duplicate email
def test_register_user_duplicate_email():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="Email already exists"):
        membership.register_user('janedoe', 'password123!', 'johndoe@example.com')
    assert len(membership.users) == 1
    assert not any(user.username == 'janedoe' for user in membership.users)

# Edge Case: Case insensitive username
def test_register_user_case_insensitive_username():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    membership.register_user('JohnDoe', 'password456!', 'john2doe@example.com')
    assert len(membership.users) == 2

# Edge Case: Case insensitive email
def test_register_user_case_insensitive_email():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'password123!', 'JohnDoe@Example.com')
    assert len(membership.users) == 2

#########################
### class LoginSystem ###
# login
# General Case: Valid login with correct username and password
def test_login_valid():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'password123!')
    assert login_system.logged_in_user.username == 'johndoe'

# General Case: Login with different valid username and password
def test_login_another_valid_user():
    membership = MembershipRegistration()
    membership.register_user('janedoe', 'Password@456', 'janedoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('janedoe', 'Password@456')
    assert login_system.logged_in_user.username == 'janedoe'

# General Case: Successful login after registering multiple users
def test_login_with_multiple_users():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'Password@456', 'janedoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('janedoe', 'Password@456')
    assert login_system.logged_in_user.username == 'janedoe'

# Edge Case: Invalid password provided for existing user
def test_login_invalid_password():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    with pytest.raises(ValueError, match="Invalid username or password"):
        login_system.login('johndoe', 'wrongpassword')
    assert login_system.logged_in_user is None

# Edge Case: Attempt to log in with a non-existent username
def test_login_nonexistent_user():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    with pytest.raises(ValueError, match="Invalid username or password"):
        login_system.login('janedoe', 'password123!')
    assert login_system.logged_in_user is None

# Edge Case: Case sensitivity in username and password
def test_login_case_sensitivity():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    # Case-sensitive username mismatch
    with pytest.raises(ValueError, match="Invalid username or password"):
        login_system.login('JohnDoe', 'password123!')
    assert login_system.logged_in_user is None
    
    # Case-sensitive password mismatch
    with pytest.raises(ValueError, match="Invalid username or password"):
        login_system.login('johndoe', 'Password123!')
    assert login_system.logged_in_user is None

# logout
# General Case: Logout a user who is currently logged in
def test_logout_with_logged_in_user():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'password123!')
    assert login_system.logged_in_user.username == 'johndoe'
    login_system.logout()
    assert login_system.logged_in_user is None

# General Case: Logout after logging in multiple times with the same user
def test_logout_after_multiple_logins():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'password123!')
    login_system.logout()
    assert login_system.logged_in_user is None
    login_system.login('johndoe', 'password123!')
    assert login_system.logged_in_user.username == 'johndoe'

# General Case: Logout one user and then log in as a different user
def test_logout_and_login_different_user():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'password456!', 'janedoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'password123!')
    assert login_system.logged_in_user.username == 'johndoe'
    login_system.logout()
    assert login_system.logged_in_user is None
    login_system.login('janedoe', 'password456!')
    assert login_system.logged_in_user.username == 'janedoe'

# Edge Case: Logout when no user is logged in
def test_logout_with_no_logged_in_user():
    membership = MembershipRegistration()
    login_system = LoginSystem(membership)
    login_system.logout()
    assert login_system.logged_in_user is None

# Edge Case: Logout immediately after failed login attempt
def test_logout_after_failed_login():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'wrongpassword')  # Failed login attempt
    assert login_system.logged_in_user is None  # Ensure no user is logged in
    login_system.logout()  # Call logout without a valid login
    assert login_system.logged_in_user is None  # Ensure state remains unchanged

# Edge Case: Logout after a login attempt with a non-existent user
def test_logout_after_nonexistent_user_login():
    membership = MembershipRegistration()
    login_system = LoginSystem(membership)
    login_system.login('nonexistentuser', 'password123!')  # Attempt to login with a non-existent user
    assert login_system.logged_in_user is None  # Ensure no user is logged in
    login_system.logout()  # Call logout without a valid login
    assert login_system.logged_in_user is None  # Ensure state remains unchanged

######################
### class Calendar ###
# Test case: calendar initialization when user is logged in
def test_calendar_initialization_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    assert calendar.user == login_system.logged_in_user

# Test case: calendar initialization when user is not logged in
def test_calendar_initialization_not_logged_in():
    user = User('johndoe', 'Password123!', 'johndoe@example.com')
    with pytest.raises(ValueError, match="User must be logged in to access the calendar"):
        Calendar(user)

# input_workout
# General Case: input workout when user is logged in
def test_input_workout_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    calendar.input_workout('2024-08-01', 'Running', 30)
    assert login_system.logged_in_user.calendar == {'2024-08-01': [{'name': 'Running', 'duration': 30}]}

# General Case: multiple exercises on one date when user is logged in
def test_input_multiple_exercises_one_date_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    calendar.input_workout('2024-08-01', 'Running', 30)
    calendar.input_workout('2024-08-01', 'Swimming', 45)
    assert login_system.logged_in_user.calendar == {
        '2024-08-01': [{'name': 'Running', 'duration': 30}, {'name': 'Swimming', 'duration': 45}]
    }

# General Case: one exercise on multiple dates when user is logged in
def test_input_one_exercise_multiple_dates_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    calendar.input_workout('2024-08-01', 'Running', 30)
    calendar.input_workout('2024-08-02', 'Running', 30)
    assert login_system.logged_in_user.calendar == {
        '2024-08-01': [{'name': 'Running', 'duration': 30}],
        '2024-08-02': [{'name': 'Running', 'duration': 30}]
    }


# Edge Case: Invalid date format
def test_input_workout_invalid_date_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    with pytest.raises(ValueError):
        calendar.input_workout('01-08-2024', 'Running', 30)
    assert '01-08-2024' not in login_system.logged_in_user.calendar

# Edge Case: Empty workout name
def test_input_workout_empty_name_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    with pytest.raises(ValueError):
        calendar.input_workout('2024-08-01', '', 30)
    assert '2024-08-01' not in login_system.logged_in_user.calendar

# Edge Case: Invalid workout duration
def test_input_workout_invalid_duration_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    with pytest.raises(ValueError):
        calendar.input_workout('2024-08-01', 'Running', -30)
    assert '2024-08-01' not in login_system.logged_in_user.calendar

# Edge Case: Exercise name too long (more than 256 letters)
def test_input_workout_name_too_long_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    long_name = 'R' * 257
    with pytest.raises(ValueError):
        calendar.input_workout('2024-08-01', long_name, 30)
    assert '2024-08-01' not in login_system.logged_in_user.calendar

# Edge Case: Workout duration is zero
def test_input_workout_zero_duration_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    with pytest.raises(ValueError):
        calendar.input_workout('2024-08-01', 'Running', 0)
    assert '2024-08-01' not in login_system.logged_in_user.calendar

# Edge Case: Workout duration is non-integer
def test_input_workout_non_integer_duration_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    with pytest.raises(TypeError):
        calendar.input_workout('2024-08-01', 'Running', 'thirty')
    assert '2024-08-01' not in login_system.logged_in_user.calendar


# show_plan
# General Case: show plan when user is logged in
def test_show_plan_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    calendar.input_workout('2024-08-01', 'Running', 30)
    schedule = calendar.show_plan('2024-08-01')
    assert schedule == [{'name': 'Running', 'duration': 30}]

# General Case: show plan with multiple exercises on the same date
def test_show_plan_multiple_exercises_same_date():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    calendar.input_workout('2024-08-01', 'Running', 30)
    calendar.input_workout('2024-08-01', 'Swimming', 45)
    schedule = calendar.show_plan('2024-08-01')
    assert schedule == [
        {'name': 'Running', 'duration': 30},
        {'name': 'Swimming', 'duration': 45}
    ]

# General Case: show plan with multiple exercises on multiple dates
def test_show_plan_multiple_exercises_multiple_dates():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    calendar.input_workout('2024-08-01', 'Running', 30)
    calendar.input_workout('2024-08-01', 'Swimming', 45)
    calendar.input_workout('2024-08-02', 'Cycling', 60)
    calendar.input_workout('2024-08-02', 'Yoga', 30)
    schedule_1 = calendar.show_plan('2024-08-01')
    schedule_2 = calendar.show_plan('2024-08-02')
    assert schedule_1 == [
        {'name': 'Running', 'duration': 30},
        {'name': 'Swimming', 'duration': 45}
    ]
    assert schedule_2 == [
        {'name': 'Cycling', 'duration': 60},
        {'name': 'Yoga', 'duration': 30}
    ]


# Edge Case: No exercises for the given date
def test_show_plan_no_exercises_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    schedule = calendar.show_plan('2024-08-01')
    assert schedule == []

# Edge Case: Invalid date format
def test_show_plan_invalid_date_format_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    with pytest.raises(ValueError):
        calendar.show_plan('01-08-2024')


# Edge Case: Show plan with no exercises on a specific date
def test_show_plan_no_exercises_on_date():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    calendar = Calendar(login_system.logged_in_user)
    calendar.input_workout('2024-08-01', 'Running', 30)
    schedule = calendar.show_plan('2024-08-02')
    assert schedule == []

###########################
### class ExerciseSystem ###

# start_exercise
# General Case: start exercise when user is logged in
def test_start_exercise_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    exercise_session.start_exercise('Running', 30)
    assert login_system.logged_in_user.exercises == [{'name': 'Running', 'duration': 30}]

# General Case: adding multiple exercises with different validations when user is logged in
def test_start_exercise_multiple_validations_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    exercise_session.start_exercise('Running', 30)
    with pytest.raises(ValueError):
        exercise_session.start_exercise('R' * 257, 30)  # Name too long
    with pytest.raises(ValueError):
        exercise_session.start_exercise('Swimming', -10)  # Invalid duration
    exercise_session.start_exercise('Cycling', 45)
    assert login_system.logged_in_user.exercises == [
        {'name': 'Running', 'duration': 30},
        {'name': 'Cycling', 'duration': 45}
    ]

# General Case: adding multiple exercises with different durations when user is logged in
def test_start_exercise_different_durations_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    exercise_session.start_exercise('Running', 30)
    exercise_session.start_exercise('Swimming', 60)
    exercise_session.start_exercise('Cycling', 45)
    assert login_system.logged_in_user.exercises == [
        {'name': 'Running', 'duration': 30},
        {'name': 'Swimming', 'duration': 60},
        {'name': 'Cycling', 'duration': 45}
    ]

# Edge Case: start exercise with empty name when user is logged in
def test_start_exercise_empty_name_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.start_exercise('', 30)

# Edge Case: start exercise with name containing only spaces when user is logged in
def test_start_exercise_name_only_spaces_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.start_exercise('   ', 30)

# Edge Case: start exercise with invalid duration when user is logged in
def test_start_exercise_invalid_duration_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.start_exercise('Running', -30)

# Edge Case: start exercise with non-integer duration when user is logged in
def test_start_exercise_non_integer_duration_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.start_exercise('Running', 'thirty')

# Edge Case: start exercise with too long name when user is logged in
def test_start_exercise_name_too_long_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.start_exercise('R' * 257, 30)

# Edge Case: start exercise with special characters in name when user is logged in
def test_start_exercise_name_with_special_characters_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.start_exercise('Running!', 30)



# Edge Case: adding multiple exercises with some invalid entries when user is logged in
def test_start_exercise_with_invalid_exercise_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    exercise_session.start_exercise('Running', 30)
    with pytest.raises(ValueError):
        exercise_session.start_exercise('', 30)  # Invalid exercise name
    exercise_session.start_exercise('Cycling', 45)
    assert login_system.logged_in_user.exercises == [
        {'name': 'Running', 'duration': 30},
        {'name': 'Cycling', 'duration': 45}
    ]



# provide_feedback
# General Case: provide feedback when user is logged in
def test_provide_feedback_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    exercise_session.start_exercise('Running', 30)
    feedback = exercise_session.provide_feedback('2024-08-01')
    assert feedback == "Total exercise duration: 30 minutes, 0 minutes short of your goal"

# General Case: provide feedback with no exercises when user is logged in
def test_provide_feedback_no_exercises_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    feedback = exercise_session.provide_feedback('2024-08-01')
    assert feedback == "Total exercise duration: 0 minutes, 0 minutes short of your goal"

# General Case: multiple users providing feedback on the same date when logged in
def test_provide_feedback_multiple_users_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'Password123!', 'janedoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session1 = ExerciseSystem(login_system.logged_in_user)
    exercise_session1.start_exercise('Running', 30)

    login_system.logout()
    login_system.login('janedoe', 'Password123!')
    exercise_session2 = ExerciseSystem(login_system.logged_in_user)
    exercise_session2.start_exercise('Cycling', 45)

    feedback1 = exercise_session1.provide_feedback('2024-08-01')
    feedback2 = exercise_session2.provide_feedback('2024-08-01')

    assert feedback1 == "Total exercise duration: 30 minutes, 0 minutes short of your goal"
    assert feedback2 == "Total exercise duration: 45 minutes, 0 minutes short of your goal"

# Edge Case: provide feedback with invalid date format when user is logged in
def test_provide_feedback_invalid_date_format_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.provide_feedback('01-08-2024')

# Edge Case: provide feedback with non-existent date when user is logged in
def test_provide_feedback_non_existent_date_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.provide_feedback('2024-14-01')

# Edge Case: provide feedback with whitespace date when user is logged in
def test_provide_feedback_whitespace_date_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    exercise_session = ExerciseSystem(login_system.logged_in_user)
    with pytest.raises(ValueError):
        exercise_session.provide_feedback(' 2024-08-01 ')


###########################
### class Ranking ###

# calculate_ranking

# General case: calculate ranking when user is logged in
def test_calculate_ranking_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})
    ranking = Ranking(membership)
    ranking.calculate_ranking()
    assert user_john.rank == 1

# General case: calculate ranking with multiple exercises for a single user
def test_calculate_ranking_multiple_exercises_single_user_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})
    user_john.exercises.append({'name': 'Cycling', 'duration': 45})

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    assert user_john.rank == 1

# General case: calculate ranking with multiple users having the same duration
def test_calculate_ranking_multiple_users_same_duration_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'Password123!', 'janedoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})

    login_system.logout()
    login_system.login('janedoe', 'Password123!')
    user_jane = login_system.logged_in_user
    user_jane.exercises.append({'name': 'Cycling', 'duration': 30})

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    assert user_john.rank == 1
    assert user_jane.rank == 1

# General case: calculate ranking with multiple exercises having the same total duration
def test_calculate_ranking_multiple_exercises_same_duration_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'Password123!', 'janedoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})
    user_john.exercises.append({'name': 'Swimming', 'duration': 45})

    login_system.logout()
    login_system.login('janedoe', 'Password123!')
    user_jane = login_system.logged_in_user
    user_jane.exercises.append({'name': 'Cycling', 'duration': 75})

    ranking = Ranking(membership)
    ranking.calculate_ranking()

    assert user_john.rank == 1
    assert user_jane.rank == 1

# General case: get user ranking after multiple exercises
def test_get_user_ranking_after_multiple_exercises_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})
    user_john.exercises.append({'name': 'Cycling', 'duration': 45})

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    rank = ranking.get_user_ranking('johndoe')
    assert rank == 1

# General case: calculate ranking with a single user having exercises
def test_calculate_ranking_single_user_with_exercises_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    assert user_john.rank == 1

# Edge case: calculate ranking with no users
def test_calculate_ranking_no_users():
    membership = MembershipRegistration()
    ranking = Ranking(membership)
    ranking.calculate_ranking()
    assert len(membership.users) == 0



# get_user_ranking

# General case: get user ranking when user is logged in
def test_get_user_ranking_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    rank = ranking.get_user_ranking('johndoe')
    assert rank == 1

# General case: calculate ranking for multiple users with different exercise durations
def test_calculate_ranking_multiple_users_different_durations_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'Password123!', 'janedoe@example.com')
    membership.register_user('mikedoe', 'Password123!', 'mikedoe@example.com')

    login_system = LoginSystem(membership)
    
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})
    
    login_system.logout()
    login_system.login('janedoe', 'Password123!')
    user_jane = login_system.logged_in_user
    user_jane.exercises.append({'name': 'Cycling', 'duration': 60})
    
    login_system.logout()
    login_system.login('mikedoe', 'Password123!')
    user_mike = login_system.logged_in_user
    user_mike.exercises.append({'name': 'Swimming', 'duration': 45})

    ranking = Ranking(membership)
    ranking.calculate_ranking()

    assert user_jane.rank == 1
    assert user_mike.rank == 2
    assert user_john.rank == 3

# General case: share ranking on social media after multiple exercises
def test_share_ranking_on_social_media_after_multiple_exercises_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})
    user_john.exercises.append({'name': 'Swimming', 'duration': 60})

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    message = ranking.share_ranking_on_social_media('johndoe')
    assert message == "User johndoe is ranked #1 in the Smart Home-Gym community!"

# General case: share ranking on social media when user is logged in
def test_share_ranking_on_social_media_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    message = ranking.share_ranking_on_social_media('johndoe')
    assert message == "User johndoe is ranked #1 in the Smart Home-Gym community!"

# Edge case: get user ranking when user is not logged in
def test_get_user_ranking_not_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    
    ranking = Ranking(membership)
    with pytest.raises(ValueError, match="User must be logged in to get ranking"):
        ranking.get_user_ranking('johndoe')

# Edge case: get user ranking for a non-existent user
def test_get_user_ranking_nonexistent():
    membership = MembershipRegistration()
    ranking = Ranking(membership)
    rank = ranking.get_user_ranking('nonexistent_user')
    assert rank is None

# Edge case: get user ranking with no exercises
def test_get_user_ranking_no_exercises_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    rank = ranking.get_user_ranking('johndoe')
    assert rank is None

# Edge case: get user ranking with whitespace username
def test_get_user_ranking_whitespace_username():
    membership = MembershipRegistration()
    ranking = Ranking(membership)
    with pytest.raises(ValueError):
        ranking.get_user_ranking(' johndoe ')

# Edge case: share ranking on social media when user is not logged in
def test_share_ranking_on_social_media_not_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    
    ranking = Ranking(membership)
    with pytest.raises(ValueError, match="User must be logged in to share ranking on social media"):
        ranking.share_ranking_on_social_media('johndoe')

# Edge case: share ranking on social media for a non-existent user
def test_share_ranking_on_social_media_nonexistent():
    membership = MembershipRegistration()
    ranking = Ranking(membership)
    message = ranking.share_ranking_on_social_media('nonexistent_user')
    assert message == "User not found or no ranking available."

# Edge case: share ranking on social media with no exercises when user is logged in
def test_share_ranking_on_social_media_no_exercises_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')

    login_system = LoginSystem(membership)
    login_system.login('johndoe', 'Password123!')

    ranking = Ranking(membership)
    ranking.calculate_ranking()
    message = ranking.share_ranking_on_social_media('johndoe')
    assert message == "User not found or no ranking available."

# Edge case: share ranking on social media with whitespace username
def test_share_ranking_on_social_media_whitespace_username():
    membership = MembershipRegistration()
    ranking = Ranking(membership)
    with pytest.raises(ValueError):
        ranking.share_ranking_on_social_media(' johndoe ')


# share_ranking_on_social_media

# General case: share ranking on social media for multiple users
def test_share_ranking_on_social_media_multiple_users_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'Password123!', 'janedoe@example.com')
    membership.register_user('mikedoe', 'Password123!', 'mikedoe@example.com')

    login_system = LoginSystem(membership)
    
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})

    login_system.logout()
    login_system.login('janedoe', 'Password123!')
    user_jane = login_system.logged_in_user
    user_jane.exercises.append({'name': 'Cycling', 'duration': 60})

    login_system.logout()
    login_system.login('mikedoe', 'Password123!')
    user_mike = login_system.logged_in_user
    user_mike.exercises.append({'name': 'Swimming', 'duration': 45})

    ranking = Ranking(membership)
    ranking.calculate_ranking()

    message_john = ranking.share_ranking_on_social_media('johndoe')
    message_jane = ranking.share_ranking_on_social_media('janedoe')
    message_mike = ranking.share_ranking_on_social_media('mikedoe')

    assert message_john == "User johndoe is ranked #3 in the Smart Home-Gym community!"
    assert message_jane == "User janedoe is ranked #1 in the Smart Home-Gym community!"
    assert message_mike == "User mikedoe is ranked #2 in the Smart Home-Gym community!"

# Edge case: calculate ranking with no exercises for one user
def test_calculate_ranking_no_exercises_for_one_user_logged_in():
    membership = MembershipRegistration()
    membership.register_user('johndoe', 'Password123!', 'johndoe@example.com')
    membership.register_user('janedoe', 'Password123!', 'janedoe@example.com')

    login_system = LoginSystem(membership)
    
    login_system.login('johndoe', 'Password123!')
    user_john = login_system.logged_in_user
    user_john.exercises.append({'name': 'Running', 'duration': 30})

    login_system.logout()
    login_system.login('janedoe', 'Password123!')
    user_jane = login_system.logged_in_user
    # user_jane has no exercises

    ranking = Ranking(membership)
    ranking.calculate_ranking()

    assert user_john.rank == 1
    assert user_jane.rank is None