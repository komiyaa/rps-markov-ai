import random

COUNTER_MOVES = {
         "r": "p",
         "p": "s",
         "s": "r"
      }

WINNING_CONDITIONS = {
         "r": "s",
         "p": "r",
         "s": "p"
      }


R1 = random.choice(["r", "p", "s"])
R2 = random.choice(["r", "p", "s"])
MOVES = [R1, R2]

AI_WINS = 1
AI_LOSS = 1
AI_DRAW = 1

def main():
      global AI_WINS, AI_LOSS, AI_DRAW

      plays = 0

      print("\n* TO EXIT write: exit *\n")

      # matrix first_order
      matrix_first_order =  {
            "r": {"r": 1, "p": 1, "s":1},
            "p": {"r": 1, "p": 1, "s":1},
            "s": {"r": 1, "p": 1, "s":1}
         }
      
      matrix_second_order = {
      "rr": {"r": 1, "p": 1, "s": 1},
      "rp": {"r": 1, "p": 1, "s": 1},
      "rs": {"r": 1, "p": 1, "s": 1},
      "pr": {"r": 1, "p": 1, "s": 1},
      "pp": {"r": 1, "p": 1, "s": 1},
      "ps": {"r": 1, "p": 1, "s": 1},
      "sr": {"r": 1, "p": 1, "s": 1},
      "sp": {"r": 1, "p": 1, "s": 1},
      "ss": {"r": 1, "p": 1, "s": 1},
          }


      while True:
        while True:
            user_move = str(input("Choose: r/p/s: ")).lower().strip()
            if user_move in BEST_MOVES:
               break
            elif user_move == "exit":
                exit()
            print("\nOnly r/p/s\n")        
            

         # sorting and assigning variables
        try:
            last_move  = MOVES[-1]
        except IndexError:
            last_move = random.choice(["r", "p", "s"])
 
        # logic 1
        row = matrix_first_order[last_move]
        total = sum(row.values())
        prob_1st = {}
        for x in row:
            prob_1st[x] = row[x] / total

        # logic 2
        last_two = MOVES[-2] + MOVES[-1]
        row_2nd = matrix_second_order[last_two]
        total_2 = sum(row_2nd.values())
        prob_2nd = {}
        for x in row_2nd:
            prob_2nd[x] = row_2nd[x] / total_2

        # weighting
        prob_all = {}
        for x in BEST_MOVES:
            prob_all[x] = 0.6 * prob_2nd[x] + 0.4 * prob_1st[x]

        # prediction
        ai_move = max(prob_all, key=lambda x: prob_all[x])
        final_move = BEST_MOVES[ai_move]
        MOVES.append(user_move)
        matrix_first_order[last_move][user_move] += 1
        matrix_second_order[last_two][user_move] += 1
        
        print(f"\nYOU: {user_move}, AI: {final_move}")
        
        if WINNING_CONDITIONS[user_move] == final_move:
            print("You Won")
            AI_LOSS += 1

        elif WINNING_CONDITIONS[final_move] == user_move:
            print("You Lost")
            AI_WINS += 1

        else:
            print("Draw")
            AI_DRAW += 1
        
        plays += 1
        print(f"AI Winrate: {AI_WINS / (AI_DRAW + AI_LOSS + AI_WINS):.2f}")
        print(f"counter: {plays}")

main()
