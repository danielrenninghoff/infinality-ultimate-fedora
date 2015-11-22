%global fontname    cantoraone

Name:    %{fontname}-ib-fonts
Version: 1.1
Release: 1%{?dist}
Summary: CantoraOne fonts

License:   OFL
URL:       http://www.impallari.com
Source0:   http://www.impallari.com/media/uploads/prosources/update-67-source.zip
Source1:   45-%{fontname}.conf
Source2:   90-tt-%{fontname}.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Cantora ('Singer' in Spanish) is a friendly semi formal, semi condensed, semi
sans serif. It has reminiscences of hand lettering, mixing straight and bowed
stems, and natural curves.

%prep
%setup -q -n CantoraOne-v1.1

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p CantoraOne-Regular.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-%{fontname}.conf %{buildroot}%{_fontconfig_confdir}/45-%{fontname}.conf
ln -s %{_fontconfig_templatedir}/90-tt-%{fontname}.conf %{buildroot}%{_fontconfig_confdir}/90-tt-%{fontname}.conf
chmod 0644 OFL.txt FONTLOG.txt
sed -i 's/\r$//' OFL.txt

%_font_pkg -f *-%{fontname}.conf *.ttf

%doc OFL.txt FONTLOG.txt

%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.1-1
- First version
