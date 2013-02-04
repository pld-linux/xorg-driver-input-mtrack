%define		subver 20120115
%define		rel		1
Summary:	Multitouch X input driver
Name:		xorg-driver-input-mtrack
Version:	1.0
Release:	0.rc2.%{subver}.%{rel}
License:	GPL v2+
Group:		X11/Applications
URL:		https://github.com/BlueDragonX/xf86-input-mtrack
Source0:	xf86-input-mtrack-%{subver}.tar.bz2
# Source0-md5:	7de920ea9bdd3dabf335a02a03755e99
Source1:	xf86-input-mtrack.conf
Patch0:		compile.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mtdev-devel >= 1.1.0
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-xserver-server-devel
%{?requires_xorg_xserver_xinput}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This X input driver provides gestures support for multitouch
touchpads, in particular those with integrated button.

%prep
%setup -q -n xf86-input-mtrack-%{subver}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/40-xf86-input-mtrack.conf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CREDITS
%{_datadir}/X11/xorg.conf.d/40-xf86-input-mtrack.conf
%attr(755,root,root) %{_libdir}/xorg/modules/input/mtrack_drv.so
