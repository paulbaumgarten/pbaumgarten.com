```bash
#!/bin/bash
# rsync -avzheP ssh /Users/pbaumgarten/ISL/projects/courses/ pbaumgarten@paulbaumgarten.net:/var/node/courses/courses
#
# http://www.jveweb.net/en/archives/2010/11/synchronizing-folders-with-rsync.html
#
# Creating keys for rsync https://www.howtoforge.com/mirroring_with_rsync
#
# -n to do a dry run
# -a archive (will also copy permissions data etc) 
# -r recurse directories
# -t preserve modification times
# -v verbose
# -z compress
# -h human readable output
# -e specify tool, in this case ssh
# -n dry run
# -P progress indicators
# --delete will delete files not in source USE WITH CAUTION
# rsync -rtvzhnP --checksum --exclude '._*' -e ssh /Users/pbaumgarten/ISL/projects/courses/ pbaumgarten@paulbaumgarten.net:/var/node/courses/courses

rsync -rtvzhP --checksum --exclude '._*' -e ssh /Users/pbaumgarten/ISL/courses/ pbaumgarten@paulbaumgarten.net:/var/node/courses/courses

```
