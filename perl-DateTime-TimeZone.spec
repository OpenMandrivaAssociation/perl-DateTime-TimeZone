%define	upstream_name    DateTime-TimeZone
%define upstream_version 1.46

# circular dependency
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DateTime\\)|perl\\(DateTime::Duration\\)|perl\\(Win32::TieRegistry\\)'
%else
%define _requires_exceptions perl(DateTime)\\|perl(DateTime::Duration)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9
Epoch:		1

Summary:	Time zone object base class and factory
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Class::Singleton) >= 1.03
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.72
BuildRequires:	perl(Pod::Man) >= 1.14

BuildArch:	noarch

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
%{__perl} Makefile.PL installdirs=vendor destdir=%{buildroot}
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DateTime
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.270.0-4mdv2012.0
+ Revision: 765161
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.270.0-2
+ Revision: 667105
- mass rebuild

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.270.0-1
+ Revision: 634264
- update to new version 1.27

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.260.0-1mdv2011.0
+ Revision: 602098
- new version
- update to new version 1.23

* Mon Aug 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.210.0-1mdv2011.0
+ Revision: 572220
- update to 1.21

* Tue Jul 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.200.0-1mdv2011.0
+ Revision: 561944
- update to 1.20

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.190.0-1mdv2011.0
+ Revision: 553121
- update to 1.19

* Tue Apr 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.180.0-1mdv2010.1
+ Revision: 536961
- update to 1.18

* Sun Apr 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.170.0-1mdv2010.1
+ Revision: 536134
- update to 1.17

* Tue Apr 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.160.0-1mdv2010.1
+ Revision: 532142
- update to 1.16

* Tue Mar 30 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.150.0-1mdv2010.1
+ Revision: 529777
- update to 1.15

* Tue Mar 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.140.0-1mdv2010.1
+ Revision: 526817
- update to 1.14

* Tue Mar 09 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.130.0-1mdv2010.1
+ Revision: 517113
- update to 1.13

* Tue Mar 02 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.110.0-1mdv2010.1
+ Revision: 513473
- update to 1.11

* Wed Jan 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.100.0-1mdv2010.1
+ Revision: 497000
- update to 1.10

* Tue Jan 19 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.90.0-1mdv2010.1
+ Revision: 493485
- update to 1.09

* Wed Dec 30 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.80.0-1mdv2010.1
+ Revision: 483884
- update to 1.08

* Mon Dec 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.70.0-1mdv2010.1
+ Revision: 483037
- update to 1.07

* Wed Dec 23 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.60.0-1mdv2010.1
+ Revision: 481709
- update to 1.06

* Tue Nov 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.50.0-1mdv2010.1
+ Revision: 466749
- update to 1.05

* Tue Nov 10 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.40.0-1mdv2010.1
+ Revision: 463919
- update to 1.04

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.30.0-1mdv2010.1
+ Revision: 461272
- update to 1.03

* Tue Sep 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.990.0-1mdv2010.0
+ Revision: 450781
- update to 0.99

* Mon Sep 14 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.980.0-1mdv2010.0
+ Revision: 439423
- update to 0.98

* Wed Sep 09 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.970.0-1mdv2010.0
+ Revision: 435736
- update to 0.97

* Thu Aug 20 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.960.0-1mdv2010.0
+ Revision: 418412
- update to 0.96

* Thu Jul 23 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.930.0-1mdv2010.0
+ Revision: 398893
- update to 0.93
- using %%perl_convert_version
- fixed license field

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.91-1mdv2010.0
+ Revision: 383476
- update to new version 0.91

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.90-1mdv2010.0
+ Revision: 370049
- update to new version 0.90

* Wed Mar 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.85-1mdv2009.1
+ Revision: 357184
- update to new version 0.85

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.84-1mdv2009.1
+ Revision: 333411
- update to new version 0.84

* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.83-1mdv2009.1
+ Revision: 297812
- update to new version 0.83

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.82-1mdv2009.1
+ Revision: 294623
- update to new version 0.82

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.81-1mdv2009.1
+ Revision: 292133
- update to new version 0.81

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.79-1mdv2009.0
+ Revision: 270348
- update to new version 0.79

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.78-1mdv2009.0
+ Revision: 236265
- update to new version 0.78

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.77-1mdv2009.0
+ Revision: 212202
- update to new version 0.77

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.76-1mdv2009.0
+ Revision: 209323
- update to new version 0.76

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.75-1mdv2009.0
+ Revision: 202307
- new version
- update to new version 0.75

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.74-1mdv2009.0
+ Revision: 194844
- update to new version 0.74
- update to new version 0.74
- update to new version 0.73
- update to new version 0.73

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.72-1mdv2008.1
+ Revision: 152830
- update to new version 0.72

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.71-1mdv2008.1
+ Revision: 139190
- update to new version 0.71

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.70-1mdv2008.1
+ Revision: 114706
- update to new version 0.70

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.69-1mdv2008.1
+ Revision: 105304
- update to new version 0.69

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.68-1mdv2008.1
+ Revision: 97439
- update to new version 0.68

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.67-1mdv2008.0
+ Revision: 69218
- update to new version 0.67

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1:0.59-3mdv2008.0
+ Revision: 67782
- rebuild


* Tue Jan 30 2007 Scott Karns <scottk@mandriva.org> 0.59-2mdv2007.0
+ Revision: 115490
- Added _requires_exceptions to handle perl(DateTime) circular dependency

* Sun Jan 28 2007 Scott Karns <scottk@mandriva.org> 1:0.59-1mdv2007.1
+ Revision: 114575
- Updated to CPAN release 0.59

* Sat Aug 26 2006 Scott Karns <scottk@mandriva.org> 1:0.47-1mdv2007.0
+ Revision: 58078
- Version 0.47
- Import perl-DateTime-TimeZone

* Wed May 10 2006 Scott Karns <scottk@mandriva.org> 1:0.46-1mdk
- 0.46

* Sat May 06 2006 Scott Karns <scottk@mandriva.org> 1:0.45-2mdk
- Updated BuildRequires

* Wed May 03 2006 Scott Karns <scottk@mandriva.org> 1:0.45-1mdk
- 0.45

* Thu Apr 20 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.44-2mdk
- Use perl Policy

* Thu Apr 20 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.44-1mdk
- New release 0.44

* Mon Feb 27 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.42-1mdk
- 0.42

* Wed Feb 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.41-1mdk
- 0.41

* Thu Dec 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.40-1mdk
- 0.40

* Mon Dec 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.39-1mdk
- 0.39. Need to increase epoch.

* Fri Nov 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.3801-1mdk
- 0.3801 (fixes generated deps)

* Tue Nov 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.38-1mdk
- 0.38

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.37-2mdk
- Fix BuildRequires
- Fix Source url
- %%mkrel

* Wed Aug 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.37-1mdk
- 0.37

* Sat Apr 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.36-1mdk
- 0.36

* Wed Mar 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.33-1mdk
- 0.33

* Tue Jan 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.32-1mdk
- 0.32

* Fri Dec 10 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.31-1mdk
- 0.31

* Fri Oct 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.30-1mdk
- 0.30 (new database of timezones)

* Tue Aug 31 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.28-2mdk
- Add manually needed provides.

* Fri Aug 27 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.28-1mdk
- Initial MDK release.

