%global fontname    gelasio

Name:    %{fontname}-ib-fonts
Version: 1.00
Release: 1%{?dist}
Summary: Gelasio fonts

License:   OFL
URL:       www.sorkintype.com
Source0:   https://googlefontdirectory.googlecode.com/hg-history/325e7174147acd060cb6dfe982cf57594a180d53/ofl/gelasio/Gelasio-Bold.ttf
Source1:   https://googlefontdirectory.googlecode.com/hg-history/325e7174147acd060cb6dfe982cf57594a180d53/ofl/gelasio/Gelasio-BoldItalic.ttf
Source2:   https://googlefontdirectory.googlecode.com/hg-history/325e7174147acd060cb6dfe982cf57594a180d53/ofl/gelasio/Gelasio-Italic.ttf
Source3:   https://googlefontdirectory.googlecode.com/hg-history/325e7174147acd060cb6dfe982cf57594a180d53/ofl/gelasio/Gelasio-Regular.ttf
Source4:   https://googlefontdirectory.googlecode.com/hg-history/325e7174147acd060cb6dfe982cf57594a180d53/ofl/gelasio/OFL.txt
Source5:   45-gelasio.conf
Source6:   90-tt-gelasio.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Gelasio fonts

%prep
install -m 0644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .
sed -i 's/\r$//' OFL.txt

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-gelasio.conf %{buildroot}%{_fontconfig_confdir}/45-gelasio.conf
ln -s %{_fontconfig_templatedir}/90-tt-gelasio.conf %{buildroot}%{_fontconfig_confdir}/90-tt-gelasio.conf
cd %{_builddir}

%_font_pkg -f *-%{fontname}.conf *.ttf

%doc OFL.txt

%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.00-1
- First version
