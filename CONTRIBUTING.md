# Contributing

This repository is a curated reading path, not a comprehensive paper index. A small, coherent
collection is more useful than a long list of famous titles.

## Proposing a Paper

In a pull request or issue, include:

- the paper title and a stable publisher, conference, DOI, or arXiv link;
- the track and level (`Essential`, `Recommended`, or `Reference`);
- one sentence explaining the idea a reader should retain;
- which existing paper it complements or replaces; and
- any important limitation, controversy, or reproducibility concern.

## Selection Standard

A strong addition should satisfy at least two criteria from the README's curation principles.
Recency, citation count, benchmark rank, or popularity alone is not enough.

Prefer replacing a weaker or redundant entry over growing a track indefinitely. Keep titles and
descriptions neutral, use open-access links where possible, and do not link to unauthorized copies.

## Editing Reading Progress

Mark a completed paper by changing `⬜` to `✅` in `README.md`, then refresh the badge:

```bash
python3 tools/update_progress.py
```

The script has no third-party dependencies.
