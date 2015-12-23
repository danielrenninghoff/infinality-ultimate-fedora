#!/bin/sh
# https://bugzilla.redhat.com/show_bug.cgi?id=1142153
M=META-INF/MANIFEST.MF
#P=/usr/lib/jvm/java/jre/lib/security
P=$1/lib/security
for f in local_policy.jar US_export_policy.jar ; do
ORIG=$P/$f
echo "processing $f ($ORIG)"
if [ ! -f  $ORIG ]; then
  echo "File not found! $ORIG"
  continue
fi
d=`mktemp -d`
NW=$d/$f
  pushd $d
    jar  xf   $ORIG
    cat $M
#    sed -i "s/Created-By.*/Created-By: 1.7.0/g"  $M
    sed -i "s/Created-By.*/Created-By: $2/g"  $M
    cat $M
    find . -exec touch -t 201401010000 {} +
    zip -rX  $f *
  popd
  echo "replacing  $ORIG"
  touch -t 201401010000 $ORIG
  md5sum    $ORIG
  sha256sum $ORIG
  echo "by $NW"
  md5sum    $NW
  sha256sum $NW
  touch -t 201401010000 $NW
  cp $NW $ORIG
  md5sum    $ORIG
  sha256sum $ORIG
  touch -t 201401010000 $ORIG
  rm -rfv $d
done
