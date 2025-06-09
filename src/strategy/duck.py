from abc import ABC, abstractmethod

# --- Behavior Interfaces (Abstract Base Classes) ---
# These define the 'contracts' for different behaviors


class FlyBehavior(ABC):
    """Abstract Base Class for flying behaviors."""

    @abstractmethod
    def fly(self):
        """Method to implement flying action."""
        pass


class QuackBehavior(ABC):
    """Abstract Base Class for quacking behaviors."""

    @abstractmethod
    def quack(self):
        """Method to implement quacking action."""
        pass


# --- Concrete Fly Behaviors ---
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!")


class NoFly(FlyBehavior):
    def fly(self):
        print("I can't fly.")


class RocketPoweredFly(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


# --- Concrete Quack Behaviors ---
class Quack(QuackBehavior):
    def quack(self):
        print("Quack!")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak!")


# --- Duck Abstract Base Class ---
# This class acts as the context for the behaviors


class Duck(ABC):
    """
    Abstract base class for all ducks, demonstrating the Strategy Pattern.
    Behaviors (fly and quack) are delegated to separate objects.
    """

    def __init__(self):
        # These will be assigned concrete behavior objects
        self.fly_behavior: FlyBehavior
        self.quack_behavior: QuackBehavior

    def set_fly_behavior(self, fb: FlyBehavior):
        """Sets the duck's flying behavior."""
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        """Sets the duck's quacking behavior."""
        self.quack_behavior = qb

    @abstractmethod
    def display(self):
        """Abstract method that concrete duck types must implement to display themselves."""
        pass

    def perform_fly(self):
        """Delegates the fly action to the assigned fly behavior object."""
        if self.fly_behavior:
            self.fly_behavior.fly()
        else:
            print("No fly behavior set.")

    def perform_quack(self):
        """Delegates the quack action to the assigned quack behavior object."""
        if self.quack_behavior:
            self.quack_behavior.quack()
        else:
            print("No quack behavior set.")

    def swim(self):
        """A concrete method common to all ducks."""
        print("All ducks float, even decoys!")


# --- Concrete Duck Implementations ---


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()  # Default behaviors
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck.")


class RedheadDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()  # Default behaviors
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a Redhead duck.")


class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = NoFly()  # Specific behaviors for a rubber duck
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm a rubber duckie.")


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = NoFly()  # Specific behaviors for a decoy duck
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a decoy duck.")


# --- Testing the Ducks ---
if __name__ == "__main__":
    print("--- Mallard Duck ---")
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_fly()
    mallard.perform_quack()
    mallard.swim()

    print("\n--- Rubber Duck ---")
    rubber_duckie = RubberDuck()
    rubber_duckie.display()
    rubber_duckie.perform_fly()
    rubber_duckie.perform_quack()
    rubber_duckie.swim()

    print("\n--- Dynamic Behavior Change (Model Duck) ---")

    # Let's create a 'model duck' that can change its behavior
    class ModelDuck(Duck):
        def __init__(self):
            super().__init__()
            self.fly_behavior = NoFly()  # Starts with no flying
            self.quack_behavior = Quack()

        def display(self):
            print("I'm a model duck.")

    model = ModelDuck()
    model.display()
    model.perform_fly()  # Can't fly initially
    model.set_fly_behavior(RocketPoweredFly())  # Give it rocket power!
    model.perform_fly()  # Now it flies with a rocket!
    model.perform_quack()
