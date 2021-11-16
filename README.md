# LinkChecker
Type to check for broken links in Melbage website. Will try and crawl though the files system/repo of the site as to checking via a online test of every link.

Will use shell prompt to create list of files/DB of what files have what linking in them. 
Knowing how Dave creates the pages they are created with .htm  and not a .html extension but will look to find all href referrences in all docs first. 

Starting Place which is the root of the site.  
/Users/paulcarter/Documents/GITHUB/Melbage/melbagesite.github.io

Run the script
```shell
./Scripts/CollectData.sh
```
simple script which looks for all htm files and check if they have href in them. It creates a file ./Data/hrefData.txt

./Data/hrefData_v1.txt has had the leading "/Users/paulcarter/Documents/GITHUB/Melbage/melbagesite.github.io//" string replaced with "./" in edit editor. (8962 times) only a test.
