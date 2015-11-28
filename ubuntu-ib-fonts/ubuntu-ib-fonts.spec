%global fontname    ubuntu

Name:    %{fontname}-ib-fonts
Version: 0.83
Release: 1%{?dist}
Summary: Ubuntu fonts

License:   Ubuntu Font Licence 1.0
URL:       http://font.ubuntu.com/
Source0:   http://font.ubuntu.com/download/ubuntu-font-family-0.83.zip
Source1:   45-ubuntu.conf
Source2:   90-tt-ubuntu.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Ubuntu fonts.

%prep
%setup -q -n ubuntu-font-family-0.83

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-ubuntu.conf %{buildroot}%{_fontconfig_confdir}/45-ubuntu.conf
ln -s %{_fontconfig_templatedir}/90-tt-ubuntu.conf %{buildroot}%{_fontconfig_confdir}/90-tt-ubuntu.conf

%_font_pkg -f *-%{fontname}.conf *.ttf

%doc LICENCE.txt FONTLOG.txt

%changelog
* Sun Nov 22 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 0.83-1
- First version
