from abc import ABC, abstractmethod

# Abstract class — Abstraction
class LockDevice(ABC):
    @abstractmethod
    def unlock(self, code):
        pass

# Concrete class — with Encapsulation
class PinCodeLock(LockDevice):
    def __init__(self, pin):
        self.__pin = pin  # Encapsulated (private) PIN

    def unlock(self, code):
        if code == self.__pin:
            print("✅ Door unlocked!")
        else:
            print("❌ Invalid PIN. Access denied.")

    def change_pin(self, new_pin):
        self.__pin = new_pin
        print("✅ PIN successfully changed.")

class SmartDoor:
    def __init__(self, lock: LockDevice):
        self.__lock = lock  # Encapsulated lock

    def try_unlock(self, code):
        self.__lock.unlock(code)

# Create a lock
my_lock = PinCodeLock("1234")

# Attach to the smart door
door = SmartDoor(my_lock)

# Try to unlock with wrong and right codes
door.try_unlock("1111")   # ❌
door.try_unlock("1234")   # ✅

# Change PIN and try again
my_lock.change_pin("4321")
door.try_unlock("1234")   # ❌
door.try_unlock("4321")   # ✅
