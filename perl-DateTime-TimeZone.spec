%define	upstream_name    DateTime-TimeZone
%define	upstream_version 0.99

# circular dependency
%define _requires_exceptions perl(DateTime)\\|perl(DateTime::Duration)

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Epoch:		1

Summary:	Time zone object base class and factory
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Class::Singleton) >= 1.03
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.72
BuildRequires:	perl(Pod::Man) >= 1.14

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Provides:	perl(DateTime::TimeZoneCatalog)

%description
This perl module defines the base class for all time zone objects. A time zone
is represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

Note that without the DateTime.pm module, this module does not do much. Its
primary interface is through a DateTime object, and most users will not need to
directly use DateTime::TimeZone methods.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
rm -rf %{buildroot}
chmod 644 Changes README
./Build install

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DateTime
%{_mandir}/*/*
