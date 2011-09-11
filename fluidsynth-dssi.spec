#
Summary:	Software synthesizer plugin for the DSSI Soft Synth Interface
Name:		fluidsynth-dssi
Version:	1.0.0
Release:	3
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/dssi/%{name}-%{version}.tar.gz
# Source0-md5:	6c9f660f0df4d2aad5076de75b2a0a67
Patch0:		%{name}-no_gtk1.patch
URL:		http://dssi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dssi-devel
BuildRequires:	fluidsynth-devel >= 1.0.3
BuildRequires:	gtk+2-devel
BuildRequires:	liblo-devel >= 0.23
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FluidSynth-DSSI is an implementation of the FluidSynth
soundfont-playing software synthesizer as a plugin for the DSSI Soft
Synth Interface. DSSI is a plugin API for software instruments (soft
synths) with user interfaces, permitting them to be hosted in-process
by audio applications.

%package gui
Summary:	Graphical interface for FluidSynth-DSSI
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui
GTK+ graphical user interface for FluidSynth-DSSI.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/dssi/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%{_libdir}/dssi/%{name}.so
%dir %{_libdir}/dssi/%{name}

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dssi/%{name}/FluidSynth-DSSI_gtk
