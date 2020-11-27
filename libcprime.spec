%global debug_package %{nil}

Name:           libcprime
Version:        4.0.0
Release:        1
Summary:        Libcprime is a library for bookmarking, saving recent activites, managing settings of CoreApps.
License:        GPL3
Group:          System/Libraries
URL:            https://gitlab.com/cubocore/coreapps/libcprime
Source0:        https://gitlab.com/cubocore/coreapps/libcprime/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires: qt5-devel
BuildRequires: qt5-qtbase-devel

# Upstream requires a dependency to "qt5-connectivity" but we at OMV split this package into two programs. So let's require two.
Requires: qt5nfc
Requires: qtbluetooth5
Requires: libnotify
  
%description
LibCPrime is a Library for bookmarking, saving recent activites, managing settings for CuboCore Application Suite.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%qmake_qt5 \
            PREFIX=/usr \
            DEFINES+="${lib^^}
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}


%files
%{_includedir}/cprime/*
%{_datadir}/coreapps/resource/*
%{_icondsdir}/hicolor/scalable/apps/applications-csuite.svg

# Broken lib
