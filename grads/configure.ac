dnl
dnl configure.ac: 
dnl
dnl  Source file for GrADS auto-configuration script. 
dnl  Run autoreconf to generate a configure script from this file
dnl  See acinclude.m4 for definitions of the GA_xxx macros   

# Require autoconf 2.52 (comes with Mac OS X 10.2) or newer
AC_PREREQ(2.52) 

# The "master" version string that will appear in all code, etc.
AC_INIT(GrADS, [2.2.0], [jadams21@gmu.edu])

# Supporting scripts are in etc/ 
AC_CONFIG_AUX_DIR(etc)
AC_CONFIG_MACRO_DIR(m4)

# Require automake 1.6 (comes with Mac OS X 10.2) or newer,
# don't #define PACKAGE and VERSION,
# disable dependency checking
AM_INIT_AUTOMAKE([1.6 no-define no-dependencies])

# This is so the configure script knows it is in the right place
AC_CONFIG_SRCDIR(src/grads.c)

# This will set up a configuration header file, src/config.h
# All the definitions will be set with use of AC_DEFINE
AC_CONFIG_HEADERS([src/config.h])

# The following macro prevents annoying interactions between CVS and 
# automake, which result in make attempting to invoke autotools 
# even when the configure script is up to date
AM_MAINTAINER_MODE 

# binaries go to ./bin by default, rather than /usr/bin or /usr/local/. 
AC_PREFIX_DEFAULT(`pwd`)

# Setup macros for libtool
LT_PREREQ([2.2])
LT_INIT([dlopen disable-static])
AC_PROG_LIBTOOL

# ----------------------------------------------------
#  Additional arguments for the configure script
# ----------------------------------------------------

AC_ARG_WITH(gui,      [AC_HELP_STRING([--with-gui],
                                      [Athena X11 widget-based GUI])])
AC_ARG_WITH(readline, [AC_HELP_STRING([--with-readline],
                                      [command line editing])])
AC_ARG_WITH(cairo,    [AC_HELP_STRING([--with-cairo],
                                      [cairo image rendering])])
AC_ARG_WITH(grib2,    [AC_HELP_STRING([--with-grib2],
                                      [GRIB2 data format])])
AC_ARG_WITH(sdf,      [AC_HELP_STRING([--with-sdf],
                                      [all self-describing formats (HDF4,HDF5,NetCDF,OPeNDAP)])])
AC_ARG_WITH(gadap,    [AC_HELP_STRING([--with-gadap],
                                      [OPeNDAP for station data])])
AC_ARG_WITH(shp,      [AC_HELP_STRING([--with-shp],
                                      [shapefile format])])
AC_ARG_WITH(geotiff,  [AC_HELP_STRING([--with-geotiff],
                                      [geotiff output])])

# ----------------------------------------------------
# Checks for programs
# ----------------------------------------------------

echo
echo Checking for programs
echo ---------------------
AC_PROG_AWK
AC_PROG_CC(xlc gcc cc)
AC_PROG_CXX(xlc++ g++ c++)
AC_PROG_INSTALL
AC_PROG_LN_S
echo

echo Setting host specific options
echo -----------------------------

# ----------------------------------------------------
# Get host platform and set host-specific options
# ----------------------------------------------------

AC_CANONICAL_HOST()

echo Host machine: "$host"
case "$host" in 

  alpha-*-osf*)
    # Option needed for IEEE floating points
    CFLAGS="$(CFLAGS) -ieee"
  ;;

  powerpc-ibm-aix*)
    LDFLAGS="$LDFLAGS -Wl,-bbigtoc -Wl,-bexpall -Wl,-brtl"
  ;;

  i*86-pc-linux-*)
    CFLAGS="$CFLAGS -rdynamic"
  ;;

  x86_64-*-linux-*)
    CFLAGS="$CFLAGS -rdynamic"
  ;;

  ia64-*-linux-*)
    CFLAGS="$CFLAGS -rdynamic"
  ;;

  *-freebsd*)
    CFLAGS="$CFLAGS -export-dynamic"
  ;;

  sparc-sun-solaris*)
    is_solaris="yes"
