CALL = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

TIEDCALL = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All"
        }

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score +=1
        else:
            self.player2_score +=1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._tied()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score_difference = self.player1_score - self.player2_score
            if abs(score_difference) == 1:
                return self._advantage(score_difference)
            elif abs(score_difference) >= 2:
                return self._win(score_difference)
        else:
            return self._regular_score()
        
    def _tied(self):
        if self.player1_score < 3:
            return f"{TIEDCALL[self.player1_score]}"
        else:
            return "Deuce"

    def _advantage(self, score_difference):
        if score_difference == 1:
            return  "Advantage player1"
        elif score_difference == -1:
            return  "Advantage player2"
    
    def _win(self, score_difference):
        if score_difference >= 2:
            return "Win for player1"
        elif score_difference <= -2:
            return "Win for player2"
    
    def _regular_score(self):
        return f"{CALL[self.player1_score]}-{CALL[self.player2_score]}"

    