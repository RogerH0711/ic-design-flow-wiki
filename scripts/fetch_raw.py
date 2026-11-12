#!/usr/bin/env python3
"""Download the raw sources listed in raw/sources.json and verify them.

    python3 scripts/fetch_raw.py            download missing files, then verify all
    python3 scripts/fetch_raw.py --verify   verify only (no network)

Every file is fetched from raw.githubusercontent.com at the pinned commit, so
the same bytes come back every time. Checksums live in raw/SHA256SUMS; a file
whose checksum changes means someone edited raw/ by hand, which AGENTS.md
forbids.
"""
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
SUMS = RAW / "SHA256SUMS"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def wanted():
    manifest = json.loads((RAW / "sources.json").read_text(encoding="utf-8"))
    for src in manifest["sources"]:
        for f in src["files"]:
            yield src["repo"], src["commit"], f["path"], f["local"]
    for lic in manifest["license_files"]:
        yield lic["repo"], lic["commit"], lic["path"], lic["local"]


def main() -> int:
    verify_only = "--verify" in sys.argv
    known = {}
    if SUMS.exists():
        for line in SUMS.read_text(encoding="utf-8").splitlines():
            digest, name = line.split("  ", 1)
            known[name] = digest

    errors = []
    for repo, commit, path, local in wanted():
        dest = RAW / local
        if not dest.exists():
            if verify_only:
                errors.append(f"missing: raw/{local}")
                continue
            url = f"https://raw.githubusercontent.com/{repo}/{commit}/{path}"
            dest.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(url, timeout=60) as resp:
                dest.write_bytes(resp.read())
            print(f"fetched  raw/{local}  ({dest.stat().st_size} bytes)")
        digest = sha256(dest)
        if local in known and known[local] != digest:
            errors.append(f"checksum changed: raw/{local}")
        known[local] = digest

    if not verify_only:
        SUMS.write_text(
            "".join(f"{known[name]}  {name}\n" for name in sorted(known)),
            encoding="utf-8",
        )

    for e in errors:
        print("ERROR", e)
    print(f"fetch_raw: {len(known)} files, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
