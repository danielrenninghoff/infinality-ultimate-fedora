%global fontname gdouros-symbola

Name:           %{fontname}-ib-fonts
Version:        8.00
Release:        1%{?dist}
Summary:        A symbol font

# https://web.archive.org/web/20150625020428/http://users.teilar.gr/~g1951d/
# "in lieu of a licence:
# Fonts and documents in this site are not pieces of property or merchandise
# items; they carry no trademark, copyright, license or other market tags;
# they are free for any use. George Douros"
License:        Public Domain
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Symbola.zip
Source1:        %{fontname}.metainfo.xml
Source2:        45-symbola.conf
Source3:        90-tt-symbola.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem
Provides:       %{fontname}-fonts = %{version}-%{release}
Conflicts:      %{fontname}-fonts

%description
Symbola covers many scripts and symbols supported by Unicode.

These include those in Basic Latin, Latin-1 Supplement, Latin Extended-A, IPA
Extensions, Spacing Modifier Letters, Greek and Coptic, Cyrillic, Cyrillic
Supplementary, General Punctuation, Superscripts and Subscripts, and many
others.

It was created by George Douros.

Infinality version.

%prep
%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Symbola.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/45-symbola.conf
ln -s %{_fontconfig_templatedir}/45-symbola.conf \
      %{buildroot}%{_fontconfig_confdir}/45-symbola.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/90-tt-symbola.conf
ln -s %{_fontconfig_templatedir}/90-tt-symbola.conf \
      %{buildroot}%{_fontconfig_confdir}/90-tt-symbola.conf

install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
      %{buildroot}/%{_datadir}/appdata/%{fontname}.metainfo.xml


%_font_pkg -f *-symbola.conf Symbola.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc Symbola.pdf

%changelog
* Wed Nov 11 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 8.00-1
- Based on gdouros-symbola-fonts 8.00-4.
