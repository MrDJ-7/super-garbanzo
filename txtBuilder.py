import builder

class TxtBuilder(builder.Builder):
    def Write(text):
        f = open("log.txt", "a")
        for word in text:
            f.write(word)
        f.write("\n")
        f.close()