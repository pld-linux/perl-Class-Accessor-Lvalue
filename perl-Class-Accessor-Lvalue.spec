#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Class
%define		pnam	Accessor-Lvalue
%include	/usr/lib/rpm/macros.perl
Summary:	Class::Accessor::Lvalue - create Lvalue accessors
Name:		perl-Class-Accessor-Lvalue
Version:	0.11
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f39c187d5c2b16200f59aaa6d532999d
URL:		http://search.cpan.org/dist/Class-Accessor-Lvalue/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Want
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module subclasses Class::Accessor in order to provide lvalue
accessor makers.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Class/Accessor/Lvalue
%{perl_vendorlib}/Class/Accessor/Lvalue.pm
%{perl_vendorlib}/Class/Accessor/Lvalue/Fast.pm
%{_mandir}/man3/*
