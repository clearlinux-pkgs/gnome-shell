#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-shell
Version  : 3.36.0
Release  : 71
URL      : https://download.gnome.org/sources/gnome-shell/3.36/gnome-shell-3.36.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell/3.36/gnome-shell-3.36.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: gnome-shell-bin = %{version}-%{release}
Requires: gnome-shell-data = %{version}-%{release}
Requires: gnome-shell-lib = %{version}-%{release}
Requires: gnome-shell-libexec = %{version}-%{release}
Requires: gnome-shell-license = %{version}-%{release}
Requires: gnome-shell-locales = %{version}-%{release}
Requires: gnome-shell-man = %{version}-%{release}
Requires: gnome-shell-services = %{version}-%{release}
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
BuildRequires : libxslt-bin
BuildRequires : mesa-dev
BuildRequires : mutter
BuildRequires : mutter-data
BuildRequires : mutter-dev
BuildRequires : pkgconfig(bash-completion)
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
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(telepathy-glib)
BuildRequires : python3-dev
BuildRequires : sassc

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

%description services
services components for the gnome-shell package.


%prep
%setup -q -n gnome-shell-3.36.0
cd %{_builddir}/gnome-shell-3.36.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585588295
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman=true -Dnetworkmanager=true -Dsystemd=true  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-shell
cp %{_builddir}/gnome-shell-3.36.0/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/gnome-shell-3.36.0/data/theme/gnome-shell-sass/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d
cp %{_builddir}/gnome-shell-3.36.0/subprojects/extensions-tool/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell/338650eb7a42dd9bc1f1c6961420f2633b24932d
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-shell

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-shell/Gvc-1.0.typelib
/usr/lib64/gnome-shell/Shell-0.1.typelib
/usr/lib64/gnome-shell/St-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-extensions
/usr/bin/gnome-shell
/usr/bin/gnome-shell-extension-prefs
/usr/bin/gnome-shell-extension-tool
/usr/bin/gnome-shell-perf-tool

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/gnome-shell-overrides.convert
/usr/share/applications/evolution-calendar.desktop
/usr/share/applications/org.gnome.Extensions.desktop
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
/usr/share/dbus-1/services/org.gnome.Shell.CalendarServer.service
/usr/share/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
/usr/share/dbus-1/services/org.gnome.Shell.PortalHelper.service
/usr/share/glib-2.0/schemas/00_org.gnome.shell.gschema.override
/usr/share/glib-2.0/schemas/org.gnome.shell.gschema.xml
/usr/share/gnome-control-center/keybindings/50-gnome-shell-system.xml
/usr/share/gnome-shell/Gvc-1.0.gir
/usr/share/gnome-shell/Shell-0.1.gir
/usr/share/gnome-shell/St-1.0.gir
/usr/share/gnome-shell/gnome-shell-dbus-interfaces.gresource
/usr/share/gnome-shell/gnome-shell-osk-layouts.gresource
/usr/share/gnome-shell/gnome-shell-theme.gresource
/usr/share/gnome-shell/perf-background.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Extensions.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Extensions.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Extensions-symbolic.svg
/usr/share/xdg-desktop-portal/portals/gnome-shell.portal

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-shell/libgnome-shell-menu.so
/usr/lib64/gnome-shell/libgnome-shell.so
/usr/lib64/gnome-shell/libgvc.so
/usr/lib64/gnome-shell/libst-1.0.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-shell-calendar-server
/usr/libexec/gnome-shell-hotplug-sniffer
/usr/libexec/gnome-shell-overrides-migration.sh
/usr/libexec/gnome-shell-perf-helper
/usr/libexec/gnome-shell-portal-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-shell/338650eb7a42dd9bc1f1c6961420f2633b24932d
/usr/share/package-licenses/gnome-shell/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnome-shell/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-extensions.1
/usr/share/man/man1/gnome-shell.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/gnome-shell-disable-extensions.service
/usr/lib/systemd/user/gnome-shell-wayland.service
/usr/lib/systemd/user/gnome-shell-wayland.target
/usr/lib/systemd/user/gnome-shell-x11.service
/usr/lib/systemd/user/gnome-shell-x11.target

%files locales -f gnome-shell.lang
%defattr(-,root,root,-)

