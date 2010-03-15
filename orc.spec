Summary:	The Oil Runtime Compiler
Name:		orc
Version:	0.4.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://code.entropywave.com/download/orc/%{name}-%{version}.tar.gz
# Source0-md5:	9b2e7030c8df8a0d371115869fe5685a
Patch0:		%{name}-build.patch
URL:		http://code.entropywave.com/projects/orc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data. The “language” is a
generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
%doc README TODO
%attr(755,root,root) %{_bindir}/orcc
%attr(755,root,root) %{_libdir}/liborc-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liborc-*.so.0
%dir %{_libdir}/orc
%attr(755,root,root) %{_libdir}/orc/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborc-*.so
%{_libdir}/liborc-*.la
%{_includedir}/orc-*
%{_pkgconfigdir}/orc-*.pc
%{_gtkdocdir}/orc

%files static
%defattr(644,root,root,755)
%{_libdir}/liborc-*.a
