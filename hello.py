# hello.py

def greet_user(name):
    """Kullanıcıya özel bir selamlaşma mesajı verir."""
    print(f"Hello, {name}! Welcome to the GitHub project.")

def main():
    """Ana fonksiyon: kullanıcıdan isim alır ve selamlaşma yapar."""
    name = input("Please enter your name: ")
    greet_user(name)

if __name__ == "__main__":
    main()
