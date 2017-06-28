import urllib.request


class DataRetrieve:

    def __init__(self, url="https://www.digikala.com"):
        fp = urllib.request.urlopen(url)

        source_code = fp.read()
        self.html_string = source_code.decode("utf8")

        fp.close()