dnl checked in AC_PATH_XTRA in X_PRE_LIBS
    host_ldadd="-lsocket -lnsl -lw"
dnl    guilibadd="-lSM -lICE"
  ;;

  *-pc-cygwin)
    host_ldadd="-lrpclib"
  ;;

  *darwin*)
    is_darwin="yes"
#    LDFLAGS="$LDFLAGS -lSystemStubs"
  ;;

  cray-*-*)
    is_cray="yes"
  ;;

  *-hpux11*)
     is_hpux11="yes"
  ;;

esac

if test is_cray!="yes" ; then
  AC_DEFINE(GRADS_CRAY, 0, [Machine is NOT a Cray])
else
  AC_DEFINE(GRADS_CRAY, 1, [Machine is a Cray])
fi

if test is_hpux11!="yes" ; then
  AC_DEFINE(GRADS_HP64, 0, [Machine is NOT a 64-bit HP])
else
  AC_DEFINE(GRADS_HP64, 1, [Machine is 64-bit HP])
fi

# ----------------------------------------------------
# Check for basic libraries: math and X11
# ----------------------------------------------------

echo
echo Checking system libraries, headers, and compiler features
echo ---------------------------------------------------------

AC_CHECK_LIB(m,cos,, AC_MSG_ERROR([Fatal: Math library not found]))
AC_PATH_XTRA

echo

# ----------------------------------------------------
# Check for basic header files.
# ----------------------------------------------------

AC_HEADER_STDC
AC_CHECK_HEADERS(malloc.h sys/file.h unistd.h)
echo

dnl Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST

dnl joew - In autoconf 2.52, AC_C_BIGENDIAN seems to ignore its
dnl parameters, so I test the internal variable that it sets.  Note
dnl that AC_BIG_ENDIAN defines its own macro, WORDS_BIGENDIAN, so
dnl really it would make most sense to replace the instances of
dnl BYTEORDER in the GrADS source; but that might cause confusion
dnl among longtime users.
AC_C_BIGENDIAN
if test $ac_cv_c_bigendian = "yes" ; then
   AC_DEFINE(BYTEORDER,1,[BIG_ENDIAN machine])
else
   AC_DEFINE(BYTEORDER,0,[little_endian machine])
fi

dnl Check for and set up large file support via fseeko()
AC_TYPE_OFF_T
AC_SYS_LARGEFILE
AC_FUNC_FSEEKO



# ----------------------------------------------------
# Check for optional feature support
# ----------------------------------------------------

echo
echo Checking for optional feature support
echo -------------------------------------


# ----------------------------------------------------
# Set supplibs directory name
# ----------------------------------------------------

GA_SET_SUPPLIBS([. ..])

AC_ARG_VAR(SUPPLIBS, [Custom path (must be absolute) to a GrADS supplib distribution])

AC_ARG_ENABLE([dyn-supplibs], 
[ --enable-dyn-supplibs   Use dynamic system libraries to support optional features when
                          required libs are not present in "supplibs" directory. [[default=no]] 
  --disable-dyn-supplibs  Do not use system libraries; look only in GrADS "supplibs" directory.
                          Use this option to maximize binary portability. 
],, 
[enableval=no])

case "${enableval}" in
  yes)
    ga_dyn_supplibs=yes
  ;;
  no)
    ga_dyn_supplibs=no
  ;;
esac


# Initialize. The assumption is that we have none of the needed libs.
use_readline=no
use_gui=no
use_freq=no
use_xaw_xlibs=no
use_geotiff=no
use_gd=no
use_grib2=no
use_hdf=no
use_hdf5=no
use_nc=no
use_nc4=no
use_dap=no
use_gadap=no
use_cairo=no
use_zlib=no
use_tiff=no
use_shp=no



have_gd=no
have_grib2c=no
have_jasper=no
have_jpeg=no
have_udunits=no
have_netcdf=no
have_hdf5_hl=no
have_hdf5=no
have_tiff=no
have_geotiff=no
have_shp=no
have_gadap=no
have_dapclient=no
have_dap=no
have_curl=no
have_cairo=no
have_Xrender=no
have_fontconfig=no
have_freetype=no
have_pixman=no
have_png=no
have_xml2=no
have_zlib=no


