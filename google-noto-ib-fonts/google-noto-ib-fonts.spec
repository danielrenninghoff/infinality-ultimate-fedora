%global fontname google-noto

Name:           %{fontname}-ib-fonts
Version:        20150929
Release:        1%{?dist}
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
Group:          User Interface/X
License:        ASL 2.0
URL:            http://www.google.com/get/noto/
Source0:        noto-fonts-2015-09-29-license-adobe.tar.gz
Source3:        40-noto-arabic.conf
Source4:        45-noto-cros.conf
Source5:        45-noto-nonlatin.conf
Source6:        45-noto-sans.conf
Source7:        45-noto-serif.conf
Source8:        90-tt-noto-cros.conf
Source9:        90-tt-noto-nonlatin.conf
Source10:       90-tt-noto-sans.conf
Source11:       90-tt-noto-serif.conf

# Add appstream metadata files
Source200:      %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

Provides: google-noto-kufi-arabic-fonts = %{version}-%{release}
Provides: google-noto-naskh-arabic-fonts = %{version}-%{release}
Provides: google-noto-naskh-arabic-ui-fonts-fonts = %{version}-%{release}
Provides: google-noto-sans-fonts = %{version}-%{release}
Provides: google-noto-sans-armenian-fonts = %{version}-%{release}
Provides: google-noto-sans-avestan-fonts = %{version}-%{release}
Provides: google-noto-sans-balinese-fonts = %{version}-%{release}
Provides: google-noto-sans-bamum-fonts = %{version}-%{release}
Provides: google-noto-sans-batak-fonts = %{version}-%{release}
Provides: google-noto-sans-bengali-fonts = %{version}-%{release}
Provides: google-noto-sans-bengali-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-brahmi-fonts = %{version}-%{release}
Provides: google-noto-sans-buginese-fonts = %{version}-%{release}
Provides: google-noto-sans-buhid-fonts = %{version}-%{release}
Provides: google-noto-sans-canadian-aboriginal-fonts = %{version}-%{release}
Provides: google-noto-sans-carian-fonts = %{version}-%{release}
Provides: google-noto-sans-cham-fonts = %{version}-%{release}
Provides: google-noto-sans-cherokee-fonts = %{version}-%{release}
Provides: google-noto-sans-coptic-fonts = %{version}-%{release}
Provides: google-noto-sans-cuneiform-fonts = %{version}-%{release}
Provides: google-noto-sans-cypriot-fonts = %{version}-%{release}
Provides: google-noto-sans-deseret-fonts = %{version}-%{release}
Provides: google-noto-sans-devanagari-fonts = %{version}-%{release}
Provides: google-noto-sans-devanagari-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-egyptian-hieroglyphs-fonts = %{version}-%{release}
Provides: google-noto-sans-ethiopic-fonts = %{version}-%{release}
Provides: google-noto-sans-georgian-fonts = %{version}-%{release}
Provides: google-noto-sans-glagolitic-fonts = %{version}-%{release}
Provides: google-noto-sans-gothic-fonts = %{version}-%{release}
Provides: google-noto-sans-gujarati-fonts = %{version}-%{release}
Provides: google-noto-sans-gujarati-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-gurmukhi-fonts = %{version}-%{release}
Provides: google-noto-sans-gurmukhi-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-hanunoo-fonts = %{version}-%{release}
Provides: google-noto-sans-hebrew-fonts = %{version}-%{release}
Provides: google-noto-sans-imperial-aramaic-fonts = %{version}-%{release}
Provides: google-noto-sans-inscriptional-pahlavi-fonts = %{version}-%{release}
Provides: google-noto-sans-inscriptional-parthian-fonts = %{version}-%{release}
Provides: google-noto-sans-javanese-fonts = %{version}-%{release}
Provides: google-noto-sans-kaithi-fonts = %{version}-%{release}
Provides: google-noto-sans-kannada-fonts = %{version}-%{release}
Provides: google-noto-sans-kannada-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-kayah-li-fonts = %{version}-%{release}
Provides: google-noto-sans-kharoshthi-fonts = %{version}-%{release}
Provides: google-noto-sans-khmer-fonts = %{version}-%{release}
Provides: google-noto-sans-khmer-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-lao-fonts = %{version}-%{release}
Provides: google-noto-sans-lao-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-lepcha-fonts = %{version}-%{release}
Provides: google-noto-sans-limbu-fonts = %{version}-%{release}
Provides: google-noto-sans-linear-b-fonts = %{version}-%{release}
Provides: google-noto-sans-lisu-fonts = %{version}-%{release}
Provides: google-noto-sans-lycian-fonts = %{version}-%{release}
Provides: google-noto-sans-lydian-fonts = %{version}-%{release}
Provides: google-noto-sans-malayalam-fonts = %{version}-%{release}
Provides: google-noto-sans-malayalam-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-mandaic-fonts = %{version}-%{release}
Provides: google-noto-sans-meetei-mayek-fonts = %{version}-%{release}
Provides: google-noto-sans-mongolian-fonts = %{version}-%{release}
Provides: google-noto-sans-myanmar-fonts = %{version}-%{release}
Provides: google-noto-sans-myanmar-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-new-tai-lue-fonts = %{version}-%{release}
Provides: google-noto-sans-nko-fonts = %{version}-%{release}
Provides: google-noto-sans-ogham-fonts = %{version}-%{release}
Provides: google-noto-sans-ol-chiki-fonts = %{version}-%{release}
Provides: google-noto-sans-old-italic-fonts = %{version}-%{release}
Provides: google-noto-sans-old-persian-fonts = %{version}-%{release}
Provides: google-noto-sans-old-south-arabian-fonts = %{version}-%{release}
Provides: google-noto-sans-old-turkic-fonts = %{version}-%{release}
Provides: google-noto-sans-osmanya-fonts = %{version}-%{release}
Provides: google-noto-sans-phags-pa-fonts = %{version}-%{release}
Provides: google-noto-sans-phoenician-fonts = %{version}-%{release}
Provides: google-noto-sans-rejang-fonts = %{version}-%{release}
Provides: google-noto-sans-runic-fonts = %{version}-%{release}
Provides: google-noto-sans-samaritan-fonts = %{version}-%{release}
Provides: google-noto-sans-saurashtra-fonts = %{version}-%{release}
Provides: google-noto-sans-shavian-fonts = %{version}-%{release}
Provides: google-noto-sans-sinhala-fonts = %{version}-%{release}
Provides: google-noto-sans-sundanese-fonts = %{version}-%{release}
Provides: google-noto-sans-syloti-nagri-fonts = %{version}-%{release}
Provides: google-noto-sans-symbols-fonts = %{version}-%{release}
Provides: google-noto-sans-syriac-eastern-fonts = %{version}-%{release}
Provides: google-noto-sans-syriac-estrangela-fonts = %{version}-%{release}
Provides: google-noto-sans-syriac-western-fonts = %{version}-%{release}
Provides: google-noto-sans-tagalog-fonts = %{version}-%{release}
Provides: google-noto-sans-tagbanwa-fonts = %{version}-%{release}
Provides: google-noto-sans-tai-le-fonts = %{version}-%{release}
Provides: google-noto-sans-tai-tham-fonts = %{version}-%{release}
Provides: google-noto-sans-tai-viet-fonts = %{version}-%{release}
Provides: google-noto-sans-tamil-fonts = %{version}-%{release}
Provides: google-noto-sans-tamil-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-telugu-fonts = %{version}-%{release}
Provides: google-noto-sans-telugu-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-thaana-fonts = %{version}-%{release}
Provides: google-noto-sans-thai-fonts = %{version}-%{release}
Provides: google-noto-sans-thai-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-tifinagh-fonts = %{version}-%{release}
Provides: google-noto-sans-ugaritic-fonts = %{version}-%{release}
Provides: google-noto-sans-ui-fonts = %{version}-%{release}
Provides: google-noto-sans-vai-fonts = %{version}-%{release}
Provides: google-noto-sans-yi-fonts = %{version}-%{release}
Provides: google-noto-serif-fonts = %{version}-%{release}
Provides: google-noto-serif-armenian-fonts = %{version}-%{release}
Provides: google-noto-serif-georgian-fonts = %{version}-%{release}
Provides: google-noto-serif-khmer-fonts = %{version}-%{release}
Provides: google-noto-serif-lao-fonts = %{version}-%{release}
Provides: google-noto-serif-thai-fonts = %{version}-%{release}
Provides: google-noto-sans-oriya-fonts = %{version}-%{release}
Provides: google-noto-sans-oriya-ui = %{version}-%{release}
Provides: google-noto-fonts-common = %{version}-%{release}

