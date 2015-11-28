%global fontname google-droid
%global archivename google-droid-fonts-%{version}

%global common_desc \
The Droid typeface family was designed in the fall of 2006 by Ascender's \
Steve Matteson, as a commission from Google to create a set of system fonts \
for its Android platform. The goal was to provide optimal quality and comfort \
on a mobile handset when rendered in application menus, web browsers and for \
other screen text. \
The family was later extended in collaboration with other designers such as \
Pascal Zoghbi of 29ArabicLetters.

Name:    %{fontname}-ib-fonts
# No sane versionning upstream, use git clone timestamp
Version: 20120715
Release: 1%{?dist}
Summary: General-purpose fonts released by Google as part of Android

License:   ASL 2.0
URL:       https://android.googlesource.com/
Source0:   %{archivename}.tar.xz
Source2:   45-droid-sans.conf
Source3:   45-droid-sans-mono.conf
Source4:   65-ttf-droid-sans.conf
Source5:   65-ttf-droid-serif.conf
Source6:   90-tt-droid-sans.conf
Source7:   90-tt-droid-sans-mono.conf
Source8:   90-tt-droid-serif.conf
Source9:   90-tt-droid-kufi.conf
Source10:  http://www.cosmix.org/software/files/DroidSansMonoSlashed.zip
Source11:  http://www.cosmix.org/software/files/DroidSansMonoDotted.zip
Source14:  %{fontname}-sans.metainfo.xml
Source15:  %{fontname}-sans-mono.metainfo.xml
Source16:  %{fontname}-serif.metainfo.xml
Source17:  %{fontname}-kufi.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc


%package -n %{fontname}-ib-sans-fonts
Summary:   A humanist sans serif typeface
Requires:  fontpackages-filesystem
Obsoletes: google-droid-fonts-common <= 20090906-5.fc12
Provides:  %{fontname}-sans-fonts = %{version}-%{release}
Conflicts: %{fontname}-sans-fonts

%description -n %{fontname}-ib-sans-fonts
%common_desc

Droid Sans is a humanist sans serif typeface designed for user interfaces and
electronic communication.

%_font_pkg -n sans -f *-sans.conf DroidSans*ttf
%exclude %{_fontdir}/DroidSansMono*ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml

%package -n %{fontname}-ib-sans-mono-fonts
Summary:  A humanist monospace sans serif typeface
Requires: fontpackages-filesystem
Provides:  %{fontname}-sans-mono-fonts = %{version}-%{release}
Conflicts: %{fontname}-sans-mono-fonts

%description -n %{fontname}-ib-sans-mono-fonts
%common_desc

Droid Sans Mono is a humanist monospace sans serif typeface designed for user
interfaces and electronic communication.

%_font_pkg -n sans-mono -f *-sans-mono.conf DroidSansMono*.ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml

%package -n %{fontname}-ib-serif-fonts
Summary:  A contemporary serif typeface
Requires: fontpackages-filesystem
Provides: %{fontname}-naskh-fonts = %{version}-%{release}
Provides:  %{fontname}-serif-fonts = %{version}-%{release}
Conflicts: %{fontname}-serif-fonts

%description -n %{fontname}-ib-serif-fonts
%common_desc

Droid Serif is a contemporary serif typeface family designed for comfortable
reading on screen. Droid Serif is slightly condensed to maximize the amount of
text displayed on small screens. Vertical stress and open forms contribute to
its readability while its proportion and overall design complement its
companion Droid Sans.
The Arabic block was designed by Pascal Zoghbi of 29ArabicLetters under the
Droid Naskh name.

%_font_pkg -n serif -f *-serif.conf DroidSerif*ttf DroidNaskh*ttf
%doc README.txt NOTICE
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%package -n %{fontname}-ib-kufi-fonts
Summary:  A kufi Arabic titling typeface designed to complement Droid Sans
Requires: fontpackages-filesystem
Requires: %{fontname}-kufi-fonts
Provides:  %{fontname}-kufi-fonts = %{version}-%{release}
Conflicts: %{fontname}-kufi-fonts

%description -n %{fontname}-ib-kufi-fonts
%common_desc

Droid Kufi is a stylized display font suitable for titles and short runs of
text, and designed to complement Droid Sans. It was initialy designed by
Steve Matteson of Ascender with consulting by Pascal Zoghbi of 29ArabicLetters
to finalize the font family.

%_font_pkg -n kufi -f *-kufi.conf DroidKufi*ttf
%{_datadir}/appdata/%{fontname}-kufi.metainfo.xml

%prep
%setup -q -a 10 -a 11 -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p $(ls *ttf | grep -v DroidSansFallbackFull\
                             | grep -v DroidSansFallbackLegacy\
                             | grep -v DroidNaskh-Regular-SystemUI) \
                    %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/45-droid-sans.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/45-droid-sans-mono.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/65-ttf-droid-sans.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/65-ttf-droid-serif.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/90-tt-droid-sans.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/90-tt-droid-sans-mono.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/90-tt-droid-serif.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/90-tt-droid-kufi.conf

for fontconf in 45-droid-sans.conf \
                45-droid-sans-mono.conf \
                65-ttf-droid-sans.conf \
                65-ttf-droid-serif.conf \
                90-tt-droid-sans.conf \
                90-tt-droid-sans-mono.conf \
                90-tt-droid-serif.conf \
                90-tt-droid-kufi.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE15} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE16} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml
install -Dm 0644 -p %{SOURCE17} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-kufi.metainfo.xml

%changelog
* Sun Nov 22 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 20120715-1
- Based on google-droid-fonts-20120715-9

