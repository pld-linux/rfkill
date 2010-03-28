Summary:	Simple /dev/rfkill userspace tool
Summary(pl.UTF-8):	Proste narzędzie przestrzeni użytkownika do urządzenia /dev/rfkill
Name:		rfkill
Version:	0.4
Release:	1
License:	MIT-like
Group:		Networking/Admin
Source0:	http://wireless.kernel.org/download/rfkill/%{name}-%{version}.tar.bz2
# Source0-md5:	727892c0fb35c80ee3849fbe89b45350
URL:		http://wireless.kernel.org/en/users/Documentation/rfkill
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	/bin

%description
Simple /dev/rfkill userspace tool.

%description -l pl.UTF-8
Proste narzędzie przestrzeni użytkownika do urządzenia /dev/rfkill.

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install rfkill $RPM_BUILD_ROOT%{_bindir}
install rfkill.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/rfkill
%{_mandir}/man8/rfkill.8*
