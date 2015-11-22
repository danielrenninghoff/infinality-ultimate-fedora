%global fontname google-crosextra-carlito

%global archivename crosextrafonts-carlito-20130920

Name:           %{fontname}-ib-fonts
Version:        1.103
Release:        0.4.20130920%{?dist}
Summary:        Sans-serif font metric-compatible with Calibri font

License:        OFL
URL:            http://code.google.com/p/chromium/issues/detail?id=280557
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.gz
Source1:        45-carlito.conf
Source2:        90-tt-carlito.conf
Source3:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

Provides: google-crosextra-carlito-fonts = %{version}-%{release}
Conflicts: google-crosextra-carlito-fonts

%description
Carlito is metric-compatible with Calibri font. Carlito comes in regular, bold,
italic, and bold italic. The family covers Latin-Greek-Cyrillic (not a 
complete set, though) with about 2,000 glyphs. It has the same character 
coverage as Calibri. This font is sans-serif typeface family based on Lato.

%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/45-carlito.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/90-tt-carlito.conf

ln -s %{_fontconfig_templatedir}/45-carlito.conf \
      %{buildroot}%{_fontconfig_confdir}/45-carlito.conf
ln -s %{_fontconfig_templatedir}/90-tt-carlito.conf \
      %{buildroot}%{_fontconfig_confdir}/90-tt-carlito.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f *-carlito.conf *.ttf
%doc LICENSE
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.103-0.4.20130920
- Based on google-crosextra-carlito-fonts-1.103-0.4.20130920
