#!/bin/bash -x
# Generates the 'source tarball' for JDK 8 projects and update spec infrastructure
# By default, this script regenerate source as they are currently used. 
# so if the version of sources change, this file changes and is pushed
#
# In any case you have to set PROJECT_NAME REPO_NAME and VERSION. eg:
# PROJECT_NAME=jdk8u   OR   aarch64-port 
# REPO_NAME=jdk8u60    OR   jdk8u60 
# VERSION=jdk8u60-b27  OR aarch64-jdk8u65-b17 OR for head, keyword 'tip' should do the job there
# 
# If you don't, default are used and so already uploaded tarball regenerated
# They are used to create correct name and are used in construction of sources url (unless REPO_ROOT is set)
# 
# For other useful variables see generate_source_tarball.sh
#
# the used values are then substituted to spec and sources

set -e

if [ "x$PROJECT_NAME" = "x" ] ; then
    PROJECT_NAME="aarch64-port"
fi
if [ "x$REPO_NAME" = "x" ] ; then
    REPO_NAME="jdk8u"
fi
if [ "x$VERSION" = "x" ] ; then
    VERSION="aarch64-jdk8u77-b03"
fi

if [ "x$COMPRESSION" = "x" ] ; then
# rhel 5 needs tar.gz
    COMPRESSION=xz
fi
if [ "x$FILE_NAME_ROOT" = "x" ] ; then
    FILE_NAME_ROOT=${PROJECT_NAME}-${REPO_NAME}-${VERSION}
fi
if [ "x$PKG" = "x" ] ; then
    URL=`cat .git/config  | grep url`
    PKG=${URL##*/}
fi
if [ "x$SPEC" = "x" ] ; then
    SPEC=${PKG}.spec
fi
if [ "x$RELEASE" = "x" ] ; then
    RELEASE=1
fi

FILENAME=${FILE_NAME_ROOT}.tar.${COMPRESSION}

if [ ! -f ${FILENAME} ] ; then
echo "Generating ${FILENAME}"
. ./generate_source_tarball.sh
else 
echo "${FILENAME} already exists, using"
fi


echo "Touching spec: $SPEC"
sed -i "s/^%global\s\+project.*/%global project         ${PROJECT_NAME}/" $SPEC 
sed -i "s/^%global\s\+repo.*/%global repo            ${REPO_NAME}/" $SPEC 
sed -i "s/^%global\s\+revision.*/%global revision        ${VERSION}/" $SPEC 
# updated sources, resetting release
sed -i "s/^Release:.*/Release: $RELEASE.%{buildver}%{?dist}/" $SPEC

git --no-pager diff $SPEC

#https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Bash
function levenshtein {
	if [ "$#" -ne "2" ]; then
		echo "Usage: $0 word1 word2" >&2
	elif [ "${#1}" -lt "${#2}" ]; then
		levenshtein "$2" "$1"
	else
		local str1len=$((${#1}))
		local str2len=$((${#2}))
		local d i j
		for i in $(seq 0 $(((str1len+1)*(str2len+1)))); do
			d[i]=0
		done
		for i in $(seq 0 $((str1len)));	do
			d[$((i+0*str1len))]=$i
		done
		for j in $(seq 0 $((str2len)));	do
			d[$((0+j*(str1len+1)))]=$j
		done

		for j in $(seq 1 $((str2len))); do
			for i in $(seq 1 $((str1len))); do
				[ "${1:i-1:1}" = "${2:j-1:1}" ] && local cost=0 || local cost=1
				local del=$((d[(i-1)+str1len*j]+1))
				local ins=$((d[i+str1len*(j-1)]+1))
				local alt=$((d[(i-1)+str1len*(j-1)]+cost))
				d[i+str1len*j]=$(echo -e "$del\n$ins\n$alt" | sort -n | head -1)
			done
		done
		echo ${d[str1len+str1len*(str2len)]}
	fi
}

# find the most similar sources name and replace it by newly generated one.
echo "Old sources"
cat sources
a_sources=`cat sources | sed "s/.*\s\+//g"`
winner=""
winnerDistance=999999
for x in $a_sources ; do
  distance=`levenshtein $x ${FILENAME}`
  if [ $distance -lt $winnerDistance ] ; then
    winner=$x
    winnerDistance=$distance
  fi
done
sum=`md5sum ${FILENAME}`
sed -i "s;.*$winner;$sum;" sources
echo "New sources"
cat sources
a_sources=`cat sources | sed "s/.*\s\+//g"`
echo "    you can get inspired by following %changelog template:"
user_name=`whoami`
user_record=$(getent passwd $user_name)
user_gecos_field=$(echo "$user_record" | cut -d ':' -f 5)
user_full_name=$(echo "$user_gecos_field" | cut -d ',' -f 1)
spec_date=`date +"%a %b %d %Y"`
# See spec:
revision_helper=`echo ${VERSION%-*}`
updatever=`echo ${revision_helper##*u}`
buildver=`echo ${VERSION##*-}`
echo "* $spec_date $user_full_name <$user_name@redhat.com> - 1:1.8.0.$updatever-$RELEASE.$buildver" 
echo "- updated to $VERSION (from $PROJECT_NAME/$REPO_NAME)"
echo "- used $FILENAME as new sources"

echo "    execute:"
echo "fedpkg/rhpkg new-sources "$a_sources
echo "    to upload sources"
echo "you can verify by fedpkg/rhpkg prep --arch XXXX on all architectures: x86_64 i386 i586 i686 ppc ppc64 ppc64le s390 s390x aarch64 armv7hl"

