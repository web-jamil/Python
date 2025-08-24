# import hashlib
# import json
# import os
# import random
# from abc import ABC, abstractmethod
# from getpass import getpass

# # Password Manager Module
# class PasswordManager:
#     def __init__(self, password_file="passwords.json"):
#         self.password_file = password_file
#         self.passwords = self._load_passwords()
        
#     def _load_passwords(self):
#         if os.path.exists(self.password_file):
#             with open(self.password_file, 'r') as f:
#                 return json.load(f)
#         return {}
    
#     def _save_passwords(self):
#         with open(self.password_file, 'w') as f:
#             json.dump(self.passwords, f)
    
#     def hash_password(self, password):
#         return hashlib.sha256(password.encode()).hexdigest()
    
#     def register_user(self, username, password):
#         if username in self.passwords:
#             return False
#         self.passwords[username] = self.hash_password(password)
#         self._save_passwords()
#         return True
    
#     def verify_user(self, username, password):
#         if username not in self.passwords:
#             return False
#         return self.passwords[username] == self.hash_password(password)

# # Game Module Interface
# class GameModule(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
#     @abstractmethod
#     def get_name(self):
#         pass

# # Concrete Game Modules
# class MathPuzzle(GameModule):
#     def get_name(self):
#         return "Math Puzzle"
    
#     def start(self):
#         print("\n=== Math Puzzle ===")
#         a, b = random.randint(1, 10), random.randint(1, 10)
#         answer = a + b
#         user_answer = input(f"What is {a} + {b}? ")
#         if int(user_answer) == answer:
#             print("Correct! You earned 10 points.")
#             return 10
#         print(f"Wrong! The correct answer was {answer}.")
#         return 0

# class WordScramble(GameModule):
#     def get_name(self):
#         return "Word Scramble"
    
#     def start(self):
#         print("\n=== Word Scramble ===")
#         words = ["python", "programming", "game", "module", "password"]
#         word = random.choice(words)
#         scrambled = ''.join(random.sample(word, len(word)))
#         print(f"Unscramble: {scrambled}")
#         user_guess = input("Your answer: ").lower()
#         if user_guess == word:
#             print("Correct! You earned 15 points.")
#             return 15
#         print(f"Wrong! The correct word was '{word}'.")
#         return 0

# class MemoryGame(GameModule):
#     def get_name(self):
#         return "Memory Game"
    
#     def start(self):
#         print("\n=== Memory Game ===")
#         sequence = [random.randint(1, 4) for _ in range(3)]
#         print("Memorize this sequence (you have 3 seconds):", sequence)
#         time.sleep(3)
#         os.system('cls' if os.name == 'nt' else 'clear')
#         user_input = input("Enter the sequence (space separated): ")
#         user_sequence = list(map(int, user_input.split()))
#         if user_sequence == sequence:
#             print("Perfect memory! You earned 20 points.")
#             return 20
#         print(f"Wrong! The sequence was {sequence}.")
#         return 0

# # Game Engine
# class GameEngine:
#     def __init__(self):
#         self.password_manager = PasswordManager()
#         self.modules = [
#             MathPuzzle(),
#             WordScramble(),
#             MemoryGame()
#         ]
#         self.scores = {}
    
#     def register(self):
#         print("\n=== Registration ===")
#         username = input("Choose a username: ")
#         password = getpass("Choose a password: ")
#         if self.password_manager.register_user(username, password):
#             print("Registration successful!")
#             self.scores[username] = 0
#             return True
#         print("Username already exists.")
#         return False
    
#     def login(self):
#         print("\n=== Login ===")
#         username = input("Username: ")
#         password = getpass("Password: ")
#         if self.password_manager.verify_user(username, password):
#             print("Login successful!")
#             if username not in self.scores:
#                 self.scores[username] = 0
#             return username
#         print("Invalid username or password.")
#         return None
    
#     def show_menu(self, username):
#         print(f"\nWelcome {username}! (Score: {self.scores[username]})")
#         print("Available Games:")
#         for i, module in enumerate(self.modules, 1):
#             print(f"{i}. {module.get_name()}")
#         print("0. Exit")
    
#     def run(self):
#         print("=== Game Portal ===")
#         current_user = None
        
#         while True:
#             if not current_user:
#                 print("\n1. Login")
#                 print("2. Register")
#                 print("0. Exit")
#                 choice = input("Select option: ")
                
#                 if choice == "1":
#                     current_user = self.login()
#                 elif choice == "2":
#                     self.register()
#                 elif choice == "0":
#                     break
#                 else:
#                     print("Invalid choice.")
#                 continue
            
#             self.show_menu(current_user)
#             choice = input("Select game: ")
            
#             if choice == "0":
#                 current_user = None
#                 continue
            
