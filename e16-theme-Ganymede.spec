%define	_tname	Ganymede
Summary:	Enlightenment Ganymede theme
Summary(pl.UTF-8):	Wystrój Ganymede dla Enlightenmenta
Name:		e16-theme-%{_tname}
Version:	0.16.8
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	c70942b619b02a548f607653d12802a8
Patch0:		%{name}-i18n.patch
URL:		http://www.enlightenment.org/
Requires:	e16
Obsoletes:	enlightenment-theme-%{_tname} <= 0.16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment Ganymede theme.

%description -l pl.UTF-8
Wystrój Ganymede dla Enlightenmenta.

%prep
%setup -q
mkdir %{_tname}
tar -zxf %{_tname}.etheme -C %{_tname}
%patch0 -p1
find -name "*.orig" -or -name "*~" -exec rm "{}" ";"
rm %{_tname}/ttfonts/*
rm %{_tname}/fonts.cfg.*

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/e16/themes/
cp -a %{_tname} $RPM_BUILD_ROOT%{_datadir}/e16/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/e16/themes/%{_tname}
