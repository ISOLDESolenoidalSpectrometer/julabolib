#!/bin/bash -ef
#
# Send an email alert
# 20190719 - Joonas Konki (joonas.konki@cern.ch)
#
if [ $# -ne 2 ]; then
	exit 1
fi

TO=liam.gaffney@cern.ch,bruno.olaizola@cern.ch
#TO=joonas.konki@cern.ch,liam.gaffney@cern.ch
/usr/sbin/sendmail -i $TO <<MAIL_END
Subject: ISSMONITORPI alert
To: $TO
This is an automatic alert email from ISSDAQPC
Device: $1
Status has changed to: $2
MAIL_END
