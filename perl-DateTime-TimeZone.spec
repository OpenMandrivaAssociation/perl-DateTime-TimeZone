%define	upstream_name    DateTime-TimeZone
%define upstream_version 1.78

# circular dependency
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DateTime\\)|perl\\(DateTime::Duration\\)|perl\\(Win32::TieRegistry\\)'
%else
%define _requires_exceptions perl(DateTime)\\|perl(DateTime::Duration)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Epoch:		1

Summary:	Time zone object base class and factory


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires: perl(Test::Fatal)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Class::Singleton) >= 1.03
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.72
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl(Test::Requires)

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL installdirs=vendor destdir=%{buildroot}
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/DateTime
%{_mandir}/*/*
