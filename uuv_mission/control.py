class PDController:
    """A discrete time proportional-derivative controller for submarine depth-control.

    Attributes:
        kp: Proportional gain
        kd: Derivative gain
        previous_error: Error signal at the previous time step which starts at 0.0
    """

    def __init__(self) -> None:
        self.kp = 0.15
        self.kd = 0.6
        self.previous_error = 0.0

    def compute_action(self, current_error: float) -> float:
        """Computes the control action at the current timestep using discrete PD control with the
        previous stored error and updates it.

        Args:
            current_error: Error (reference - observation depth) at the current timestep

        Returns:
            Computed control action which is input to the plant
        """
        action = self.kp * current_error + self.kd * (current_error - self.previous_error)
        self.previous_error = current_error
        return action

    def reset(self) -> None:
        """Resets the previous error to 0.0 and should be called before each new simulation."""
        self.previous_error = 0.0
