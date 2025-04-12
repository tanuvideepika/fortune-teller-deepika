# fortune.py v1.0

print("🔮 Welcome to Deepika Tanuvi's Fortune Teller (21JE0293) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Deepika! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Tough times never last, but tough people like you do. ✨")
elif mood == "neutral":
    print("✨ Your fortune: Stay open to new experiences — surprises are coming your way. ✨")
else:
    print("✨ I can't read that mood... maybe try happy, sad, or neutral? ✨")
