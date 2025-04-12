import random

print("🔮 Welcome to Deepika Tanuvi's Fortune Teller (21JE0293) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": [
        "✨ Your fortune: Great things await you, Deepika! Keep smiling. ✨",
        "✨ Happiness multiplies when you share it. Spread the joy! ✨"
    ],
    "sad": [
        "✨ Your fortune: Tough times never last, but tough people like you do. ✨",
        "✨ It's okay to feel down. A rainbow is waiting after the storm. ✨"
    ],
    "neutral": [
        "✨ Your fortune: Stay open to new experiences — surprises are coming your way. ✨",
        "✨ Sometimes calm is the best place to find clarity. ✨"
    ],
    "stressed": [
        "✨ Your fortune: Breathe. You’ve handled worse — you’ve got this. ✨",
        "✨ Stress fades when you trust your inner strength. ✨"
    ]
}

if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("✨ I can't read that mood... maybe try happy, sad, neutral, or stressed? ✨")
