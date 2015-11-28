%global fontname open-sans

Name:       %{fontname}-ib-fonts
Version:    1.10
Release:    1%{?dist}
Summary:    Open Sans is a humanist sans-serif typeface designed by Steve Matteson

License:    ASL 2.0
URL:        http://www.google.com/fonts/specimen/Open+Sans

Source0:    open-sans-fonts-%{version}.tar.xz
Source1:    45-opensans.conf
Source2:    90-tt-opensans.conf

BuildArch:  noarch
BuildRequires:  fontpackages-devel
BuildRequires:  ttembed
Requires:   fontpackages-filesystem
Provides:   open-sans-fonts = %{version}-%{release}
Conflicts:  open-sans-fonts

%description
Open Sans is a humanist sans serif typeface designed by Steve Matteson, Type
Director of Ascender Corp. This version contains the complete 897 character
set, which includes the standard ISO Latin 1, Latin CE, Greek and Cyrillic
character sets. Open Sans was designed with an upright stress, open forms and
a neutral, yet friendly appearance. It was optimized for print, web, and mobile
interfaces, and has excellent legibility characteristics in its letter forms.

%prep
%setup -q -n open-sans-fonts-1.10

%build
# set Embedding permission to 'Installable'
ls *.ttf | xargs ttembed

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
    %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
    %{buildroot}%{_fontconfig_templatedir}/45-opensans.conf
    install -m 0644 -p %{SOURCE2} \
    %{buildroot}%{_fontconfig_templatedir}/90-tt-opensans.conf

ln -s %{_fontconfig_templatedir}/45-opensans.conf \
    %{buildroot}%{_fontconfig_confdir}/45-opensans.conf
ln -s %{_fontconfig_templatedir}/90-tt-opensans.conf \
    %{buildroot}%{_fontconfig_confdir}/90-tt-opensans.conf

%_font_pkg -f *.conf *.ttf
%doc LICENSE.txt

%changelog
* Sun Nov 22 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.10-1
- Based on open-sans-fonts-1.10-3
