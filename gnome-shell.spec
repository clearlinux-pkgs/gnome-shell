#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-shell
Version  : 43.0
Release  : 133
URL      : https://download.gnome.org/sources/gnome-shell/43/gnome-shell-43.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell/43/gnome-shell-43.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
Requires: gnome-shell-bin = %{version}-%{release}
Requires: gnome-shell-data = %{version}-%{release}
Requires: gnome-shell-filemap = %{version}-%{release}
Requires: gnome-shell-lib = %{version}-%{release}
Requires: gnome-shell-libexec = %{version}-%{release}
Requires: gnome-shell-license = %{version}-%{release}
Requires: gnome-shell-locales = %{version}-%{release}
Requires: gnome-shell-man = %{version}-%{release}
Requires: gnome-shell-services = %{version}-%{release}
Requires: libgweather
BuildRequires : appstream-glib
BuildRequires : asciidoc
BuildRequires : bash-completion-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : clutter-dev
BuildRequires : docbook-xml
BuildRequires : evolution-data-server-dev
BuildRequires : glibc-bin
BuildRequires : gnome-bluetooth-dev
BuildRequires : gnome-control-center-dev
BuildRequires : gnome-desktop-dev
BuildRequires : gstreamer-dev
BuildRequires : libsass-dev
BuildRequires : libsoup-dev
BuildRequires : libxslt-bin
BuildRequires : mesa-dev
BuildRequires : mutter
BuildRequires : mutter-data
BuildRequires : mutter-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(gcr-4)
BuildRequires : pkgconfig(gcr-base-3)
BuildRequires : pkgconfig(gjs-1.0)
BuildRequires : pkgconfig(gnome-autoar-0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(libcanberra)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libcroco-0.6)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(telepathy-glib)
BuildRequires : python3-dev
BuildRequires : sassc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Please keep in sync with gnome-panel.

%package bin
Summary: bin components for the gnome-shell package.
Group: Binaries
Requires: gnome-shell-data = %{version}-%{release}
Requires: gnome-shell-libexec = %{version}-%{release}
Requires: gnome-shell-license = %{version}-%{release}
Requires: gnome-shell-services = %{version}-%{release}
Requires: gnome-shell-filemap = %{version}-%{release}

%description bin
bin components for the gnome-shell package.


%package data
Summary: data components for the gnome-shell package.
Group: Data

%description data
data components for the gnome-shell package.


%package filemap
Summary: filemap components for the gnome-shell package.
Group: Default

%description filemap
filemap components for the gnome-shell package.


%package lib
Summary: lib components for the gnome-shell package.
Group: Libraries
Requires: gnome-shell-data = %{version}-%{release}
Requires: gnome-shell-libexec = %{version}-%{release}
Requires: gnome-shell-license = %{version}-%{release}
Requires: gnome-shell-filemap = %{version}-%{release}

%description lib
lib components for the gnome-shell package.


%package libexec
Summary: libexec components for the gnome-shell package.
Group: Default
Requires: gnome-shell-license = %{version}-%{release}
Requires: gnome-shell-filemap = %{version}-%{release}

%description libexec
libexec components for the gnome-shell package.


%package license
Summary: license components for the gnome-shell package.
Group: Default

%description license
license components for the gnome-shell package.


%package locales
Summary: locales components for the gnome-shell package.
Group: Default

%description locales
locales components for the gnome-shell package.


%package man
Summary: man components for the gnome-shell package.
Group: Default

%description man
man components for the gnome-shell package.


%package services
Summary: services components for the gnome-shell package.
Group: Systemd services

%description services
services components for the gnome-shell package.


