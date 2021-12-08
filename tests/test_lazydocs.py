from lazydocs import generate_docs
import pytest

def test_generate_lazydocs():
    generate_docs(["arcus"], output_path="docs/preview/sdk", overview_file="index.md", remove_package_prefix=True)