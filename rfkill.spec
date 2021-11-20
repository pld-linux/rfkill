Summary:	Simple /dev/rfkill userspace tool
Summary(pl.UTF-8):	Proste narzędzie przestrzeni użytkownika do urządzenia /dev/rfkill
Name:		rfkill
Version:	1.0
Release:	2
License:	MIT-like
Group:		Networking/Admin
Source0:	https://www.kernel.org/pub/software/network/rfkill/%{name}-%{version}.tar.xz
# Source0-md5:	914fb2858b655db67d82c50fb77eb8ab
URL:		https://wireless.wiki.kernel.org/en/users/documentation/rfkill
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
cp -p rfkill.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/rfkill
%{_mandir}/man8/rfkill.8*
