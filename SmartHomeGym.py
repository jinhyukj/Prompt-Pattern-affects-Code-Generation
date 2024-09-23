# Import Statements
from typing import List
import re

# Class Name
class User:
    # Class Constructor
    def __init__(self, username: str, password: str, email: str):
        """
        Initializes a new user with a username, password, email, and initializes exercise list and rank.
        """
        # username = username.strip()
        if not (3 <= len(username) <= 20 and username.isalnum()):
            raise ValueError("Invalid username")
        if not self._is_valid_password(password):
            raise ValueError("Invalid password")
        
        email = email.strip()  
        if not self._is_valid_email(email):
            raise ValueError("Invalid email")
        
        self.username = username
        self.password = password
        self.email = email.strip()
        self.exercises = []
        self.calendar = {}
        self.rank = None
        self.logged_in = False

    @staticmethod
    def _is_valid_password(password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in "!@#$%^&*()_+" for char in password):
            return False
        # if any(char.isspace() for char in password):
        #     return False
        return True

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        email_regex = re.compile(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        )
        if not email_regex.match(email):
            return False
        # Additional checks
        if ".." in email or email.startswith(".") or email.endswith("."):
            return False
        if "@" in email.split('@')[0] or email.count('@') != 1:
            return False
        # if len(email) > 254:
        #     return False
        return (1 <= len(email) <= 254) and True
    
    def login(self):
        self.logged_in = True
    
    def logout(self):
        self.logged_in = False

# Class Name
class Feed:
    # Class Constructor
    def __init__(self, user: User):
        """
        Initializes the feed system for a specific user with a list of articles.
        """
        self.user = user
        self.articles = [
            "10 Tips for Effective Home Workouts",
            "How to Stay Motivated to Exercise",
            "Best Exercises for Building Strength"
        ]

    def add_feed(self, article: str):
        # Functional Description
        """
        Adds a new article to the user's feed.

        # Parameter Description
        :param article: str, the title of the article to be added.
        """
        if not article:
            raise ValueError("Article title cannot be empty.")
        trimmed_article = article.strip()
        if len(trimmed_article) > 256:
            raise ValueError("Article title cannot exceed 256 characters.")
        self.articles.append(trimmed_article)
    
    # Method Signature
    def show_feed(self) -> List[str]:
        # Functional Description
        """
        Displays a list of articles relevant to the user's interests.

        # Parameter/Return Description
        :return: List[str], a list of article titles.
        """
        return self.articles

# Class Name
class MembershipRegistration:
    # Class Constructor
    def __init__(self):
        """
        Initializes the membership registration system with an empty user list.
        """
        self.users = []

    # Method Signature
    def register_user(self, username: str, password: str, email: str) -> bool:
        # Functional Description
        """
        Registers a new user if the username does not already exist.

        # Parameter/Return Description
        :param username: str, the username for the new user.
        :param password: str, the password for the new user.
        :param email: str, the email address for the new user.
        :return: bool, True if registration is successful, False otherwise.
        """
        if username != username.strip():
            raise ValueError("Invalid username")
        
        if any(user.email == email for user in self.users):
            raise ValueError("Email already exists")

        if any(user.username == username for user in self.users):
            raise ValueError("Username already exists")
        new_user = User(username, password, email)
        self.users.append(new_user)
        return True

# Class Name
class LoginSystem:
    # Class Constructor
    def __init__(self, membership: MembershipRegistration):
        """
        Initializes the login system with a membership registration instance and no logged-in user.
        """
        self.membership = membership
        self.logged_in_user = None

    # Method Signature
    def login(self, username: str, password: str) -> bool:
        # Functional Description
        """
        Authenticates a user with given username and password.

        # Parameter/Return Description
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: bool, True if login is successful, False otherwise.
        """
        user = next((user for user in self.membership.users if user.username == username and user.password == password), None)

        if user:
            self.logged_in_user = user
            user.logged_in = True
            return True
        return False

    # Method Signature
    def logout(self):
        # Functional Description
        """
        Logs out the current logged-in user.
        """
        self.logged_in_user = None

