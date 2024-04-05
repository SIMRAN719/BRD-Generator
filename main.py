from app import generate_brd

if __name__ == "__main__":
    text = "The system shall allow users to log in using their email and password."
    result = generate_brd(text)
    print(result)


    