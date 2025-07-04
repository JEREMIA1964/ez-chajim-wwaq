#!/bin/bash
# PaRDeS Module Komplett-Installation
# Stand: 8. Tammus 5785

cd ~/ez-chajim-wwaq/ez-chajim-wwaq

# 1. src/pardes/__init__.py
cat > src/pardes/__init__.py << 'EOF'
"""PaRDeS-Modul für Ez Chajim"""
from .core.pardes_system import *
__version__ = "1.0.0"
EOF

# 2. src/pardes/cli.py
cat > src/pardes/cli.py << 'EOF'
#!/usr/bin/env python3
import click
from .core.pardes_system import PardesAnalyzer

@click.command()
@click.argument('text')
def analyze(text):
    """Analysiere Text mit PaRDeS"""
    analyzer = PardesAnalyzer()
    report = analyzer.generate_report(text)
    click.echo(report)

if __name__ == '__main__':
    analyze()
EOF

# 3. tests/pardes/test_pardes_system.py
mkdir -p tests/pardes
cat > tests/pardes/test_pardes_system.py << 'EOF'
import pytest
from src.pardes.core.pardes_system import PardesAnalyzer, PardesLevel

def test_all_levels():
    analyzer = PardesAnalyzer()
    text = "בראשית"
    results = analyzer.analyze_text(text)
    assert len(results) == 4
    assert PardesLevel.PSCHAT in results
EOF

# 4. setup.py
cat > setup.py << 'EOF'
from setuptools import setup, find_packages

setup(
    name="ez-chajim-pardes",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click", "PyYAML"],
    entry_points={
        "console_scripts": ["pardes=pardes.cli:analyze"],
    },
)
EOF

# 5. requirements.txt
cat > requirements.txt << 'EOF'
click>=8.1.7
PyYAML>=6.0.1
pytest>=7.4.0
pyluach>=2.0.0
EOF

# 6. Git Push
git add -A
git commit -m "feat: complete PaRDeS module setup"
git push

echo "PaRDeS-Module installiert! Q!"
