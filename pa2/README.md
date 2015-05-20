# pa2

Put your pa2 submission in this folder. Please include all your deliverables.

I did not include the data, since large files like that do not belong in a Git
repository. Ideally, make your code assume that the data is in `pa2/data`
(you'll have to create this directory), so that I know where to put it if I
want to re-run your code.

Make sure you do not add the data when you commit! I would suggest that you
always add files individually and not the entire `pa2` directory. That way, it
is harder for unwanted files to accidentally get through (such as `.pyc` files
or temporary files from your code editor). Before you commit, I suggest always
to check

    git status

to make sure unwanted files are not staged. Let's say you see `pa2/data`
staged. In that case you can unstage it by:

    git reset HEAD pa2/data
