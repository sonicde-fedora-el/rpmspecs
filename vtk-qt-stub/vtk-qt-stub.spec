# Stub soname-provider for Fedora's vtk-qt.
#
# Fedora's opencv-devel hard-requires opencv-viz, which pulls in the real
# vtk stack: opencv-viz -> vtk -> python3-vtk -> libvtkRenderingQt.so.1 ->
# vtk-qt. On rawhide vtk-qt is built against Fedora's qt6-qtbase-6.12 and
# needs libQt6Core.so.6(Qt_6.12) symbols that our pinned qt6-qtbase 6.11.3
# cannot provide, so the whole buildroot resolution fails.
#
# Nothing in the SonicDE stack uses vtk's Qt rendering support; the viz
# library is only a buildroot dependency of opencv-devel. Shipping the
# soname as a literal provide lets the solver satisfy python3-vtk's
# requirement without installing the real vtk-qt, so opencv-devel can be
# installed. Because the provides are unversioned sonames, the stub keeps
# working across Fedora vtk rebuilds until the vtk soname itself bumps.
Name:           vtk-qt-stub
Version:        1.0
Release:        1%{?dist}
Summary:        Stub provider of vtk-qt sonames for SonicDE buildroots
License:        MIT
BuildArch:      noarch

Provides:       libvtkRenderingQt.so.1()(64bit)
Provides:       libvtkRenderingQt.so.1
Provides:       libvtkGUISupportQt.so.1()(64bit)
Provides:       libvtkGUISupportQt.so.1
Provides:       libvtkGUISupportQtQuick.so.1()(64bit)
Provides:       libvtkGUISupportQtQuick.so.1
Provides:       libvtkGUISupportQtSQL.so.1()(64bit)
Provides:       libvtkGUISupportQtSQL.so.1
Provides:       libvtkViewsQt.so.1()(64bit)
Provides:       libvtkViewsQt.so.1

%description
Empty package that provides the vtk-qt shared-library sonames so that
Fedora's opencv-devel -> opencv-viz -> vtk -> python3-vtk chain can be
satisfied in SonicDE buildroots where the real vtk-qt is uninstallable
due to its qt6 symbol requirements. No actual vtk-qt functionality is
included; nothing in the SonicDE stack consumes it.

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
echo 'vtk-qt soname stub - see package description' > %{buildroot}%{_docdir}/%{name}/STUB

%files
%doc %{_docdir}/%{name}/STUB

%changelog
* Tue Feb 10 2026 Anders da Silva Rytter Hansen <andersrh@users.noreply.github.com> - 1.0-1
- Stub soname provider to break the opencv-viz -> vtk-qt -> qt6.12 chain
