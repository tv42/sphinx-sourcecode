import docutils.nodes
import docutils.parsers.rst.directives
import os
import pygments
import pygments.formatters
import pygments.lexers
import sphinx.util.compat

class Sourcecode(sphinx.util.compat.Directive):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = dict(
        filename=docutils.parsers.rst.directives.path,
        title=docutils.parsers.rst.directives.unchanged,
        )

    def run(self):
        filename = self.options.get('filename', None)
        if filename is None:
            code = u'\n'.join(self.content)
        else:
            source = self.state_machine.input_lines.source(
                self.lineno - self.state_machine.input_offset - 1)
            source_dir = os.path.dirname(os.path.abspath(source))
            filename = os.path.normpath(os.path.join(source_dir, filename))
            filename = docutils.utils.relative_path(None, filename)
            self.state.document.settings.record_dependencies.add(filename)
            with file(filename) as f:
                code = f.read().decode('utf-8')

        if self.arguments:
            (syntax,) = self.arguments
        else:
            syntax = 'text'
        lexer = pygments.lexers.get_lexer_by_name(syntax)
        formatter = pygments.formatters.HtmlFormatter()
        html = pygments.highlight(
            code=code,
            lexer=lexer,
            formatter=formatter,
            )

        title_text = self.options.get('title')
        if title_text:
            text_nodes, messages = self.state.inline_text(title_text, self.lineno)
            title = docutils.nodes.caption('', '# ', *text_nodes)
        else:
            messages = []
            title = None

        fig = docutils.nodes.figure('')
        fig['classes'].append('py-listing')
        if title is not None:
            fig += title

        fig += docutils.nodes.raw('', html, format='html')

        return [fig] + messages

def setup(Sphinx):
    Sphinx.add_directive('sourcecode', Sourcecode)
