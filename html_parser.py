from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.discountList = []
        self.inDiscountSection = False
        self.inDiscountSpan = False
        self.inProductItemSection = False
        self.inProductItemSpan = False
        self.tempUrl = None
        self.tempHref = None

    def handle_starttag(self, tag, attributes):
        if tag != 'span' and tag != 'a':
            return
        elif tag == 'a':
            for key, value in attributes:
                if key == 'class' and value == 'slideItem':
                    self.inDiscountSection = True
                elif key == 'class' and value == 'productItem':
                    self.inProductItemSection = True
                elif key == 'href':
                    self.tempHref = value

            if self.inDiscountSection or self.inProductItemSection:
                self.tempUrl = self.tempHref

        elif tag == 'span':
            for key, value in attributes:
                if self.inDiscountSection and key == 'class' and value == 'price-final':
                    self.inDiscountSpan = True
                    break
                elif self.inProductItemSection and key == 'class' and value == 'final-price':
                    self.inProductItemSpan = True
                    break

    def handle_endtag(self, tag):
        if tag == 'a' and self.inDiscountSection:
            self.inDiscountSection = False
        elif tag == 'span' and self.inDiscountSpan:
            self.inDiscountSpan = False
        elif tag == 'a' and self.inProductItem:
            self.inProductItemSection = False

    def handle_data(self, data):
        if self.inDiscountSection and self.inDiscountSpan:
            self.discountList.append((self.tempUrl, data))
        elif self.inProductItemSection and self.inProductItemSpan:
            self.discountList.append((self.tempUrl, data))
