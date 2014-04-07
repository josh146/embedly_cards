# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from pelican import signals

def content_object_init(instance):

    class EmbedlyCard(Directive):
        required_arguments = 1
        optional_arguments = 0
        option_spec = {
            'title': directives.unchanged,
            'card-chrome': directives.nonnegative_int
        }

        final_argument_whitespace = True
        has_content = True

        def run(self):
            url = self.arguments[0].strip()
            title = ""
            cardChrome = 0

            if 'title' in self.options:
                title = self.options['title']

            if 'card-chrome' in self.options:
                cardChrome = self.options['card-chrome']

            linkHTML = "<a class='embedly-card' data-card-chrome='{2}' href='{0}'>{1}</a>".format(url, title, cardChrome)
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

            return [nodes.raw('', linkHTML, format='html'),
                    nodes.raw('', scriptHTML, format='html')]

    directives.register_directive('embedly-card', EmbedlyCard)

def register():
    signals.content_object_init.connect(content_object_init)

