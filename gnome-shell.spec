#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-shell
Version  : 3.26.2
Release  : 28
URL      : https://download.gnome.org/sources/gnome-shell/3.26/gnome-shell-3.26.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell/3.26/gnome-shell-3.26.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-shell-bin
Requires: gnome-shell-lib
Requires: gnome-shell-data
Requires: gnome-shell-locales
Requires: gnome-shell-doc
BuildRequires : clutter-dev
BuildRequires : docbook-xml
BuildRequires : evolution-data-server-dev
BuildRequires : glibc-bin
BuildRequires : gnome-bluetooth-dev
BuildRequires : gstreamer-dev
BuildRequires : libxslt-bin
BuildRequires : mesa-dev
BuildRequires : meson
BuildRequires : mutter
BuildRequires : mutter-data
BuildRequires : mutter-dev
BuildRequires : ninja
BuildRequires : pkgconfig(gcr-base-3)
BuildRequires : pkgconfig(gjs-1.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(libcanberra)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libcroco-0.6)
BuildRequires : pkgconfig(libnm-glib)
BuildRequires : pkgconfig(libnm-gtk)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(telepathy-glib)
BuildRequires : python3
BuildRequires : python3-dev
Patch1: blur.patch

%description
GNOME Shell provides core user interface functions for the GNOME 3 desktop,
like switching to windows and launching applications. GNOME Shell takes
advantage of the capabilities of modern graphics hardware and introduces
innovative user interface concepts to provide a visually attractive and
easy to use experience.

%package bin
Summary: bin components for the gnome-shell package.
Group: Binaries
Requires: gnome-shell-data

%description bin
bin components for the gnome-shell package.


%package data
Summary: data components for the gnome-shell package.
Group: Data

%description data
data components for the gnome-shell package.


%package doc
Summary: doc components for the gnome-shell package.
Group: Documentation

%description doc
doc components for the gnome-shell package.


%package lib
Summary: lib components for the gnome-shell package.
Group: Libraries
Requires: gnome-shell-data

%description lib
lib components for the gnome-shell package.


%package locales
Summary: locales components for the gnome-shell package.
Group: Default

%description locales
locales components for the gnome-shell package.


%prep
%setup -q -n gnome-shell-3.26.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522083283
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Denable-man=true -Denable-networkmanager=yes -Denable-systemd=yes builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-shell

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-shell/Gvc-1.0.typelib
/usr/lib64/gnome-shell/Shell-0.1.typelib
/usr/lib64/gnome-shell/ShellMenu-0.1.typelib
/usr/lib64/gnome-shell/St-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-shell
/usr/bin/gnome-shell-extension-prefs
/usr/bin/gnome-shell-extension-tool
/usr/bin/gnome-shell-perf-tool
/usr/libexec/gnome-shell-calendar-server
/usr/libexec/gnome-shell-hotplug-sniffer
/usr/libexec/gnome-shell-perf-helper
/usr/libexec/gnome-shell-portal-helper

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/gnome-shell-overrides.convert
/usr/share/applications/evolution-calendar.desktop
/usr/share/applications/gnome-shell-extension-prefs.desktop
/usr/share/applications/org.gnome.Shell.PortalHelper.desktop
/usr/share/applications/org.gnome.Shell.desktop
/usr/share/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
/usr/share/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
/usr/share/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
/usr/share/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
/usr/share/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
/usr/share/dbus-1/services/org.gnome.Shell.CalendarServer.service
/usr/share/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
/usr/share/dbus-1/services/org.gnome.Shell.PortalHelper.service
/usr/share/glib-2.0/schemas/org.gnome.shell.gschema.xml
/usr/share/gnome-control-center/keybindings/50-gnome-shell-system.xml
/usr/share/gnome-shell/Gvc-1.0.gir
/usr/share/gnome-shell/Shell-0.1.gir
/usr/share/gnome-shell/ShellMenu-0.1.gir
/usr/share/gnome-shell/St-1.0.gir
/usr/share/gnome-shell/gnome-shell-theme.gresource
/usr/share/gnome-shell/perf-background.xml
/usr/share/xdg-desktop-portal/portals/gnome-shell.portal

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-shell/libgnome-shell-menu.so
/usr/lib64/gnome-shell/libgnome-shell.so
/usr/lib64/gnome-shell/libgvc.so
/usr/lib64/gnome-shell/libst-1.0.so
/usr/lib64/mozilla/plugins/libgnome-shell-browser-plugin.so

%files locales -f gnome-shell.lang
%defattr(-,root,root,-)

