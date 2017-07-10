import urllib
import ssl


class DataRetrieve:

    def __init__(self, url="https://www.digikala.com"):

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        # fp = urllib.urlopen(url)
        fp = urllib.urlopen(url, context=ctx)

        source_code = fp.read()
        self.html_string = source_code.decode("utf8")

        fp.close()