# Class Name
class Calendar:
    # Class Constructor
    def __init__(self, user: User):
        """
        Initializes the calendar system for a specific user.
        """
        if not user.logged_in:
            raise ValueError("User must be logged in to access the calendar")
        self.user = user

    # def input_workout(self, date: str, exercise_name: str, duration: int):
    #     """
    #     Input an exercise and duration for a specific date.
    #     """
    #     calendar = self.user.calendar
    #     if date in calendar:
    #         self.user.calendar[date].append({'name': exercise_name, 'duration': duration})
    #     else:
    #         self.user.calendar.update({date: [{'name': exercise_name, 'duration': duration}]})

    def input_workout(self, date: str, exercise_name: str, duration: int):
        """Input an exercise and duration for a specific date."""
        
        # Validate the date format (expecting YYYY-MM-DD)
        if not re.match(r"\d{4}-\d{2}-\d{2}", date):
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
        
        # Validate that the exercise name is not empty
        if not exercise_name.strip():
            raise ValueError("Exercise name cannot be empty.")
        
        # Validate that the exercise name is not too long
        if len(exercise_name) > 256:
            raise ValueError("Exercise name cannot exceed 256 characters.")
        
        # Validate that the duration is positive
        if duration <= 0:
            raise ValueError("Duration must be a positive number.")
        
        calendar = self.user.calendar
        if date in calendar:
            self.user.calendar[date].append({'name': exercise_name, 'duration': duration})
        else:
            self.user.calendar.update({date: [{'name': exercise_name, 'duration': duration}]})

    # Method Signature
    def show_plan(self, date: str) -> List[dict]:
        # Functional Description
        """
        Displays the user's exercise schedule for input date.

        # Parameter/Return Description
        :return: List[dict], a list of exercise records.
        """
        # Validate the date format (expecting YYYY-MM-DD)
        if not re.match(r"\d{4}-\d{2}-\d{2}", date):
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")

        # return self.user.calendar[date]
        return self.user.calendar.get(date, [])

# Class Name
class ExerciseSystem:
    # Class Constructor
    def __init__(self, user: User):
        """
        Initializes the exercise system for a specific user.
        """
        self.user = user

    # Method Signature
    def start_exercise(self, exercise_name: str, duration: int):
        # Functional Description
        """
        Records a new exercise activity for the user.

        # Parameter/Return Description
        :param exercise_name: str, the name of the exercise.
        :param duration: int, the duration of the exercise in minutes.
        """

        # exercise = {
        #     'name': exercise_name,
        #     'duration': duration
        # }
        # self.user.exercises.append(exercise)


        # Validate that the exercise name is not empty
        if not exercise_name.strip():
            raise ValueError("Exercise name cannot be empty.")

        # Validate that the exercise name contains only alphanumeric characters and spaces
        if not re.match(r'^[a-zA-Z0-9 ]+$', exercise_name):
            raise ValueError("Exercise name can only contain alphanumeric characters and spaces.")

        # Validate that the exercise name is not too long
        if len(exercise_name) > 256:
            raise ValueError("Exercise name cannot exceed 256 characters.")

        # Validate that the duration is an integer
        if not isinstance(duration, int):
            raise ValueError("Duration must be an integer.")
        
        # Validate that the duration is positive
        if duration <= 0:
            raise ValueError("Duration must be a positive number.")
        
        # If validations pass, add the exercise to the user's session
        self.user.exercises.append({'name': exercise_name, 'duration': duration})

    # Method Signature
    def provide_feedback(self, date: str):
        # Functional Description
        """
        Provides feedback on the user's total exercise duration.

        # Parameter/Return Description
        :return: str, the total exercise duration in minutes.
        """
        # total_duration = sum(exercise['duration'] for exercise in self.user.exercises)
        # goal = sum(exercise['duration'] for exercise in self.user.calendar[date])

        # if total_duration >= goal: 
        #     return f"Total exercise duration: {total_duration} minutes, exceeded goal by {total_duration - goal} minutes"
        # else:
        #     return f"Total exercise duration: {total_duration} minutes, {goal - total_duration} minutes short of your goal"

        ############################################################
        # # Trim whitespace from date
        # date = date.strip()

        # # Validate date format (expecting YYYY-MM-DD)
        # if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        #     raise ValueError(f"Invalid date format: {date}. Expected format is YYYY-MM-DD.")

        # # Check for valid month and day (basic check, could be extended for leap years)
        # year, month, day = map(int, date.split('-'))
        # if not (1 <= month <= 12) or not (1 <= day <= 31):  # Simplified validation
        #     raise ValueError(f"Non-existent date: {date}.")

        # # Check if exercises exist for the provided date
        # if date not in self.user.calendar or not self.user.calendar[date]:
        #     # If no exercises found for the date, raise a ValueError
        #     raise ValueError(f"No exercises found for date: {date}")

        # # Calculate total duration and compare with the goal
        # goal = sum(exercise['duration'] for exercise in self.user.calendar[date])
        # total_duration = sum(exercise['duration'] for exercise in self.user.exercises)

        # if total_duration >= goal:
        #     return f"Total exercise duration: {total_duration} minutes, exceeded goal by {total_duration - goal} minutes"
        # else:
        #     return f"Total exercise duration: {total_duration} minutes, {goal - total_duration} minutes short of your goal"

        ###################################
        # Trim whitespace from date
        date = date.strip()

        # Validate date format (expecting YYYY-MM-DD)
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            raise ValueError(f"Invalid date format: {date}. Expected format is YYYY-MM-DD.")

        # Check for valid month and day (basic check, could be extended for leap years)
        year, month, day = map(int, date.split('-'))
        if not (1 <= month <= 12) or not (1 <= day <= 31):  # Simplified validation
            raise ValueError(f"Non-existent date: {date}.")

        # Check if exercises exist for the provided date in the user's calendar
        user_exercises_on_date = self.user.calendar.get(date, [])

        # If no exercises are found, treat it as zero minutes, instead of raising an error
        if not user_exercises_on_date:
            return f"Total exercise duration: 0 minutes, 0 minutes short of your goal"

        # Calculate total duration of exercises on that date
        goal = sum(exercise['duration'] for exercise in user_exercises_on_date)
        total_duration = sum(exercise['duration'] for exercise in user_exercises_on_date)

        # Provide feedback based on whether total duration meets or exceeds the goal
        if total_duration >= goal:
            return f"Total exercise duration: {total_duration} minutes, 0 minutes short of your goal"
        else:
            return f"Total exercise duration: {total_duration} minutes, {goal - total_duration} minutes short of your goal"


