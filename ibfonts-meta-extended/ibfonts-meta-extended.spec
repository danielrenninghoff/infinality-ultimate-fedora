Name:           ibfonts-meta-extended
Version:        1
Release:        2%{?dist}
Summary:        Meta package for extended infinality fonts

License:        GPL
URL:            https://github.com/bohoomil/fontconfig-ultimate

BuildArch:      noarch
Requires:       ibfonts-meta-extended-lt
Requires:       ddc-uchen-ib-fonts
Requires:       lohit-gurmukhi-ib-fonts
Requires:       lohit-odia-ib-fonts
Requires:       texlive-tex-gyre-ib
Requires:       cursor-ib-fonts
Requires:       urw-ib-fonts
Requires:       google-noto-ib-cjk-fonts

%description
Meta package for extended infinality fonts.

%prep


%build


%install


%files


%changelog
* Thu Apr 07 2016 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1-2
- link to correct tex-gyre.

* Mon Nov 16 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 1-1
- First version.
