import datetime
import os


def assess_mood():
    moods = {
        'happy': 2,
        'relaxed': 1,
        'apathetic': 0,
        'sad': -1,
        'angry': -2
    }

    date_today = datetime.date.today()
    date_today_str = str(date_today)

    mood_file_dir = 'data'
    mood_file_path = os.path.join(mood_file_dir, 'mood_diary.txt')

    if not os.path.exists(mood_file_dir):
        os.makedirs(mood_file_dir)

    if os.path.exists(mood_file_path):
        with open(mood_file_path, 'r') as file:
            entries = file.readlines()
            for entry in entries:
                date, _ = entry.strip().split(',')
                if date == date_today_str:
                    print("Sorry, you have already entered your mood today.")
                    return

    while True:
        mood_input = input("Please enter your current mood (happy, relaxed, apathetic, sad, angry): ").lower()
        if mood_input in moods:
            mood_value = moods[mood_input]
            with open(mood_file_path, 'a') as file:
                file.write(f"{date_today_str},{mood_value}\n")
            print("Your mood has been recorded.")
            break
        else:
            print("Invalid mood. Please enter a valid mood.")


def diagnose_mood_disorders():
    mood_file_path = os.path.join('data', 'mood_diary.txt')

    if not os.path.exists(mood_file_path):
        print("No mood data available.")
        return

    date_today = datetime.date.today()
    week_ago = date_today - datetime.timedelta(days=7)

    mood_entries = []
    with open(mood_file_path, 'r') as file:
        entries = file.readlines()
        for entry in entries:
            date_str, mood_value = entry.strip().split(',')
            date = datetime.date.fromisoformat(date_str)
            mood_value = int(mood_value)
            if date > week_ago:
                mood_entries.append(mood_value)

    if not mood_entries:
        print("No mood data available for the past 7 days.")
        return

    avg_mood = sum(mood_entries) / len(mood_entries)

    if avg_mood >= 1:
        print("You seem to be in a generally good mood!")
    elif avg_mood <= -1:
        print("You might be experiencing some negative feelings. Consider talking to someone.")
    else:
        print("Your mood seems to be neutral or mixed.")
