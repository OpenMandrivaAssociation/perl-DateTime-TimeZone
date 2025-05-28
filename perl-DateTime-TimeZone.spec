%define	upstream_name    DateTime-TimeZone

# circular dependency
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DateTime\\)|perl\\(DateTime::Duration\\)|perl\\(Win32::TieRegistry\\)'
%else
%define _requires_exceptions perl(DateTime)\\|perl(DateTime::Duration)
%endif

Name:		perl-%{upstream_name}
Version:	2.65
Release:	1

Summary:	Time zone object base class and factory


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/DateTime::TimeZone
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Class::Singleton)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Params::ValidationCompiler)
BuildRequires:	perl(Specio::Library::String)
BuildRequires:	perl(Specio::Library::Builtins)
BuildRequires:	perl(Sub::Identify)

BuildArch:	noarch

Provides:	perl(DateTime::TimeZoneCatalog)
Requires:	perl(namespace::clean)

%description
This perl module defines the base class for all time zone objects. A time zone
is represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

Note that without the DateTime.pm module, this module does not do much. Its
primary interface is through a DateTime object, and most users will not need to
directly use DateTime::TimeZone methods.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL installdirs=vendor destdir=%{buildroot}
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes 
%{perl_vendorlib}/DateTime
%{_mandir}/*/*
