Summary:	Multitouch X input driver
Name:		xorg-driver-input-mtrack
Version:	0.3.0
Release:	5
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
URL:		https://github.com/BlueDragonX/xf86-input-mtrack
Source0:	https://github.com/BlueDragonX/xf86-input-mtrack/archive/v%{version}.tar.gz?/mtrack-%{version}.tgz
# Source0-md5:	111803d7728036d3ab75c587adf23130
Source1:	xf86-input-mtrack.conf
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
%setup -q -n xf86-input-mtrack-%{version}

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

install -d $RPM_BUILD_ROOT/etc/X11/xorg.conf.d
cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/xorg.conf.d/40-xf86-input-mtrack.conf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CREDITS
%config(noreplace) %verify(not md5 mtime size) /etc/X11/xorg.conf.d/40-xf86-input-mtrack.conf
%attr(755,root,root) %{_libdir}/xorg/modules/input/mtrack_drv.so
