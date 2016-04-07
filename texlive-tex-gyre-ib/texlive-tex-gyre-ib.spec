%global source_date 20150728_r37987
%global tl_version 2015
%global tl_rel 25
%global tl_release %{tl_rel}.%{source_date}%{?dist}
%global tl_noarch_release %{tl_rel}%{?dist}


%{!?_texdir: %global _texdir %{_datadir}/texlive}

Name: texlive-tex-gyre-ib
URL: http://www.gust.org.pl/projects/e-foundry/tex-gyre/

Source0: http://ctan.sharelatex.com/tex-archive/systems/texlive/tlnet/archive/tex-gyre.tar.xz
Source1: 45-tex-gyre.conf
Source2: 90-non-tt-tex-gyre.conf
Source3: gfsl.txt
Provides: texlive-tex-gyre = %{version}-%{release}
Conflicts: texlive-tex-gyre

Provides: tex-gyre-ib-fonts
Conflicts: tex-gyre-ib-fonts

Provides: tex-tex-gyre = %{tl_version}
License: GFSL
Summary: TeX Fonts extending freely available URW fonts
Version: svn18651.2.004
Release: %{tl_noarch_release}.1
BuildArch: noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Requires: texlive-base
Requires: texlive-kpathsea-bin, tex-kpathsea
Requires: texlive-tetex-bin, tex-tetex
Requires(post,postun): texlive-tetex-bin, tex-tetex, tex-hyphen-base, texlive-base, texlive-texlive.infra
Requires(post,postun): coreutils
Requires: tex(tgcursor.sty)
Requires: tex(tgheros.sty)
Requires: tex(tgchorus.sty)
Requires: tex(kvoptions.sty)
Provides: tex(q-cs-sc.enc) = %{tl_version}
Provides: tex(q-cs.enc) = %{tl_version}
Provides: tex(q-csm-sc.enc) = %{tl_version}
Provides: tex(q-csm.enc) = %{tl_version}
Provides: tex(q-cszc.enc) = %{tl_version}
Provides: tex(q-ec-sc.enc) = %{tl_version}
Provides: tex(q-ec.enc) = %{tl_version}
Provides: tex(q-l7x-sc.enc) = %{tl_version}
Provides: tex(q-l7x.enc) = %{tl_version}
Provides: tex(q-l7xzc.enc) = %{tl_version}
Provides: tex(q-qx-sc.enc) = %{tl_version}
Provides: tex(q-qx.enc) = %{tl_version}
Provides: tex(q-qxm-sc.enc) = %{tl_version}
Provides: tex(q-qxm.enc) = %{tl_version}
Provides: tex(q-qxzc.enc) = %{tl_version}
Provides: tex(q-rm-sc.enc) = %{tl_version}
Provides: tex(q-rm.enc) = %{tl_version}
Provides: tex(q-rmm-sc.enc) = %{tl_version}
Provides: tex(q-rmm.enc) = %{tl_version}
Provides: tex(q-rmzc.enc) = %{tl_version}
Provides: tex(q-t5-sc.enc) = %{tl_version}
Provides: tex(q-t5.enc) = %{tl_version}
Provides: tex(q-texnansi-sc.enc) = %{tl_version}
Provides: tex(q-texnansi.enc) = %{tl_version}
Provides: tex(q-texnansizc.enc) = %{tl_version}
Provides: tex(q-ts1.enc) = %{tl_version}
Provides: tex(qag-cs.map) = %{tl_version}
Provides: tex(qag-ec.map) = %{tl_version}
Provides: tex(qag-l7x.map) = %{tl_version}
Provides: tex(qag-qx.map) = %{tl_version}
Provides: tex(qag-rm.map) = %{tl_version}
Provides: tex(qag-t5.map) = %{tl_version}
Provides: tex(qag-texnansi.map) = %{tl_version}
Provides: tex(qag-ts1.map) = %{tl_version}
Provides: tex(qag.map) = %{tl_version}
Provides: tex(qbk-cs.map) = %{tl_version}
Provides: tex(qbk-ec.map) = %{tl_version}
Provides: tex(qbk-l7x.map) = %{tl_version}
Provides: tex(qbk-qx.map) = %{tl_version}
Provides: tex(qbk-rm.map) = %{tl_version}
Provides: tex(qbk-t5.map) = %{tl_version}
Provides: tex(qbk-texnansi.map) = %{tl_version}
Provides: tex(qbk-ts1.map) = %{tl_version}
Provides: tex(qbk.map) = %{tl_version}
Provides: tex(qcr-cs.map) = %{tl_version}
Provides: tex(qcr-ec.map) = %{tl_version}
Provides: tex(qcr-l7x.map) = %{tl_version}
Provides: tex(qcr-qx.map) = %{tl_version}
Provides: tex(qcr-rm.map) = %{tl_version}
Provides: tex(qcr-t5.map) = %{tl_version}
Provides: tex(qcr-texnansi.map) = %{tl_version}
Provides: tex(qcr-ts1.map) = %{tl_version}
Provides: tex(qcr.map) = %{tl_version}
Provides: tex(qcs-cs.map) = %{tl_version}
Provides: tex(qcs-ec.map) = %{tl_version}
Provides: tex(qcs-l7x.map) = %{tl_version}
Provides: tex(qcs-qx.map) = %{tl_version}
Provides: tex(qcs-rm.map) = %{tl_version}
Provides: tex(qcs-t5.map) = %{tl_version}
Provides: tex(qcs-texnansi.map) = %{tl_version}
Provides: tex(qcs-ts1.map) = %{tl_version}
Provides: tex(qcs.map) = %{tl_version}
Provides: tex(qhv-cs.map) = %{tl_version}
Provides: tex(qhv-ec.map) = %{tl_version}
Provides: tex(qhv-l7x.map) = %{tl_version}
Provides: tex(qhv-qx.map) = %{tl_version}
Provides: tex(qhv-rm.map) = %{tl_version}
Provides: tex(qhv-t5.map) = %{tl_version}
Provides: tex(qhv-texnansi.map) = %{tl_version}
Provides: tex(qhv-ts1.map) = %{tl_version}
Provides: tex(qhv.map) = %{tl_version}
Provides: tex(qpl-cs.map) = %{tl_version}
Provides: tex(qpl-ec.map) = %{tl_version}
Provides: tex(qpl-l7x.map) = %{tl_version}
Provides: tex(qpl-qx.map) = %{tl_version}
Provides: tex(qpl-rm.map) = %{tl_version}
Provides: tex(qpl-t5.map) = %{tl_version}
Provides: tex(qpl-texnansi.map) = %{tl_version}
Provides: tex(qpl-ts1.map) = %{tl_version}
Provides: tex(qpl.map) = %{tl_version}
Provides: tex(qtm-cs.map) = %{tl_version}
Provides: tex(qtm-ec.map) = %{tl_version}
Provides: tex(qtm-l7x.map) = %{tl_version}
Provides: tex(qtm-qx.map) = %{tl_version}
Provides: tex(qtm-rm.map) = %{tl_version}
Provides: tex(qtm-t5.map) = %{tl_version}
Provides: tex(qtm-texnansi.map) = %{tl_version}
Provides: tex(qtm-ts1.map) = %{tl_version}
Provides: tex(qtm.map) = %{tl_version}
Provides: tex(qzc-cs.map) = %{tl_version}
Provides: tex(qzc-ec.map) = %{tl_version}
Provides: tex(qzc-l7x.map) = %{tl_version}
Provides: tex(qzc-qx.map) = %{tl_version}
Provides: tex(qzc-rm.map) = %{tl_version}
Provides: tex(qzc-t5.map) = %{tl_version}
Provides: tex(qzc-texnansi.map) = %{tl_version}
Provides: tex(qzc-ts1.map) = %{tl_version}
Provides: tex(qzc.map) = %{tl_version}
Provides: tex(texgyreadventor-bold.otf) = %{tl_version}
Provides: tex(texgyreadventor-bolditalic.otf) = %{tl_version}
Provides: tex(texgyreadventor-italic.otf) = %{tl_version}
Provides: tex(texgyreadventor-regular.otf) = %{tl_version}
Provides: tex(texgyrebonum-bold.otf) = %{tl_version}
Provides: tex(texgyrebonum-bolditalic.otf) = %{tl_version}
Provides: tex(texgyrebonum-italic.otf) = %{tl_version}
Provides: tex(texgyrebonum-regular.otf) = %{tl_version}
Provides: tex(texgyrechorus-mediumitalic.otf) = %{tl_version}
Provides: tex(texgyrecursor-bold.otf) = %{tl_version}
Provides: tex(texgyrecursor-bolditalic.otf) = %{tl_version}
Provides: tex(texgyrecursor-italic.otf) = %{tl_version}
Provides: tex(texgyrecursor-regular.otf) = %{tl_version}
Provides: tex(texgyreheros-bold.otf) = %{tl_version}
Provides: tex(texgyreheros-bolditalic.otf) = %{tl_version}
Provides: tex(texgyreheros-italic.otf) = %{tl_version}
Provides: tex(texgyreheros-regular.otf) = %{tl_version}
Provides: tex(texgyreheroscn-bold.otf) = %{tl_version}
Provides: tex(texgyreheroscn-bolditalic.otf) = %{tl_version}
Provides: tex(texgyreheroscn-italic.otf) = %{tl_version}
Provides: tex(texgyreheroscn-regular.otf) = %{tl_version}
Provides: tex(texgyrepagella-bold.otf) = %{tl_version}
Provides: tex(texgyrepagella-bolditalic.otf) = %{tl_version}
Provides: tex(texgyrepagella-italic.otf) = %{tl_version}
Provides: tex(texgyrepagella-regular.otf) = %{tl_version}
Provides: tex(texgyreschola-bold.otf) = %{tl_version}
Provides: tex(texgyreschola-bolditalic.otf) = %{tl_version}
Provides: tex(texgyreschola-italic.otf) = %{tl_version}
Provides: tex(texgyreschola-regular.otf) = %{tl_version}
Provides: tex(texgyretermes-bold.otf) = %{tl_version}
Provides: tex(texgyretermes-bolditalic.otf) = %{tl_version}
Provides: tex(texgyretermes-italic.otf) = %{tl_version}
Provides: tex(texgyretermes-regular.otf) = %{tl_version}
Provides: tex(cs-qagb-sc.tfm) = %{tl_version}
Provides: tex(cs-qagb.tfm) = %{tl_version}
Provides: tex(cs-qagbi-sc.tfm) = %{tl_version}
Provides: tex(cs-qagbi.tfm) = %{tl_version}
Provides: tex(cs-qagr-sc.tfm) = %{tl_version}
Provides: tex(cs-qagr.tfm) = %{tl_version}
Provides: tex(cs-qagri-sc.tfm) = %{tl_version}
Provides: tex(cs-qagri.tfm) = %{tl_version}
Provides: tex(cs-qbkb-sc.tfm) = %{tl_version}
Provides: tex(cs-qbkb.tfm) = %{tl_version}
Provides: tex(cs-qbkbi-sc.tfm) = %{tl_version}
Provides: tex(cs-qbkbi.tfm) = %{tl_version}
Provides: tex(cs-qbkr-sc.tfm) = %{tl_version}
Provides: tex(cs-qbkr.tfm) = %{tl_version}
Provides: tex(cs-qbkri-sc.tfm) = %{tl_version}
Provides: tex(cs-qbkri.tfm) = %{tl_version}
Provides: tex(cs-qcrb-sc.tfm) = %{tl_version}
Provides: tex(cs-qcrb.tfm) = %{tl_version}
Provides: tex(cs-qcrbi-sc.tfm) = %{tl_version}
Provides: tex(cs-qcrbi.tfm) = %{tl_version}
Provides: tex(cs-qcrr-sc.tfm) = %{tl_version}
Provides: tex(cs-qcrr.tfm) = %{tl_version}
Provides: tex(cs-qcrri-sc.tfm) = %{tl_version}
Provides: tex(cs-qcrri.tfm) = %{tl_version}
Provides: tex(cs-qcsb-sc.tfm) = %{tl_version}
Provides: tex(cs-qcsb.tfm) = %{tl_version}
Provides: tex(cs-qcsbi-sc.tfm) = %{tl_version}
Provides: tex(cs-qcsbi.tfm) = %{tl_version}
Provides: tex(cs-qcsr-sc.tfm) = %{tl_version}
Provides: tex(cs-qcsr.tfm) = %{tl_version}
Provides: tex(cs-qcsri-sc.tfm) = %{tl_version}
Provides: tex(cs-qcsri.tfm) = %{tl_version}
Provides: tex(cs-qhvb-sc.tfm) = %{tl_version}
Provides: tex(cs-qhvb.tfm) = %{tl_version}
Provides: tex(cs-qhvbi-sc.tfm) = %{tl_version}
Provides: tex(cs-qhvbi.tfm) = %{tl_version}
Provides: tex(cs-qhvcb-sc.tfm) = %{tl_version}
Provides: tex(cs-qhvcb.tfm) = %{tl_version}
Provides: tex(cs-qhvcbi-sc.tfm) = %{tl_version}
Provides: tex(cs-qhvcbi.tfm) = %{tl_version}
Provides: tex(cs-qhvcr-sc.tfm) = %{tl_version}
Provides: tex(cs-qhvcr.tfm) = %{tl_version}
Provides: tex(cs-qhvcri-sc.tfm) = %{tl_version}
Provides: tex(cs-qhvcri.tfm) = %{tl_version}
Provides: tex(cs-qhvr-sc.tfm) = %{tl_version}
Provides: tex(cs-qhvr.tfm) = %{tl_version}
Provides: tex(cs-qhvri-sc.tfm) = %{tl_version}
Provides: tex(cs-qhvri.tfm) = %{tl_version}
Provides: tex(cs-qplb-sc.tfm) = %{tl_version}
Provides: tex(cs-qplb.tfm) = %{tl_version}
Provides: tex(cs-qplbi-sc.tfm) = %{tl_version}
Provides: tex(cs-qplbi.tfm) = %{tl_version}
Provides: tex(cs-qplr-sc.tfm) = %{tl_version}
Provides: tex(cs-qplr.tfm) = %{tl_version}
Provides: tex(cs-qplri-sc.tfm) = %{tl_version}
Provides: tex(cs-qplri.tfm) = %{tl_version}
Provides: tex(cs-qtmb-sc.tfm) = %{tl_version}
Provides: tex(cs-qtmb.tfm) = %{tl_version}
Provides: tex(cs-qtmbi-sc.tfm) = %{tl_version}
Provides: tex(cs-qtmbi.tfm) = %{tl_version}
Provides: tex(cs-qtmr-sc.tfm) = %{tl_version}
Provides: tex(cs-qtmr.tfm) = %{tl_version}
Provides: tex(cs-qtmri-sc.tfm) = %{tl_version}
Provides: tex(cs-qtmri.tfm) = %{tl_version}
Provides: tex(cs-qzcmi.tfm) = %{tl_version}
Provides: tex(ec-qagb-sc.tfm) = %{tl_version}
Provides: tex(ec-qagb.tfm) = %{tl_version}
Provides: tex(ec-qagbi-sc.tfm) = %{tl_version}
Provides: tex(ec-qagbi.tfm) = %{tl_version}
Provides: tex(ec-qagr-sc.tfm) = %{tl_version}
Provides: tex(ec-qagr.tfm) = %{tl_version}
Provides: tex(ec-qagri-sc.tfm) = %{tl_version}
Provides: tex(ec-qagri.tfm) = %{tl_version}
Provides: tex(ec-qbkb-sc.tfm) = %{tl_version}
Provides: tex(ec-qbkb.tfm) = %{tl_version}
Provides: tex(ec-qbkbi-sc.tfm) = %{tl_version}
Provides: tex(ec-qbkbi.tfm) = %{tl_version}
Provides: tex(ec-qbkr-sc.tfm) = %{tl_version}
Provides: tex(ec-qbkr.tfm) = %{tl_version}
Provides: tex(ec-qbkri-sc.tfm) = %{tl_version}
Provides: tex(ec-qbkri.tfm) = %{tl_version}
Provides: tex(ec-qcrb-sc.tfm) = %{tl_version}
Provides: tex(ec-qcrb.tfm) = %{tl_version}
Provides: tex(ec-qcrbi-sc.tfm) = %{tl_version}
Provides: tex(ec-qcrbi.tfm) = %{tl_version}
Provides: tex(ec-qcrr-sc.tfm) = %{tl_version}
Provides: tex(ec-qcrr.tfm) = %{tl_version}
Provides: tex(ec-qcrri-sc.tfm) = %{tl_version}
Provides: tex(ec-qcrri.tfm) = %{tl_version}
Provides: tex(ec-qcsb-sc.tfm) = %{tl_version}
Provides: tex(ec-qcsb.tfm) = %{tl_version}
Provides: tex(ec-qcsbi-sc.tfm) = %{tl_version}
Provides: tex(ec-qcsbi.tfm) = %{tl_version}
Provides: tex(ec-qcsr-sc.tfm) = %{tl_version}
Provides: tex(ec-qcsr.tfm) = %{tl_version}
Provides: tex(ec-qcsri-sc.tfm) = %{tl_version}
Provides: tex(ec-qcsri.tfm) = %{tl_version}
Provides: tex(ec-qhvb-sc.tfm) = %{tl_version}
Provides: tex(ec-qhvb.tfm) = %{tl_version}
Provides: tex(ec-qhvbi-sc.tfm) = %{tl_version}
Provides: tex(ec-qhvbi.tfm) = %{tl_version}
Provides: tex(ec-qhvcb-sc.tfm) = %{tl_version}
Provides: tex(ec-qhvcb.tfm) = %{tl_version}
Provides: tex(ec-qhvcbi-sc.tfm) = %{tl_version}
Provides: tex(ec-qhvcbi.tfm) = %{tl_version}
Provides: tex(ec-qhvcr-sc.tfm) = %{tl_version}
Provides: tex(ec-qhvcr.tfm) = %{tl_version}
Provides: tex(ec-qhvcri-sc.tfm) = %{tl_version}
Provides: tex(ec-qhvcri.tfm) = %{tl_version}
Provides: tex(ec-qhvr-sc.tfm) = %{tl_version}
Provides: tex(ec-qhvr.tfm) = %{tl_version}
Provides: tex(ec-qhvri-sc.tfm) = %{tl_version}
Provides: tex(ec-qhvri.tfm) = %{tl_version}
Provides: tex(ec-qplb-sc.tfm) = %{tl_version}
Provides: tex(ec-qplb.tfm) = %{tl_version}
Provides: tex(ec-qplbi-sc.tfm) = %{tl_version}
Provides: tex(ec-qplbi.tfm) = %{tl_version}
Provides: tex(ec-qplr-sc.tfm) = %{tl_version}
Provides: tex(ec-qplr.tfm) = %{tl_version}
Provides: tex(ec-qplri-sc.tfm) = %{tl_version}
Provides: tex(ec-qplri.tfm) = %{tl_version}
Provides: tex(ec-qtmb-sc.tfm) = %{tl_version}
Provides: tex(ec-qtmb.tfm) = %{tl_version}
Provides: tex(ec-qtmbi-sc.tfm) = %{tl_version}
Provides: tex(ec-qtmbi.tfm) = %{tl_version}
Provides: tex(ec-qtmr-sc.tfm) = %{tl_version}
Provides: tex(ec-qtmr.tfm) = %{tl_version}
Provides: tex(ec-qtmri-sc.tfm) = %{tl_version}
Provides: tex(ec-qtmri.tfm) = %{tl_version}
Provides: tex(ec-qzcmi.tfm) = %{tl_version}
Provides: tex(l7x-qagb-sc.tfm) = %{tl_version}
Provides: tex(l7x-qagb.tfm) = %{tl_version}
Provides: tex(l7x-qagbi-sc.tfm) = %{tl_version}
Provides: tex(l7x-qagbi.tfm) = %{tl_version}
Provides: tex(l7x-qagr-sc.tfm) = %{tl_version}
Provides: tex(l7x-qagr.tfm) = %{tl_version}
Provides: tex(l7x-qagri-sc.tfm) = %{tl_version}
Provides: tex(l7x-qagri.tfm) = %{tl_version}
Provides: tex(l7x-qbkb-sc.tfm) = %{tl_version}
Provides: tex(l7x-qbkb.tfm) = %{tl_version}
Provides: tex(l7x-qbkbi-sc.tfm) = %{tl_version}
Provides: tex(l7x-qbkbi.tfm) = %{tl_version}
Provides: tex(l7x-qbkr-sc.tfm) = %{tl_version}
Provides: tex(l7x-qbkr.tfm) = %{tl_version}
Provides: tex(l7x-qbkri-sc.tfm) = %{tl_version}
Provides: tex(l7x-qbkri.tfm) = %{tl_version}
Provides: tex(l7x-qcrb-sc.tfm) = %{tl_version}
Provides: tex(l7x-qcrb.tfm) = %{tl_version}
Provides: tex(l7x-qcrbi-sc.tfm) = %{tl_version}
Provides: tex(l7x-qcrbi.tfm) = %{tl_version}
Provides: tex(l7x-qcrr-sc.tfm) = %{tl_version}
Provides: tex(l7x-qcrr.tfm) = %{tl_version}
Provides: tex(l7x-qcrri-sc.tfm) = %{tl_version}
Provides: tex(l7x-qcrri.tfm) = %{tl_version}
Provides: tex(l7x-qcsb-sc.tfm) = %{tl_version}
Provides: tex(l7x-qcsb.tfm) = %{tl_version}
Provides: tex(l7x-qcsbi-sc.tfm) = %{tl_version}
Provides: tex(l7x-qcsbi.tfm) = %{tl_version}
Provides: tex(l7x-qcsr-sc.tfm) = %{tl_version}
Provides: tex(l7x-qcsr.tfm) = %{tl_version}
Provides: tex(l7x-qcsri-sc.tfm) = %{tl_version}
Provides: tex(l7x-qcsri.tfm) = %{tl_version}
Provides: tex(l7x-qhvb-sc.tfm) = %{tl_version}
Provides: tex(l7x-qhvb.tfm) = %{tl_version}
Provides: tex(l7x-qhvbi-sc.tfm) = %{tl_version}
Provides: tex(l7x-qhvbi.tfm) = %{tl_version}
Provides: tex(l7x-qhvcb-sc.tfm) = %{tl_version}
Provides: tex(l7x-qhvcb.tfm) = %{tl_version}
Provides: tex(l7x-qhvcbi-sc.tfm) = %{tl_version}
Provides: tex(l7x-qhvcbi.tfm) = %{tl_version}
Provides: tex(l7x-qhvcr-sc.tfm) = %{tl_version}
Provides: tex(l7x-qhvcr.tfm) = %{tl_version}
Provides: tex(l7x-qhvcri-sc.tfm) = %{tl_version}
Provides: tex(l7x-qhvcri.tfm) = %{tl_version}
Provides: tex(l7x-qhvr-sc.tfm) = %{tl_version}
Provides: tex(l7x-qhvr.tfm) = %{tl_version}
Provides: tex(l7x-qhvri-sc.tfm) = %{tl_version}
Provides: tex(l7x-qhvri.tfm) = %{tl_version}
Provides: tex(l7x-qplb-sc.tfm) = %{tl_version}
Provides: tex(l7x-qplb.tfm) = %{tl_version}
Provides: tex(l7x-qplbi-sc.tfm) = %{tl_version}
Provides: tex(l7x-qplbi.tfm) = %{tl_version}
Provides: tex(l7x-qplr-sc.tfm) = %{tl_version}
Provides: tex(l7x-qplr.tfm) = %{tl_version}
Provides: tex(l7x-qplri-sc.tfm) = %{tl_version}
Provides: tex(l7x-qplri.tfm) = %{tl_version}
Provides: tex(l7x-qtmb-sc.tfm) = %{tl_version}
Provides: tex(l7x-qtmb.tfm) = %{tl_version}
Provides: tex(l7x-qtmbi-sc.tfm) = %{tl_version}
Provides: tex(l7x-qtmbi.tfm) = %{tl_version}
Provides: tex(l7x-qtmr-sc.tfm) = %{tl_version}
Provides: tex(l7x-qtmr.tfm) = %{tl_version}
Provides: tex(l7x-qtmri-sc.tfm) = %{tl_version}
Provides: tex(l7x-qtmri.tfm) = %{tl_version}
Provides: tex(l7x-qzcmi.tfm) = %{tl_version}
Provides: tex(qx-qagb-sc.tfm) = %{tl_version}
Provides: tex(qx-qagb.tfm) = %{tl_version}
Provides: tex(qx-qagbi-sc.tfm) = %{tl_version}
Provides: tex(qx-qagbi.tfm) = %{tl_version}
Provides: tex(qx-qagr-sc.tfm) = %{tl_version}
Provides: tex(qx-qagr.tfm) = %{tl_version}
Provides: tex(qx-qagri-sc.tfm) = %{tl_version}
Provides: tex(qx-qagri.tfm) = %{tl_version}
Provides: tex(qx-qbkb-sc.tfm) = %{tl_version}
Provides: tex(qx-qbkb.tfm) = %{tl_version}
Provides: tex(qx-qbkbi-sc.tfm) = %{tl_version}
Provides: tex(qx-qbkbi.tfm) = %{tl_version}
Provides: tex(qx-qbkr-sc.tfm) = %{tl_version}
Provides: tex(qx-qbkr.tfm) = %{tl_version}
Provides: tex(qx-qbkri-sc.tfm) = %{tl_version}
Provides: tex(qx-qbkri.tfm) = %{tl_version}
Provides: tex(qx-qcrb-sc.tfm) = %{tl_version}
Provides: tex(qx-qcrb.tfm) = %{tl_version}
Provides: tex(qx-qcrbi-sc.tfm) = %{tl_version}
Provides: tex(qx-qcrbi.tfm) = %{tl_version}
Provides: tex(qx-qcrr-sc.tfm) = %{tl_version}
Provides: tex(qx-qcrr.tfm) = %{tl_version}
Provides: tex(qx-qcrri-sc.tfm) = %{tl_version}
Provides: tex(qx-qcrri.tfm) = %{tl_version}
Provides: tex(qx-qcsb-sc.tfm) = %{tl_version}
Provides: tex(qx-qcsb.tfm) = %{tl_version}
Provides: tex(qx-qcsbi-sc.tfm) = %{tl_version}
Provides: tex(qx-qcsbi.tfm) = %{tl_version}
Provides: tex(qx-qcsr-sc.tfm) = %{tl_version}
Provides: tex(qx-qcsr.tfm) = %{tl_version}
Provides: tex(qx-qcsri-sc.tfm) = %{tl_version}
Provides: tex(qx-qcsri.tfm) = %{tl_version}
Provides: tex(qx-qhvb-sc.tfm) = %{tl_version}
Provides: tex(qx-qhvb.tfm) = %{tl_version}
Provides: tex(qx-qhvbi-sc.tfm) = %{tl_version}
Provides: tex(qx-qhvbi.tfm) = %{tl_version}
Provides: tex(qx-qhvcb-sc.tfm) = %{tl_version}
Provides: tex(qx-qhvcb.tfm) = %{tl_version}
Provides: tex(qx-qhvcbi-sc.tfm) = %{tl_version}
Provides: tex(qx-qhvcbi.tfm) = %{tl_version}
Provides: tex(qx-qhvcr-sc.tfm) = %{tl_version}
Provides: tex(qx-qhvcr.tfm) = %{tl_version}
Provides: tex(qx-qhvcri-sc.tfm) = %{tl_version}
Provides: tex(qx-qhvcri.tfm) = %{tl_version}
Provides: tex(qx-qhvr-sc.tfm) = %{tl_version}
Provides: tex(qx-qhvr.tfm) = %{tl_version}
Provides: tex(qx-qhvri-sc.tfm) = %{tl_version}
Provides: tex(qx-qhvri.tfm) = %{tl_version}
Provides: tex(qx-qplb-sc.tfm) = %{tl_version}
Provides: tex(qx-qplb.tfm) = %{tl_version}
Provides: tex(qx-qplbi-sc.tfm) = %{tl_version}
Provides: tex(qx-qplbi.tfm) = %{tl_version}
Provides: tex(qx-qplr-sc.tfm) = %{tl_version}
Provides: tex(qx-qplr.tfm) = %{tl_version}
Provides: tex(qx-qplri-sc.tfm) = %{tl_version}
Provides: tex(qx-qplri.tfm) = %{tl_version}
Provides: tex(qx-qtmb-sc.tfm) = %{tl_version}
Provides: tex(qx-qtmb.tfm) = %{tl_version}
Provides: tex(qx-qtmbi-sc.tfm) = %{tl_version}
Provides: tex(qx-qtmbi.tfm) = %{tl_version}
Provides: tex(qx-qtmr-sc.tfm) = %{tl_version}
Provides: tex(qx-qtmr.tfm) = %{tl_version}
Provides: tex(qx-qtmri-sc.tfm) = %{tl_version}
Provides: tex(qx-qtmri.tfm) = %{tl_version}
Provides: tex(qx-qzcmi.tfm) = %{tl_version}
Provides: tex(rm-qagb-sc.tfm) = %{tl_version}
Provides: tex(rm-qagb.tfm) = %{tl_version}
Provides: tex(rm-qagbi-sc.tfm) = %{tl_version}
Provides: tex(rm-qagbi.tfm) = %{tl_version}
Provides: tex(rm-qagr-sc.tfm) = %{tl_version}
Provides: tex(rm-qagr.tfm) = %{tl_version}
Provides: tex(rm-qagri-sc.tfm) = %{tl_version}
Provides: tex(rm-qagri.tfm) = %{tl_version}
Provides: tex(rm-qbkb-sc.tfm) = %{tl_version}
Provides: tex(rm-qbkb.tfm) = %{tl_version}
Provides: tex(rm-qbkbi-sc.tfm) = %{tl_version}
Provides: tex(rm-qbkbi.tfm) = %{tl_version}
Provides: tex(rm-qbkr-sc.tfm) = %{tl_version}
Provides: tex(rm-qbkr.tfm) = %{tl_version}
Provides: tex(rm-qbkri-sc.tfm) = %{tl_version}
Provides: tex(rm-qbkri.tfm) = %{tl_version}
Provides: tex(rm-qcrb-sc.tfm) = %{tl_version}
Provides: tex(rm-qcrb.tfm) = %{tl_version}
Provides: tex(rm-qcrbi-sc.tfm) = %{tl_version}
Provides: tex(rm-qcrbi.tfm) = %{tl_version}
Provides: tex(rm-qcrr-sc.tfm) = %{tl_version}
Provides: tex(rm-qcrr.tfm) = %{tl_version}
Provides: tex(rm-qcrri-sc.tfm) = %{tl_version}
Provides: tex(rm-qcrri.tfm) = %{tl_version}
Provides: tex(rm-qcsb-sc.tfm) = %{tl_version}
Provides: tex(rm-qcsb.tfm) = %{tl_version}
Provides: tex(rm-qcsbi-sc.tfm) = %{tl_version}
Provides: tex(rm-qcsbi.tfm) = %{tl_version}
Provides: tex(rm-qcsr-sc.tfm) = %{tl_version}
Provides: tex(rm-qcsr.tfm) = %{tl_version}
Provides: tex(rm-qcsri-sc.tfm) = %{tl_version}
Provides: tex(rm-qcsri.tfm) = %{tl_version}
Provides: tex(rm-qhvb-sc.tfm) = %{tl_version}
Provides: tex(rm-qhvb.tfm) = %{tl_version}
Provides: tex(rm-qhvbi-sc.tfm) = %{tl_version}
Provides: tex(rm-qhvbi.tfm) = %{tl_version}
Provides: tex(rm-qhvcb-sc.tfm) = %{tl_version}
Provides: tex(rm-qhvcb.tfm) = %{tl_version}
Provides: tex(rm-qhvcbi-sc.tfm) = %{tl_version}
Provides: tex(rm-qhvcbi.tfm) = %{tl_version}
Provides: tex(rm-qhvcr-sc.tfm) = %{tl_version}
Provides: tex(rm-qhvcr.tfm) = %{tl_version}
Provides: tex(rm-qhvcri-sc.tfm) = %{tl_version}
Provides: tex(rm-qhvcri.tfm) = %{tl_version}
Provides: tex(rm-qhvr-sc.tfm) = %{tl_version}
Provides: tex(rm-qhvr.tfm) = %{tl_version}
Provides: tex(rm-qhvri-sc.tfm) = %{tl_version}
Provides: tex(rm-qhvri.tfm) = %{tl_version}
Provides: tex(rm-qplb-sc.tfm) = %{tl_version}
Provides: tex(rm-qplb.tfm) = %{tl_version}
Provides: tex(rm-qplbi-sc.tfm) = %{tl_version}
Provides: tex(rm-qplbi.tfm) = %{tl_version}
Provides: tex(rm-qplr-sc.tfm) = %{tl_version}
Provides: tex(rm-qplr.tfm) = %{tl_version}
Provides: tex(rm-qplri-sc.tfm) = %{tl_version}
Provides: tex(rm-qplri.tfm) = %{tl_version}
Provides: tex(rm-qtmb-sc.tfm) = %{tl_version}
Provides: tex(rm-qtmb.tfm) = %{tl_version}
Provides: tex(rm-qtmbi-sc.tfm) = %{tl_version}
Provides: tex(rm-qtmbi.tfm) = %{tl_version}
Provides: tex(rm-qtmr-sc.tfm) = %{tl_version}
Provides: tex(rm-qtmr.tfm) = %{tl_version}
Provides: tex(rm-qtmri-sc.tfm) = %{tl_version}
Provides: tex(rm-qtmri.tfm) = %{tl_version}
Provides: tex(rm-qzcmi.tfm) = %{tl_version}
Provides: tex(t5-qagb-sc.tfm) = %{tl_version}
Provides: tex(t5-qagb.tfm) = %{tl_version}
Provides: tex(t5-qagbi-sc.tfm) = %{tl_version}
Provides: tex(t5-qagbi.tfm) = %{tl_version}
Provides: tex(t5-qagr-sc.tfm) = %{tl_version}
Provides: tex(t5-qagr.tfm) = %{tl_version}
Provides: tex(t5-qagri-sc.tfm) = %{tl_version}
Provides: tex(t5-qagri.tfm) = %{tl_version}
Provides: tex(t5-qbkb-sc.tfm) = %{tl_version}
Provides: tex(t5-qbkb.tfm) = %{tl_version}
Provides: tex(t5-qbkbi-sc.tfm) = %{tl_version}
Provides: tex(t5-qbkbi.tfm) = %{tl_version}
Provides: tex(t5-qbkr-sc.tfm) = %{tl_version}
Provides: tex(t5-qbkr.tfm) = %{tl_version}
Provides: tex(t5-qbkri-sc.tfm) = %{tl_version}
Provides: tex(t5-qbkri.tfm) = %{tl_version}
Provides: tex(t5-qcrb-sc.tfm) = %{tl_version}
Provides: tex(t5-qcrb.tfm) = %{tl_version}
Provides: tex(t5-qcrbi-sc.tfm) = %{tl_version}
Provides: tex(t5-qcrbi.tfm) = %{tl_version}
Provides: tex(t5-qcrr-sc.tfm) = %{tl_version}
Provides: tex(t5-qcrr.tfm) = %{tl_version}
Provides: tex(t5-qcrri-sc.tfm) = %{tl_version}
Provides: tex(t5-qcrri.tfm) = %{tl_version}
Provides: tex(t5-qcsb-sc.tfm) = %{tl_version}
Provides: tex(t5-qcsb.tfm) = %{tl_version}
Provides: tex(t5-qcsbi-sc.tfm) = %{tl_version}
Provides: tex(t5-qcsbi.tfm) = %{tl_version}
Provides: tex(t5-qcsr-sc.tfm) = %{tl_version}
Provides: tex(t5-qcsr.tfm) = %{tl_version}
Provides: tex(t5-qcsri-sc.tfm) = %{tl_version}
Provides: tex(t5-qcsri.tfm) = %{tl_version}
Provides: tex(t5-qhvb-sc.tfm) = %{tl_version}
Provides: tex(t5-qhvb.tfm) = %{tl_version}
Provides: tex(t5-qhvbi-sc.tfm) = %{tl_version}
Provides: tex(t5-qhvbi.tfm) = %{tl_version}
Provides: tex(t5-qhvcb-sc.tfm) = %{tl_version}
Provides: tex(t5-qhvcb.tfm) = %{tl_version}
Provides: tex(t5-qhvcbi-sc.tfm) = %{tl_version}
Provides: tex(t5-qhvcbi.tfm) = %{tl_version}
Provides: tex(t5-qhvcr-sc.tfm) = %{tl_version}
Provides: tex(t5-qhvcr.tfm) = %{tl_version}
Provides: tex(t5-qhvcri-sc.tfm) = %{tl_version}
Provides: tex(t5-qhvcri.tfm) = %{tl_version}
Provides: tex(t5-qhvr-sc.tfm) = %{tl_version}
Provides: tex(t5-qhvr.tfm) = %{tl_version}
Provides: tex(t5-qhvri-sc.tfm) = %{tl_version}
Provides: tex(t5-qhvri.tfm) = %{tl_version}
Provides: tex(t5-qplb-sc.tfm) = %{tl_version}
Provides: tex(t5-qplb.tfm) = %{tl_version}
Provides: tex(t5-qplbi-sc.tfm) = %{tl_version}
Provides: tex(t5-qplbi.tfm) = %{tl_version}
Provides: tex(t5-qplr-sc.tfm) = %{tl_version}
Provides: tex(t5-qplr.tfm) = %{tl_version}
Provides: tex(t5-qplri-sc.tfm) = %{tl_version}
Provides: tex(t5-qplri.tfm) = %{tl_version}
Provides: tex(t5-qtmb-sc.tfm) = %{tl_version}
Provides: tex(t5-qtmb.tfm) = %{tl_version}
Provides: tex(t5-qtmbi-sc.tfm) = %{tl_version}
Provides: tex(t5-qtmbi.tfm) = %{tl_version}
Provides: tex(t5-qtmr-sc.tfm) = %{tl_version}
Provides: tex(t5-qtmr.tfm) = %{tl_version}
Provides: tex(t5-qtmri-sc.tfm) = %{tl_version}
Provides: tex(t5-qtmri.tfm) = %{tl_version}
Provides: tex(t5-qzcmi.tfm) = %{tl_version}
Provides: tex(texnansi-qagb-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qagb.tfm) = %{tl_version}
Provides: tex(texnansi-qagbi-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qagbi.tfm) = %{tl_version}
Provides: tex(texnansi-qagr-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qagr.tfm) = %{tl_version}
Provides: tex(texnansi-qagri-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qagri.tfm) = %{tl_version}
Provides: tex(texnansi-qbkb-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qbkb.tfm) = %{tl_version}
Provides: tex(texnansi-qbkbi-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qbkbi.tfm) = %{tl_version}
Provides: tex(texnansi-qbkr-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qbkr.tfm) = %{tl_version}
Provides: tex(texnansi-qbkri-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qbkri.tfm) = %{tl_version}
Provides: tex(texnansi-qcrb-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qcrb.tfm) = %{tl_version}
Provides: tex(texnansi-qcrbi-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qcrbi.tfm) = %{tl_version}
Provides: tex(texnansi-qcrr-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qcrr.tfm) = %{tl_version}
Provides: tex(texnansi-qcrri-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qcrri.tfm) = %{tl_version}
Provides: tex(texnansi-qcsb-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qcsb.tfm) = %{tl_version}
Provides: tex(texnansi-qcsbi-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qcsbi.tfm) = %{tl_version}
Provides: tex(texnansi-qcsr-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qcsr.tfm) = %{tl_version}
Provides: tex(texnansi-qcsri-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qcsri.tfm) = %{tl_version}
Provides: tex(texnansi-qhvb-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qhvb.tfm) = %{tl_version}
Provides: tex(texnansi-qhvbi-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qhvbi.tfm) = %{tl_version}
Provides: tex(texnansi-qhvcb-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qhvcb.tfm) = %{tl_version}
Provides: tex(texnansi-qhvcbi-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qhvcbi.tfm) = %{tl_version}
Provides: tex(texnansi-qhvcr-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qhvcr.tfm) = %{tl_version}
Provides: tex(texnansi-qhvcri-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qhvcri.tfm) = %{tl_version}
Provides: tex(texnansi-qhvr-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qhvr.tfm) = %{tl_version}
Provides: tex(texnansi-qhvri-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qhvri.tfm) = %{tl_version}
Provides: tex(texnansi-qplb-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qplb.tfm) = %{tl_version}
Provides: tex(texnansi-qplbi-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qplbi.tfm) = %{tl_version}
Provides: tex(texnansi-qplr-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qplr.tfm) = %{tl_version}
Provides: tex(texnansi-qplri-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qplri.tfm) = %{tl_version}
Provides: tex(texnansi-qtmb-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qtmb.tfm) = %{tl_version}
Provides: tex(texnansi-qtmbi-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qtmbi.tfm) = %{tl_version}
Provides: tex(texnansi-qtmr-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qtmr.tfm) = %{tl_version}
Provides: tex(texnansi-qtmri-sc.tfm) = %{tl_version}
Provides: tex(texnansi-qtmri.tfm) = %{tl_version}
Provides: tex(texnansi-qzcmi.tfm) = %{tl_version}
Provides: tex(ts1-qagb.tfm) = %{tl_version}
Provides: tex(ts1-qagbi.tfm) = %{tl_version}
Provides: tex(ts1-qagr.tfm) = %{tl_version}
Provides: tex(ts1-qagri.tfm) = %{tl_version}
Provides: tex(ts1-qbkb.tfm) = %{tl_version}
Provides: tex(ts1-qbkbi.tfm) = %{tl_version}
Provides: tex(ts1-qbkr.tfm) = %{tl_version}
Provides: tex(ts1-qbkri.tfm) = %{tl_version}
Provides: tex(ts1-qcrb.tfm) = %{tl_version}
Provides: tex(ts1-qcrbi.tfm) = %{tl_version}
Provides: tex(ts1-qcrr.tfm) = %{tl_version}
Provides: tex(ts1-qcrri.tfm) = %{tl_version}
Provides: tex(ts1-qcsb.tfm) = %{tl_version}
Provides: tex(ts1-qcsbi.tfm) = %{tl_version}
Provides: tex(ts1-qcsr.tfm) = %{tl_version}
Provides: tex(ts1-qcsri.tfm) = %{tl_version}
Provides: tex(ts1-qhvb.tfm) = %{tl_version}
Provides: tex(ts1-qhvbi.tfm) = %{tl_version}
Provides: tex(ts1-qhvcb.tfm) = %{tl_version}
Provides: tex(ts1-qhvcbi.tfm) = %{tl_version}
Provides: tex(ts1-qhvcr.tfm) = %{tl_version}
Provides: tex(ts1-qhvcri.tfm) = %{tl_version}
Provides: tex(ts1-qhvr.tfm) = %{tl_version}
Provides: tex(ts1-qhvri.tfm) = %{tl_version}
Provides: tex(ts1-qplb.tfm) = %{tl_version}
Provides: tex(ts1-qplbi.tfm) = %{tl_version}
Provides: tex(ts1-qplr.tfm) = %{tl_version}
Provides: tex(ts1-qplri.tfm) = %{tl_version}
Provides: tex(ts1-qtmb.tfm) = %{tl_version}
Provides: tex(ts1-qtmbi.tfm) = %{tl_version}
Provides: tex(ts1-qtmr.tfm) = %{tl_version}
Provides: tex(ts1-qtmri.tfm) = %{tl_version}
Provides: tex(ts1-qzcmi.tfm) = %{tl_version}
Provides: tex(qagb.pfb) = %{tl_version}
Provides: tex(qagbi.pfb) = %{tl_version}
Provides: tex(qagr.pfb) = %{tl_version}
Provides: tex(qagri.pfb) = %{tl_version}
Provides: tex(qbkb.pfb) = %{tl_version}
Provides: tex(qbkbi.pfb) = %{tl_version}
Provides: tex(qbkr.pfb) = %{tl_version}
Provides: tex(qbkri.pfb) = %{tl_version}
Provides: tex(qcrb.pfb) = %{tl_version}
Provides: tex(qcrbi.pfb) = %{tl_version}
Provides: tex(qcrr.pfb) = %{tl_version}
Provides: tex(qcrri.pfb) = %{tl_version}
Provides: tex(qcsb.pfb) = %{tl_version}
Provides: tex(qcsbi.pfb) = %{tl_version}
Provides: tex(qcsr.pfb) = %{tl_version}
Provides: tex(qcsri.pfb) = %{tl_version}
Provides: tex(qhvb.pfb) = %{tl_version}
Provides: tex(qhvbi.pfb) = %{tl_version}
Provides: tex(qhvcb.pfb) = %{tl_version}
Provides: tex(qhvcbi.pfb) = %{tl_version}
Provides: tex(qhvcr.pfb) = %{tl_version}
Provides: tex(qhvcri.pfb) = %{tl_version}
Provides: tex(qhvr.pfb) = %{tl_version}
Provides: tex(qhvri.pfb) = %{tl_version}
Provides: tex(qplb.pfb) = %{tl_version}
Provides: tex(qplbi.pfb) = %{tl_version}
Provides: tex(qplr.pfb) = %{tl_version}
Provides: tex(qplri.pfb) = %{tl_version}
Provides: tex(qtmb.pfb) = %{tl_version}
Provides: tex(qtmbi.pfb) = %{tl_version}
Provides: tex(qtmr.pfb) = %{tl_version}
Provides: tex(qtmri.pfb) = %{tl_version}
Provides: tex(qzcmi.pfb) = %{tl_version}
Provides: tex(il2qag.fd) = %{tl_version}
Provides: tex(il2qbk.fd) = %{tl_version}
Provides: tex(il2qcr.fd) = %{tl_version}
Provides: tex(il2qcs.fd) = %{tl_version}
Provides: tex(il2qhv.fd) = %{tl_version}
Provides: tex(il2qhvc.fd) = %{tl_version}
Provides: tex(il2qpl.fd) = %{tl_version}
Provides: tex(il2qtm.fd) = %{tl_version}
Provides: tex(il2qzc.fd) = %{tl_version}
Provides: tex(l7xqag.fd) = %{tl_version}
Provides: tex(l7xqbk.fd) = %{tl_version}
Provides: tex(l7xqcr.fd) = %{tl_version}
Provides: tex(l7xqcs.fd) = %{tl_version}
Provides: tex(l7xqhv.fd) = %{tl_version}
Provides: tex(l7xqhvc.fd) = %{tl_version}
Provides: tex(l7xqpl.fd) = %{tl_version}
Provides: tex(l7xqtm.fd) = %{tl_version}
Provides: tex(l7xqzc.fd) = %{tl_version}
Provides: tex(ly1qag.fd) = %{tl_version}
Provides: tex(ly1qbk.fd) = %{tl_version}
Provides: tex(ly1qcr.fd) = %{tl_version}
Provides: tex(ly1qcs.fd) = %{tl_version}
Provides: tex(ly1qhv.fd) = %{tl_version}
Provides: tex(ly1qhvc.fd) = %{tl_version}
Provides: tex(ly1qpl.fd) = %{tl_version}
Provides: tex(ly1qtm.fd) = %{tl_version}
Provides: tex(ly1qzc.fd) = %{tl_version}
Provides: tex(ot1qag.fd) = %{tl_version}
Provides: tex(ot1qbk.fd) = %{tl_version}
Provides: tex(ot1qcr.fd) = %{tl_version}
Provides: tex(ot1qcs.fd) = %{tl_version}
Provides: tex(ot1qhv.fd) = %{tl_version}
Provides: tex(ot1qhvc.fd) = %{tl_version}
Provides: tex(ot1qpl.fd) = %{tl_version}
Provides: tex(ot1qtm.fd) = %{tl_version}
Provides: tex(ot1qzc.fd) = %{tl_version}
Provides: tex(ot4qag.fd) = %{tl_version}
Provides: tex(ot4qbk.fd) = %{tl_version}
Provides: tex(ot4qcr.fd) = %{tl_version}
Provides: tex(ot4qcs.fd) = %{tl_version}
Provides: tex(ot4qhv.fd) = %{tl_version}
Provides: tex(ot4qhvc.fd) = %{tl_version}
Provides: tex(ot4qpl.fd) = %{tl_version}
Provides: tex(ot4qtm.fd) = %{tl_version}
Provides: tex(ot4qzc.fd) = %{tl_version}
Provides: tex(qbookman.sty) = %{tl_version}
Provides: tex(qcourier.sty) = %{tl_version}
Provides: tex(qpalatin.sty) = %{tl_version}
Provides: tex(qswiss.sty) = %{tl_version}
Provides: tex(qtimes.sty) = %{tl_version}
Provides: tex(qxqag.fd) = %{tl_version}
Provides: tex(qxqbk.fd) = %{tl_version}
Provides: tex(qxqcr.fd) = %{tl_version}
Provides: tex(qxqcs.fd) = %{tl_version}
Provides: tex(qxqhv.fd) = %{tl_version}
Provides: tex(qxqhvc.fd) = %{tl_version}
Provides: tex(qxqpl.fd) = %{tl_version}
Provides: tex(qxqtm.fd) = %{tl_version}
Provides: tex(qxqzc.fd) = %{tl_version}
Provides: tex(qzapfcha.sty) = %{tl_version}
Provides: tex(t1qag.fd) = %{tl_version}
Provides: tex(t1qbk.fd) = %{tl_version}
Provides: tex(t1qcr.fd) = %{tl_version}
Provides: tex(t1qcs.fd) = %{tl_version}
Provides: tex(t1qhv.fd) = %{tl_version}
Provides: tex(t1qhvc.fd) = %{tl_version}
Provides: tex(t1qpl.fd) = %{tl_version}
Provides: tex(t1qtm.fd) = %{tl_version}
Provides: tex(t1qzc.fd) = %{tl_version}
Provides: tex(t5qag.fd) = %{tl_version}
Provides: tex(t5qbk.fd) = %{tl_version}
Provides: tex(t5qcr.fd) = %{tl_version}
Provides: tex(t5qcs.fd) = %{tl_version}
Provides: tex(t5qhv.fd) = %{tl_version}
Provides: tex(t5qhvc.fd) = %{tl_version}
Provides: tex(t5qpl.fd) = %{tl_version}
Provides: tex(t5qtm.fd) = %{tl_version}
Provides: tex(t5qzc.fd) = %{tl_version}
Provides: tex(tgadventor.sty) = %{tl_version}
Provides: tex(tgbonum.sty) = %{tl_version}
Provides: tex(tgchorus.sty) = %{tl_version}
Provides: tex(tgcursor.sty) = %{tl_version}
Provides: tex(tgheros.sty) = %{tl_version}
Provides: tex(tgpagella.sty) = %{tl_version}
Provides: tex(tgschola.sty) = %{tl_version}
Provides: tex(tgtermes.sty) = %{tl_version}
Provides: tex(ts1qag.fd) = %{tl_version}
Provides: tex(ts1qbk.fd) = %{tl_version}
Provides: tex(ts1qcr.fd) = %{tl_version}
Provides: tex(ts1qcs.fd) = %{tl_version}
Provides: tex(ts1qhv.fd) = %{tl_version}
Provides: tex(ts1qhvc.fd) = %{tl_version}
Provides: tex(ts1qpl.fd) = %{tl_version}
Provides: tex(ts1qtm.fd) = %{tl_version}
Provides: tex(ts1qzc.fd) = %{tl_version}

