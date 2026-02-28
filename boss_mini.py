# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

#SECURITY ISSUE: Hardcoded access code allows for instant win in boss fight.
#Remove any cheat related logic and variables to fix.
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

#LOGIC ERROR: Attack does not subtract health from boss.
#Add logic such as b_hp -= 10 to apply damage.
def attack():
  global b_hp
    print("You deal 10 damage!")

#LOGIC ERROR: Healing has no upper or lower limit, allowing for overhealing and healing after defeat.
#Add conditions to cap healing between 0 and 50 hp.
def heal():
  global p_hp
  p_hp += 20
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
#LOGIC ERROR: There is no win condition if the boss health reaches 0.
#add a condition where 0 boss health moves player to win state.
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  elif choice == 'c':
    if input("Code: ") == SECRET_CODE:
      b_hp = 0
  
  if b_hp > 0:
    p_hp -= 10

print("Game Over!")
