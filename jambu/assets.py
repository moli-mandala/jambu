from pathlib import Path

from clld.web.assets import environment

import jambu


environment.append_path(
    Path(jambu.__file__).parent.joinpath('static').as_posix(),
    url='/jambu:static/')
environment.load_path = list(reversed(environment.load_path))
