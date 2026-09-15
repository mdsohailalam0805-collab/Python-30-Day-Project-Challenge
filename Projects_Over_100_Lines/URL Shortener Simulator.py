import random
import string

urls = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    
    short_code = " "
    
    for i in range(6):
        short_code += random_choice(characters)
        
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
        print("/n No Urls Available!")
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
        
        print("1.Generate Short Code")
        print("2. Create Short URL")
        print("3. Open Short Url")
        print("4. View All Urls")
        print("5. Delete Short Url")
        print("6. Exit")
        
        choice = input("Enter Your Choice:")
        
        if choice == "1":
            generate_short_code()
            
        elif choice == "2":
            create_short_url()
            
        elif choice == "3":
            open_short_url()
            
        elif choice == "4":
            view_all_urls()
            
        elif choice == "5":
            delete_short_url()
            
        elif choice == "6":
            print("\n Thank You For Using This Application!")
            break
        
        else:
            print("Invalid Choice , Try Again!")
main_menu()