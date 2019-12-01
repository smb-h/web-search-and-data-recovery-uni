from time import sleep


def search_it():
    pass


def main():

    print("Developed by SMBH ;))")
    sleep(.5)
    print("enter 0 to exit the app...")
    sleep(.3)
    print("otherwise")

    # input loop breaks on 0
    while True:
        tmp = input("Search : ")
        if tmp == "0":
            break
        else:
            search_it(tmp)




if __name__ == "__main__":
    main()

