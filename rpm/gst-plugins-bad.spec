%define majorminor   1.0
%define gstreamer    gstreamer

%global _vpath_srcdir subprojects/gst-plugins-bad
%global _vpath_builddir subprojects/gst-plugins-bad/_build

Summary:     GStreamer streaming media framework "bad" plug-ins
Name:        %{gstreamer}%{majorminor}-plugins-bad
Version:     1.24.6
Release:     1
License:     LGPLv2+
URL:         http://gstreamer.freedesktop.org/
Source:      %{name}-%{version}.tar.xz
Patch1:      0001-Set-video-branch-to-NULL-after-finishing-video-recor.patch
Patch2:      0002-Keep-video-branch-in-NULL-state.patch
Patch3:      0003-jifmux-cope-with-missing-EOI-marker.patch
Patch4:      0004-Don-t-build-dxva-on-non-windows-platforms.patch
Patch5:      0005-Revert-jpegparse-bump-to-primary-rank.patch

%define sonamever %(echo %{version} | cut -d '+' -f 1)

Requires:      orc >= 0.4.18
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0) >= %{sonamever}
BuildRequires: gstreamer1.0-tools
BuildRequires: check
BuildRequires: pkgconfig(nice) >= 0.1.14
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(orc-0.4) >= 0.4.18
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= 1.15
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libsrtp2)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(sbc)
BuildRequires: pkgconfig(libsrtp2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(libdrm)
%ifnarch %{ix86} x86_64
BuildRequires: libatomic
%endif
BuildRequires: meson
BuildRequires: gettext-devel

BuildRequires: pkgconfig(wpe-webkit-2.0)
BuildRequires: pkgconfig(wpebackend-fdo-1.0)

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

%package devel
Summary: Development files for the GStreamer media framework "bad" plug-ins
Requires: %{name} = %{version}-%{release}
Requires: gstreamer1.0-plugins-base-devel

%description devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development files for the plug-ins that
are not tested well enough, or the code is not of good enough quality.

%package wpe
Summary:    GStreamer Plugins Bad WPE
Requires:   %{gstreamer}1.0-plugins-base = %{version}

%description wpe
GStreamer Plugins Bad WPE plugin

%package apps
Summary:    GStreamer Plugins Bad library applications
Requires:   %{gstreamer}1.0-plugins-base = %{version}

%description apps
GStreamer Plugins Bad library applications

%prep
%autosetup -p1 -n gstreamer1.0-plugins-bad-%{version}/gstreamer

%build

# OBS inserts --auto-features=enabled to verify that every plugin is
# specified one way or the other. Add this below for testing.
%meson \
  --auto-features=disabled \
  -Dpackage-name='SailfishOS GStreamer package plugins (bad set)' \
  -Dpackage-origin='http://sailfishos.org/' -Dorc=disabled \
  -Dintrospection=enabled -Dexamples=disabled -Ddoc=disabled -Dnls=disabled \
  -Daccurip=disabled -Dadpcmdec=disabled -Dadpcmenc=disabled -Daom=disabled \
  -Daes=disabled -Damfcodec=disabled -Dasfmux=disabled -D=assrender=disabled \
  -Daudiofxbad=disabled -Daudiovisualizers=disabled -Dautoconvert=disabled \
  -Dbayer=disabled -Dbluez=disabled -Dbs2b=disabled -Dbz2=disabled \
  -Dchromaprint=disabled -Dcoloreffects=disabled -Dcurl=disabled -Ddash=disabled \
  -Daja=disabled -Ddc1394=disabled -Dcodec2json=disabled -Dcodecalpha=disabled \
  -Ddebugutils=disabled -Ddecklink=disabled -D=directfb=disabled -Ddirectshow=disabled \
  -Ddts=disabled -Ddvb=disabled -Ddvbsuboverlay=disabled -Ddvdspu=disabled \
  -Dfaac=disabled -Dfaad=disabled -Dfaceoverlay=disabled -Dfbdev=disabled \
  -Dfdkaac=disabled -Dfestival=disabled -Dfieldanalysis=disabled \
  -Dflite=disabled -Dfluidsynth=disabled -Dfreeverb=disabled -Dfrei0r=disabled \
  -Dgs=disabled -Dgaudieffects=disabled -Dgdp=disabled -Dgeometrictransform=disabled \
  -Dgme=disabled -Dgsm=disabled -Dgtk3=disabled -Did3tag=disabled -Dinter=disabled \
  -Disac=disabled -Dinterlace=disabled -Diqa=disabled -Divfparse=disabled \
  -Divtc=disabled -Djp2kdecimator=disabled -Dladspa=disabled -Dlc3=disabled \
  -Dldac=disabled -Dlibde265=disabled -Dlibrfb=disabled -Dlv2=disabled \
  -Dmidi=disabled -Dmodplug=disabled -Dmpeg2enc=disabled -Dmpegpsmux=disabled \
  -Dmpegtsmux=disabled -Dmplex=disabled -Dmsdk=disabled -Dmusepack=disabled \
  -Dmxf=disabled -Dneon=disabled -Donnx=disabled \
  -Dopenal=disabled -Dopenaptx=disabled -Dopencv=disabled -Dopenexr=disabled \
  -Dopenh264=disabled -Dopenmpt=disabled -Dopenni2=disabled -Dopensles=disabled \
  -Dpcapparse=disabled -Dpnm=disabled -Dqroverlay=disabled -Dqsv=disabled \
  -Dqt6d3d11=disabled \
  -Dremovesilence=disabled -Dresindvd=disabled -Drsvg=disabled -Drtmp=disabled \
  -Dsctp=disabled -Dsdp=disabled -Dsegmentclip=disabled -Dsiren=disabled \
  -Dsmooth=disabled -Dsmoothstreaming=disabled -Dsoundtouch=disabled \
  -Dspandsp=disabled -Dspeed=disabled -Dsrt=disabled -Dsubenc=disabled -Dsvtav1=disabled \
  -Dteletext=disabled -Dtinyalsa=disabled -Dvideofilters=disabled \
  -Dvideosignal=disabled -Dvmnc=disabled -Dvoaacenc=disabled \
  -Dvoamrwbenc=disabled -Dvulkan=disabled -Dwasapi=disabled -Dwasapi2=disabled \
  -Dwebrtcdsp=disabled -Dwildmidi=disabled -Dwpe=enabled -Dx11=disabled \
  -Dx265=disabled -Dy4m=disabled -Dzbar=disabled -Dcolormanagement=disabled \
  -Dmagicleap=disabled -Dva=disabled -Davtp=disabled -Dmicrodns=disabled \
  -Dsvthevcenc=disabled -Dzxing=disabled

%meson_build

%install
%meson_install

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# remove waylandsink. It does not run because we do not support all the interfaces it needs.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
rm -f $RPM_BUILD_ROOT%{_libdir}/libgstwayland-%{majorminor}.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files

%files devel

%files apps

%files wpe
%{_libdir}/gstreamer-%{majorminor}/libgstwpe.so
%{_libdir}/gst-plugins-bad/wpe-extension/libgstwpeextension.so
