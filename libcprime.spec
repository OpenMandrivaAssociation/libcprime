
%define major 4
%define libpackage %mklibname cprime %{major}
%define devpackage %mklibname -d cprime

Name:           libcprime
Version:        4.2.2
Release:        1
Summary:        Libcprime is a library for bookmarking, saving recent activites, managing settings of CoreApps.
License:        GPLv3
Group:          System/Libraries
URL:            https://gitlab.com/cubocore/coreapps/libcprime
Source0:        https://gitlab.com/cubocore/coreapps/libcprime/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: qt5-devel
BuildRequires: qt5-qtbase-devel

# Upstream requires a dependency to "qt5-connectivity" but we at OMV split this package into two programs. So let's require two.
Requires: qt5nfc
Requires: qtbluetooth5
Requires: libnotify

%description
LibCPrime is a Library for bookmarking, saving recent activites, managing settings for CuboCore Application Suite.

%package -n %{libpackage}
Summary:	Libcprime is a library for bookmarking, saving recent activites, managing settings of CoreApps.
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libpackage}
Libcprime is a library for bookmarking, saving recent activites, managing settings of CoreApps.

%package -n %{devpackage}
Summary:	Development files for libcprime
Group:		System/Libraries
Requires:	%{libpackage} = %{EVRD}

%description -n %{devpackage}
Development files for libcprime.

Libcprime is a library for bookmarking, saving recent activites, managing settings of CoreApps.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libpackage}
%{_libdir}/libcprime*.so.%{major}*

%files -n %{devpackage}
%{_includedir}/cprime/*
%{_libdir}/libcprime*.so
%{_datadir}/pkgconfig/cprime*.pc
