#!/usr/bin/env python3
import json
import re
import subprocess
from typing import Dict, List

import toml

PAT_SPACES = re.compile(r"\s+")


def git(args: List[str]) -> str:
    return subprocess.check_output(["git"] + args).decode("utf8")


def get_git_filemap(repo_dir: str):
    log_cmd = [
        "-c",
        "diff.renames=0",
        "-c",
        "log.showSignature=0",
        "-C",
        repo_dir,
        "log",
        "--name-only",
        "--no-merges",
        "--format=format:%x1e%H%x1f%h%x1f%s%x1f%aN%x1f%aE%x1f%ai%x1f%ci",
        "HEAD",
    ]

    log = git(log_cmd).split("\n\x1e")

    filemap = {}
    for entry in log[::-1]:
        info, *files = entry.strip().split("\n")

        info = info.split("\x1f")
        for file in files:
            filemap[file] = info

    return filemap


def get_go_mod_mappings() -> Dict[str, str]:
    replace_mapping = {}

    with open("go.mod", "r") as f:
        for line in f:
            line = PAT_SPACES.sub(line.strip(), " ")
            if not line.startswith("replace "):
                continue

            line = line[8:]

            # remove any comments
            if "//" in line:
                line = line[: line.index("//")]

            repo_path, dir_path = line.split(" => ")

            replace_mapping[repo_path] = dir_path

        return replace_mapping


def get_hugo_imports() -> List[str]:
    with open("config.toml", "r") as f:
        config = toml.load(f)

    return [x["path"] for x in config["module"]["imports"]]


def main():
    hugo_imports = get_hugo_imports()
    mod_mappings = get_go_mod_mappings()

    annot_map = {}

    for repo in hugo_imports:
        if repo not in mod_mappings:
            print(f"Missing path mapping for {repo!r}")
            continue

        repo_dir = mod_mappings[repo]

        print(repo, repo_dir)

        annot_map[repo] = {
            "branch": git(["-C", repo_dir, "branch", "--show-current"]).strip(),
            "files": get_git_filemap(repo_dir),
        }

    with open("git_info.json", "w") as f:
        json.dump(annot_map, f)


if __name__ == "__main__":
    main()
