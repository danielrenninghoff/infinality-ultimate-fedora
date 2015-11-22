%global freetype_version 2.1.4

Summary:	Font configuration and customization library
Name:		fontconfig-infinality-ultimate
Version:	2.11.94
Release:	1%{?dist}
# src/ftglue.[ch] is in Public Domain
# src/fccache.c contains Public Domain code
# fc-case/CaseFolding.txt is in the UCD
# otherwise MIT
License:	MIT and Public Domain and UCD
Group:		System Environment/Libraries
Source:		http://fontconfig.org/release/fontconfig-%{version}.tar.bz2
URL:		http://fontconfig.org
Source1:	conf.d.infinality.tar.bz2
Source2:	presets.tar.bz2

# https://bugzilla.redhat.com/show_bug.cgi?id=140335
Patch0:		fontconfig-sleep-less.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1236034
Patch1:		fontconfig-lock-cache.patch
Patch3: 	01-configure.patch
Patch4: 	02-configure.ac.patch
Patch5: 	03-Makefile.in.patch
Patch6: 	04-Makefile.conf.d.patch
Patch7: 	05-Makefile.am.in.patch

BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= %{freetype_version}
BuildRequires:	fontpackages-devel
BuildRequires:	autoconf automake libtool

Requires:	fontpackages-filesystem
Requires(pre):	freetype
Requires(post):	grep coreutils
Requires:	font(:lang=en)
Provides:	fontconfig = %{version}-%{release}
Provides:	fontconfig%{?_isa} = %{version}-%{release}
Conflicts:	fontconfig

%description
Fontconfig is designed to locate fonts within the
system and select them according to requirements specified by 
applications.

%package	devel
Summary:	Font configuration and customization library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	freetype-devel >= %{freetype_version}
Requires:	pkgconfig
Provides:	fontconfig-devel = %{version}-%{release}
Conflicts:  fontconfig-devel

%description	devel
The fontconfig-devel package includes the header files,
and developer docs for the fontconfig package.

Install fontconfig-devel if you want to develop programs which 
will use fontconfig.

%package	devel-doc
Summary:	Development Documentation files for fontconfig library
Group:		Documentation
BuildArch:	noarch
Requires:	%{name}-devel = %{version}-%{release}
Provides:	fontconfig-doc = %{version}-%{release}
Conflicts:  fontconfig-doc

%description	devel-doc
The fontconfig-devel-doc package contains the documentation files
which is useful for developing applications that uses fontconfig.

%prep
%setup -q -b 2 -T -n presets
cd ..
%setup -q -a 1 -n fontconfig-%{version}
%patch0 -p1 -b .sleep-less
%patch1 -p1 -b .lock-cache
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

aclocal
libtoolize -f
automake -afi

%build
# We don't want to rebuild the docs, but we want to install the included ones.
export HASDOCBOOK=no

%configure	--with-add-fonts=/usr/share/X11/fonts/Type1,/usr/share/X11/fonts/TTF,/usr/local/share/fonts \
		--disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

install -p -d %{buildroot}%{_datadir}/fontconfig/conf.avail.infinality/{combi,free,ms}
install -p %{_builddir}/presets/combi/*.conf %{buildroot}%{_datadir}/fontconfig/conf.avail.infinality/combi
install -p %{_builddir}/presets/free/*.conf %{buildroot}%{_datadir}/fontconfig/conf.avail.infinality/free
install -p %{_builddir}/presets/ms/*.conf %{buildroot}%{_datadir}/fontconfig/conf.avail.infinality/ms
install -p %{_builddir}/presets/fc-presets %{buildroot}%{_bindir}/fc-presets
ln -sf %{_datadir}/fontconfig/conf.avail.infinality/free/30-metric-aliases-free.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/
ln -sf %{_datadir}/fontconfig/conf.avail.infinality/free/37-repl-global-free.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/
ln -sf %{_datadir}/fontconfig/conf.avail.infinality/free/60-latin-free.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/
ln -sf %{_datadir}/fontconfig/conf.avail.infinality/free/65-non-latin-free.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/
ln -sf %{_datadir}/fontconfig/conf.avail.infinality/free/66-aliases-wine-free.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/

# move installed doc files back to build directory to package themm
# in the right place
mv $RPM_BUILD_ROOT%{_docdir}/fontconfig/* .
rmdir $RPM_BUILD_ROOT%{_docdir}/fontconfig/

%check
make check

%post
/sbin/ldconfig

umask 0022

mkdir -p %{_localstatedir}/cache/fontconfig

# Force regeneration of all fontconfig cache files
# The check for existance is needed on dual-arch installs (the second
#  copy of fontconfig might install the binary instead of the first)
# The HOME setting is to avoid problems if HOME hasn't been reset
if [ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache --version 2>&1 | grep -q %{version} ; then
  HOME=/root /usr/bin/fc-cache -f
fi

%postun -p /sbin/ldconfig

%files
%doc README AUTHORS COPYING
%doc fontconfig-user.txt fontconfig-user.html
%doc %{_fontconfig_confdir}/README
%{_libdir}/libfontconfig.so.*
%{_bindir}/fc-cache
%{_bindir}/fc-cat
%{_bindir}/fc-list
%{_bindir}/fc-match
%{_bindir}/fc-pattern
%{_bindir}/fc-query
%{_bindir}/fc-scan
%{_bindir}/fc-validate
%{_bindir}/fc-presets
%{_fontconfig_templatedir}/*.conf
%{_datadir}/fontconfig/conf.avail.infinality/*.conf
%{_datadir}/fontconfig/conf.avail.infinality/{combi,free,ms}/*.conf
%{_datadir}/xml/fontconfig
# fonts.conf is not supposed to be modified.
# If you want to do so, you should use local.conf instead.
%config %{_fontconfig_masterdir}/fonts.conf
%config(noreplace) %{_fontconfig_confdir}/*.conf
%dir %{_localstatedir}/cache/fontconfig
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%{_libdir}/libfontconfig.so
%{_libdir}/pkgconfig/*
%{_includedir}/fontconfig
%{_mandir}/man3/*

%files devel-doc
%doc fontconfig-devel.txt fontconfig-devel

%changelog
* Fri Nov 20 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.11.94-1
- Based on fontconfig-2.11.94-4
