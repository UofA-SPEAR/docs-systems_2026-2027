#!/bin/sh
set -e
pip3 install -r requirements.txt
brew install graphviz plantuml 2>/dev/null || sudo apt-get install -y graphviz plantuml
git remote add wiki https://github.com/UofA-SPEAR/docs-systems_2026-2027.wiki.git 2>/dev/null || true
git config core.hooksPath .githooks