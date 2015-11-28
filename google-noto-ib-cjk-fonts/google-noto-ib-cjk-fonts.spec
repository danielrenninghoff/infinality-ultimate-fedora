%global fontname google-noto

Name:           %{fontname}-ib-cjk-fonts
Version:        20150929
Release:        1%{?dist}
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
Group:          User Interface/X
License:        ASL 2.0
URL:            http://www.google.com/get/noto/
# from https://github.com/googlei18n/noto-cjk/archive/v1.004.tar.gz, repackaged to make srpm muuuuch smaller.
Source0:        NotoSansCJK.ttc.zip
Source1:        LICENSE

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

Provides: google-noto-sans-cjk-fonts = %{version}-%{release}
Provides: google-noto-sans-japanese-fonts = %{version}-%{release}
Provides: google-noto-sans-korean-fonts = %{version}-%{release}
Provides: google-noto-sans-simplified-chinese-fonts = %{version}-%{release}
Provides: google-noto-sans-traditional-chinese-fonts = %{version}-%{release}
Conflicts: google-noto-sans-cjk-fonts
Conflicts: google-noto-sans-japanese-fonts
Conflicts: google-noto-sans-korean-fonts
Conflicts: google-noto-sans-simplified-chinese-fonts
Conflicts: google-noto-sans-traditional-chinese-fonts

%description
Noto fonts aims to remove tofu from web by providing fonts for all
Unicode supported scripts. Its design goal is to achieve visual harmonization
between multiple scripts. Noto family supports almost all scripts available
in Unicode.

%prep
%setup -q -c noto-cjk-1.004
cp %{SOURCE1} .

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p NotoSansCJK.ttc %{buildroot}%{_fontdir}

%_font_pkg NotoSansCJK.ttc
%doc LICENSE


%changelog
* Wed Nov 11 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 20150929-1
- Based on google-noto-fonts 20150417-2.
