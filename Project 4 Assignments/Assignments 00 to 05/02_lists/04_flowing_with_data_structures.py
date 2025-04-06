"""
In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside

a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. 

This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. 

Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

Here is an example run of this program (user input in bold italics):

Enter a message to copy: Hello world!

List before: []

List after: ['Hello world!', 'Hello world!', 'Hello world!']

(Note. The concept of immutable/mutable data types is called mutability. Be careful because different programming languages have different rules regarding mutability!)

"""


# 1
def add_three_copies(lst, data):
    """Yeh function list ko modify karega bina return kiye"""
    lst.append(data)
    lst.append(data)
    lst.append(data)
    # Function add_three_copies(lst, data)
    # Ye function ek list lst ko modify karega bina return kiye.
    # Ye function 3 baar data ko lst me append karega.

def main():
    message = input("Enter a message to copy: ")
    # 🔹 User se input lena
    # User se input lena
    # message = input("Enter a message to copy: ")
    # Suppose user input kare "Hello world!".

    my_list = []
    # 🔹 Empty list banani
    # my_list = [] (Ye ek khaali list hai)

    print("List before:", my_list) 
    # Output print karna


    add_three_copies(my_list, message)
    # 🔹 Function call karna (yeh asli list ko modify karega)
    # Function ko call karna
    # add_three_copies(my_list, message)
    # Ye asal list ko modify karega, kyunki lists mutable hoti hain.

    print("List after:", my_list)
    # Output print karna

if __name__ == '__main__':
    main()
    # Yeh line ensure karti hai ke jab script direct run ho, tab main() function execute ho.





# 2
def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()

