import random

balance = 100

symbols = ["🎃", "🎇", "👌", "👎"]

print("🎰 ----- Welcome to Python Slot Machine ----- 🎰")
print(f"💰 Your Available Balance is: ₹{balance}")

while balance > 0:

    bet = int(input("\nEnter Your Bet Amount: ₹"))

    if bet <= 0:
        print("❌ Enter a valid amount")
        continue

    if bet > balance:
        print("❌ Insufficient Balance")
        continue

    print("\n🎲 ----- Spinning ----- 🎲")

    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)

    print(f"| {slot1} | {slot2} | {slot3} |")

    # Jackpot
    if slot1 == slot2 == slot3:
        winning = bet * 10
        balance += winning

        print(f"🎉 Jackpot! You Won ₹{winning}")

    # Two symbols matched
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        winning = bet * 5
        balance += winning

        print(f"😎 Nice! Two symbols matched.")
        print(f"🏆 You Won ₹{winning}")

    # Lost
    else:
        balance -= bet

        print(f"😢 You Lost ₹{bet}")

    print(f"💰 Current Balance: ₹{balance}")

    play_again = input("\nDo You Want To Play Again? (yes/no): ").lower()

    if play_again != "yes":
        break

print(f"\n💵 Remaining Balance: ₹{balance}")
print("🙏 Thanks For Playing Python Slot Machine")
