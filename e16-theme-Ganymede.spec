%define	_tname	Ganymede
Summary:	Enlightenment Ganymede theme
Summary(pl):	Wystrój Ganymede dla Enlightenmenta
Name:		enlightenment-theme-%{_tname}
Version:	0.16
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	15d97ff251beb62ee481e2c67fe9a86d
# Source0-size:	2537767
Patch0:		%{name}-i18n.patch
URL:		http://www.enlightenment.org/
Requires:	enlightenment
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment Ganymede theme.

%description -l pl
Wystrój Ganymede dla Enlightenmenta.

%prep
%setup -q
mkdir %{_tname}
tar -zxf %{_tname}.etheme -C %{_tname}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/themes/
cp -a %{_tname} $RPM_BUILD_ROOT%{_datadir}/enlightenment/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/themes/%{_tname}
