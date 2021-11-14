# DataCollectionLocation='/Users/paulcarter/Documents/GITHUB/Melbage/melbagesite.github.io'
# DataDumpLocation='/Users/paulcarter/Documents/GITHUB/Melbage/LinkChecker'
# DataDumpFile='/hrefData.txt'
# FileType='/*.htm?'
# TAG='href='
# grep -R ${TAG} '${DataCollectionLocation}${FileType}' >> '${DataDumpLocation}${DataDumpFile}'

find /Users/paulcarter/Documents/GITHUB/Melbage/melbagesite.github.io/ -name "*.htm" -type f -print -exec grep -H "href=*.htm*" '{}' + > ../Data/hrefData.txt