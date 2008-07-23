%define name	candido
%define tarname candido-engine
%define version	0.9.1
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Candido GTK2 cairo theme
Version: 	%{version}
Release: 	%{release}
Source:		%{tarname}-%{version}.tar.bz2
URL:		http://candido.berlios.de/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk2-devel

%description
The Candido engine is a cairo-based GTK2 engine for new thems.  
It's very fast and clean.

%prep
%setup -q -n %{tarname}-%{version}

%build
%configure2_5x --enable-animation
%make										
%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README
%{_libdir}/gtk-2.0/*/engines/libcandido.so
%{_libdir}/gtk-2.0/*/engines/libcandido.la

