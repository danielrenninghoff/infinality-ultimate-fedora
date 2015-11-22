%global fontname    signika

Name:    %{fontname}-ib-fonts
Version: 1.0001
Release: 1%{?dist}
Summary: Signika fonts

License:   OFL
URL:       http://fontfabric.com/signika-font/
Source0:   signika.zip
Source1:   45-signika.conf
Source2:   90-tt-signika.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Signika fonts.

%prep
%setup -q -n Signika

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-signika.conf %{buildroot}%{_fontconfig_confdir}/45-signika.conf
ln -s %{_fontconfig_templatedir}/90-tt-signika.conf %{buildroot}%{_fontconfig_confdir}/90-tt-signika.conf
sed -i 's/\r$//' OFL.txt

%_font_pkg -f *-%{fontname}.conf *.ttf

%doc OFL.txt

%changelog
* Sun Nov 22 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.0001-1
- First version
