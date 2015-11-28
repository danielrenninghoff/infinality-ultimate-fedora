%global fontname google-crosextra-caladea

%global archivename crosextrafonts-20130214

Name:           %{fontname}-ib-fonts
Version:        1.002
Release:        0.6.20130214%{?dist}
Summary:        Serif font metric-compatible with Cambria font

# License added in font as "otfinfo -i Caladea-Regular.ttf | grep License"
# also from http://code.google.com/p/chromium/issues/detail?id=280557
License:        ASL 2.0
URL:            http://code.google.com/p/chromium/issues/detail?id=168879
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.gz
Source1:        45-caladea.conf
Source2:        90-tt-caladea.conf
Source3:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

Provides:       google-crosextra-caladea-fonts = %{version}-%{release}
Conflicts:      google-crosextra-caladea-fonts

%description
Caladea is metric-compatible with Cambria font. This font is a serif
typeface family based on Lato.

%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/45-caladea.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/90-tt-caladea.conf

ln -s %{_fontconfig_templatedir}/45-caladea.conf \
      %{buildroot}%{_fontconfig_confdir}/45-caladea.conf
ln -s %{_fontconfig_templatedir}/90-tt-caladea.conf \
      %{buildroot}%{_fontconfig_confdir}/90-tt-caladea.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f *-caladea.conf *.ttf
%doc
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.002-0.6.20130214
- Based on google-crosextra-caladea-fonts-1.002-0.6.20130214
