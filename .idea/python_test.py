import unittest
import python_test_func

# юнит тест функции
class TestUpper(unittest.TestCase):
    """docstring for ClassName"""
    def test_one_word(self):
        number = 3
        result = python_test_func.square(number)
        self.assertEqual(result, 9)
        self.assertNotEqual(result, 6)

class CoolGameFunctionsTest(unittest.TestCase):

    def test_greet(self):
        """greet() have to return 'How are you?' if isEnemy == False"""
        self.assertEqual(python_test_func.greet('Jack', False), 'Hello Jack! How are you?')

    def test_greet_enemy(self):
        """greet() have to return 'I will kill you, bastard!' if isEnemy == True"""
        self.assertEqual(python_test_func.greet('Ivan', True), 'Hello Ivan! I will kill you, bastard!')

    def test_greet_enemy_boolean(self):
        with self.assertRaises(ValueError):
            python_test_func.greet('Ivan', 'Bla-bla')

    def test_eat_burgers(self):
        """eat_burgers() have to return 'Mmm! That was excellent!' if number <= 3"""
        self.assertEqual(python_test_func.eat_burgers(3), 'Mmm! That was excellent!')

    def test_eat_too_much_burgers(self):
        """eat_burgers() have to return 'Oh! I overate!' if number > 3"""
        self.assertEqual(python_test_func.eat_burgers(4), 'Oh! I overate!')

    def test_can_fly_batman(self):
        """Test comment: Batman have to be able to fly"""
        self.assertTrue(python_test_func.can_fly('Batman'), 'Batman have to be able to fly')

    def test_can_fly_anyone_else(self):
        self.assertEqual(python_test_func.can_fly('Bob'), False)
        self.assertEqual(python_test_func.can_fly('Jim'), False)
        self.assertEqual(python_test_func.can_fly('Kevin'), False)
    # self.assertFalse(python_test_func.can_fly('Bob'), 'Anyone else have to not be able to fly')
    # self.assertFalse(python_test_func.can_fly('Jim'), 'Anyone else have to not be able to fly')
    # self.assertFalse(python_test_func.can_fly('Kevin'), 'Anyone else have to not be able to fly')

    def test_get_arsenal(self):
        self.assertIn(python_test_func.get_arsenal(), ('knife', 'handgun', 'machine gun'))

class ShooterTest(unittest.TestCase):

    mock_data = []

    # setUp() - runs before each test method
    # tearDown() - runs after each test method
    def setUp(self):
        self.jake = python_test_func.Shooter('Jake')
        print(self.mock_data)
        self.mock_data = [1, 2, 3, 4, 5]

    def tearDown(self):
        print(self.mock_data)
        self.mock_data = []

    def test_get_cash(self):
        # jake = Shooter('Jake')
        self.jake.get_cash(500)
        self.assertEqual(self.jake.money, 1500)
        print(self.mock_data)

    def test_greet(self):
        # jake = Shooter('Jake')
        self.assertEqual(self.jake.greet(), 'Hello! How are you?')
        self.jake.money = 50
        self.assertEqual(self.jake.greet(), 'Hello! I need cash!')

if __name__ == "__main__":
    unittest.main()
