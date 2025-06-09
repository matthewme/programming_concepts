from pytest import fixture
from src.oop import Parent, Child


@fixture
def parent1():
    return Parent("Mom", 35)


@fixture
def child() -> Child:
    return Child("Kid", 3)


# Test case for creating an instance of Parent
def test_parent_initialization(parent1: Parent):
    # Test that the name and age are set correctly
    assert parent1.name == "Mom"
    assert parent1.age == 35


# Test case for the 'description' method
def test_parent_description_method(parent1: Parent):
    # Test that the description method returns the correct string
    assert parent1.description() == "Mom is 35 years old"


# Test case for the 'speak' method
def test_parent_speak_method(parent1: Parent):
    # Test that the speak method returns the correct string when a sound is provided
    assert parent1.speak("Hello!") == "Mom says Hello!"
    assert parent1.speak("Goodbye") == "Mom says Goodbye"


# Test case for the class attribute 'speaks'
def test_class_attribute_speaks(parent1: Parent):
    # Test that the class attribute 'speaks' is correct
    assert parent1.speaks == ["English"]

    # Modify the class attribute for a different instance
    stepMom = Parent("Step Mom", 40)
    assert stepMom.speaks == ["English"]  # Same class attribute for both instances

    # Check if changing the class attribute reflects for all instances
    Parent.speaks = ["English", "Spanish"]
    assert stepMom.speaks == ["English", "Spanish"]
    assert parent1.speaks == ["English", "Spanish"]


# Test case for creating an instance of child
def test_child_initialization(child: Child):
    # Test that the name and age are set correctly
    assert child.name == "Kid"
    assert child.age == 3


# Test case for the 'speak' method w/ inheritance
def test_child_speak_method_inheritance(child: Child):
    # Test speak method is inherited.
    assert child.speak("Hello!") == "Kid says Hello!"
    assert child.speak("Goodbye") == "Kid says Goodbye"


# Test case for the 'description' method polymorphism
def test_child_description_method_polymorphism(child: Child):
    # Test description method is morphed
    assert child.description() == "Kid is 3 years of age."