Conflicts: google-noto-kufi-arabic-fonts
Conflicts: google-noto-naskh-arabic-fonts
Conflicts: google-noto-naskh-arabic-ui-fonts-fonts
Conflicts: google-noto-sans-fonts
Conflicts: google-noto-sans-armenian-fonts
Conflicts: google-noto-sans-avestan-fonts
Conflicts: google-noto-sans-balinese-fonts
Conflicts: google-noto-sans-bamum-fonts
Conflicts: google-noto-sans-batak-fonts
Conflicts: google-noto-sans-bengali-fonts
Conflicts: google-noto-sans-bengali-ui-fonts
Conflicts: google-noto-sans-brahmi-fonts
Conflicts: google-noto-sans-buginese-fonts
Conflicts: google-noto-sans-buhid-fonts
Conflicts: google-noto-sans-canadian-aboriginal-fonts
Conflicts: google-noto-sans-carian-fonts
Conflicts: google-noto-sans-cham-fonts
Conflicts: google-noto-sans-cherokee-fonts
Conflicts: google-noto-sans-coptic-fonts
Conflicts: google-noto-sans-cuneiform-fonts
Conflicts: google-noto-sans-cypriot-fonts
Conflicts: google-noto-sans-deseret-fonts
Conflicts: google-noto-sans-devanagari-fonts
Conflicts: google-noto-sans-devanagari-ui-fonts
Conflicts: google-noto-sans-egyptian-hieroglyphs-fonts
Conflicts: google-noto-sans-ethiopic-fonts
Conflicts: google-noto-sans-georgian-fonts
Conflicts: google-noto-sans-glagolitic-fonts
Conflicts: google-noto-sans-gothic-fonts
Conflicts: google-noto-sans-gujarati-fonts
Conflicts: google-noto-sans-gujarati-ui-fonts
Conflicts: google-noto-sans-gurmukhi-fonts
Conflicts: google-noto-sans-gurmukhi-ui-fonts
Conflicts: google-noto-sans-hanunoo-fonts
Conflicts: google-noto-sans-hebrew-fonts
Conflicts: google-noto-sans-imperial-aramaic-fonts
Conflicts: google-noto-sans-inscriptional-pahlavi-fonts
Conflicts: google-noto-sans-inscriptional-parthian-fonts
Conflicts: google-noto-sans-javanese-fonts
Conflicts: google-noto-sans-kaithi-fonts
Conflicts: google-noto-sans-kannada-fonts
Conflicts: google-noto-sans-kannada-ui-fonts
Conflicts: google-noto-sans-kayah-li-fonts
Conflicts: google-noto-sans-kharoshthi-fonts
Conflicts: google-noto-sans-khmer-fonts
Conflicts: google-noto-sans-khmer-ui-fonts
Conflicts: google-noto-sans-lao-fonts
Conflicts: google-noto-sans-lao-ui-fonts
Conflicts: google-noto-sans-lepcha-fonts
Conflicts: google-noto-sans-limbu-fonts
Conflicts: google-noto-sans-linear-b-fonts
Conflicts: google-noto-sans-lisu-fonts
Conflicts: google-noto-sans-lycian-fonts
Conflicts: google-noto-sans-lydian-fonts
Conflicts: google-noto-sans-malayalam-fonts
Conflicts: google-noto-sans-malayalam-ui-fonts
Conflicts: google-noto-sans-mandaic-fonts
Conflicts: google-noto-sans-meetei-mayek-fonts
Conflicts: google-noto-sans-mongolian-fonts
Conflicts: google-noto-sans-myanmar-fonts
Conflicts: google-noto-sans-myanmar-ui-fonts
Conflicts: google-noto-sans-new-tai-lue-fonts
Conflicts: google-noto-sans-nko-fonts
Conflicts: google-noto-sans-ogham-fonts
Conflicts: google-noto-sans-ol-chiki-fonts
Conflicts: google-noto-sans-old-italic-fonts
Conflicts: google-noto-sans-old-persian-fonts
Conflicts: google-noto-sans-old-south-arabian-fonts
Conflicts: google-noto-sans-old-turkic-fonts
Conflicts: google-noto-sans-osmanya-fonts
Conflicts: google-noto-sans-phags-pa-fonts
Conflicts: google-noto-sans-phoenician-fonts
Conflicts: google-noto-sans-rejang-fonts
Conflicts: google-noto-sans-runic-fonts
Conflicts: google-noto-sans-samaritan-fonts
Conflicts: google-noto-sans-saurashtra-fonts
Conflicts: google-noto-sans-shavian-fonts
Conflicts: google-noto-sans-sinhala-fonts
Conflicts: google-noto-sans-sundanese-fonts
Conflicts: google-noto-sans-syloti-nagri-fonts
Conflicts: google-noto-sans-symbols-fonts
Conflicts: google-noto-sans-syriac-eastern-fonts
Conflicts: google-noto-sans-syriac-estrangela-fonts
Conflicts: google-noto-sans-syriac-western-fonts
Conflicts: google-noto-sans-tagalog-fonts
Conflicts: google-noto-sans-tagbanwa-fonts
Conflicts: google-noto-sans-tai-le-fonts
Conflicts: google-noto-sans-tai-tham-fonts
Conflicts: google-noto-sans-tai-viet-fonts
Conflicts: google-noto-sans-tamil-fonts
Conflicts: google-noto-sans-tamil-ui-fonts
Conflicts: google-noto-sans-telugu-fonts
Conflicts: google-noto-sans-telugu-ui-fonts
Conflicts: google-noto-sans-thaana-fonts
Conflicts: google-noto-sans-thai-fonts
Conflicts: google-noto-sans-thai-ui-fonts
Conflicts: google-noto-sans-tifinagh-fonts
Conflicts: google-noto-sans-ugaritic-fonts
Conflicts: google-noto-sans-ui-fonts
Conflicts: google-noto-sans-vai-fonts
Conflicts: google-noto-sans-yi-fonts
Conflicts: google-noto-serif-fonts
Conflicts: google-noto-serif-armenian-fonts
Conflicts: google-noto-serif-georgian-fonts
Conflicts: google-noto-serif-khmer-fonts
Conflicts: google-noto-serif-lao-fonts
Conflicts: google-noto-serif-thai-fonts
Conflicts: google-noto-sans-oriya-fonts
Conflicts: google-noto-sans-oriya-ui
Conflicts: google-noto-fonts-common

