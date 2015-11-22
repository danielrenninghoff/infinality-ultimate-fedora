%global fontname    tex-gyre

Name:    %{fontname}-ib-fonts
Version: 2.005
Release: 1%{?dist}
Summary: TeX Gyre OTF fonts

License:   LPPL
URL:       http://www.gust.org.pl/projects/e-foundry/tex-gyre/
Source0:   http://www.gust.org.pl/projects/e-foundry/tex-gyre/whole/tg-2.005otf.zip
Source1:   45-tex-gyre.conf
Source2:   90-non-tt-tex-gyre.conf
Source3:   http://www.gust.org.pl/projects/e-foundry/licenses/GUST-FONT-LICENSE.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
TeX Gyre is an extensive remake and extension of the freely available 35 base
PostScript fonts distributed with Ghostscript ver. 4.00. The important aspect of
the project is providing not only the support for TeX but also the
cross-platform OpenType format of the fonts. Infinality version.

%prep
%setup -q -c tex-gyre
install -m 0644 %{SOURCE3} .

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-tex-gyre.conf %{buildroot}%{_fontconfig_confdir}/45-tex-gyre.conf
ln -s %{_fontconfig_templatedir}/90-non-tt-tex-gyre.conf %{buildroot}%{_fontconfig_confdir}/90-non-tt-tex-gyre.conf

%_font_pkg -f *-%{fontname}.conf *.otf

%doc GUST-FONT-LICENSE.txt

%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.005-1
- First version