# check in supplibs directory 
if test "Z$ga_supplib_dir" != "Z" ; then 

  echo "Checking in $ga_supplib_dir for libraries to support extra features ..."

  # command line editing
  echo 
  echo readline
  echo --------
  GA_SET_FLAGS([])
  AC_CHECK_HEADER(readline/readline.h,
  [ AC_CHECK_HEADER(readline/history.h,
    [ AC_CHECK_LIB(readline,tgetent,
      [ use_readline=yes
        GA_SET_LIB_VAR([readline_libs],[readline])
        GA_SET_DYNLIB_VAR([readline_dynlibs],[readline])
      ],
      [ AC_CHECK_LIB(ncurses,tgetent,
	[ use_readline=yes
          GA_SET_LIB_VAR([readline_libs],[readline ncurses])
          GA_SET_DYNLIB_VAR([readline_dynlibs],[readline ncurses])
        ])
      ])
    ])
  ])
  GA_UNSET_FLAGS

  # geotiff
  echo 
  echo geotiff
  echo -------
  GA_SET_FLAGS([],[],[-ltiff])
  AC_CHECK_HEADER(geotiff.h,
  [ AC_CHECK_HEADER(geotiffio.h,
    [ AC_CHECK_HEADER(xtiffio.h, 
      [ AC_CHECK_LIB([tiff], [main], 
        [ AC_CHECK_LIB([geotiff], [main], 
          [ have_geotiff=yes
            have_tiff=yes
            GA_SET_LIB_VAR([geotiff_libs], [tiff geotiff])
            GA_SET_DYNLIB_VAR([geotiff_dynlibs], [tiff geotiff])
            use_geotiff=yes
          ])
        ])
      ])
    ])
  ])
  GA_UNSET_FLAGS

  # shapefiles
  echo 
  echo shapefiles
  echo ----------
  GA_SET_FLAGS([])
  AC_CHECK_HEADER([shapefil.h], 
  [ AC_CHECK_LIB([shp], [main], 
    [ have_shp=yes 
      GA_SET_LIB_VAR([shp_libs], [shp])
      GA_SET_DYNLIB_VAR([shp_dynlibs], [shp])
      use_shp=yes 
    ])
  ])    
  GA_UNSET_FLAGS

  # png15
  echo 
  echo png
  echo ---
  GA_SET_FLAGS([])
  AC_CHECK_LIB([png15], [main], [have_png=yes])
  GA_UNSET_FLAGS

  # zlib
  echo 
  echo zlib
  echo ----
  GA_SET_FLAGS([])
  AC_CHECK_HEADER([zlib.h], 
  [ AC_CHECK_LIB([z], [compress], [have_zlib=yes])
  ])
  GA_UNSET_FLAGS

  # jpeg
  echo 
  echo jpeg
  echo ----
  GA_SET_FLAGS([])
  AC_CHECK_LIB([jpeg], [main], [have_jpeg=yes])
  GA_UNSET_FLAGS

  # jasper
  echo 
  echo jasper
  echo ------
  GA_SET_FLAGS([jasper])
  AC_CHECK_HEADER([jasper.h],
  [ AC_CHECK_LIB([jasper], [main], [have_jasper=yes])
  ])
  GA_UNSET_FLAGS

  # gd 
  echo 
  echo gd
  echo --
  if test "$have_png" = "yes" -a "$have_zlib" = "yes" -a "$have_jpeg" = "yes" ; then
    GA_SET_FLAGS([])
    AC_CHECK_HEADER(gd.h,
    [ AC_CHECK_LIB([gd], [gdImageCreate], 
      [ AC_CHECK_LIB([gd], [gdImageJpeg], 
        [ use_gd=yes
  	  GA_SET_LIB_VAR([gd_libs], [gd])
  	  GA_SET_DYNLIB_VAR([gd_dynlibs], [gd])
        ])
      ])
    ])
    GA_UNSET_FLAGS
  fi 

  # grib2
  echo 
  echo grib2
  echo -----
  if test "$have_zlib" = "yes" -a "$have_png" = "yes" -a "$have_jasper" = "yes" ; then
    GA_SET_FLAGS([])
    AC_CHECK_HEADER(grib2.h,
    [ AC_CHECK_LIB([grib2c], [main], 
      [ use_grib2=yes 
        GA_SET_LIB_VAR([grib2_libs], [grib2c jasper png15 z])
        GA_SET_DYNLIB_VAR([grib2_dynlibs], [grib2c jasper png15 z])
      ])
    ])
    GA_UNSET_FLAGS
  fi

  # xml2
  echo 
  echo xml2
  echo ----
  if test "$have_zlib" = "yes" ; then
    GA_SET_FLAGS([libxml2],[],[],[-lz])
    AC_CHECK_LIB([xml2], [main], [have_xml2=yes])
    GA_UNSET_FLAGS
  fi

  # cairo and its dependents
  echo 
  echo Cairo
  echo -----
  if test "$have_xml2" = "yes" -a  "$have_zlib" = "yes" -a "$have_png" = "yes" ; then
    # check for required header files 
    GA_SET_FLAGS([cairo freetype2])
    AC_CHECK_HEADER(cairo.h,
    [ AC_CHECK_HEADER(cairo-xlib.h,
    [ AC_CHECK_HEADER(ft2build.h,
    [ AC_CHECK_LIB(pixman-1,main,
      [ AC_CHECK_LIB(fontconfig,main,
      [ AC_CHECK_LIB(freetype,main,
      [ AC_CHECK_LIB(Xrender,main,
      [ AC_CHECK_LIB(cairo,main,
        [ use_cairo="yes"
          have_cairo="yes"
          GA_SET_INCLUDE_VAR([cairo_inc], [cairo freetype2])
          GA_SET_LIB_VAR(cairo_libs, [cairo Xrender fontconfig freetype pixman-1 png15 xml2 z])
          GA_SET_DYNLIB_VAR(cairo_dynlibs, [cairo])
        ])
      ])
      ])
      ])
      ])
    ])
    ])
    ])
    GA_UNSET_FLAGS
  fi

  # udunits (needed for hdf4 and netcdf sdfopen interfaces)
  echo 
  echo udunits
  echo -------
  GA_SET_FLAGS([])
  AC_CHECK_HEADER([udunits.h], 
  [ AC_CHECK_LIB([udunits], [utInit], 
    [ have_udunits=yes 
    ])
  ])
  GA_UNSET_FLAGS	

  # curl (needed for netcdf4 and gadap)
  echo 
  echo curl
  echo ----
  GA_SET_FLAGS([])
  AC_CHECK_LIB([curl], [main], 
  [ have_curl=yes 
    # this will be used to check if curl is https-enabled
    CURL_CONFIG=${ga_supplib_dir}/bin/curl-config
  ])
  GA_UNSET_FLAGS	

  # hdf5
  echo 
  echo hdf5
  echo ----
  if test "$have_zlib" = "yes" ; then
    GA_SET_FLAGS([])
    AC_CHECK_HEADER([hdf5.h],
    [ AC_CHECK_LIB([hdf5], [main], 
      [ AC_CHECK_LIB([hdf5_hl], [main], 
        [ use_hdf5=yes 
          have_hdf5=yes
          GA_SET_LIB_VAR([hdf5_libs], [hdf5 z])
          GA_SET_DYNLIB_VAR([hdf5_dynlibs], [hdf5])
        ])
      ])
    ])
    GA_UNSET_FLAGS
  fi

  # hdf4
  echo 
  echo hdf4
  echo ----
  if test "$have_zlib" = "yes" -a "$have_jpeg" = "yes" -a "$have_udunits" = "yes" ; then
    GA_SET_FLAGS([])
    AC_CHECK_HEADER([mfhdf.h],
    [ AC_CHECK_LIB([df], [main], 
      [ AC_CHECK_LIB([mfhdf], [main],
        [ use_hdf=yes 
          GA_SET_LIB_VAR([hdf_libs], [mfhdf df jpeg z udunits])
          GA_SET_DYNLIB_VAR([hdf_dynlibs], [mfhdf df jpeg z udunits])
        ])
      ])
    ])
    GA_UNSET_FLAGS
  fi

  # netcdf 
  echo 
  echo netcdf
  echo ------
  if test "$have_udunits" = "yes" ; then
    GA_SET_FLAGS([])
    AC_CHECK_HEADER([netcdf.h],
    [ AC_CHECK_LIB([netcdf], [main],
      [ use_nc="yes"
        # check if we have nc-config utility
        NC_CONFIG=${ga_supplib_dir}/bin/nc-config
	if test ! -f "$NC_CONFIG" || test ! -x "$NC_CONFIG"; then
          use_nc4="no"
          GA_SET_LIB_VAR(nc_libs, [udunits netcdf])
          GA_SET_DYNLIB_VAR(nc_dynlibs, [udunits netcdf])
        else
          # check if netcdf lib has hdf5 and if dap-enabled
          nchdf5=`$NC_CONFIG --has-hdf5`
          use_dap=`$NC_CONFIG --has-dap`
          if test "$nchdf5" = "yes" -a "$use_dap" = "yes" -a "$have_curl" = "yes" ; then
            use_nc4="yes"
            GA_SET_LIB_VAR(nc_libs, [udunits netcdf hdf5_hl hdf5 curl z])
            GA_SET_DYNLIB_VAR(nc_dynlibs, [udunits netcdf hdf5_hl hdf5 curl z])
          fi
        fi
      ])
    ])
  fi

  # gadap
  echo 
  echo gadap
  echo -----
  if test "$have_curl" = "yes" -a "$have_xml2" = "yes" -a "$have_zlib" = "yes" ; then
    GA_SET_FLAGS([],[],[],[-lz])
    AC_CHECK_HEADER(gadap.h,
    [ AC_CHECK_LIB(gadap,main,
      [ AC_CHECK_LIB(dap,main,
        [ AC_CHECK_LIB(dapclient,main,
          [ use_gadap="yes"
            GA_SET_LIB_VAR(gadap_libs, [gadap dapclient dap curl xml2 z])
            GA_SET_DYNLIB_VAR(gadap_dynlibs, [gadap dapclient dap curl xml2 z])
          ])
        ])
      ])
    ])
    GA_UNSET_FLAGS
  fi

