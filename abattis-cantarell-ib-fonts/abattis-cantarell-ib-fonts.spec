%global actualname cantarell

%global fontname abattis-%{actualname}

%global archivename1 Cantarell-Bold
%global archivename2 Cantarell-Regular

Name: %{fontname}-ib-fonts
Version: 0.0.18.1
Release: 1%{?dist}
Summary: Cantarell, a Humanist sans-serif font family

Group: User Interface/X
License: OFL
URL: https://git.gnome.org/browse/cantarell-fonts/
Source0: http://download.gnome.org/sources/%{actualname}-fonts/0.0/%{actualname}-fonts-%{version}.tar.xz
Source1: %{fontname}.metainfo.xml
Source2: 45-cantarell.conf
Source3: 90-non-tt-cantarell.conf

BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge
Requires: fontpackages-filesystem

Provides: abattis-cantarell-fonts = %{version}-%{release}
Conflicts: abattis-cantarell-fonts

%description
Cantarell is a set of fonts designed by Dave Crossland.
It is a sans-serif humanist typeface family.

%prep
%autosetup -n %{actualname}-fonts-%{version}
# Force regeneration
rm otf/*.otf

%build
%configure --enable-source-rebuild
make %{?_smp_mflags}

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p otf/*.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-cantarell.conf \
      %{buildroot}%{_fontconfig_confdir}/45-cantarell.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/90-non-tt-cantarell.conf \
      %{buildroot}%{_fontconfig_confdir}/90-non-tt-cantarell.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f *-cantarell.conf *.otf
%license COPYING
%doc NEWS README
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Mon Nov 16 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 0.0.18.1-1
- based on abattis-cantarell-fonts-0.0.18.fc24.

