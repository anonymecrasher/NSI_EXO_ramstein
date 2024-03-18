
class item:
    
    def __init__(self):
        self.a = "a"
        self.b = "b"
        self.c = "c"
        
    def __str__(self):
        return f"{self.a},{self.b},{self.c}"
def main():
    it = item()
    print(it)
    
if __name__ == '__main__':
    main()
