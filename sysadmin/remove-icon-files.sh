#!/bin/bash
# Credit: https://superuser.com/a/1322432
# Credit: http://www.cfchimp.com/wordpress/2014/06/clean-up-google-drive-icon-files/

find . -type f -name "Icon?" -size 0 -print0 -exec rm {} \;

