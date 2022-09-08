from markdown import markdown
from clld.web.util.helpers import link
import re

def markdown_handle_links(req, m):
    return markdown(m.replace('\\n', '\n'))