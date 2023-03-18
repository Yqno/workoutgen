import random

# Define a list of exercises
exercises = ['Bench press', 'Squats', 'Deadlifts', 'Pull-ups', 'Push-ups', 'Rows', 'Curls']

# Define a function to generate a workout plan
def generate_workout_plan(num_exercises):
    workout_plan = []
    for i in range(num_exercises):
        exercise = random.choice(exercises)
        sets = random.randint(3, 5)
        reps = random.randint(8, 12)
        workout_plan.append((exercise, sets, reps))
    return workout_plan

# Get user input for the number of exercises they want in their workout plan
num_exercises = int(input("How many exercises do you want in your workout plan? "))

# Generate the workout plan
workout_plan = generate_workout_plan(num_exercises)

# Print the workout plan
print("Your workout plan for today is:")
for exercise, sets, reps in workout_plan:
    print(f"{exercise} - {sets} sets of {reps} reps")