fi  # end of code block for checking in supplibs


# if we haven't got what we need, check system locations
if test "$ga_dyn_supplibs" = "yes" ; then
  echo Checking in system locations for any remaining needed libraries ...
  echo -------------------------------------------------------------------
  # gui interface
  if test "$use_gui" != "yes" ; then
    GA_CHECK_GUI([
      use_gui=yes
      GA_SET_LIB_VAR(gui_libs, [sx])
      if test z"$gui_libs_Xext" != 'z'; then
        gui_libs="$gui_libs -lXext"
      fi
      gui_libs="$gui_libs -lXaw -lXpm -lXmu -lXt"
    ])
    if test $use_gui != "yes" ; then
      GA_CHECK_LIBSX([use_gui=yes;use_freq=yes],[use_gui=yes;use_freq=no])
      gui_libs="$GA_LIBSX_LIBS"
      grads_xlibs="$XAW_XLIBS"
      use_xaw_xlibs=yes
    fi
  fi

  # readline
  if test "$use_readline" != "yes" ; then
    GA_LIB_READLINE([use_readline=yes readline_libs=""])
  fi

  # geotiff
  if test "$use_geotiff" != "yes" ; then
    AC_CHECK_GEOTIFF([
      LDFLAGS="$LDFLAGS $GEOTIFF_LDFLAGS"
      geotiff_libs="$GEOTIFF_LIBS"
      geotiff_inc=$GEOTIFF_CFLAGS
      use_geotiff=yes
    ]) 
  fi

  # grib2
  if test "$use_grib2" != "yes" ; then
    GA_CHECK_LIB_GRIB2(
    [ use_grib2=yes 
      grib2_libs=$G2_LIBS
    ])
  fi

  # gd
  if test "$use_gd" != "yes" ; then
    GA_CHECK_LIB_GD(
    [ use_gd=yes 
      gd_inc=$GD_CFLAGS
      gd_libs=$gd_libs
    ])
  fi

  # hdf4
  if test $use_hdf != "yes" ; then
    GA_CHECK_UDUNITS(
    [ AC_CHECK_HDF4_NETCDF([use_hdf=yes], [use_hdf=yes])
      if test "$use_hdf" = 'yes'; then
        LDFLAGS="$LDFLAGS $HDF4_LDFLAGS"
        hdf_libs="$HDF4_LIBS $UDUNITS_LIBS"
      fi
    ])
  fi

  # hdf5
  if test "$use_hdf5" != "yes" ; then
    AC_CHECK_HDF5([
      LDFLAGS="$LDFLAGS $HDF5_LDFLAGS"
      hdf5_libs="$HDF5_LIBS"
      hdf5_inc=$HDF5_CFLAGS
      use_hdf5='yes'
    ])
  fi

