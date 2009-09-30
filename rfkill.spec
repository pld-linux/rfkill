Summary:	Simple /dev/rfkill userspace tool
Name:		rfkill
Version:	0.3
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://wireless.kernel.org/download/rfkill/%{name}-%{version}.tar.bz2
# Source0-md5:	f4d693c2a3e5f0503a3cde3d84be8919
URL:		http://wireless.kernel.org/en/users/Documentation/rfkill
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	/bin

%description
Simple /dev/rfkill userspace tool.

%prep
%setup -q

%build
%{__make} \
	V=1 \
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
