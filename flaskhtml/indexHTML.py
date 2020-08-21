class indexHTML:
    pageStr=""
    def __init__(self):
        with open('/root/covid19/flaskhtml/templates/index.html', 'r') as myfile:
            self.pageStr = myfile.read()
            #print(":"+pageStr)
    def __str__(self):
        #print(":"+self.pageStr)
        return self.pageStr


