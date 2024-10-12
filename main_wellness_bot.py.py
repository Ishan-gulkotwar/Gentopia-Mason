import random
from datetime import datetime
import matplotlib.pyplot as plt


class WellnessBot:
    def __init__(self):
        self.journal_prompts = [
            "What is one thing you learned this week?",
            "Who is someone you can reach out to when you need support?",
            "How have you been resilient this month?",
            "What self-care activity made you feel good recently?",
            "Describe a positive experience from your day."
        ]
        self.mood_log = {}

    def log_mood(self, mood):
        """Log the user's mood with a timestamp."""
        timestamp = datetime.now()
        self.mood_log[timestamp] = mood
        print(f"Mood logged: {mood} at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    def predict_mood(self):
        """Generate insights based on logged moods."""
        if len(self.mood_log) > 3:
            last_moods = list(self.mood_log.values())[-3:]
            positive_count = sum(1 for m in last_moods if m in ["happy", "content"])
            if positive_count >= 2:
                return "You've had some positive days recently! Keep it up!"
            return "It looks like you've been having a few challenges. Remember to take care of yourself."
        return "Keep tracking your mood so I can help you with insights."

    def mood_visualization(self):
        """Visualize the mood trends using a simple plot."""
        if not self.mood_log:
            print("No mood data available to display.")
            return

        timestamps = list(self.mood_log.keys())
        moods = [
            self.mood_log[timestamp] if self.mood_log[timestamp] in ["happy", "stressed", "sad",
                                                                     "anxious"] else "neutral"
            for timestamp in timestamps
        ]

        plt.figure(figsize=(10, 5))
        plt.title('Mood Tracking')
        plt.xlabel('Date and Time')
        plt.ylabel('Mood')
        color_map = {'happy': 'green', 'sad': 'blue', 'stressed': 'orange', 'anxious': 'red', 'neutral': 'grey'}
        plt.scatter(timestamps, moods, color=[color_map[mood] for mood in moods], marker='o')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid()
        plt.show()

    def personalized_wellness_recommendation(self, mood):
        """Provide a wellness recommendation based on mood."""
        recommendations = {
            "happy": "Keep the positivity going! Consider sharing your happiness with someone else.",
            "content": "That's great! Engage in an activity you enjoy.",
            "sad": "It's okay to feel down. Take some time to relax or reach out to someone you trust.",
            "stressed": "Take a deep breath. Mindfulness exercises or a short walk can help.",
            "anxious": "Focus on grounding techniques like deep breathing or enjoy a calming activity.",
            "neutral": "Perhaps explore something new to lift your spirits!"
        }
        return recommendations.get(mood.lower(), "Engage in a self-care activity that you enjoy.")

    def fetch_wellness_resources(self, topic):
        """Fetch mental health resources from a simulated API or website."""
        print(f"Fetching resources for '{topic}'...")

        # Simulating an API response
        resources = {
            "stress": [
                "1. Stress Management Techniques: Visit [link1]",
                "2. Understanding Stress: Visit [link2]",
                "3. Relaxation Exercises: Visit [link3]"
            ],
            "anxiety": [
                "1. Coping with Anxiety: Visit [link4]",
                "2. Breathing Techniques: Visit [link5]",
                "3. Mindfulness for Anxiety: Visit [link6]"
            ],
            "general": [
                "1. Mental Health Awareness: Visit [link7]",
                "2. Self-Care Tips: Visit [link8]",
                "3. Finding Support: Visit [link9]"
            ]
        }
        return resources.get(topic.lower(), ["No resources found for this topic. Try something else."])

    def get_journal_prompt(self):
        """Return a random journal prompt."""
        return random.choice(self.journal_prompts)


# Example interaction
if __name__ == "__main__":
    wellness_bot = WellnessBot()

    while True:
        user_input = input(" ```python")
        user_input = input("How are you feeling today? (Type 'exit' to quit) ")
        if user_input.lower() == 'exit':
            break

        # Log the user's mood
        wellness_bot.log_mood(user_input)

        # Generate mood prediction and recommendations
        mood_prediction = wellness_bot.predict_mood()
        print(mood_prediction)

        wellness_recommendation = wellness_bot.personalized_wellness_recommendation(user_input)
        print(f"Recommendation: {wellness_recommendation}")

        # Provide a journaling prompt
        journal_prompt = wellness_bot.get_journal_prompt()
        print(f"Your journaling prompt for today: {journal_prompt}")

        # Ask user for resource query
        resource_topic = input(
            "What specific topic of mental health resources are you interested in? (e.g., stress, anxiety, general) ")
        resources = wellness_bot.fetch_wellness_resources(resource_topic)
        print("Here are some resources you might find helpful:")
        for resource in resources:
            print(resource)

        # Show mood visualization
        wellness_bot.mood_visualization()

    print("Thank you for using WellnessBot! Take care of yourself.")