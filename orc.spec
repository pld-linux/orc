#
# Conditional build:
%bcond_without	static_libs	# static libraries build

%define	libver	0.4
Summary:	The Oil Runtime Compiler
Summary(pl.UTF-8):	Oil Runtime Compiler - kompilator zoptymalizowanych pętli wewnętrznych
Name:		orc
Version:	0.4.23
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.xz
# Source0-md5:	72e0612ace54d77aa2f7a006348ee81a
URL:		http://code.entropywave.com/projects/orc/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.11
BuildRequires:	gtk-doc >= 1.12
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
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

%prep
%setup -q

%{__rm} m4/libtool.m4 m4/lt*.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README TODO
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
%{_libdir}/liborc-%{libver}.la
%{_libdir}/liborc-test-%{libver}.la
%{_includedir}/orc-%{libver}
%{_pkgconfigdir}/orc-%{libver}.pc
%{_aclocaldir}/orc.m4
%{_gtkdocdir}/orc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liborc-%{libver}.a
%{_libdir}/liborc-test-%{libver}.a
%endif