#             try:
#                 game_index = int(choice) - 1
#                 if 0 <= game_index < len(self.modules):
#                     points = self.modules[game_index].start()
#                     self.scores[current_user] += points
#                 else:
#                     print("Invalid choice.")
#             except ValueError:
#                 print("Please enter a number.")

# # Main Execution
# if __name__ == "__main__":
#     import time
#     engine = GameEngine()
#     engine.run()
    
    
    
    
import hashlib
import json
import os
import random
import time
import importlib
import inspect
from abc import ABC, abstractmethod
from getpass import getpass
from dataclasses import dataclass
from typing import Dict, List, Type, Optional
from pathlib import Path

## --------------------------
## Core Infrastructure Modules
## --------------------------

@dataclass
class PlayerProfile:
    username: str
    score: int = 0
    level: int = 1
    achievements: List[str] = None
    inventory: Dict[str, int] = None
    
    def __post_init__(self):
        if self.achievements is None:
            self.achievements = []
        if self.inventory is None:
            self.inventory = {}

class ModuleLoader:
    @staticmethod
    def discover_modules(module_dir="game_modules"):
        """Dynamically load all game modules from specified directory"""
        modules = []
        module_path = Path(module_dir)
        
        if not module_path.exists():
            module_path.mkdir()
            return modules
            
        for file in module_path.glob("*.py"):
            if file.name.startswith("_"):
                continue
                
            module_name = file.stem
            try:
                spec = importlib.util.spec_from_file_location(
                    f"game_modules.{module_name}", file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                for name, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and issubclass(obj, GameModule) and obj != GameModule):
                        modules.append(obj())
            except Exception as e:
                print(f"Error loading module {module_name}: {e}")
                
        return modules

class PasswordManager:
    def __init__(self, data_dir="user_data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
    def _get_user_file(self, username):
        return self.data_dir / f"{username}.json"
    
    def hash_password(self, password, salt=None):
        salt = salt or os.urandom(16).hex()
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        ).hex(), salt
    
    def register_user(self, username, password, email=None):
        user_file = self._get_user_file(username)
        if user_file.exists():
            return False, "Username already exists"
            
        password_hash, salt = self.hash_password(password)
        
        profile = {
            "username": username,
            "password_hash": password_hash,
            "salt": salt,
            "email": email,
            "created": time.time(),
            "last_login": None
        }
        
        with open(user_file, 'w') as f:
            json.dump(profile, f)
            
        return True, "Registration successful"
    
    def verify_user(self, username, password):
        user_file = self._get_user_file(username)
        if not user_file.exists():
            return False, "Invalid username or password"
            
        with open(user_file, 'r') as f:
            profile = json.load(f)
            
        test_hash, _ = self.hash_password(password, profile['salt'])
        if test_hash != profile['password_hash']:
            return False, "Invalid username or password"
            
        # Update last login time
        profile['last_login'] = time.time()
        with open(user_file, 'w') as f:
            json.dump(profile, f)
            
        return True, "Login successful"
    
    def load_profile(self, username):
        user_file = self._get_user_file(username)
        if not user_file.exists():
            return None
            
        with open(user_file, 'r') as f:
            data = json.load(f)
            
        player_file = self.data_dir / f"{username}_player.json"
        if player_file.exists():
            with open(player_file, 'r') as f:
                player_data = json.load(f)
        else:
            player_data = {}
            
        return PlayerProfile(
            username=username,
            score=player_data.get('score', 0),
            level=player_data.get('level', 1),
            achievements=player_data.get('achievements', []),
            inventory=player_data.get('inventory', {})
        )
    
    def save_profile(self, profile):
        player_file = self.data_dir / f"{profile.username}_player.json"
        data = {
            'score': profile.score,
            'level': profile.level,
            'achievements': profile.achievements,
            'inventory': profile.inventory
        }
        with open(player_file, 'w') as f:
            json.dump(data, f)

## --------------------------
## Game Module Architecture
## --------------------------

