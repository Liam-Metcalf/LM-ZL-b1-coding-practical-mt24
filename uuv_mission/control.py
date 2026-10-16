class PDController:
    def __init__(self) -> None:
        self.kp = 0.15
        self.kd = 0.6
        self.previous_error = 0.0

    def compute_action(self, current_error: float) -> float:
        action = self.kp * current_error + self.kd * (current_error - self.previous_error)
        self.previous_error = current_error
        return action

    def reset(self) -> None:
        self.previous_error = 0