%description
The TeX-GYRE bundle consists of six font families: TeX Gyre
Adventor is based on the URW Gothic L family of fonts (which is
derived from ITC Avant Garde Gothic, designed by Herb Lubalin
and Tom Carnase). TeX Gyre Bonum is based on the URW Bookman L
family (from Bookman Old Style, designed by Alexander
Phemister). TeX Gyre Chorus is based on URW Chancery L Medium
Italic (from ITC Zapf Chancery, designed by Hermann Zapf in
1979). TeX-Gyre Cursor is based on URW Nimbus Mono L (based on
Courier, designed by Howard G. Kettler in 1955, for IBM). TeX
Gyre Heros is based on URW Nimbus Sans L (from Helvetica,
prepared by Max Miedinger, with Eduard Hoffmann in 1957). TeX
Gyre Pagella is based on URW Palladio L (from Palatino,
designed by Hermann Zapf in the 1940s). TeX Gyre Schola is
based on the URW Century Schoolbook L family (which was
designed by Morris Fuller Benton for the American Type
Founders). TeX Gyre Termes is based on the URW Nimbus Roman No9
L family of fonts (whose original, Times, was designed by
Stanley Morison together with Starling Burgess and Victor
Lardent and first offered by Monotype). The constituent
standard faces of each family have been greatly extended, and
contain nearly 1100 glyphs each (though Chorus omits Greek
support, has no small-caps family and has approximately 800
glyphs). Each family is available in Adobe Type 1 and Open Type
formats, and LaTeX support (for use with a variety of
encodings) is provided. Vietnamese characters were added by Han
The Thanh.

