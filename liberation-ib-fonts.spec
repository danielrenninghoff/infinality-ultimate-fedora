%global fontname liberation
%global fontconf1 45-%{fontname}
%global fontconf2 90-tt-%{fontname}
%global archivename %{fontname}-fonts-%{version}
%global narrowver 1.07.4
%global common_desc \
The Liberation Fonts are intended to be replacements for the three most \
commonly used fonts on Microsoft systems: Times New Roman, Arial, and Courier \
New.

%define catalogue %{_sysconfdir}/X11/fontpath.d

Name:             %{fontname}-ib-fonts
Summary:          Fonts to replace commonly used Microsoft Windows fonts
Version:          2.00.1
Release:          1%{?dist}
Epoch:            1
# The license of the Liberation Fonts is a EULA that contains GPLv2 and two
# exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like the one in
# GPLv3. This license is Free, but GPLv2 and GPLv3 incompatible.
License:          Liberation
Group:            User Interface/X
URL:              http://fedorahosted.org/liberation-fonts/
Source0:          https://fedorahosted.org/releases/l/i/liberation-fonts/%{archivename}.tar.gz
Source1:          https://fedorahosted.org/releases/l/i/liberation-fonts/liberation-fonts-%{narrowver}.tar.gz
Source2:          45-liberation-mono.conf
Source3:          45-liberation-narrow.conf
Source4:          45-liberation-sans.conf
Source5:          45-liberation-serif.conf
Source6:          90-tt-liberation-mono.conf
Source7:          90-tt-liberation-narrow.conf
Source8:          90-tt-liberation-sans.conf
Source9:          90-tt-liberation-serif.conf
Source10:         %{fontname}.metainfo.xml
Source11:         %{fontname}-mono.metainfo.xml
Source12:         %{fontname}-sans.metainfo.xml
Source13:         %{fontname}-serif.metainfo.xml
Source14:         %{fontname}-narrow.metainfo.xml
BuildArch:        noarch

BuildRequires:    fontpackages-devel >= 1.13, xorg-x11-font-utils
BuildRequires:    fontforge
BuildRequires:    python2-fonttools

Requires:         %{fontname}-mono-fonts = %{epoch}:%{version}-%{release}
Requires:         %{fontname}-narrow-fonts = %{epoch}:%{version}-%{release}
Requires:         %{fontname}-sans-fonts = %{epoch}:%{version}-%{release}
Requires:         %{fontname}-serif-fonts = %{epoch}:%{version}-%{release}
Provides:         %{fontname}-fonts = %{epoch}:%{version}-%{release}
Conflicts:        %{fontname}-fonts

%description
%common_desc

Meta-package of Liberation fonts which installs Sans, Serif, and Monospace,
Narrow families.

%package -n %{fontname}-ib-fonts-common
Epoch:            1
Summary:          Shared common files of Liberation font families
Group:            User Interface/X
Requires:         fontpackages-filesystem >= 1.13
Provides:         %{fontname}-fonts-common = %{epoch}:%{version}-%{release}
Conflicts:        %{fontname}-fonts-common

%description -n %{fontname}-ib-fonts-common
%common_desc

Shared common files of Liberation font families.

%files -n %{fontname}-ib-fonts-common
%doc AUTHORS ChangeLog LICENSE README TODO
%dir %{_fontdir}
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}
%{_datadir}/appdata/liberation.metainfo.xml

%package -n %{fontname}-ib-sans-fonts
Summary:      Sans-serif fonts to replace commonly used Microsoft Arial
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{epoch}:%{version}-%{release}
Provides:     %{fontname}-sans-fonts = %{epoch}:%{version}-%{release}
Conflicts:    %{fontname}-sans-fonts

%description -n %{fontname}-ib-sans-fonts
%common_desc

This is Sans-serif TrueType fonts that replaced commonly used Microsoft Arial.

%_font_pkg -n sans -f *-%{fontname}-sans.conf  LiberationSans-*.ttf
%{_datadir}/appdata/liberation-sans.metainfo.xml

%package -n %{fontname}-ib-serif-fonts
Summary:      Serif fonts to replace commonly used Microsoft Times New Roman
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{epoch}:%{version}-%{release}
Provides:     %{fontname}-serif-fonts = %{epoch}:%{version}-%{release}
Conflicts:    %{fontname}-serif-fonts

%description -n %{fontname}-ib-serif-fonts
%common_desc

This is Serif TrueType fonts that replaced commonly used Microsoft Times New \
Roman.

%_font_pkg -n serif -f *-%{fontname}-serif.conf  LiberationSerif*.ttf
%{_datadir}/appdata/liberation-serif.metainfo.xml

%package -n %{fontname}-ib-mono-fonts
Summary:      Monospace fonts to replace commonly used Microsoft Courier New
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{epoch}:%{version}-%{release}
Provides:     %{fontname}-mono-fonts = %{epoch}:%{version}-%{release}
Conflicts:    %{fontname}-mono-fonts

%description -n %{fontname}-ib-mono-fonts
%common_desc

This is Monospace TrueType fonts that replaced commonly used Microsoft Courier \
New.

%_font_pkg -n mono -f *-%{fontname}-mono.conf  LiberationMono*.ttf
%{_datadir}/appdata/liberation-mono.metainfo.xml

%package -n %{fontname}-ib-narrow-fonts
Summary:      Sans-serif Narrow fonts to replace commonly used Microsoft Arial Narrow
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{epoch}:%{version}-%{release}
Provides:     %{fontname}-narrow-fonts = %{epoch}:%{version}-%{release}
Conflicts:    %{fontname}-narrow-fonts

%description -n %{fontname}-ib-narrow-fonts
%common_desc

This is Sans-Serif Narrow TrueType fonts that replaced commonly used Microsoft \
Arial Narrow.

%_font_pkg -n narrow -f *-%{fontname}-narrow.conf LiberationSansNarrow*.ttf
%{_datadir}/appdata/liberation-narrow.metainfo.xml

%prep
%setup -q -b 1 -T -n liberation-fonts-%{narrowver}
cd ..
%setup -q -n %{archivename}

%build
make %{?_smp_mflags}
mv liberation-fonts-ttf-%{version}/* .
cd ../liberation-fonts-%{narrowver}
make %{?_smp_mflags}
mv liberation-fonts-ttf-%{narrowver}/LiberationSansNarrow*.ttf ../%{archivename}
cd ../%{archivename}


%install
# fonts .ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_fontdir} %{buildroot}%{catalogue}/%{name}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}-mono.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}-narrow.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}-sans.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}-serif.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}-mono.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}-narrow.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}-sans.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}-serif.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-narrow.metainfo.xml

for fconf in %{fontconf1}-mono.conf \
             %{fontconf1}-sans.conf \
             %{fontconf1}-serif.conf \
             %{fontconf1}-narrow.conf \
             %{fontconf2}-mono.conf \
             %{fontconf2}-sans.conf \
             %{fontconf2}-serif.conf \
             %{fontconf2}-narrow.conf \
             ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}

%changelog
* Wed Nov 11 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1:2.00.1-1
- Based on liberation-fonts 1:1.07.4-6.
