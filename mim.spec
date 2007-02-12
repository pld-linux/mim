Summary:	MIM Isn't Mtv
Summary(pl.UTF-8):   MIM Inny niż Mtv
Name:		mim
Version:	1.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://limestone.uoregon.edu/pub/videolab/%{name}-%{version}.tar.gz
# Source0-md5:	a9fe1664e3b44aa684e5127bec2711dd
URL:		http://videolab.uoregon.edu/mim/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
View mpeg-1 audio and video multicast rtp streams.

%description -l pl.UTF-8
Odtwarzacz dźwięku i obrazu MPEG-1 oraz multicastowych strumieni rtp.

%prep
%setup -q

%build
rm -f config.cache
%configure2_13 \
	--enable-gui \
        --with-gtk-prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/sdr/plugins,%{_mandir}/man1}
install examples/* $RPM_BUILD_ROOT%{_sysconfdir}/sdr/plugins
install docs/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sdr/plugins/*