%description
Noto fonts aims to remove tofu from web by providing fonts for all
Unicode supported scripts. Its design goal is to achieve visual harmonization
between multiple scripts. Noto family supports almost all scripts available
in Unicode.

%prep
%setup -q -n noto-fonts-2015-09-29-license-adobe

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %_builddir/noto-fonts-2015-09-29-license-adobe/hinted/Noto*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE4} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}

ln -s %{_fontconfig_templatedir}/40-noto-arabic.conf %{buildroot}%{_fontconfig_confdir}/40-noto-arabic.conf
ln -s %{_fontconfig_templatedir}/45-noto-cros.conf %{buildroot}%{_fontconfig_confdir}/45-noto-cros.conf
ln -s %{_fontconfig_templatedir}/45-noto-nonlatin.conf %{buildroot}%{_fontconfig_confdir}/45-noto-nonlatin.conf
ln -s %{_fontconfig_templatedir}/45-noto-sans.conf %{buildroot}%{_fontconfig_confdir}/45-noto-sans.conf
ln -s %{_fontconfig_templatedir}/45-noto-serif.conf %{buildroot}%{_fontconfig_confdir}/45-noto-serif.conf
ln -s %{_fontconfig_templatedir}/90-tt-noto-cros.conf %{buildroot}%{_fontconfig_confdir}/90-tt-noto-cros.conf
ln -s %{_fontconfig_templatedir}/90-tt-noto-nonlatin.conf %{buildroot}%{_fontconfig_confdir}/90-tt-noto-nonlatin.conf
ln -s %{_fontconfig_templatedir}/90-tt-noto-sans.conf %{buildroot}%{_fontconfig_confdir}/90-tt-noto-sans.conf
ln -s %{_fontconfig_templatedir}/90-tt-noto-serif.conf %{buildroot}%{_fontconfig_confdir}/90-tt-noto-serif.conf

# Add appstream metadata
install -Dm 0644 -p %{SOURCE200} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml


%_font_pkg -f *.conf *.ttf
%doc LICENSE
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Wed Nov 11 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 20150929-1
- Based on google-noto-fonts 20150417-2.
