#!/bin/bash
# Generates the 'source tarball' for JDK 8 projects.
#
# Example:
# When used from local repo set REPO_ROOT pointing to file:// with your repo
# if your local repo follows upstream forests conventions, you may be enough by setting OPENJDK_URL
# if you wont to use local copy of patch PR2126 set path to it to PR2126 variable
#
# In any case you have to set PROJECT_NAME REPO_NAME and VERSION. eg:
# PROJECT_NAME=jdk8u   OR   aarch64-port 
# REPO_NAME=jdk8u60    OR   jdk8u60 
# VERSION=jdk8u60-b27  OR aarch64-jdk8u65-b17 OR for head, keyword 'tip' should do the job there
# 
# They are used to create correct name and are used in construction of sources url (unless REPO_ROOT is set)

# This script creates a single source tarball out of the repository
# based on the given tag and removes code not allowed in fedora/rhel. For
# consistency, the source tarball will always contain 'openjdk' as the top
# level folder, name is created, based on parameter
#

set -e

OPENJDK_URL_DEFAULT=http://hg.openjdk.java.net
COMPRESSION_DEFAULT=xz

if [ "x$1" = "xhelp" ] ; then
    echo -e "Behaviour may be specified by setting the following variables:\n"
    echo "VERSION - the version of the specified OpenJDK project"
    echo "PROJECT_NAME -- the name of the OpenJDK project being archived (optional; only needed by defaults)"
    echo "REPO_NAME - the name of the OpenJDK repository (optional; only needed by defaults)"
    echo "OPENJDK_URL - the URL to retrieve code from (optional; defaults to ${OPENJDK_URL_DEFAULT})"
    echo "COMPRESSION - the compression type to use (optional; defaults to ${COMPRESSION_DEFAULT})"
    echo "FILE_NAME_ROOT - name of the archive, minus extensions (optional; defaults to PROJECT_NAME-REPO_NAME-VERSION)"
    echo "REPO_ROOT - the location of the Mercurial repository to archive (optional; defaults to OPENJDK_URL/PROJECT_NAME/REPO_NAME)"
    echo "PR2126 - the path to the PR2126 patch to apply (optional; downloaded if unavailable)"
    exit 1;
fi


if [ "x$VERSION" = "x" ] ; then
    echo "No VERSION specified"
    exit -2
fi
echo "Version: ${VERSION}"
    
# REPO_NAME is only needed when we default on REPO_ROOT and FILE_NAME_ROOT
if [ "x$FILE_NAME_ROOT" = "x" -o "x$REPO_ROOT" = "x" ] ; then
    if [ "x$PROJECT_NAME" = "x" ] ; then
	echo "No PROJECT_NAME specified"
	exit -1
    fi
    echo "Project name: ${PROJECT_NAME}"
    if [ "x$REPO_NAME" = "x" ] ; then
	echo "No REPO_NAME specified"
	exit -3
    fi
    echo "Repository name: ${REPO_NAME}"
fi

if [ "x$OPENJDK_URL" = "x" ] ; then
    OPENJDK_URL=${OPENJDK_URL_DEFAULT}
    echo "No OpenJDK URL specified; defaulting to ${OPENJDK_URL}"
else
    echo "OpenJDK URL: ${OPENJDK_URL}"
fi

if [ "x$COMPRESSION" = "x" ] ; then
# rhel 5 needs tar.gz
    COMPRESSION=${COMPRESSION_DEFAULT}
fi
echo "Creating a tar.${COMPRESSION} archive"

if [ "x$FILE_NAME_ROOT" = "x" ] ; then
    FILE_NAME_ROOT=${PROJECT_NAME}-${REPO_NAME}-${VERSION}
    echo "No file name root specified; default to ${FILE_NAME_ROOT}"
fi
if [ "x$REPO_ROOT" = "x" ] ; then
    REPO_ROOT="${OPENJDK_URL}/${PROJECT_NAME}/${REPO_NAME}"
    echo "No repository root specified; default to ${REPO_ROOT}"
fi;

mkdir "${FILE_NAME_ROOT}"
pushd "${FILE_NAME_ROOT}"

echo "Cloning ${VERSION} root repository from ${REPO_ROOT}"
hg clone ${REPO_ROOT} openjdk -r ${VERSION}
pushd openjdk
	
#jdk is last for its size
repos="hotspot corba jaxws jaxp langtools nashorn jdk"

for subrepo in $repos
do
    echo "Cloning ${VERSION} ${subrepo} repository from ${REPO_ROOT}"
    hg clone ${REPO_ROOT}/${subrepo} -r ${VERSION}
done


echo "Removing EC source code we don't build"

mv -v jdk/src/share/native/sun/security/ec/impl/ecc_impl.h .
rm -vrf jdk/src/share/native/sun/security/ec/impl
mkdir jdk/src/share/native/sun/security/ec/impl
mv -v ecc_impl.h jdk/src/share/native/sun/security/ec/impl

echo "Syncing EC list with NSS"
if [ "x$PR2126" = "x" ] ; then
# get pr2126.patch (from http://icedtea.classpath.org//hg/icedtea?cmd=changeset;node=8d2c9a898f50) from most correct tag
# Do not push it or publish it (see http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=2126)
    wget http://icedtea.classpath.org/hg/icedtea/raw-file/tip/patches/pr2126.patch
    patch -Np1 < pr2126.patch
    rm pr2126.patch
else
    echo "Applying ${PR2126}"
    patch -Np1 < $PR2126
fi;

popd
echo "Compressing remaining forest"
if [ "X$COMPRESSION" = "Xxz" ] ; then
    tar --exclude-vcs -cJf ${FILE_NAME_ROOT}.tar.${COMPRESSION} openjdk
else
    tar --exclude-vcs -czf ${FILE_NAME_ROOT}.tar.${COMPRESSION} openjdk
fi

mv ${FILE_NAME_ROOT}.tar.${COMPRESSION}  ..
popd
echo "Done. You may want to remove the uncompressed version."


