%global fontname lohit-odia

Name:           %{fontname}-ib-fonts
Version:        2.91.0
Release:        1%{?dist}
Summary:        Free truetype font for Odia language

License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
Source1:        40-lohit-odia.conf
Source2:        66-lohit-odia.conf
Source3:        90-tt-lohit-odia.conf
Source4:        %{fontname}.metainfo.xml
BuildArch:      noarch
BuildRequires:  fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Provides:       lohit-oriya-fonts = %{version}-%{release}
Provides:       lohit-odia-fonts = %{version}-%{release}
Conflicts:      lohit-odia-fonts
Obsoletes:      lohit-oriya-fonts < 2.5.4.1-4

%description
This package provides a free truetype font for Odia language.

%prep
%setup -q -n %{fontname}-%{version} 

%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/40-lohit-odia.conf
ln -s %{_fontconfig_templatedir}/40-lohit-odia.conf \
      %{buildroot}%{_fontconfig_confdir}/40-lohit-odia.conf

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/66-lohit-odia.conf
ln -s %{_fontconfig_templatedir}/66-lohit-odia.conf \
      %{buildroot}%{_fontconfig_confdir}/66-lohit-odia.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/90-tt-lohit-odia.conf
ln -s %{_fontconfig_templatedir}/90-tt-lohit-odia.conf \
      %{buildroot}%{_fontconfig_confdir}/90-tt-lohit-odia.conf


# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f *.conf *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Sun Nov 22 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 2.91.0-1
- based on lohit-odia-fonts-2.91.0-2
