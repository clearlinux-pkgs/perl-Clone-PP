#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Clone-PP
Version  : 1.08
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Clone-PP-1.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Clone-PP-1.08.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Clone-PP-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Clone::PP - Recursively copy Perl datatypes
SYNOPSIS
use Clone::PP qw(clone);

$item = { 'foo' => 'bar', 'move' => [ 'zig', 'zag' ]  };
$copy = clone( $item );

%package dev
Summary: dev components for the perl-Clone-PP package.
Group: Development
Provides: perl-Clone-PP-devel = %{version}-%{release}
Requires: perl-Clone-PP = %{version}-%{release}

%description dev
dev components for the perl-Clone-PP package.


%package perl
Summary: perl components for the perl-Clone-PP package.
Group: Default
Requires: perl-Clone-PP = %{version}-%{release}

%description perl
perl components for the perl-Clone-PP package.


%prep
%setup -q -n Clone-PP-1.08
cd %{_builddir}/Clone-PP-1.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Clone::PP.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Clone/PP.pm
