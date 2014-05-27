%define	_class	Translation2
%define	modname	%{_class}
%define __noautoreq '/usr/bin/php'

Summary:	Class for multilingual applications management
Name:		php-pear-%{modname}
Version:	2.0.4
Release:	8
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Translation2/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This class provides an easy way to retrieve all the strings for a
multilingual site from a data source (i.e. db). A PEAR::DB and a
PEAR::MDB container are provided, more containers will follow. It is
designed to reduce the number of queries to the db, caching the
results when possible. An Admin class is provided to easily manage
translations (add/remove a language, add/remove a string).

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/*
%{_bindir}/t2xmlchk.php
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

