import builder

class HtmlBuilder(builder.Builder):
    def Write(text):
        f = open("log.html", "a")
        for word in text:
            f.write(word)
        f.write("\n")
        f.close()
