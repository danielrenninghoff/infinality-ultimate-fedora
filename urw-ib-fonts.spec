%global filippov_version 1.0.7pre44
%global fontdir %{_datadir}/fonts/default/Type1
%global fontconfig_templatedir %{_datadir}/fontconfig/conf.avail
%global fontconfig_confdir %{_sysconfdir}/fonts/conf.d
%global catalogue /etc/X11/fontpath.d

Summary: Free versions of the 35 standard PostScript fonts
Name: urw-ib-fonts
Version: 2.4
Release: 1%{?dist}
Source0: urw-fonts-%{filippov_version}.tar.bz2
Source1: 45-urw-fonts.conf
Source2: 90-non-tt-urw-fonts.conf
URL: http://svn.ghostscript.com/ghostscript/tags/urw-fonts-1.0.7pre44/
# URW holds copyright, No version specified
License: GPL+
Group: User Interface/X
BuildArch: noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Requires(post): fontconfig
Requires(post): xorg-x11-font-utils
Requires(postun): fontconfig
Epoch: 3
Provides: urw-fonts = %{epoch}:%{version}-%{release}
Conflicts: urw-fonts

%description 
Free good quality versions of the 35 standard PostScript(TM) fonts,
donated under the GPL by URW++ Design and Development GmbH.

Install the urw-fonts package if you need free versions of standard
PostScript fonts.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{fontdir}
install -m 0644 *.afm *.pfb $RPM_BUILD_ROOT%{fontdir}/

install -m 0755 -d %{buildroot}%{fontconfig_templatedir} \
                   %{buildroot}%{fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{fontconfig_templatedir}
ln -s %{fontconfig_templatedir}/45-urw-fonts.conf %{buildroot}%{fontconfig_confdir}/45-urw-fonts.conf
ln -s %{fontconfig_templatedir}/90-non-tt-urw-fonts.conf %{buildroot}%{fontconfig_confdir}/90-non-tt-urw-fonts.conf

# Touch ghosted files
touch $RPM_BUILD_ROOT%{fontdir}/{fonts.{dir,scale,cache-1},encodings.dir}

# Install catalogue symlink
mkdir -p $RPM_BUILD_ROOT%{catalogue}
ln -sf %{fontdir} $RPM_BUILD_ROOT%{catalogue}/fonts-default

%post
{
   umask 133
   mkfontscale %{fontdir} || :
   mkfontdir %{fontdir} || :
   fc-cache %{fontdir}
} &> /dev/null || :

%postun
{
   if [ "$1" = "0" ]; then
      fc-cache %{fontdir}
   fi
} &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc COPYING README README.tweaks
%dir %{_datadir}/fonts/default
%dir %{fontdir}
%dir %{fontconfig_templatedir}
%dir %{fontconfig_confdir}
%{catalogue}/fonts-default
%ghost %verify(not md5 size mtime) %{fontdir}/fonts.dir
%ghost %verify(not md5 size mtime) %{fontdir}/fonts.scale
%ghost %verify(not md5 size mtime) %{fontdir}/fonts.cache-1
%ghost %verify(not md5 size mtime) %{fontdir}/encodings.dir
%{fontdir}/*.afm
%{fontdir}/*.pfb
%{fontconfig_templatedir}/*.conf
%{fontconfig_confdir}/*.conf

%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 3:2.4-1
- based on urw-fonts-3:2.4-21.
