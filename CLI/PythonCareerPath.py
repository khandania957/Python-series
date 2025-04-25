print("Welcome! I'll help you decide a career path focused on Python, based on your interests."
      "\nAnswer a few questions to find out your ideal Python career path.")

score = {"Data Science": 0, "Web/App Development": 0, "AI/ML": 0, "Game Development": 0}

print("\nQ1: What kind of problems do you enjoy solving?"
      "\nA. Analyzing numbers and finding patterns"
      "\nB. Building websites or online stores"
      "\nC. Designing games and challenges"
      "\nD. Teaching machines to think and learn")

answer = input("\nEnter your answer (A/B/C/D): ").upper()

if answer == "A":
    score["Data Science"] += 1
elif answer == "B":
    score["Web/App Development"] += 1
elif answer == "C":
    score["Game Development"] += 1
elif answer == "D":
    score["AI/ML"] += 1

print("\nQ2: Which project sounds most exciting to you?"
      "\nA. Finding insights from a huge dataset"
      "\nB. Building a blog website from scratch"
      "\nC. Creating a new video game"
      "\nD. Developing a chatbot that can talk like a human")

answer = input("\nEnter your answer (A/B/C/D): ").upper()

if answer == "A":
    score["Data Science"] += 1
elif answer == "B":
    score["Web/App Development"] += 1
elif answer == "C":
    score["Game Development"] += 1
elif answer == "D":
    score["AI/ML"] += 1

print("\nQ3: What excites you the most about Python?"
      "\nA. Making sense of messy real-world data"
      "\nB. Creating fast and beautiful websites"
      "\nC. Designing player experiences in games"
      "\nD. Building intelligent systems like recommendation engines")

answer = input("\nEnter your answer (A/B/C/D): ").upper()

if answer == "A":
    score["Data Science"] += 1
elif answer == "B":
    score["Web/App Development"] += 1
elif answer == "C":
    score["Game Development"] += 1
elif answer == "D":
    score["AI/ML"] += 1

print("\nQ4: What kind of tasks do you find most satisfying?"
      "\nA. Finding hidden insights by digging into messy data"
      "\nB. Designing cool websites that people actually use"
      "\nC. Creating stories and characters that players will love"
      "\nD. Making machines smarter so they can help people automatically")

answer = input("\nEnter your answer (A/B/C/D): ").upper()

if answer == "A":
    score["Data Science"] += 1
elif answer == "B":
    score["Web/App Development"] += 1
elif answer == "C":
    score["Game Development"] += 1
elif answer == "D":
    score["AI/ML"] += 1

print("\nQ5: Imagine your dream project. Which one would you pick?"
      "\nA. Analyze world health data to find hidden trends"
      "\nB. Build a social media website for a niche community"
      "\nC. Develop a multiplayer adventure game"
      "\nD. Create an AI system that writes poetry")

answer = input("\nEnter your answer (A/B/C/D): ").upper()

if answer == "A":
    score["Data Science"] += 1
elif answer == "B":
    score["Web/App Development"] += 1
elif answer == "C":
    score["Game Development"] += 1
elif answer == "D":
    score["AI/ML"] += 1

best_fit = max(score, key=score.get)

print(f"Based on your answer the best fit for you is {best_fit}."
      "\nThanks for playing the Python Career Path Quiz.")