# Class Name
class Ranking:
    # Class Constructor
    def __init__(self, membership: MembershipRegistration):
        """
        Initializes the ranking system with a membership registration instance.
        """
        self.membership = membership

    # Method Signature
    def calculate_ranking(self):
        # Functional Description
        """
        Calculates and updates the exercise rankings for all users.
        """
        # sorted_users = sorted(self.membership.users, key=lambda user: sum(ex['duration'] for ex in user.exercises), reverse=True)
        # for rank, user in enumerate(sorted_users, 1):
        #     user.rank = rank

        # Create a list of (user, total_duration) tuples
        user_durations = [(user, sum(exercise['duration'] for exercise in user.exercises)) for user in self.membership.users]
        
        # Sort users by total exercise duration in descending order
        user_durations.sort(key=lambda x: x[1], reverse=True)
        
        # Assign ranks, handling ties for equal durations
        current_rank = 1
        for i, (user, duration) in enumerate(user_durations):
            if i > 0 and duration == user_durations[i - 1][1]:
                user.rank = user_durations[i - 1][0].rank  # Assign same rank as previous user if same duration
            else:
                user.rank = current_rank
            current_rank += 1

        # Set rank to None for users with no exercises
        for user in self.membership.users:
            if not user.exercises:
                user.rank = None

    # Method Signature
    def get_user_ranking(self, username: str) -> int:
        # Functional Description
        """
        Retrieves the ranking of a specific user.

        # Parameter/Return Description
        :param username: str, the username of the user.
        :return: int, the rank of the user, or None if the user is not found.
        """
        # user = next((user for user in self.membership.users if user.username == username), None)
        # if user:
        #     return user.rank
        # return None

        # Find the user
        user = next((user for user in self.membership.users if user.username == username), None)
        
        if user is None:
            raise ValueError(f"User {username} does not exist.")
        
        # Check if the user is logged in
        if not user.logged_in:
            raise ValueError("User must be logged in to get ranking")
        
        # Return the user's rank
        return user.rank

    # Method Signature
    def share_ranking_on_social_media(self, username: str) -> str:
        # Functional Description
        """
        Shares the user's ranking on social media.

        # Parameter/Return Description
        :param username: str, the username of the user.
        :return: str, a message about the user's ranking.
        """
        # rank = self.get_user_ranking(username)
        # if rank:
        #     return f"User {username} is ranked #{rank} in the Smart Home-Gym community!"
        # return "User not found or no ranking available."


        # Check if username contains leading or trailing whitespace
        if username.strip() != username:
            raise ValueError("Username contains leading or trailing whitespace.")
        
        # Strip whitespace from the username
        username = username.strip()
        
        # Raise ValueError if the username is empty after stripping whitespace
        if not username:
            raise ValueError("Invalid username. Username cannot be empty.")
        
        # Find the user
        user = next((user for user in self.membership.users if user.username == username), None)
        
        # Raise ValueError if the user does not exist
        if user is None:
            return "User not found or no ranking available."
        
        # Check if the user is logged in
        if not user.logged_in:
            raise ValueError("User must be logged in to share ranking on social media")
        
        # Get the user's rank
        rank = self.get_user_ranking(username)
        
        if rank:
            return f"User {username} is ranked #{rank} in the Smart Home-Gym community!"
        return "User not found or no ranking available."