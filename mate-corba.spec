%define major		0
%define libname		%mklibname MateCORBA2 %{major}
%define develname	%mklibname MateCORBA2 -d

Name:		mate-corba
Summary:	MateCORBA is a fork of GNOME's Orbit
Version:	1.2.2
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(libIDL-2.0)
BuildRequires:	mate-common
BuildRequires:	gtk-doc >= 1.0

%description
MateCORBA is a fork of GNOME's Orbit.

%package -n %{libname}
Summary:	MateCORBA is a fork of GNOME's Orbit
Group:		System/Libraries

%description -n %{libname}
MateCORBA is a fork of GNOME's Orbit.

%package -n %{develname}
Summary:	MateCORBA is a fork of GNOME's Orbit
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{name} = %{version}

%description -n %{develname}
MateCORBA is a fork of GNOME's Orbit.

%prep
%setup -q

%build
./autogen.sh \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
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
%doc AUTHORS NEWS README TODO

%files -n %{libname}
%{_libdir}/libMateCORBA*.so.%{major}*

%files -n %{develname}
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
%doc AUTHORS NEWS README TODO
