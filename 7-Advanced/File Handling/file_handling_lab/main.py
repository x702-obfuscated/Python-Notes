'''
File Handling Lab

'''

from datetime import datetime

def log(filepath:str, message:str) -> None:
    with open(filepath, "a") as file:
        file.write(f"{message}\n")   


def main():
    try:
        with open("example.txt", "x") as file:
            file.write("File Created Successfully!")
    except FileExistsError:
        log("lab.log",f"{datetime.now()}: File Already Exists.")


if __name__ == "__main__":
    main()