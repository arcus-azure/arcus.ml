from lazydocs import generate_docs
import pytest
import glob, os, os.path

def test_generate_apidocs():
    # Remove all files
    files_to_ignore = ['ml.images.md', 'ml.md', 'ml.evaluation.md', 'ml.neuralnetworks.md', 'ml.timeseries.md']
    sdk_docs_dir = 'docs/preview/sdk'
    filelist = glob.glob(os.path.join(sdk_docs_dir, "*.md"))
    for f in filelist:
        os.remove(f)
    generate_docs(['arcus'], output_path=sdk_docs_dir, overview_file="index.md", remove_package_prefix=True)
    for f in files_to_ignore:
        os.remove(os.path.join(sdk_docs_dir, f))
    filelist = glob.glob(os.path.join(sdk_docs_dir, "*.md"))
    for f in filelist:
        __fix_html_file(f)

def __fix_html_file(md_file:str):
    # Read in the file
    with open(md_file, 'r') as file :
        filedata = file.read()

    # Close the img tag
    filedata = filedata.replace('></a>', ' /></a>')

    # Write the file out again
    with open(md_file, 'w') as file:
        file.write(filedata)