%define tarname candido-engine

Name: 	 	candido
Summary: 	GTK2 cairo theme
Version: 	0.9.1
Release: 	6
Source:		%{tarname}-%{version}.tar.bz2
Patch0:		candido-engine-0.9.1-glib-includes.patch
URL:		http://candido.berlios.de/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRequires:	gtk2-devel

%description
The Candido engine is a cairo-based GTK2 engine for new thems.  
It's very fast and clean.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1

%build
%configure2_5x --enable-animation
%make										
%install
%makeinstall

%files
%defattr(-,root,root)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README
%{_libdir}/gtk-2.0/*/engines/libcandido.so


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-5mdv2011.0
+ Revision: 616936
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.9.1-4mdv2010.0
+ Revision: 424744
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-3mdv2009.0
+ Revision: 243431
- rebuild

* Wed Jan 09 2008 Lev Givon <lev@mandriva.org> 0.9.1-1mdv2008.1
+ Revision: 147367
- import candido


* Wed Jan 09 2008 Lev Givon <lev@mandriva.org> 0.9.1-1mdv2008.0
- Package for Mandriva.
