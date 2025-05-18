class GoalSystem:
    def __init__(self):
        self.goals = ["stay active", "learn", "avoid failure"]

    def update_goals(self, emotions):
        if emotions["fear"] > 0.7:
            self.goals.append("stay safe")

    def get_top_goal(self):
        return self.goals[0]
