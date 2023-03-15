import random 
import string

class Password():
    def __init__(self, lenght):
        self.lenght = lenght
    
    # generate method 
    def generate(self):
        result_str = ''
        letters = string.ascii_letters + string.digits + string.punctuation
        for i in range(0, self.lenght):
            ctrl_str = random.choice(letters)
            result_str += ctrl_str 
        print("Secure Random Password of lenght", self.lenght, "is", result_str)