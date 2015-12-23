%{!?with_xfree86:%define with_xfree86 1}

Summary: A free and portable font rendering engine
Name: freetype-infinality-ultimate
Version: 2.6.2
Release: 3%{?dist}
License: (FTL or GPLv2+) and BSD and MIT and Public Domain and zlib with acknowledgement
Group: System Environment/Libraries
URL: http://www.freetype.org
Source:  http://download.savannah.gnu.org/releases/freetype/freetype-%{version}.tar.bz2
Source1: http://download.savannah.gnu.org/releases/freetype/freetype-doc-%{version}.tar.bz2
Source2: http://download.savannah.gnu.org/releases/freetype/ft2demos-%{version}.tar.bz2
Source3: ftconfig.h
Source4: infinality-settings.sh
Source5: infinality-settings-generic
Source6: xft-settings.sh

Patch1:  freetype-2.2.1-enable-valid.patch
Patch2:  02-upstream-2015.12.05.patch
Patch3:  03-infinality-2.6.2-2015.12.05.patch

# Enable additional demos
Patch47:  freetype-2.5.2-more-demos.patch

# Fix multilib conflicts
Patch88:  freetype-multilib.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1161963
Patch92:  freetype-2.5.3-freetype-config-prefix.patch

Buildroot: %{_tmppath}/freetype-%{version}-root-%(%{__id_u} -n)

BuildRequires: libX11-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel

Provides: freetype-bytecode = %{version}-%{release}
Provides: freetype-subpixel = %{version}-%{release}
Provides: freetype = %{version}-%{release}
Provides: freetype%{?_isa} = %{version}-%{release}
Provides: freetype-freeworld%{?_isa} = %{version}-%{release}
Provides: freetype-freeworld = %{version}-%{release}

Conflicts: freetype-freeworld%{?_isa}
Conflicts: freetype%{?_isa}

%description
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.


%package demos
Summary: A collection of FreeType demos
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Provides: freetype-demos = %{version}-%{release}
Provides: freetype-demos%{?_isa} = %{version}-%{release}
Conflicts: freetype-demos%{?_isa}

%description demos
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments.  The demos package includes a set of useful
small utilities showing various capabilities of the FreeType library.


%package devel
Summary: FreeType development libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: freetype-devel = %{version}-%{release}
Provides: freetype-devel%{?_isa} = %{version}-%{release}
Conflicts: freetype-devel%{?_isa}

%description devel
The freetype-devel package includes the static libraries and header files
for the FreeType font rendering engine.

Install freetype-devel if you want to develop programs which will use
FreeType.


%prep
%setup -q -b 1 -a 2 -n freetype-%{version}

%patch1  -p1 -b .enable-valid
%patch2  -p1 -b .upstream
%patch3  -p1 -b .infinality


pushd ft2demos-%{version}
%patch47  -p1 -b .more-demos
popd

%patch88 -p1 -b .multilib

%patch92 -p1 -b .freetype-config-prefix

cp %{SOURCE4} .
cp %{SOURCE5} .

%build

%configure --disable-static \
           --with-zlib=yes \
           --with-bzip2=yes \
           --with-png=yes \
           --with-harfbuzz=no
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' builds/unix/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' builds/unix/libtool
make %{?_smp_mflags}

%if %{with_xfree86}
# Build demos
pushd ft2demos-%{version}
make TOP_DIR=".."
popd
%endif

# Convert FTL.txt and example3.cpp to UTF-8
pushd docs
iconv -f latin1 -t utf-8 < FTL.TXT > FTL.TXT.tmp && \
touch -r FTL.TXT FTL.TXT.tmp && \
mv FTL.TXT.tmp FTL.TXT

iconv -f iso-8859-1 -t utf-8 < "tutorial/example3.cpp" > "tutorial/example3.cpp.utf8"
touch -r tutorial/example3.cpp tutorial/example3.cpp.utf8 && \
mv tutorial/example3.cpp.utf8 tutorial/example3.cpp
popd


%install
rm -rf $RPM_BUILD_ROOT


%makeinstall gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

{
  for ftdemo in ftbench ftchkwd ftmemchk ftpatchk fttimer ftdump ftlint ftmemchk ftvalid ; do
      builds/unix/libtool --mode=install install -m 755 ft2demos-%{version}/bin/$ftdemo $RPM_BUILD_ROOT/%{_bindir}
  done
}
%if %{with_xfree86}
{
  for ftdemo in ftdiff ftgamma ftgrid ftmulti ftstring fttimer ftview ; do
      builds/unix/libtool --mode=install install -m 755 ft2demos-%{version}/bin/$ftdemo $RPM_BUILD_ROOT/%{_bindir}
  done
}
%endif

# fix multilib issues
%define wordsize %{__isa_bits}

mv $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig.h \
   $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig-%{wordsize}.h
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig.h

# install infinality-settings.sh
install -p -m 755 -D %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/xft-settings.sh

# Don't package static a or .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- freetype < 2.0.5-3
{
  # ttmkfdir updated - as of 2.0.5-3, on upgrades we need xfs to regenerate
  # things to get the iso10646-1 encoding listed.
  for I in %{_datadir}/fonts/*/TrueType /usr/share/X11/fonts/TTF; do
      [ -d $I ] && [ -f $I/fonts.scale ] && [ -f $I/fonts.dir ] && touch $I/fonts.scale
  done
  exit 0
}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libfreetype.so.*
%{_sysconfdir}/X11/xinit/xinitrc.d/xft-settings.sh
%doc README
%doc docs/LICENSE.TXT docs/FTL.TXT docs/GPLv2.TXT
%doc docs/CHANGES docs/VERSION.DLL docs/formats.txt docs/ft2faq.html
%doc infinality-settings.sh infinality-settings-generic

%files demos
%defattr(-,root,root)
%{_bindir}/ftbench
%{_bindir}/ftchkwd
%{_bindir}/ftmemchk
%{_bindir}/ftpatchk
%{_bindir}/fttimer
%{_bindir}/ftdump
%{_bindir}/ftlint
%{_bindir}/ftmemchk
%{_bindir}/ftvalid
%if %{with_xfree86}
%{_bindir}/ftdiff
%{_bindir}/ftgamma
%{_bindir}/ftgrid
%{_bindir}/ftmulti
%{_bindir}/ftstring
%{_bindir}/fttimer
%{_bindir}/ftview
%endif
%doc ChangeLog README

%files devel
%defattr(-,root,root)
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_libdir}/libfreetype.so
%{_bindir}/freetype-config
%{_libdir}/pkgconfig/freetype2.pc
%doc docs/design
%doc docs/glyphs
%doc docs/reference
%doc docs/tutorial
%{_mandir}/man1/*

%changelog
* Sun Dec 06 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.6.2-3
* apply fixes by bohoomil and git commits.

* Mon Nov 30 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.6.2-2
* apply fixes by bohoomil and git commits.

* Sun Nov 29 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.6.2-1
- Updated to new upstream version.

* Mon Nov 23 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.6.1-4
- Fixed a multilib bug.

* Sun Nov 22 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.6.1-3
- Fixed a dependency bug.

* Mon Nov 16 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.6.1-2
- Update to latest version from bohoomil.

* Mon Nov 09 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.6.1-1
- Use base freetype package to create freetype-infinality-ultimate.
