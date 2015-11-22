%global fontname    quintessential

Name:    %{fontname}-ib-fonts
Version: 1.001
Release: 1%{?dist}
Summary: Quintessential fonts

License:   OFL
URL:       https://plus.google.com/110671794147246487935/about
# https://github.com/google/fonts/tree/master/ofl/quintessential
Source0:   http://googlefontdirectory.googlecode.com/hg/ofl/quintessential/src/Quintessential-Regular.otf
Source1:   45-quintessential.conf
Source2:   90-non-tt-quintessential.conf
Source3:   http://googlefontdirectory.googlecode.com/hg/ofl/quintessential/OFL.txt
Source4:   http://googlefontdirectory.googlecode.com/hg/ofl/quintessential/FONTLOG.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
The Quintessential typeface is a calligraphic lettering style based on the
Italic Hand. Infinality version.

%prep
install -m 0644 %{SOURCE3} %{SOURCE4} %{_builddir}

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-quintessential.conf %{buildroot}%{_fontconfig_confdir}/45-quintessential.conf
ln -s %{_fontconfig_templatedir}/90-non-tt-quintessential.conf %{buildroot}%{_fontconfig_confdir}/90-non-tt-quintessential.conf
cd %{_builddir}

%_font_pkg -f *-%{fontname}.conf *.otf

%doc OFL.txt FONTLOG.txt

%changelog
* Sat Nov 21 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1.001-1
- First version