%prep
%setup -q -n gnome-shell-43.0
cd %{_builddir}/gnome-shell-43.0
pushd ..
cp -a gnome-shell-43.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664940811
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman=true \
-Dnetworkmanager=true \
-Dsystemd=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman=true \
-Dnetworkmanager=true \
-Dsystemd=true  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-shell
cp %{_builddir}/gnome-shell-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/gnome-shell-%{version}/data/theme/gnome-shell-sass/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d || :
cp %{_builddir}/gnome-shell-%{version}/subprojects/extensions-app/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/gnome-shell-%{version}/subprojects/extensions-tool/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/338650eb7a42dd9bc1f1c6961420f2633b24932d || :
cp %{_builddir}/gnome-shell-%{version}/subprojects/shew/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-shell
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-shell/Gvc-1.0.typelib
/usr/lib64/gnome-shell/Shell-0.1.typelib
/usr/lib64/gnome-shell/St-1.0.typelib
/usr/lib64/gnome-shell/girepository-1.0/Shew-0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-extensions
/usr/bin/gnome-extensions-app
/usr/bin/gnome-shell
/usr/bin/gnome-shell-extension-prefs
/usr/bin/gnome-shell-extension-tool
/usr/bin/gnome-shell-perf-tool
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/applications/evolution-calendar.desktop
/usr/share/applications/org.gnome.Extensions.desktop
/usr/share/applications/org.gnome.Shell.Extensions.desktop
/usr/share/applications/org.gnome.Shell.PortalHelper.desktop
/usr/share/applications/org.gnome.Shell.desktop
/usr/share/bash-completion/completions/gnome-extensions
/usr/share/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
/usr/share/dbus-1/interfaces/org.gnome.Shell.Introspect.xml
/usr/share/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
/usr/share/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
/usr/share/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
/usr/share/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
/usr/share/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
/usr/share/dbus-1/services/org.gnome.Extensions.service
/usr/share/dbus-1/services/org.gnome.ScreenSaver.service
/usr/share/dbus-1/services/org.gnome.Shell.CalendarServer.service
/usr/share/dbus-1/services/org.gnome.Shell.Extensions.service
/usr/share/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
/usr/share/dbus-1/services/org.gnome.Shell.Notifications.service
/usr/share/dbus-1/services/org.gnome.Shell.PortalHelper.service
/usr/share/dbus-1/services/org.gnome.Shell.Screencast.service
/usr/share/glib-2.0/schemas/00_org.gnome.shell.gschema.override
/usr/share/glib-2.0/schemas/org.gnome.shell.gschema.xml
/usr/share/gnome-control-center/keybindings/50-gnome-shell-launchers.xml
/usr/share/gnome-control-center/keybindings/50-gnome-shell-screenshots.xml
/usr/share/gnome-control-center/keybindings/50-gnome-shell-system.xml
/usr/share/gnome-shell/Gvc-1.0.gir
/usr/share/gnome-shell/Shell-0.1.gir
/usr/share/gnome-shell/St-1.0.gir
/usr/share/gnome-shell/gir-1.0/Shew-0.gir
/usr/share/gnome-shell/gnome-shell-dbus-interfaces.gresource
/usr/share/gnome-shell/gnome-shell-icons.gresource
/usr/share/gnome-shell/gnome-shell-osk-layouts.gresource
/usr/share/gnome-shell/gnome-shell-theme.gresource
/usr/share/gnome-shell/org.gnome.Extensions
/usr/share/gnome-shell/org.gnome.Extensions.data.gresource
/usr/share/gnome-shell/org.gnome.Extensions.src.gresource
/usr/share/gnome-shell/org.gnome.ScreenSaver
/usr/share/gnome-shell/org.gnome.ScreenSaver.src.gresource
/usr/share/gnome-shell/org.gnome.Shell.Extensions
/usr/share/gnome-shell/org.gnome.Shell.Extensions.src.gresource
/usr/share/gnome-shell/org.gnome.Shell.Notifications
/usr/share/gnome-shell/org.gnome.Shell.Notifications.src.gresource
/usr/share/gnome-shell/org.gnome.Shell.Screencast
/usr/share/gnome-shell/org.gnome.Shell.Screencast.src.gresource
/usr/share/gnome-shell/perf-background.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Extensions.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Extensions.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Shell.Extensions.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Extensions-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Shell.Extensions-symbolic.svg
/usr/share/metainfo/org.gnome.Extensions.metainfo.xml
/usr/share/xdg-desktop-portal/portals/gnome-shell.portal

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-gnome-shell

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-shell/libgnome-shell-menu.so
/usr/lib64/gnome-shell/libgnome-shell.so
/usr/lib64/gnome-shell/libgvc.so
/usr/lib64/gnome-shell/libshew-0.so
/usr/lib64/gnome-shell/libst-1.0.so
/usr/share/clear/optimized-elf/other*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-shell-calendar-server
/usr/libexec/gnome-shell-hotplug-sniffer
/usr/libexec/gnome-shell-overrides-migration.sh
/usr/libexec/gnome-shell-perf-helper
/usr/libexec/gnome-shell-portal-helper
/usr/share/clear/optimized-elf/exec*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-shell/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/gnome-shell/338650eb7a42dd9bc1f1c6961420f2633b24932d
/usr/share/package-licenses/gnome-shell/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnome-shell/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-extensions.1
/usr/share/man/man1/gnome-shell.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/org.gnome.Shell-disable-extensions.service
/usr/lib/systemd/user/org.gnome.Shell.target
/usr/lib/systemd/user/org.gnome.Shell@wayland.service
/usr/lib/systemd/user/org.gnome.Shell@x11.service

%files locales -f gnome-shell.lang
%defattr(-,root,root,-)

