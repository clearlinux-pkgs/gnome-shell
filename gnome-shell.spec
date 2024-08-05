#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v18
# autospec commit: f35655a
#
Name     : gnome-shell
Version  : 46.4
Release  : 185
URL      : https://download.gnome.org/sources/gnome-shell/46/gnome-shell-46.4.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell/46/gnome-shell-46.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
Requires: gnome-shell-bin = %{version}-%{release}
Requires: gnome-shell-data = %{version}-%{release}
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
BuildRequires : libei-dev
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

%description bin
bin components for the gnome-shell package.


%package data
Summary: data components for the gnome-shell package.
Group: Data

%description data
data components for the gnome-shell package.


%package lib
Summary: lib components for the gnome-shell package.
Group: Libraries
Requires: gnome-shell-data = %{version}-%{release}
Requires: gnome-shell-libexec = %{version}-%{release}
Requires: gnome-shell-license = %{version}-%{release}

%description lib
lib components for the gnome-shell package.


%package libexec
Summary: libexec components for the gnome-shell package.
Group: Default
Requires: gnome-shell-license = %{version}-%{release}

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
Requires: systemd

%description services
services components for the gnome-shell package.


%prep
%setup -q -n gnome-shell-46.4
cd %{_builddir}/gnome-shell-46.4
pushd ..
cp -a gnome-shell-46.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722868750
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman=true \
-Dnetworkmanager=true \
-Dsystemd=true  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman=true \
-Dnetworkmanager=true \
-Dsystemd=true  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-shell
cp %{_builddir}/gnome-shell-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/gnome-shell-%{version}/data/theme/gnome-shell-sass/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d || :
cp %{_builddir}/gnome-shell-%{version}/subprojects/extensions-app/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/gnome-shell-%{version}/subprojects/extensions-tool/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/338650eb7a42dd9bc1f1c6961420f2633b24932d || :
cp %{_builddir}/gnome-shell-%{version}/subprojects/shew/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-shell
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-shell/Gvc-1.0.typelib
/usr/lib64/gnome-shell/Shell-14.typelib
/usr/lib64/gnome-shell/St-14.typelib
/usr/lib64/gnome-shell/girepository-1.0/Shew-0.typelib

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gnome-extensions
/V3/usr/bin/gnome-shell
/usr/bin/gnome-extensions
/usr/bin/gnome-extensions-app
/usr/bin/gnome-shell
/usr/bin/gnome-shell-extension-prefs
/usr/bin/gnome-shell-extension-tool
/usr/bin/gnome-shell-test-tool

%files data
%defattr(-,root,root,-)
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
/usr/share/glib-2.0/schemas/org.gnome.Extensions.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.gschema.xml
/usr/share/gnome-control-center/keybindings/50-gnome-shell-launchers.xml
/usr/share/gnome-control-center/keybindings/50-gnome-shell-screenshots.xml
/usr/share/gnome-control-center/keybindings/50-gnome-shell-system.xml
/usr/share/gnome-shell/Gvc-1.0.gir
/usr/share/gnome-shell/Shell-14.gir
/usr/share/gnome-shell/St-14.gir
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

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gnome-shell/libgnome-shell-menu.so
/V3/usr/lib64/gnome-shell/libgvc.so
/V3/usr/lib64/gnome-shell/libshell-14.so
/V3/usr/lib64/gnome-shell/libshew-0.so
/V3/usr/lib64/gnome-shell/libst-14.so
/usr/lib64/gnome-shell/libgnome-shell-menu.so
/usr/lib64/gnome-shell/libgvc.so
/usr/lib64/gnome-shell/libshell-14.so
/usr/lib64/gnome-shell/libshew-0.so
/usr/lib64/gnome-shell/libst-14.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gnome-shell-calendar-server
/V3/usr/libexec/gnome-shell-hotplug-sniffer
/V3/usr/libexec/gnome-shell-perf-helper
/V3/usr/libexec/gnome-shell-portal-helper
/usr/libexec/gnome-shell-calendar-server
/usr/libexec/gnome-shell-hotplug-sniffer
/usr/libexec/gnome-shell-perf-helper
/usr/libexec/gnome-shell-portal-helper

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

