Summary:	Easy-to-install, and easy-to-use multi-room PHP/DB chat.
Summary(pl):	Prosty w instalacji i u¿yciu wielopokojowy chat oparty na PHP/DB
Name:		phpMyChat
Version:	0.14.5
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/phpmychat/%{name}-%{version}.zip	
# Source0-md5:	86b961cba624a5d3ea5bebf52a90fec5
URL:		http://sourceforge.net/projects/phpmychat/
Requires:	php-mysql
Requires:	php-pcre
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_mychatdir	/home/services/httpd/html/mychat

%description
phpMyChat is an easy-to-install, easy-to-use multi-room PHP/DB chat.
It is currently available for MySQL, PostgreSQL, and ODBC, and the
work on Oracle is in progress. It supports IRC-like commands,
moderators, and is available with 37 languages.

%description -l pl
phpMyChat jest to prosty w instalacji i u¿yciu wielopokojowy chat
oparty na PHP/DB. Aktualnie dostêpny dla MySQL, PostgreSQL i ODBC, a w
trakcie s± ju¿ prace nad Oracle. Chat obs³ugiwany jest przed polecenia
podobne do tych, które znamy z IRCa, dostêpne s± równie¿ opcje
moderatorskie, a wszystko to posiada wspracie dla 37 jêzyków.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mychatdir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install chat_activity.php3 phpMyChat.php3 $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -af chat/*				  $RPM_BUILD_ROOT%{_mychatdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* readme.txt
%{_examplesdir}/%{name}-%{version}/chat_activity.php3
%dir %{_mychatdir}
%{_mychatdir}/admin/
%{_mychatdir}/config/
%{_mychatdir}/images/
%{_mychatdir}/install/
%{_mychatdir}/lib/
%{_mychatdir}/localization/
%{_mychatdir}/*.php3
%{_mychatdir}/favicon*
%{_mychatdir}/link*
