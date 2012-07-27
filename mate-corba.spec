%define major	0
%define libname	%mklibname MateCORBA2_ %{major}
%define devname	%mklibname MateCORBA2 -d

Summary:	MateCORBA is a fork of GNOME's Orbit
Name:		mate-corba
Version:	1.4.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(libIDL-2.0)

%description
MateCORBA is a fork of GNOME's Orbit.

%package -n %{libname}
Summary:	MateCORBA is a fork of GNOME's Orbit
Group:		System/Libraries
Obsoletes:	%{_lib}MateCORBA20 <= %{EVRD}

%description -n %{libname}
MateCORBA is a fork of GNOME's Orbit.

%package -n %{devname}
Summary:	MateCORBA is a fork of GNOME's Orbit
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{name} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
MateCORBA is a fork of GNOME's Orbit.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/matecorba2-config

%multiarch_includes %{buildroot}%{_includedir}/matecorba-2.0/matecorba/matecorba-config.h

%files
%{_bindir}/matecorba-ior-decode-2
%{_bindir}/matecorba-linc-cleanup-sockets
%{_bindir}/matecorba-typelib-dump
%{_libdir}/matecorba-2.0/Everything_module.so
%{_datadir}/idl/matecorba-2.0/

%files -n %{libname}
%{_libdir}/libMateCORBA*.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README TODO
%{_includedir}/matecorba-2.0/
%{_libdir}/libMateCORBA*.so
%{_libdir}/libname-matecorba-server-2.a
%{_libdir}/pkgconfig/MateCORBA*.pc
%{_datadir}/aclocal/MateCORBA2.m4
%{_bindir}/matecorba2-config
%{_bindir}/matecorba-idl-2
%{_datadir}/gtk-doc/html/MateCORBA2/
%{multiarch_bindir}/matecorba2-config
%{multiarch_includedir}/matecorba-2.0/

