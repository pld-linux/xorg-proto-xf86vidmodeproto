Summary:	XF86VidMode extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XF86VidMode
Name:		xorg-proto-xf86vidmodeproto
Version:	2.3
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-%{version}.tar.bz2
# Source0-md5:	4434894fc7d4eeb4a22e6b876d56fdaa
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86VidMode extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia XF86VidMode.

%package devel
Summary:	XF86VidMode extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XF86VidMode
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
XF86VidMode extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia XF86VidMode.

%prep
%setup -q -n xf86vidmodeproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/xf86vm*.h
%{_pkgconfigdir}/xf86vidmodeproto.pc
