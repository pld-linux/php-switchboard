Summary:	MVC framework written in PHP
Name:		php-switchboard
Version:	2.0.1
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://www.danielslaughter.com/files/scripts/sb_%{version}.zip
# Source0-md5:	8ec708c1c4edd0b3f31901fade8ac8f6
URL:		http://www.danielslaughter.com/projects/
BuildRequires:	php-common
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unrar
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Switch Board is a MVC framework written for PHP. Its original concepts
were taken from a preexisting ColdFusion/PHP framework called Fusebox.
Its evolution through development has greatly changed its structure to
have very little resemblance to Fusebox other than slight
functionality of the switch, settings and template files.

%prep
%setup -qcT
# ehm, the file is .rar actually
unrar x -idq %{SOURCE0}
mv sb_20/{.??*,*} .; rmdir sb_20

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php
%{_appdir}
