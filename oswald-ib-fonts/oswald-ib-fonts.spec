%global fontname    oswald

Name:    %{fontname}-ib-fonts
Version: 3.0
Release: 1%{?dist}
Summary: Oswald fonts

Group:     User Interface/X
License:   OFL
URL:       http://oswaldfont.com
# commit 9dd0521c8c06dd24998fe5d9cd644dab9cbbacca from the github repo, available at
# https://github.com/vernnobile/OswaldFont.git
Source0:   OswaldFont-master.zip
Source1:   45-oswald.conf
Source2:   90-non-tt-oswald.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Oswald fonts for Infinality.

%prep
%setup -q -n "OswaldFont-master/3.0"

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p {Italic,Roman}/[2-8]00/src/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-oswald.conf %{buildroot}%{_fontconfig_confdir}/45-oswald.conf
ln -s %{_fontconfig_templatedir}/90-non-tt-oswald.conf %{buildroot}%{_fontconfig_confdir}/90-non-tt-oswald.conf
chmod 0644 OFL.txt
sed -i 's/\r$//' OFL.txt

%_font_pkg -f *-%{fontname}.conf *.otf

%doc FONTLOG.txt OFL.txt README

%changelog
* Tue Nov 10 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 3.0-1
- First version
