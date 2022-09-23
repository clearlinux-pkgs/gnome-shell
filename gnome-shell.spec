#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-shell
Version  : 43.0
Release  : 117
URL      : https://download.gnome.org/sources/gnome-shell/43/gnome-shell-43.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell/43/gnome-shell-43.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
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
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsoup-2.4)
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
export SOURCE_DATE_EPOCH=1663952434
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
