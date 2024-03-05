"""HunFlair implementation of Ab3P.

  this code is modified and simplified to not depend on the Flair library and is reduced to the use we have.

  Essentially it downloads a precompiled version of Ab3P from https://github.com/dmis-lab/BioSyn/tree/master/Ab3P
  and runs it via subprocess.

  This approach only works on linux.
"""

import os
import re
import stat
import subprocess
import tempfile
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlparse
import requests
import shutil


def get_from_cache(url: str, cache_dir: Path) -> Path:
    cache_dir.mkdir(parents=True, exist_ok=True)

    filename = re.sub(r".+/", "", url)

    cache_path = cache_dir / filename
    if cache_path.exists():
        return cache_path

    response = requests.head(
        url, headers={"User-Agent": "HunFlair"}, allow_redirects=True
    )
    if response.status_code != 200:
        raise OSError(
            f"HEAD request failed for url {url} with status code {response.status_code}."
        )

    if not cache_path.exists():
        fd, temp_filename = tempfile.mkstemp()

        req = requests.get(url, stream=True, headers={"User-Agent": "Flair"})
        with open(temp_filename, "wb") as temp_file:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    temp_file.write(chunk)

        shutil.copyfile(temp_filename, str(cache_path))
        os.close(fd)
        os.remove(temp_filename)

    return cache_path


def cached_path(url_or_filename: str, cache_dir: Path) -> Path:

    parsed = urlparse(url_or_filename)

    if parsed.scheme in ("http", "https"):
        return get_from_cache(url_or_filename, cache_dir)
    elif len(parsed.scheme) < 2 and Path(url_or_filename).exists():
        return Path(url_or_filename)
    elif len(parsed.scheme) < 2:
        raise FileNotFoundError(f"file {url_or_filename} not found")
    else:
        raise ValueError(
            f"unable to parse {url_or_filename} as a URL or as a local path"
        )


class HunFlairAb3P:
    def __init__(
        self,
    ) -> None:
        self.ab3p_path = self._get_biosyn_ab3p_paths()

    def get_abbreviations(self, text: str) -> List[Tuple[str, str]]:
        abbreviations = {}
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8") as temp_file:
            temp_file.write(text + "\n")
            temp_file.flush()

            result = subprocess.run(
                [self.ab3p_path, temp_file.name],
                capture_output=True,
                check=True,
            )
            line = result.stdout.decode("utf-8")
            lines = line.split("\n")
            for line in lines:
                if len(line.split("|")) == 3:
                    sf, lf, _ = line.split("|")
                    sf = sf.strip()
                    lf = lf.strip()
                    abbreviations[sf] = lf
            return list(abbreviations.items())

    def _get_biosyn_ab3p_paths(self) -> Path:
        data_dir = Path(__file__).parent / "hunflair_ab3p_biosyn"
        data_dir.mkdir(parents=True, exist_ok=True)

        ab3p_path = self._download_biosyn_ab3p(data_dir)

        return ab3p_path

    def _download_biosyn_ab3p(self, data_dir: Path) -> Path:
        ab3p_path = cached_path(
            "https://github.com/dmis-lab/BioSyn/raw/master/Ab3P/identify_abbr", data_dir
        )

        ab3p_path.chmod(ab3p_path.stat().st_mode | stat.S_IXUSR)
        return ab3p_path
