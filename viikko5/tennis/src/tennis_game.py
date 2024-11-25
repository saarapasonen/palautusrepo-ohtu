class TennisGame:
    score_names = ["Love", "Fifteen", "Thirty", "Forty"]
    deuce_threshold = 3
    win_advantage_threshold = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

#useampiin pienempiin metodeihin tästä eteenpäin että ymmärtää koodia

    def get_score(self):
        if self.is_tied():
            return self.get_tied_score()
        if self.is_endgame():
            return self.get_endgame_score()
        return self.get_running_score()

    def is_tied(self):
        return self.player1_score == self.player2_score

    def is_endgame(self):
        return self.player1_score >= self.win_advantage_threshold or self.player2_score >= self.win_advantage_threshold

    def get_tied_score(self):
        if self.player1_score >= self.deuce_threshold:
            return "Deuce"
        return f"{self.score_names[self.player1_score]}-All"

    def get_endgame_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        if score_difference == -1:
            return f"Advantage {self.player2_name}"
        if score_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def get_running_score(self):
        player1_score_name = self.score_names[self.player1_score]
        player2_score_name = self.score_names[self.player2_score]
        return f"{player1_score_name}-{player2_score_name}"