class GameModule(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Display name of the game"""
        pass
    
    @property
    @abstractmethod
    def version(self) -> str:
        """Module version"""
        pass
    
    @property
    def required_level(self) -> int:
        """Minimum player level required to play"""
        return 1
    
    @property
    def cost(self) -> Dict[str, int]:
        """Resources needed to play this game"""
        return {}
    
    @property
    def rewards(self) -> Dict[str, int]:
        """Potential rewards from this game"""
        return {'points': 10}
    
    @abstractmethod
    def start(self, profile: PlayerProfile) -> Dict[str, int]:
        """Main game execution"""
        pass
    
    def can_play(self, profile: PlayerProfile) -> bool:
        """Check if player meets requirements to play"""
        if profile.level < self.required_level:
            return False
            
        for item, quantity in self.cost.items():
            if profile.inventory.get(item, 0) < quantity:
                return False
                
        return True
    
    def get_requirements(self) -> str:
        """Human-readable requirements"""
        reqs = []
        if self.required_level > 1:
            reqs.append(f"Level {self.required_level}+")
            
        for item, quantity in self.cost.items():
            reqs.append(f"{quantity} {item}")
            
        return ", ".join(reqs) if reqs else "None"

class ModuleDecorator(GameModule):
    """Base class for module decorators/wrappers"""
    def __init__(self, module: GameModule):
        self._module = module
    
    @property
    def name(self):
        return self._module.name
    
    @property
    def version(self):
        return self._module.version
    
    @property
    def required_level(self):
        return self._module.required_level
    
    @property
    def cost(self):
        return self._module.cost
    
    @property
    def rewards(self):
        return self._module.rewards
    
    def start(self, profile):
        return self._module.start(profile)
    
    def can_play(self, profile):
        return self._module.can_play(profile)
    
    def get_requirements(self):
        return self._module.get_requirements()

class TimedGameDecorator(ModuleDecorator):
    """Adds time limit to a game module"""
    def __init__(self, module: GameModule, time_limit: int = 30):
        super().__init__(module)
        self.time_limit = time_limit
    
    @property
    def name(self):
        return f"Timed {self._module.name} ({self.time_limit}s)"
    
    def start(self, profile):
        print(f"You have {self.time_limit} seconds to complete this challenge!")
        start_time = time.time()
        
        result = self._module.start(profile)
        
        time_taken = time.time() - start_time
        if time_taken > self.time_limit:
            print(f"Time's up! You took {time_taken:.1f}s (limit: {self.time_limit}s)")
            return {'penalty': 5}
        
        print(f"Completed in {time_taken:.1f}s! Bonus for speed!")
        result['points'] = result.get('points', 0) + int(5 * (1 - time_taken/self.time_limit))
        return result

## --------------------------
## Sample Game Modules
## --------------------------

class MathPuzzle(GameModule):
    @property
    def name(self):
        return "Math Puzzle"
    
    @property
    def version(self):
        return "1.2"
    
    @property
    def rewards(self):
        return {'points': random.randint(5, 15), 'coins': 1}
    
    def start(self, profile):
        print("\n=== Math Puzzle ===")
        difficulty = min(10, profile.level)
        a = random.randint(1, difficulty * 2)
        b = random.randint(1, difficulty * 2)
        op = random.choice(['+', '-', '*'])
        
        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        else:
            answer = a * b
            
        user_answer = input(f"What is {a} {op} {b}? ")
        
        try:
            if int(user_answer) == answer:
                print("Correct!")
                return self.rewards
            print(f"Wrong! The answer was {answer}.")
            return {'points': 1}  # Participation points
        except ValueError:
            print("Invalid input - no points awarded")
            return {}

class MemoryGame(GameModule):
    @property
    def name(self):
        return "Memory Challenge"
    
    @property
    def version(self):
        return "1.3"
    
    @property
    def required_level(self):
        return 3
    
    @property
    def cost(self):
        return {'coins': 2}
    
    @property
    def rewards(self):
        return {'points': 25, 'coins': random.randint(0, 5), 'memory_token': 1}
    
    def start(self, profile):
        print("\n=== Memory Challenge ===")
        seq_length = min(10, 3 + profile.level // 2)
        sequence = [random.randint(0, 9) for _ in range(seq_length)]
        
        print("Memorize this sequence (5 seconds):", sequence)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        user_input = input("Enter the sequence (space separated): ")
        user_sequence = list(map(int, user_input.split()))
        
        if user_sequence == sequence:
            print("Perfect memory!")
            return self.rewards
        
        print(f"Wrong! The sequence was {sequence}.")
        return {'points': 5}  # Partial credit

## --------------------------
## Game Engine Core
## --------------------------

class GameEngine:
    def __init__(self):
        self.password_manager = PasswordManager()
        self.modules = ModuleLoader.discover_modules()
        self.current_player = None
        self.session_stats = {
            'games_played': 0,
            'points_earned': 0,
            'modules_loaded': len(self.modules)
        }
        
        # Decorate some modules for variety
        if len(self.modules) > 1:
            self.modules[1] = TimedGameDecorator(self.modules[1], 45)
    
    def register(self):
        print("\n=== Registration ===")
        username = input("Username: ").strip()
        email = input("Email (optional): ").strip() or None
        password = getpass("Password: ")
        confirm = getpass("Confirm password: ")
        
        if password != confirm:
            print("Passwords don't match!")
            return False
            
        success, message = self.password_manager.register_user(username, password, email)
        print(message)
        return success
    
    def login(self):
        print("\n=== Login ===")
        username = input("Username: ").strip()
        password = getpass("Password: ")
        
        success, message = self.password_manager.verify_user(username, password)
        print(message)
        if success:
            self.current_player = self.password_manager.load_profile(username)
            return True
        return False
    
    def logout(self):
        if self.current_player:
            self.password_manager.save_profile(self.current_player)
            print(f"\nGoodbye {self.current_player.username}! Your progress has been saved.")
            self.current_player = None
    
    def show_main_menu(self):
        print("\n=== Game Portal ===")
        if self.current_player:
            print(f"Logged in as: {self.current_player.username}")
            print(f"Level: {self.current_player.level} | Score: {self.current_player.score}")
            print("1. Play Games")
            print("2. View Profile")
            print("3. Logout")
        else:
            print("1. Login")
            print("2. Register")
        print("0. Exit")
    
    def show_game_menu(self):
        print(f"\n=== Game Selection ===")
        print(f"Player: {self.current_player.username} (Level {self.current_player.level})")
        print("Available Games:")
        
        for i, module in enumerate(self.modules, 1):
            status = "✓" if module.can_play(self.current_player) else "✗"
            print(f"{i}. {module.name} {status} (Req: {module.get_requirements()})")
        print("0. Back")
    
    def play_game(self, module_index):
        module = self.modules[module_index]
        
        if not module.can_play(self.current_player):
            print("\nYou don't meet the requirements for this game!")
            print(f"Needed: {module.get_requirements()}")
            return
            
        print(f"\nStarting: {module.name}")
        print(f"Possible rewards: {module.rewards}")
        
        # Deduct costs
        for item, quantity in module.cost.items():
            self.current_player.inventory[item] = self.current_player.inventory.get(item, 0) - quantity
            
        # Play the game
        result = module.start(self.current_player)
        
        # Apply rewards
        self.session_stats['games_played'] += 1
        points_earned = result.get('points', 0)
        self.current_player.score += points_earned
        self.session_stats['points_earned'] += points_earned
        
        for item, quantity in result.items():
            if item != 'points':
                self.current_player.inventory[item] = self.current_player.inventory.get(item, 0) + quantity
                
        # Check for level up
        if self.current_player.score >= self.current_player.level * 100:
            self.current_player.level += 1
            print(f"\nLEVEL UP! You are now level {self.current_player.level}!")
    
    def view_profile(self):
        p = self.current_player
        print(f"\n=== Player Profile ===")
        print(f"Username: {p.username}")
        print(f"Level: {p.level}")
        print(f"Score: {p.score}")
        print("\nInventory:")
        for item, quantity in p.inventory.items():
            print(f"- {item}: {quantity}")
        print("\nAchievements:")
        for ach in p.achievements:
            print(f"- {ach}")
        if not p.achievements:
            print("None yet - keep playing!")
    
    def run(self):
        while True:
            self.show_main_menu()
            choice = input("Select option: ").strip()
            
            if not self.current_player:
                # Not logged in options
                if choice == "1":
                    if self.login():
                        continue
                elif choice == "2":
                    self.register()
                elif choice == "0":
                    break
                else:
                    print("Invalid choice")
                continue
                
            # Logged in options
            if choice == "1":
                while True:
                    self.show_game_menu()
                    game_choice = input("Select game: ").strip()
                    
                    if game_choice == "0":
                        break
                        
                    try:
                        idx = int(game_choice) - 1
                        if 0 <= idx < len(self.modules):
                            self.play_game(idx)
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a number")
            elif choice == "2":
                self.view_profile()
            elif choice == "3":
                self.logout()
            elif choice == "0":
                self.logout()
                break
            else:
                print("Invalid choice")
        
        print("\nSession Summary:")
        print(f"- Games Played: {self.session_stats['games_played']}")
        print(f"- Points Earned: {self.session_stats['points_earned']}")
        print(f"- Modules Available: {self.session_stats['modules_loaded']}")
        print("Thank you for playing!")

## --------------------------
## Main Execution
## --------------------------

if __name__ == "__main__":
    # Create sample modules directory if it doesn't exist
    modules_dir = Path("game_modules")
    modules_dir.mkdir(exist_ok=True)
    
    # Create sample module if none exist
    if not list(modules_dir.glob("*.py")):
        sample_module = modules_dir / "sample_game.py"
        with open(sample_module, 'w') as f:
            f.write('''from game_framework import GameModule

class SampleGame(GameModule):
    @property
    def name(self):
        return "Sample Game"
    
    @property
    def version(self):
        return "1.0"
    
    def start(self, profile):
        print("\\n=== Sample Game ===")
        print("This is a sample game module!")
        answer = input("What's your favorite color? ")
        print(f"{answer} is a nice color! Here's 5 points.")
        return {'points': 5}
''')
    
    engine = GameEngine()
    engine.run()