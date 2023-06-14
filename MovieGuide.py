with open("movies.txt", "w") as file:
    file.write("Cat on a Hot Tin Roof\n")
    file.write("On the Waterfront\n")
    file.write("Monty Python and the Holy Grail to the file\n")

    def display_menu():
        print(" === Movie List Progam ===")
        print("1. Display all movie titles")
        print("2. Add a movie title")
        print("3. Delete a movie title")
        print("4. Exit")

   
    def load_movie_titles():
        movie_titles = []
        with open("movies.txt", "r") as file:
            for line in file:
                movie_titles.append(line.strip())
                return movie_titles


    def display_titles(movie_list):
        print(" === Movie title === ")
        for title in movie_list:
            print(title)
            
    def add_title(movie_list):
       new_title = input("Enter a new movie title: ")
       movie_list.append(new_title)
       with open("movies.txt", "w") as file:
           for title in movie_list:
              file.write(title + "\n")
       print("Title added successfully")
       
    def delete_title(movie_list):
        display_titles(movie_list)
        try:
            index = int(input("Enter the nnumber of the title to delete: ")) - 1
            if 0 <= index < len(movie_list):
                deleted_title = movie_list.pop(index)
                with open("movies.txt", "w") as file:
                    for title in movie_list:
                        file.write(title + "\n")
                print(f"{delete_title} deleted successfully")
            else:
                print("Invalid number. No title deleted")
        except ValueError:
            print("Invalid input. No title deleted")

    def main():
        movie_list = load_movie_titles()
        while True:
            display_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                display_titles(movie_list)
            elif choice == "2":
                add_title(movie_list)
            elif choice == "3":
                delete_title(movie_list)
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid command. Please try again.")
main()




