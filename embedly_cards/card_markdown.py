from __future__ import unicode_literals
from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension

EMBED_REGEX = '\[!embedlycard(\?(.*))?\]\((.*)\)'


class EmbedlyCardPattern(Pattern):

    def __init__(self, md):
        super(EmbedlyCardPattern, self).__init__(EMBED_REGEX)
        self.md = md

    def handleMatch(self, m):
        url = m.group(4)

        if m.group(3) is not None:
            parameters = dict([i.split('=') for i in m.group(3).split('?')])
        else:
            parameters = {}

        if 'title' in parameters:
            title = parameters['title']
        else:
            title = ""

        if 'chrome' in parameters:
            chrome = int(parameters['chrome'])
        else:
            chrome = 0

        linkHTML = "<a class='embedly-card' data-card-chrome='{2}' href='{0}'>{1}</a>".format(url, title, chrome)
        scriptHTML = """
            <script>
            !function(a){
                var b="embedly-platform",c="script";
                if(!a.getElementById(b)){
                    var d=a.createElement(c);
                    d.id=b;
                    d.src=("https:"===document.location.protocol?"https":"http")+"://cdn.embedly.com/widgets/platform.js";
                    var e=document.getElementsByTagName(c)[0];e.parentNode.insertBefore(d,e)}
                }(document);
            </script>
            """

        return self.md.htmlStash.store(linkHTML+scriptHTML)


class EmbedlyCardExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('embedlycard', EmbedlyCardPattern(md), '_begin')


def makeExtension(configs=None):
    return EmbedlyCardExtension(configs)
