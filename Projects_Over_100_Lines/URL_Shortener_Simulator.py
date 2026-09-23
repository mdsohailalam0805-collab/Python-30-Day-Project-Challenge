import random
import string

urls = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    
    short_code = ""
    
    for i in range(6):
        short_code += random.choice(characters)
        
    return short_code


def create_short_url():
    original_url = input("Enter Your URl:")
    
    short_code = generate_short_code()
    
    urls[short_code] = original_url
    
    print("\n=====SHORT URL CREATED=====")
    print(f" original Url : {original_url}")
    print(f"Short Code : {short_code}")
    print(f" Short Url : short.ly/{short_code}" )
    print("-------------------------------------")
    
    
def open_short_url():
    short_code = input("Enter short Code:")
    
    if short_code in urls:
        original_url = urls[short_code]
    
        print("\n=====ORIGINAL URL=====")
        print(f"Short Code : {short_code}")
        print(f"Original Url : {original_url}")
        print("-------------------------------")
        
    else:
        print("\n Short code not found!")
        
        
def view_all_urls():
    if not urls:
        print("\n No Urls Available!")
        return
    
    print("=====ALL SHORTENED URLs=====")
    
    for short_code, original_url in urls.items():
        print(f"Short Code : {short_code}")
        print(f"Original URL : {original_url}")
        print(f"Short URL : short.ly/{short_code}")
        print("------------------------------------")
        

def delete_short_url():
    short_code = input("Enter short code to delete:")
    
    if short_code in urls:
        del urls[short_code] 
        
        print("\n Short Url deleted Successfully!")
        print("-------------------------------------")
        
    else:
        print("\n Short Code Not Found!") 
        
def main_menu():
    
    while True:
        
        print("\n===== URL SHORTENER =====")
        print("1. Create Short URL")
        print("2. Open Short URL")
        print("3. View All URLs")
        print("4. Delete Short URL")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            create_short_url()

        elif choice == "2":
            open_short_url()

        elif choice == "3":
            view_all_urls()

        elif choice == "4":
            delete_short_url()

        elif choice == "5":
            print("\nThank You For Using This Application!")
            break

        else:
            print("\nInvalid Choice, Try Again!")


main_menu()