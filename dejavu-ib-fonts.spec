%global fontname    dejavu
%global archivename dejavu-fonts-%{archiveversion}

#global alphatag .20130819.2534
#global alphatag .rc1

#global archiveversion 2.33-20130819-2534
%global archiveversion %{version}

# Common description
%global common_desc \
The DejaVu font set is based on the “Bitstream Vera” fonts, release 1.10. Its\
purpose is to provide a wider range of characters, while maintaining the \
original style, using an open collaborative development process.


Name:    %{fontname}-ib-fonts
Version: 2.35
Release: 1%{?alphatag}%{?dist}
Summary: DejaVu fonts

Group:     User Interface/X
# original bitstream glyphs are Bitstream Vera
# glyphs modifications by dejavu project are Public Domain
# glyphs imported from Arev fonts are under BitStream Vera compatible license
License:   Bitstream Vera and Public Domain
URL:       http://dejavu-fonts.org/
Source0:   %{?!alphatag:http://downloads.sourceforge.net/%{fontname}}%{?alphatag:%{fontname}.sourceforge.net/snapshots}/%{archivename}.tar.bz2
Source1:   %{fontname}.metainfo.xml
Source2:   %{fontname}-sans.metainfo.xml
Source3:   %{fontname}-sans-mono.metainfo.xml
Source4:   %{fontname}-serif.metainfo.xml
Source5:   45-dejavu-sans.conf
Source6:   45-dejavu-sans-mono.conf
Source7:   45-dejavu-serif.conf
Source8:   90-tt-dejavu-sans.conf
Source9:   90-tt-dejavu-sans-mono.conf
Source10:  90-tt-dejavu-serif.conf


# Older fontforge versions will not work due to sfd format changes
BuildRequires: fontforge >= 20080429
BuildRequires: perl(Font::TTF)
# Needed to compute unicode coverage
BuildRequires: unicode-ucd

BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc


%package common
Summary:  Common files for the Dejavu font set
Requires: fontpackages-filesystem

Obsoletes: dejavu-fonts-doc < 2.26-6
Obsoletes: dejavu-fonts-compat < 2.29-3
Obsoletes: dejavu-fonts-lgc-compat < 2.29-3

Provides: dejavu-fonts-common = %{version}-%{release}
Conflicts: dejavu-fonts-common

%description common
%common_desc

This package consists of files used by other DejaVu packages.


%package -n %{fontname}-ib-sans-fonts
Summary:  Variable-width sans-serif font faces
Requires: %{name}-common = %{version}-%{release}

Obsoletes: dejavu-fonts-sans < 2.28-2

Provides: %{fontname}-sans-fonts = %{version}-%{release}
Conflicts: %{fontname}-sans-fonts
Obsoletes: %{fontname}-lgc-sans-fonts
Provides: %{fontname}-lgc-sans-fonts = %{version}-%{release}

%description -n %{fontname}-ib-sans-fonts
%common_desc

This package consists of the DejaVu sans-serif variable-width font faces, in
their unabridged version.

%_font_pkg -n sans -f *-%{fontname}-sans.conf DejaVuSans.ttf DejaVuSans-*.ttf DejaVuSansCondensed*.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml


%package -n %{fontname}-ib-serif-fonts
Summary:  Variable-width serif font faces
Requires: %{name}-common = %{version}-%{release}

Obsoletes: %{fontname}-fonts-serif < 2.28-2

Provides: %{fontname}-serif-fonts = %{version}-%{release}
Conflicts: %{fontname}-serif-fonts
Obsoletes: %{fontname}-lgc-serif-fonts
Provides: %{fontname}-lgc-serif-fonts = %{version}-%{release}

%description -n %{fontname}-ib-serif-fonts
%common_desc

This package consists of the DejaVu serif variable-width font faces, in their
unabridged version.

%_font_pkg -n serif -f *-%{fontname}-serif.conf DejaVuSerif.ttf DejaVuSerif-*.ttf DejaVuSerifCondensed*.ttf
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml


%package -n %{fontname}-ib-sans-mono-fonts
Summary:  Monospace sans-serif font faces
Requires: %{name}-common = %{version}-%{release}

Obsoletes: %{fontname}-fonts-sans-mono < 2.28-2

Provides: %{fontname}-sans-mono-fonts = %{version}-%{release}
Conflicts: %{fontname}-sans-mono-fonts
Obsoletes: %{fontname}-lgc-sans-mono-fonts
Provides: %{fontname}-lgc-sans-mono-fonts = %{version}-%{release}

%description -n %{fontname}-ib-sans-mono-fonts
%common_desc

This package consists of the DejaVu sans-serif monospace font faces, in their
unabridged version.

%_font_pkg -n sans-mono -f *-%{fontname}-sans-mono.conf DejaVuSansMono*.ttf
%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml

%prep
%setup -q -n %{archivename}

%build
make %{?_smp_mflags} VERSION=%{version} FC-LANG="" \
     BLOCKS=/usr/share/unicode/ucd/Blocks.txt UNICODEDATA=/usr/share/unicode/ucd/UnicodeData.txt

# Stop the desktop people from complaining this file is too big
bzip2 -9 build/status.txt


%check
make check


%install
rm -fr %{buildroot}
rm build/DejaVuLGC*.ttf

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p build/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-dejavu-sans.conf %{buildroot}%{_fontconfig_confdir}/45-dejavu-sans.conf
ln -s %{_fontconfig_templatedir}/45-dejavu-sans-mono.conf %{buildroot}%{_fontconfig_confdir}/45-dejavu-sans-mono.conf
ln -s %{_fontconfig_templatedir}/45-dejavu-serif.conf %{buildroot}%{_fontconfig_confdir}/45-dejavu-serif.conf
ln -s %{_fontconfig_templatedir}/90-tt-dejavu-sans.conf %{buildroot}%{_fontconfig_confdir}/90-tt-dejavu-sans.conf
ln -s %{_fontconfig_templatedir}/90-tt-dejavu-sans-mono.conf %{buildroot}%{_fontconfig_confdir}/90-tt-dejavu-sans-mono.conf
ln -s %{_fontconfig_templatedir}/90-tt-dejavu-serif.conf %{buildroot}%{_fontconfig_confdir}/90-tt-dejavu-serif.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%clean
rm -fr %{buildroot}


%files common
%defattr(0644,root,root,0755)
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc AUTHORS BUGS LICENSE NEWS README
%doc build/unicover.txt build/status.txt.bz2


%changelog
* Tue Nov 10 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.35-1
- Infinality patched font based on dejavu-fonts-2.35-2.fc23
