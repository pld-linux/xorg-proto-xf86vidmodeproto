Summary:	XF86VidMode extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86VidMode
Name:		xorg-proto-xf86vidmodeproto
Version:	2.3.1
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-%{version}.tar.bz2
# Source0-md5:	e793ecefeaecfeabd1aed6a01095174e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86VidMode (XFree86 Video Mode) extension defines a protocol for
dynamically configuring modelines and gamma.

%description -l pl.UTF-8
Rozszerzenie XF86VidMode (XFree86 Video Mode) definiuje protokół do
dynamicznej konfiguracji linii opisujących tryb (modeline) oraz
korekcji gamma.

%package devel
Summary:	XF86VidMode extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86VidMode
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
XF86VidMode (XFree86 Video Mode) extension defines a protocol for
dynamically configuring modelines and gamma.

%description devel -l pl.UTF-8
Rozszerzenie XF86VidMode (XFree86 Video Mode) definiuje protokół do
dynamicznej konfiguracji linii opisujących tryb (modeline) oraz
korekcji gamma.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_includedir}/X11/extensions/xf86vm*.h
%{_pkgconfigdir}/xf86vidmodeproto.pc