# JMA are these macros smart enough to know difference from nc3 and nc4?
  if test "$use_nc4" != "yes" ; then
    GA_CHECK_UDUNITS(
    [ AC_CHECK_NETCDF(
      [ use_nc4=yes 
        LDFLAGS="$LDFLAGS $NC_LDFLAGS"
        nc_libs="$NC_LIBS $UDUNITS_LIBS"
        nc_inc="$NC_CFLAGS $UDUNITS_CFLAGS"
      ],,
      [])
    ])
    NC_CONFIG="`pkg-config --variable=prefix netcdf`/bin/nc-config"
    CURL_CONFIG="`pkg-config --variable=prefix libcurl`/bin/curl-config"
  fi

  if test $use_nc != "yes"  -a "$ga_dyn_supplibs" = "yes" ; then
    # check for netcdf 3 
    GA_CHECK_UDUNITS(
    [ AC_CHECK_NETCDF(
      [ use_nc=yes 
        LDFLAGS="$LDFLAGS $NC_LDFLAGS"
        nc_libs="$NC_LIBS $UDUNITS_LIBS"
      ],,
      [3])
    ])
  fi

  # Add macros to look outside supplibs for:
  #  shapelib, cairo, gadap

fi
# end of code block for checking system locations for libs not found in supplibs


