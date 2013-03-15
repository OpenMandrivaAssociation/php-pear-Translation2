%define		_class		Translation2
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	2.0.4
Release:	3
Summary:	Class for multilingual applications management
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Translation2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This class provides an easy way to retrieve all the strings for a
multilingual site from a data source (i.e. db). A PEAR::DB and a
PEAR::MDB container are provided, more containers will follow. It is
designed to reduce the number of queries to the db, caching the
results when possible. An Admin class is provided to easily manage
translations (add/remove a language, add/remove a string).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_bindir}/t2xmlchk.php
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-2mdv2011.0
+ Revision: 667643
- mass rebuild

* Wed Dec 29 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-1mdv2011.0
+ Revision: 625901
- 2.0.4

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-6mdv2011.0
+ Revision: 607155
- rebuild

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.1-5mdv2010.1
+ Revision: 466330
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.1-4mdv2010.0
+ Revision: 426670
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 2.0.1-3mdv2009.1
+ Revision: 368292
- Increase release to override old 2.0.0beta8 known as 2.0.1 release
- Update php pear Translation2 to 2.0.1 stable version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-2mdv2009.1
+ Revision: 321906
- rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.1-1mdv2009.1
+ Revision: 305817
- update to new version 2.0.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-11mdv2009.0
+ Revision: 224884
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-10mdv2008.1
+ Revision: 178540
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-9mdv2008.0
+ Revision: 90140
- rebuild


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-8mdv2007.0
+ Revision: 81236
- Import php-pear-Translation2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-8mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-7mdk
- 2.0.0beta8

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-1mdk
- initial Mandriva package (PLD import)

