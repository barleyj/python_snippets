import html_formatter

class Formattable:
    formatFunction = 'object'
    def format_object(self, visitor):
        format = getattr(visitor, self.formatFunction)
        return format(self)

class Word(Formattable):
    formatFunction = 'formatWord'
    word = 'BIRD!!!'
    
class WordCloud(Formattable):
    name = 'Fake Name'
    formatFunction = 'formatWordCloud'
    words = [Word()]
    
class OtherWordCloud(WordCloud):
    name = 'Other fake name'

class HtmlFormatter:
    def formatWord(self, word):
        return '<span title="{0}">{1}</span>'.format(word.word, word.word)
    
    def formatWordCloud(self, word_cloud):
        words = '\n\t'.join([w.format_object(self) for w in word_cloud.words])
        return '<div>\n\t{0}\n\t{1}\n</span>'.format(word_cloud.name, words)

class JsonFormatter:
    def formatWord(self, word):
        return '"{0}"'.format(word.word)
    
    def formatWordCloud(self, word_cloud):
        words = ', '.join([w.format_object(self) for w in word_cloud.words])
        return '{{"blah" : "{0}", "words" : [{1}]}}'.format(word_cloud.name, words)

c = WordCloud()
o = OtherWordCloud()
h = HtmlFormatter()
j = JsonFormatter()

print c.format_object(h)
print o.format_object(h)
print c.format_object(j)
print o.format_object(j)

print c.format_object(html_formatter)
