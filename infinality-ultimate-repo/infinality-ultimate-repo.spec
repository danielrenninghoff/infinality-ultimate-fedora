Name:           infinality-ultimate-repo
Version:        24
Release:        1
Summary:        Infinality Ultimate Repo

Group:          System Environment/Base
License:        BSD
URL:            http://danielrenninghoff.com
Source1:        infinality-ultimate.repo
Source2:        RPM-GPG-KEY-dnlrn
BuildArch:      noarch

Requires:       system-release >= %{version}

%description
Infinality Ultimate repo.

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install

install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%{__install} -Dp -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

%{__install} -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d


%files
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%changelog
* Fri Apr 01 2016 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 24-1
- Updated for F24.

* Sun Nov 29 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 23-2
- Fixed wrong SRPM url.

* Sat Nov 28 2015 Daniel Renninghoff <daniel.renninghoff@gmail.com> - 23-1
- First version.
