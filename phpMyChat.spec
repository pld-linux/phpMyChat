# TODO
# - webapps
Summary:	Easy-to-install, and easy-to-use multi-room PHP/DB chat
Summary(pl.UTF-8):   Prosty w instalacji i użyciu wielopokojowy chat oparty na PHP/DB
Name:		phpMyChat
Version:	0.14.5
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/phpmychat/%{name}-%{version}.zip
# Source0-md5:	86b961cba624a5d3ea5bebf52a90fec5
Source1:	%{name}.conf
URL:		http://sourceforge.net/projects/phpmychat/
BuildRequires:	unzip
Requires:	php(mysql)
Requires:	php(pcre)
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_mychatdir	%{_datadir}/%{name}
%define		_sysconfdir	/etc/%{name}

%description
phpMyChat is an easy-to-install, easy-to-use multi-room PHP/DB chat.
It is currently available for MySQL, PostgreSQL, and ODBC, and the
work on Oracle is in progress. It supports IRC-like commands,
moderators, and is available with 37 languages.

%description -l pl.UTF-8
phpMyChat jest to prosty w instalacji i użyciu wielopokojowy chat
oparty na PHP/DB. Aktualnie dostępny dla MySQL, PostgreSQL i ODBC, a w
trakcie są już prace nad Oracle. Chat obsługiwany jest przed polecenia
podobne do tych, które znamy z IRCa, dostępne są również opcje
moderatorskie, a wszystko to posiada wsparcie dla 37 języków.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mychatdir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT{%{_sysconfdir},/etc/httpd}

install chat_activity.php3 phpMyChat.php3 $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -af chat/* $RPM_BUILD_ROOT%{_mychatdir}
rm -f $RPM_BUILD_ROOT%{_mychatdir}/config/*

cp chat/config/* $RPM_BUILD_ROOT%{_sysconfdir}
ln -sf %{_sysconfdir}/admin.css.php3 $RPM_BUILD_ROOT%{_mychatdir}/config/admin.css.php3
ln -sf %{_sysconfdir}/config.lib.php3 $RPM_BUILD_ROOT%{_mychatdir}/config/config.lib.php3
ln -sf %{_sysconfdir}/start_page.css.php3 $RPM_BUILD_ROOT%{_mychatdir}/config/start_page.css.php3
ln -sf %{_sysconfdir}/style.css.php3 $RPM_BUILD_ROOT%{_mychatdir}/config/style.css.php3

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
elif [ -d /etc/httpd/httpd.conf ]; then
	ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/usr/sbin/apachectl restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	umask 027
	if [ -d /etc/httpd/httpd.conf ]; then
		rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	else
		grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
			/etc/httpd/httpd.conf.tmp
		mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
		if [ -f /var/lock/subsys/httpd ]; then
			/usr/sbin/apachectl restart 1>&2
		fi
	fi
fi

%files
%defattr(644,root,root,755)
%doc docs/* readme.txt
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/chat_activity.php3
%dir %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%config(noreplace) %verify(not md5 mtime size) /etc/httpd/%{name}.conf
%dir %{_mychatdir}
%{_mychatdir}/admin
%{_mychatdir}/config
%{_mychatdir}/images
%{_mychatdir}/install
%{_mychatdir}/lib
%{_mychatdir}/localization
%{_mychatdir}/*.php3
%{_mychatdir}/favicon*
%{_mychatdir}/link*
