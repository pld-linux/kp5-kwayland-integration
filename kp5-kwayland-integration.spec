%define		kdeplasmaver	5.21.2
%define		qtver		5.9.0
%define		kpname		kwayland-integration

Summary:	Provides integration plugins for various KDE frameworks for the wayland windowing system
Name:		kp5-%{kpname}
Version:	5.21.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	8d3a080f54c4ff75d96175c7f81e443d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-kidletime-devel
BuildRequires:	kf5-kwayland-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Provides integration plugins for various KDE frameworks for the
wayland windowing system.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWaylandPlugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kguiaddons/kmodifierkey/kmodifierkey_wayland.so
%{_datadir}/qlogging-categories5/kwindowsystem.kwayland.categories
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kwindowsystem/KF5WindowSystemKWaylandPlugin.so
