%global fontname    ddc-uchen

Name:    %{fontname}-ib-fonts
Version: 1.000
Release: 1%{?dist}
Summary: DDC Uchen fonts

License:   OFL
URL:       https://sites.google.com/site/chrisfynn2/home/fonts/ddc-uchen
Source0:   http://www.dzongkha.gov.bt/IT/download/fonts/DDC_Uchen.ttf
Source1:   40-ddc-uchen.conf
Source2:   90-tt-ddc-uchen.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
DDC Uchen is a font designed by Chris Fynn for the Dzongkha Development
Commission.

%prep

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/40-ddc-uchen.conf %{buildroot}%{_fontconfig_confdir}/40-ddc-uchen.conf
ln -s %{_fontconfig_templatedir}/90-tt-ddc-uchen.conf %{buildroot}%{_fontconfig_confdir}/90-tt-ddc-uchen.conf

%_font_pkg -f *-%{fontname}.conf *.ttf

%changelog
* Sun Nov 22 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.000-1
- First version
