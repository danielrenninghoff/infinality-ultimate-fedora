%global fontname    merriweather-sans

Name:    %{fontname}-ib-fonts
Version: 1.003
Release: 1%{?dist}
Summary: Merriweather Sans fonts

License:   OFL
URL:       http://www.sorkintype.com
Source0:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/MerriweatherSans-ExtraBold.ttf
Source1:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/MerriweatherSans-Bold.ttf
Source2:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/MerriweatherSans-BoldItalic.ttf
Source3:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/MerriweatherSans-ExtraBoldItalic.ttf
Source4:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/MerriweatherSans-Italic.ttf
Source5:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/MerriweatherSans-Light.ttf
Source6:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/MerriweatherSans-LightItalic.ttf
Source7:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/MerriweatherSans-Regular.ttf
Source8:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/OFL.txt
Source9:   https://github.com/google/fonts/raw/master/ofl/merriweathersans/FONTLOG.txt
Source10:  45-merriweather-sans.conf
Source11:  90-tt-merriweather-sans.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Merriweather Sans fonts

%prep
install -m 0644 %{SOURCE8} %{SOURCE9} .
sed -i 's/\r$//' OFL.txt

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-merriweather-sans.conf %{buildroot}%{_fontconfig_confdir}/45-merriweather-sans.conf
ln -s %{_fontconfig_templatedir}/90-tt-merriweather-sans.conf %{buildroot}%{_fontconfig_confdir}/90-tt-merriweather-sans.conf
cd %{_builddir}

%_font_pkg -f *-%{fontname}.conf *.ttf

%doc OFL.txt FONTLOG.txt

%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.003-1
- First version
