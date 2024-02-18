#
# Conditional build:
%bcond_without	static_libs	# static libraries

%define	libver	0.4
Summary:	The Oil Runtime Compiler
Summary(pl.UTF-8):	Oil Runtime Compiler - kompilator zoptymalizowanych pętli wewnętrznych
Name:		orc
Version:	0.4.37
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.xz
# Source0-md5:	de1de1bdd9b35252035a3b996afc9425
URL:		https://gstreamer.freedesktop.org/modules/orc.html
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gtk-doc >= 1.12
BuildRequires:	meson >= 0.55.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.749
BuildRequires:	tar >= 1:1.22
BuildRequires:	which
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data. The "language" is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%description -l pl.UTF-8
Orc to biblioteka i zestaw narzędzi do kompilowania i wykonywania
bardzo prostych programów operujących na tablicach danych. "Język" to
ogólny asembler reprezentujący wiele możliwości dostępnych w
architekturach SIMD, w tym ograniczone dodawanie i odejmowanie oraz
wiele operacji arytmetycznych.

%package devel
Summary:	Header files for orc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki orc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for orc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki orc.

%package static
Summary:	Static orc library
Summary(pl.UTF-8):	Statyczna biblioteka orc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static orc library.

%description static -l pl.UTF-8
Statyczna biblioteka orc.

%package apidocs
Summary:	API documentation for orc library
Summary(pl.UTF-8):	Dokumentacja API biblioteki orc
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for orc library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki orc.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README RELEASE TODO
%attr(755,root,root) %{_bindir}/orc-bugreport
%attr(755,root,root) %{_bindir}/orcc
%attr(755,root,root) %{_libdir}/liborc-%{libver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liborc-%{libver}.so.0
%attr(755,root,root) %{_libdir}/liborc-test-%{libver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liborc-test-%{libver}.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborc-%{libver}.so
%attr(755,root,root) %{_libdir}/liborc-test-%{libver}.so
%{_includedir}/orc-%{libver}
%{_pkgconfigdir}/orc-%{libver}.pc
%{_pkgconfigdir}/orc-test-%{libver}.pc
%{_aclocaldir}/orc.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liborc-%{libver}.a
%{_libdir}/liborc-test-%{libver}.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/orc