date: 2014-06-07 20:47:53 +0200

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_texdir}/../texmf
mkdir -p %{buildroot}%{_texdir}/texmf-distmkdir -p %{buildroot}%{_texdir}/texmf-distmkdir -p %{buildroot}%{_texdir}/texmf-dist

xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist

mkdir -p %{buildroot}%{_datadir}/fonts
pushd %{buildroot}%{_datadir}/fonts
ln -s %{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre tex-gyre
popd

# install licenses
cp %{SOURCE3} .

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/45-tex-gyre.conf %{buildroot}%{_fontconfig_confdir}/45-tex-gyre.conf
ln -s %{_fontconfig_templatedir}/90-non-tt-tex-gyre.conf %{buildroot}%{_fontconfig_confdir}/90-non-tt-tex-gyre.conf


rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
if [ $1 -gt 0 ] ; then
%{_bindir}/updmap-sys --quiet --nomkmap --enable Map=qag.map > /dev/null 2>&1
%{_bindir}/updmap-sys --quiet --nomkmap --enable Map=qbk.map > /dev/null 2>&1
%{_bindir}/updmap-sys --quiet --nomkmap --enable Map=qcr.map > /dev/null 2>&1
%{_bindir}/updmap-sys --quiet --nomkmap --enable Map=qcs.map > /dev/null 2>&1
%{_bindir}/updmap-sys --quiet --nomkmap --enable Map=qhv.map > /dev/null 2>&1
%{_bindir}/updmap-sys --quiet --nomkmap --enable Map=qpl.map > /dev/null 2>&1
%{_bindir}/updmap-sys --quiet --nomkmap --enable Map=qtm.map > /dev/null 2>&1
%{_bindir}/updmap-sys --quiet --nomkmap --enable Map=qzc.map > /dev/null 2>&1
touch /var/run/texlive/run-updmap
fi
:

%postun
if [ $1 == 0 ] ; then
%{_bindir}/updmap-sys --nomkmap --disable Map=qag.map > /dev/null 2>&1
%{_bindir}/updmap-sys --nomkmap --disable Map=qbk.map > /dev/null 2>&1
%{_bindir}/updmap-sys --nomkmap --disable Map=qcr.map > /dev/null 2>&1
%{_bindir}/updmap-sys --nomkmap --disable Map=qcs.map > /dev/null 2>&1
%{_bindir}/updmap-sys --nomkmap --disable Map=qhv.map > /dev/null 2>&1
%{_bindir}/updmap-sys --nomkmap --disable Map=qpl.map > /dev/null 2>&1
%{_bindir}/updmap-sys --nomkmap --disable Map=qtm.map > /dev/null 2>&1
%{_bindir}/updmap-sys --nomkmap --disable Map=qzc.map > /dev/null 2>&1
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
touch /var/run/texlive/run-mtxrun
touch /var/run/texlive/run-updmap
fi
:

%posttrans
if [ -e /var/run/texlive/run-texhash ]; then %{_bindir}/texhash 2> /dev/null; rm -f /var/run/texlive/run-texhash; fi
if [ -e /var/run/texlive/run-updmap ]; then %{_bindir}/updmap-sys --quiet --nomkmap &> /dev/null;rm -f /var/run/texlive/run-updmap; fi
if [ -e /var/run/texlive/run-mtxrun ]; then export TEXMF=/usr/share/texlive/texmf-dist; export TEXMFCNF=/usr/share/texlive/texmf-dist/web2c; export TEXMFCACHE=/var/lib/texmf; %{_bindir}/mtxrun --generate &> /dev/null; rm -f /var/run/texlive/run-mtxrun; fi
:

%files
%defattr(-,root,root)
%doc gfsl.txt
%{_datadir}/fonts/tex-gyre
%{_fontconfig_confdir}
%{_fontconfig_templatedir}/45-tex-gyre.conf
%{_fontconfig_templatedir}/90-non-tt-tex-gyre.conf
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qagb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qagbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qagr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qagri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qbkb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qbkbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qbkr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qbkri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcrb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcrbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcrr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcrri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcsb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcsbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcsr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcsri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvcb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvcbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvcr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvcri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qplb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qplbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qplr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qplri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qtmb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qtmbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qtmr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qtmri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qzcmi.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-cs-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-cs.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-csm-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-csm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-cszc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-ec-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-ec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-l7x-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-l7x.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-l7xzc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qx-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qx.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qxm-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qxm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qxzc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rm-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rmm-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rmm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rmzc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-t5-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-t5.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-texnansi-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-texnansi.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-texnansizc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-ts1.enc
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc.map
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrechorus-mediumitalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-regular.otf
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qzcmi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qzcmi.pfm
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qbookman.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qcourier.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qpalatin.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qswiss.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qtimes.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qzapfcha.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgadventor.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgbonum.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgchorus.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgcursor.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgheros.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgpagella.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgschola.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgtermes.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qzc.fd

%changelog
* Thu Apr 07 2016 Daniel Renninghoff <daniel.renninghoff@gmail.com> - svn18651.2.004-25
- Fixed small bug.

* Thu Apr 07 2016 Daniel Renninghoff <daniel.renninghoff@gmail.com> - svn18651.2.004-24
- First version