# Review

if test $use_gui != "yes" ; then
  AC_DEFINE(USEGUI, 0, [Disable GUI widgets]) 
else
  AC_DEFINE(USEGUI, 1, [Enable GUI widgets]) 
# if the gui is built, we use the X flags from Xaw.
  if test "$use_xaw_xlibs" != 'yes'; then
    grads_xlibs="$X_PRE_LIBS -lX11 $X_EXTRA_LIBS"
    AC_SUBST(grads_xlibs)
  fi
  if test $use_freq = 'yes'; then
    AC_DEFINE(USEFREQ, 1, [Use GetFile from freq])
  else
    AC_DEFINE(USEFREQ, 0, [Use GetFile from freq])
  fi
  GA_SET_INCLUDE_VAR([gui_inc],[libsx]) 
  AC_SUBST(gui_inc)
  AC_SUBST(gui_libs)
fi


if test $use_readline != "yes" ; then
  AC_DEFINE(READLINE, 0, [Disable command line editing]) 
else
  AC_DEFINE(READLINE, 1, [Enable command line editing]) 
  AC_SUBST(readline_libs)
  AC_SUBST(readline_dynlibs)
fi

if test "$use_geotiff" != "yes" ; then
  AC_DEFINE(GEOTIFF, 0, [Disable geotiff])
else
  AC_DEFINE(GEOTIFF, 1, [Enable geotiff])
  AC_SUBST(geotiff_libs)
  AC_SUBST(geotiff_dynlibs)
fi

if test "$use_shp" != "yes" ; then
  AC_DEFINE(USESHP, 0, [Disable shapefile])
else
  AC_DEFINE(USESHP, 1, [Enable shapefile])
  AC_SUBST(shp_libs)
  AC_SUBST(shp_dynlibs)
fi

if test "$use_gd" != "yes" ; then
# JMA reperscussions are different here ... means we won't build gxpGD.so
  AC_DEFINE(USEGD, 0, [Disable gd])
