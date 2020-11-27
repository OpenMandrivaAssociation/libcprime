Name:           libcprime
Version:        4.0.0
Release:        1
Summary:        Libcprime is a library for bookmarking, saving recent activites, managing settings of CoreApps.
License:        GPL3
Group:          System/Libraries
URL:            https://gitlab.com/cubocore/coreapps/libcprime
Source0:        https://gitlab.com/cubocore/coreapps/libcprime/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  qt5-devel

  
%description
LibCPrime is a Library for bookmarking, saving recent activites, managing settings for CuboCore Application Suite.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}


%files
