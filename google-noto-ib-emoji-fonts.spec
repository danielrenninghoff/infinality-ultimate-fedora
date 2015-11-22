%global fontname google-noto

Name:           %{fontname}-ib-emoji-fonts
Version:        20150929
Release:        1%{?dist}
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
Group:          User Interface/X
License:        ASL 2.0
URL:            http://www.google.com/get/noto/
Source2:        noto-emoji-2015-09-29-license-apache.tar.gz

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Noto fonts aims to remove tofu from web by providing fonts for all
Unicode supported scripts. Its design goal is to achieve visual harmonization
between multiple scripts. Noto family supports almost all scripts available
in Unicode.

%prep
%setup -q -b 2 -T -n noto-emoji-2015-09-29-license-apache

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %_builddir/noto-emoji-2015-09-29-license-apache/NotoEmoji-Regular.ttf %{buildroot}%{_fontdir}


%_font_pkg *.ttf
%doc LICENSE AUTHORS CONTRIBUTORS

%changelog
* Wed Nov 11 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 20150929-1
- Based on google-noto-fonts 20150417-2.