else
  AC_DEFINE(USEGD, 1, [Enable gd])
  AC_SUBST(gd_inc)
  AC_SUBST(gd_libs)
  AC_SUBST(gd_dynlibs)
fi

if test "$use_cairo" != "yes" ; then
# JMA reperscussions are different here ... means we won't build gx*Cairo.so
  AC_DEFINE(USECAIRO, 0, [Disable cairo])
else
  AC_DEFINE(USECAIRO, 1, [Enable cairo])
  AC_SUBST(cairo_inc)
  AC_SUBST(cairo_libs)
  AC_SUBST(cairo_dynlibs)
fi

if test "$use_grib2" != "yes" ; then
  AC_DEFINE(GRIB2, 0, [Disable grib2])
else
  AC_DEFINE(GRIB2, 1, [Enable grib2])
  AC_SUBST(grib2_libs)
  AC_SUBST(grib2_dynlibs)
fi

if test $use_hdf != "yes" ; then
  AC_DEFINE(USEHDF, 0, [Disable hdf4])
else
  AC_DEFINE(USEHDF, 1, [Enable hdf4])
  AC_SUBST(hdf_inc)
  AC_SUBST(hdf_libs)
  AC_SUBST(hdf_dynlibs)
fi

if test $use_hdf5 != "yes" ; then
  AC_DEFINE(USEHDF5, 0, [Enable hdf5])
else
  AC_DEFINE(USEHDF5, 1, [Enable hdf5])
  AC_SUBST(hdf5_inc)
  AC_SUBST(hdf5_libs)
  AC_SUBST(hdf5_dynlibs)
fi

if test $use_nc != "yes" ; then
  AC_DEFINE(USENETCDF, 0, [Enable netcdf])
  AC_DEFINE(HAVENETCDF4, 0, [Enable netcdf4])
  AC_DEFINE(USEDAP, 0, [Enable OPeNDAP for grids])
else
  AC_DEFINE(USENETCDF, 1, [Enable netcdf])
  if test $use_nc4 != "yes" ; then
    AC_DEFINE(HAVENETCDF4, 0, [Enable netcdf4])
  else
    AC_DEFINE(HAVENETCDF4, 1, [Enable netcdf4])
    if test $use_dap = "yes" ; then
      AC_DEFINE(USEDAP, 1, [Enable OPeNDAP for grids])
    else
      AC_DEFINE(USEDAP, 0, [Enable OPeNDAP for grids])
    fi
  fi
  # check if we have curl-config utility
  if test -f "$CURL_CONFIG" || test -x "$CURL_CONFIG"; then
    # find out if curl is https-enabled
    https=`$CURL_CONFIG  --protocols | grep HTTPS`
    if test $https = "HTTPS" ; then
      nc_extra_libs="-lssl -lcrypto"
    fi
  fi
  # merge nc_libs and extras
  nc_libs="$nc_libs $nc_extra_libs"
  AC_SUBST(nc_inc)
  AC_SUBST(nc_libs)
  AC_SUBST(nc_dynlibs)
fi

if test $use_gadap != "yes" ; then
  AC_DEFINE(USEGADAP, 0, [Enable OPeNDAP for station data])
else
  AC_DEFINE(USEGADAP, 1, [Enable OPeNDAP for station data])
  # JMA add linking options
  if test "$is_darwin" = "yes" ; then 
    gadap_extra_libs="-lpthread -lm -liconv"
  else
    gadap_extra_libs="-lpthread -lm -ldl -lrt"
  fi
  # merge gadap and extras
  gadap_libs="$gadap_libs $gadap_extra_libs"
  # 
  AC_SUBST(gadap_inc)
  AC_SUBST(gadap_libs)
  AC_SUBST(gadap_dynlibs)
fi


# ----------------------------------------------------
# Send test results to makefile and config.h
# ----------------------------------------------------

# Some non-configuration-dependent GrADS macros
AC_DEFINE(GRADS_VERSION, "AC_PACKAGE_VERSION", [GrADS version])

