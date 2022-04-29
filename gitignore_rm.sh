#!! DELETE
#// https://stackoverflow.com/questions/63712737/how-to-delete-all-pycache-folders-in-directory-tree

find . | grep -E "(__pycache__|\.pytest_cache|\.pyc|\.pyo$)" | xargs rm -rf