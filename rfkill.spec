%define	snap	20090719
Summary:	Simple /dev/rfkill userspace tool
Name:		rfkill
Version:	0.1
Release:	0.%{snap}.1
License:	GPL
Group:		Networking/Admin
# git clone http://git.sipsolutions.net/rfkill.git
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	3edde5a4e66ad8848036805d8adeb1c4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	/bin

%description
Simple /dev/rfkill userspace tool.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install rfkill $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
