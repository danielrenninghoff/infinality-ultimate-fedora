%global fontname    merriweather

Name:    %{fontname}-ib-fonts
Version: 1.583
Release: 1%{?dist}
Summary: Merriweather fonts

License:   OFL
URL:       www.sorkintype.com
Source0:   https://github.com/google/fonts/raw/master/ofl/merriweather/Merriweather-Black.ttf
Source1:   https://github.com/google/fonts/raw/master/ofl/merriweather/Merriweather-Bold.ttf
Source2:   https://github.com/google/fonts/raw/master/ofl/merriweather/Merriweather-BoldItalic.ttf
Source3:   https://github.com/google/fonts/raw/master/ofl/merriweather/Merriweather-BlackItalic.ttf
Source4:   https://github.com/google/fonts/raw/master/ofl/merriweather/Merriweather-Italic.ttf
Source5:   https://github.com/google/fonts/raw/master/ofl/merriweather/Merriweather-Light.ttf
Source6:   https://github.com/google/fonts/raw/master/ofl/merriweather/Merriweather-LightItalic.ttf
Source7:   https://github.com/google/fonts/raw/master/ofl/merriweather/Merriweather-Regular.ttf
Source8:   https://github.com/google/fonts/raw/master/ofl/merriweather/OFL.txt
Source9:   https://github.com/google/fonts/raw/master/ofl/merriweather/FONTLOG.txt
Source10:  45-merriweather.conf
Source11:  90-tt-merriweather.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Merriweather fonts

%prep
install -m 0644 %{SOURCE8} %{SOURCE9} .

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-merriweather.conf %{buildroot}%{_fontconfig_confdir}/45-merriweather.conf
ln -s %{_fontconfig_templatedir}/90-tt-merriweather.conf %{buildroot}%{_fontconfig_confdir}/90-tt-merriweather.conf
cd %{_builddir}

%_font_pkg -f *-%{fontname}.conf *.ttf

%doc OFL.txt FONTLOG.txt

%changelog
* Sat Mar 12 2016 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.583-1
- Updated to version 1.583.

* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.4-1
- First version
