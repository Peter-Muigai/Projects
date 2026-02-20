from abc import ABC, abstractmethod

class LockDoor(ABC):
    @abstractmethod
    def unlock(self, code):
        pass

class PinCode(LockDoor):
    def __init__(self, pin):
        self.__pin = pin

    def unlock(self, code):
        if code == self.__pin:
            print("Unlocked")
        else:
            print("Invalid pin!. Access Denied!!")

    def change_pin(self, new_pin):
        self.__pin = new_pin
        print("✅ PIN successfully changed.")

class SmartDoor:
    def __init__(self, lock: LockDoor):
        self.__lock = lock

    def try_unlock(self, code):
        self.__lock.unlock(code)

my_lock = PinCode("4321")

door = SmartDoor(my_lock)

door.try_unlock("1111")   # ❌
door.try_unlock("4321")   # ✅

# Change PIN and try again
my_lock.change_pin("2134")
door.try_unlock("1234")   # ❌ (this should say 1234 is wrong)
door.try_unlock("2134")   # ✅ (correct new pin)

