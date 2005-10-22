Summary:	XF86VidMode protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86VidMode i pomocnicze
Name:		xorg-proto-xf86vidmodeproto
Version:	2.2.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/xf86vidmodeproto-%{version}.tar.bz2
# Source0-md5:	e125b82299fa2e9c955e2277744694c6
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86VidMode protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u XF86VidMode i pomocnicze.

%package devel
Summary:	XF86VidMode protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86VidMode i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
XF86VidMode protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u XF86VidMode i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xf86vidmodeproto.pc
