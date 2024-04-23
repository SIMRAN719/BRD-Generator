from Application.brd import BRD_Generator

if __name__ == "__main__":
    text = "Face Recognition System"
    result = BRD_Generator(text)
    print(result.generate_brd())
