Name:       harbour-osmscout-server-module-fonts

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    OSM Scout Server Module: Fonts
Version:    0.10.0
Release:    1
Group:      Qt/Qt
License:    LGPL3
URL:        https://github.com/rinigus/osmscout-server-fonts
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch

BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils
Requires: sailfishsilica-qt5 >= 0.10.9
Requires: libsailfishapp-launcher

%description
This a module for OSM Scout Server providing fonts for Mapnik
rendering backend

PackageName: OSM Scout Server Fonts
Type: addon
Category:
  - Font
  - Other

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5 SPECVERSION='%{version}'

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%qmake5_install


%files
%defattr(644,root,root,755)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

