from random import choice


class RandomWalk:
    """Class to randomly walk in different directions."""

    def __init__(self, amount_of_steps=5000):
        """Initializes the random walk class."""
        self.amount_of_steps = amount_of_steps
        self.x_values = [0]
        self.y_values = [0]

    def walk(self):
        """Moves the character in any direction."""
        while len(self.x_values) < self.amount_of_steps:
            x_walk = self.get_steps()
            y_walk = self.get_steps()

            if x_walk == 0 and y_walk == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_walk)
            self.y_values.append(self.y_values[-1] + y_walk)

    def get_steps(self):
        """Calculates the number of steps to take in a particular direction and returns the value."""
        direction = choice([-1, 1])
        moves = choice([0, 1, 2, 3, 4])
        steps = direction * moves
        return steps
