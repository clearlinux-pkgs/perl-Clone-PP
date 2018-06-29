#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Clone-PP
Version  : 1.07
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Clone-PP-1.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Clone-PP-1.07.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Clone-PP-man

%description
NAME
Clone::PP - Recursively copy Perl datatypes
SYNOPSIS
use Clone::PP qw(clone);

$item = { 'foo' => 'bar', 'move' => [ 'zig', 'zag' ]  };
$copy = clone( $item );

%package man
Summary: man components for the perl-Clone-PP package.
Group: Default

%description man
man components for the perl-Clone-PP package.


%prep
%setup -q -n Clone-PP-1.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Clone/PP.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Clone::PP.3
