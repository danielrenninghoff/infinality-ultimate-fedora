#!/bin/sh

ZIP_SRC=jdk8/jdk/src/share/native/java/util/zip/zlib-*
JPEG_SRC=jdk8/jdk/src/share/native/sun/awt/image/jpeg
GIF_SRC=jdk8/jdk/src/share/native/sun/awt/giflib
PNG_SRC=jdk8/jdk/src/share/native/sun/awt/libpng
LCMS_SRC=jdk8/jdk/src/share/native/sun/java2d/cmm/lcms

echo "Removing built-in libs (they will be linked)"

echo "Removing zlib"
if [ ! -d ${ZIP_SRC} ]; then
	echo "${ZIP_SRC} does not exist. Refusing to proceed."
	exit 1
fi	
rm -rvf ${ZIP_SRC}

echo "Removing libjpeg"
if [ ! -f ${JPEG_SRC}/jdhuff.c ]; then # some file that sound definitely exist
	echo "${JPEG_SRC} does not contain jpeg sources. Refusing to proceed."
	exit 1
fi	

rm -vf ${JPEG_SRC}/jcomapi.c
rm -vf ${JPEG_SRC}/jdapimin.c
rm -vf ${JPEG_SRC}/jdapistd.c
rm -vf ${JPEG_SRC}/jdcoefct.c
rm -vf ${JPEG_SRC}/jdcolor.c
rm -vf ${JPEG_SRC}/jdct.h
rm -vf ${JPEG_SRC}/jddctmgr.c
rm -vf ${JPEG_SRC}/jdhuff.c
rm -vf ${JPEG_SRC}/jdhuff.h
rm -vf ${JPEG_SRC}/jdinput.c
rm -vf ${JPEG_SRC}/jdmainct.c
rm -vf ${JPEG_SRC}/jdmarker.c
rm -vf ${JPEG_SRC}/jdmaster.c
rm -vf ${JPEG_SRC}/jdmerge.c
rm -vf ${JPEG_SRC}/jdphuff.c
rm -vf ${JPEG_SRC}/jdpostct.c
rm -vf ${JPEG_SRC}/jdsample.c
rm -vf ${JPEG_SRC}/jerror.c
rm -vf ${JPEG_SRC}/jerror.h
rm -vf ${JPEG_SRC}/jidctflt.c
rm -vf ${JPEG_SRC}/jidctfst.c
rm -vf ${JPEG_SRC}/jidctint.c
rm -vf ${JPEG_SRC}/jidctred.c
rm -vf ${JPEG_SRC}/jinclude.h
rm -vf ${JPEG_SRC}/jmemmgr.c
rm -vf ${JPEG_SRC}/jmemsys.h
rm -vf ${JPEG_SRC}/jmemnobs.c
rm -vf ${JPEG_SRC}/jmorecfg.h
rm -vf ${JPEG_SRC}/jpegint.h
rm -vf ${JPEG_SRC}/jpeglib.h
rm -vf ${JPEG_SRC}/jquant1.c
rm -vf ${JPEG_SRC}/jquant2.c
rm -vf ${JPEG_SRC}/jutils.c
rm -vf ${JPEG_SRC}/jcapimin.c
rm -vf ${JPEG_SRC}/jcapistd.c
rm -vf ${JPEG_SRC}/jccoefct.c
rm -vf ${JPEG_SRC}/jccolor.c
rm -vf ${JPEG_SRC}/jcdctmgr.c
rm -vf ${JPEG_SRC}/jchuff.c
rm -vf ${JPEG_SRC}/jchuff.h
rm -vf ${JPEG_SRC}/jcinit.c
rm -vf ${JPEG_SRC}/jconfig.h
rm -vf ${JPEG_SRC}/jcmainct.c
rm -vf ${JPEG_SRC}/jcmarker.c
rm -vf ${JPEG_SRC}/jcmaster.c
rm -vf ${JPEG_SRC}/jcparam.c
rm -vf ${JPEG_SRC}/jcphuff.c
rm -vf ${JPEG_SRC}/jcprepct.c
rm -vf ${JPEG_SRC}/jcsample.c
rm -vf ${JPEG_SRC}/jctrans.c
rm -vf ${JPEG_SRC}/jdtrans.c
rm -vf ${JPEG_SRC}/jfdctflt.c
rm -vf ${JPEG_SRC}/jfdctfst.c
rm -vf ${JPEG_SRC}/jfdctint.c
rm -vf ${JPEG_SRC}/jversion.h
rm -vf ${JPEG_SRC}/README

echo "Removing giflib"
if [ ! -d ${GIF_SRC} ]; then
	echo "${GIF_SRC} does not exist. Refusing to proceed."
	exit 1
fi	
rm -rvf ${GIF_SRC}

echo "Removing libpng"
if [ ! -d ${PNG_SRC} ]; then
	echo "${PNG_SRC} does not exist. Refusing to proceed."
	exit 1
fi	
rm -rvf ${PNG_SRC}

echo "Removing lcms"
if [ ! -d ${LCMS_SRC} ]; then
	echo "${LCMS_SRC} does not exist. Refusing to proceed."
	exit 1
fi
# temporary change to move bundled LCMS
if [ ! true ]; then
rm -vf ${LCMS_SRC}/cmscam02.c
rm -vf ${LCMS_SRC}/cmscgats.c
rm -vf ${LCMS_SRC}/cmscnvrt.c
rm -vf ${LCMS_SRC}/cmserr.c
rm -vf ${LCMS_SRC}/cmsgamma.c
rm -vf ${LCMS_SRC}/cmsgmt.c
rm -vf ${LCMS_SRC}/cmshalf.c
rm -vf ${LCMS_SRC}/cmsintrp.c
rm -vf ${LCMS_SRC}/cmsio0.c
rm -vf ${LCMS_SRC}/cmsio1.c
rm -vf ${LCMS_SRC}/cmslut.c
rm -vf ${LCMS_SRC}/cmsmd5.c
rm -vf ${LCMS_SRC}/cmsmtrx.c
rm -vf ${LCMS_SRC}/cmsnamed.c
rm -vf ${LCMS_SRC}/cmsopt.c
rm -vf ${LCMS_SRC}/cmspack.c
rm -vf ${LCMS_SRC}/cmspcs.c
rm -vf ${LCMS_SRC}/cmsplugin.c
rm -vf ${LCMS_SRC}/cmsps2.c
rm -vf ${LCMS_SRC}/cmssamp.c
rm -vf ${LCMS_SRC}/cmssm.c
rm -vf ${LCMS_SRC}/cmstypes.c
rm -vf ${LCMS_SRC}/cmsvirt.c
rm -vf ${LCMS_SRC}/cmswtpnt.c
rm -vf ${LCMS_SRC}/cmsxform.c
rm -vf ${LCMS_SRC}/lcms2.h
rm -vf ${LCMS_SRC}/lcms2_internal.h
rm -vf ${LCMS_SRC}/lcms2_plugin.h
fi
