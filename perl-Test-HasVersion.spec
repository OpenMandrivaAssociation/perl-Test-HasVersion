%define upstream_name    Test-HasVersion
%define upstream_version 0.012

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Check Perl modules have version numbers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Do you wanna check that every one of your Perl modules in a distribution
has a version number? You wanna make sure you don't forget the brand new
modules you just added? Well, that's the module you have been looking for.
Use it!

Do you wanna check someone else's distribution to make sure the author have
not commited the sin of leaving Perl modules without a version that can be
used to tell if you have this or that feature? 'Test::HasVersion' is also
for you, nasty little fellow.

There's a script _test_version_ which is installed with this distribution.
You may invoke it from within the root directory of a distribution you just
unpacked, and it will check every _.pm_ file in the directory and under
_lib/_ (if any).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/test_version

