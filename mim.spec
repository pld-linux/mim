Summary:	MIM Isn't mtv
Name:		mim
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://limestone.uoregon.edu/pub/videolab/%{name}-%{version}.tar.gz
URL:		http://videolab.uoregon.edu/mim/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
View mpeg-1 audio and video multicast rtp streams.

%prep
%setup -q

%build
rm config.cache
%configure \
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

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sdr/plugins/*
