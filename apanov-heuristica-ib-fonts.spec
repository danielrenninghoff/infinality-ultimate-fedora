%global fontname apanov-heuristica
%global archivename heuristica-ttf-%{version}

Name:    %{fontname}-ib-fonts
Version: 1.0.2
Release: 1%{?dist}
Epoch:   1
Summary: A serif Latin & Cyrillic font

License:   OFL
URL:       http://sourceforge.net/projects/heuristica/

Source0:   http://downloads.sourceforge.net/project/heuristica/%{archivename}.tar.xz
Source1:   %{fontname}.metainfo.xml
Source2:   45-heuristica.conf
Source3:   90-tt-heuristica.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: dos2unix
Requires:      fontpackages-filesystem

Provides:      apanov-heuristica-fonts = %{epoch}:%{version}-%{release}
Conflicts:     apanov-heuristica-fonts

%description
Heuristica is a serif Latin & Cyrillic font, derived from the “Adobe Utopia”
font that was released to the TeX Users Group under a liberal license.

Infinality version.


%prep
%setup -q -c
dos2unix OFL-FAQ.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *\.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/45-heuristica.conf
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/90-tt-heuristica.conf
ln -s %{_fontconfig_templatedir}/45-heuristica.conf %{buildroot}%{_fontconfig_confdir}/45-heuristica.conf
ln -s %{_fontconfig_templatedir}/90-tt-heuristica.conf %{buildroot}%{_fontconfig_confdir}/90-tt-heuristica.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f *-heuristica.conf *.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Tue Nov 10 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1:1.0.2-1
- Based on apanov-heuristica-fonts-1:1.0.2-1.fc23
