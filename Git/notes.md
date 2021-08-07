https://stackoverflow.com/questions/1425892/how-do-you-merge-two-git-repositories

If you want to merge project-a into project-b:

cd path/to/project-b
git remote add project-a /path/to/project-a
git fetch project-a --tags
git merge --allow-unrelated-histories project-a/master # or whichever branch you want to merge
git remote remove project-a

Example:

- Create a new repo
- CD over that repo
- git remote add MyToolbox https://github.com/NicolasRementeria/MyToolbox.git
- git fetch MyToolbox --tags
- git merge --allow-unrelated-histories MyToolbox/master 