# These are used to add the necessary source files to Makefile targets
AM_CONDITIONAL(READLINE, [ test "$use_readline"  = "yes" ] )
AM_CONDITIONAL(USEGUI,   [ test "$use_gui"  = "yes" ] )
AM_CONDITIONAL(GEOTIFF,  [ test "$use_geotiff"  = "yes" ] )
AM_CONDITIONAL(USESHP,   [ test "$use_shp"  = "yes" ] )
AM_CONDITIONAL(USEGADAP, [ test "$use_gadap" = "yes" ] )
AM_CONDITIONAL(USEDAP,   [ test "$use_dap" = "yes" ] )
AM_CONDITIONAL(USEHDF,   [ test "$use_hdf" = "yes" ] )
AM_CONDITIONAL(USEGD,    [ test "$use_gd" = "yes" ] )
AM_CONDITIONAL(USECAIRO, [ test "$use_cairo" = "yes" ] )

# Host specific linker flags
AC_SUBST(host_ldadd)


# ----------------------------------------------------
# Write output files
# ----------------------------------------------------
echo "configure: creating src/VERSION"
echo AC_PACKAGE_VERSION > src/VERSION

echo "configure: creating src/buildinfo.h"
build_info="Configured on `date +%D` for ${host}"
mkdir -p src
echo "static char *buildinfo = \"${build_info}\";" > src/buildinfo.h

AC_CONFIG_FILES([Makefile src/Makefile])
AC_OUTPUT


# ----------------------------------------------------
# Print summary 
# ----------------------------------------------------
   echo 
   echo \
"  +=========================================================================+"
   echo "   GrADS "AC_PACKAGE_VERSION ":" $build_info
   echo \
"  +=========================================================================+"
   echo     
   echo "  +-------------------------------+"
   echo "  |                               |"
   echo "  |  GrADS will be built with:    |"
   echo "  |                               |"
if test "$use_gui" = "yes" ; then
   echo "  |  + GUI enabled                |"
else
   echo "  |  - GUI disabled               |"
fi 
if test "$use_readline" = "yes" ; then
   echo "  |  + READLINE enabled           |"
else
   echo "  |  - READLINE disabled          |"
fi 
if test "$use_geotiff" = "yes" ; then
   echo "  |  + GEOTIFF enabled            |"
else
   echo "  |  - GEOTIFF disabled           |"
fi 
if test "$use_shp" = "yes" ; then
   echo "  |  + SHAPEFILE enabled          |"
else
   echo "  |  - shapefile disabled         |"
fi 
if test "$use_gd" = "yes" ; then
   echo "  |  + GD enabled                 |"
else
   echo "  |  - GD disabled                |"
fi 
if test "$use_cairo" = "yes" ; then
   echo "  |  + CAIRO enabled              |"
else
   echo "  |  - CAIRO disabled             |"
fi 
if test "$use_grib2" = "yes" ; then
   echo "  |  + GRIB2 enabled              |"
else
   echo "  |  - GRIB2 disabled             |"
fi 
if test "$use_hdf" = "yes" ; then
   echo "  |  + HDF4 enabled               |"
else
   echo "  |  - HDF4 disabled              |"
fi 
if test "$use_hdf5" = "yes" ; then
   echo "  |  + HDF5 enabled               |"
else
   echo "  |  - HDF5 disabled              |"
fi 
if test "$use_nc" != "yes" ; then
   echo "  |  - NETCDF disabled            |"
else
  if test "$use_nc4" = "yes" ; then
     echo "  |  + NETCDF4 enabled            |"
  else 
     echo "  |  + NETCDF3 enabled            |"
  fi 
fi 
if test "$use_gadap" = "yes" -o "$use_dap" = "yes" ; then
  echo "  |  + OPeNDAP enabled            |"
  if test "$use_gadap" = "yes" -a "$use_dap" = "yes" ; then
    echo "  |     for grids and stn data    |"
  else
    if test "$use_gadap" = "yes" ; then
      echo "  |     for stn data only         |"
    else
      echo "  |     for grids only            |"
    fi
  fi
else
  echo "  |  - OPeNDAP disabled           |"
fi
   echo "  |                               |"
   echo "  +-------------------------------+"


echo
echo "Run 'make && make install' to build GrADS."
echo "Executables will be installed" \
     "to bin/ in current dir, unless prefix was specified."
echo
