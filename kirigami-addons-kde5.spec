#define git 20230821

Name:		kirigami-addons-kde5
Version:	0.11.0
Release:	%{?git:0.%{git}.}1
Summary:	Add-on widgets for the Kirigami library
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/kirigami-addons/-/archive/master/kirigami-addons-master.tar.bz2
%else
Source0:	https://download.kde.org/stable/kirigami-addons/kirigami-addons-%{version}.tar.xz
%endif
Patch0:		kirigami-addons-qt-6.6.patch
License:	LGPLv2+
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
Suggests:	kirigami-addons-translations

%description
Add-on widgets for the Kirigami library.

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description devel
This package contains header files needed if you wish to build
applications based on %{name}.

%prep
%autosetup -p1 -n kirigami-addons-%{?git:master}%{!?git:%{version}}
CMAKE_BUILD_DIR=build-kde5 %cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=OFF \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build-kde5

%install
%ninja_install -C build-kde5

# Since the filenames and installation locations clash, we get the translations
# from the newer version for KDE 6...
rm -rf %{buildroot}%{_datadir}/locale

%files
%{_libdir}/qt5/qml/org/kde/kirigamiaddons

%files devel
%{_libdir}/cmake/KF5KirigamiAddons
