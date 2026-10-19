while True:
    answer = input("Wer wurde 2026 Fussball Weltmeister? ")
    if answer.strip().lower() == "spanien":
        print("Gratulation, du hast richtig geantwortet!")
        break
    else:
        print("Tut mir leid, leider falsch. Versuch es nochmal.")
