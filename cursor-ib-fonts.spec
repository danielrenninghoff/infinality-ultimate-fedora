%global fontname    cursor

Name:    %{fontname}-ib-fonts
Version: 1.04
Release: 1%{?dist}
Summary: Cursor T1 fonts

License:   XFree86
URL:       http://xorg.freedesktop.org
Source0:   http://xorg.freedesktop.org/releases/individual/font/font-xfree86-type1-1.0.4.tar.bz2

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Cursor T1 fonts.

%prep
%setup -q -n font-xfree86-type1-1.0.4

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_fontdir}
cp cursor.pfa %{buildroot}%{_fontdir}

%_font_pkg *.pfa

%doc COPYING

%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.04-1
- First version
