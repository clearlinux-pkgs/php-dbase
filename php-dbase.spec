#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-dbase
Version  : 7.1.1
Release  : 69
URL      : https://pecl.php.net/get/dbase-7.1.1.tgz
Source0  : https://pecl.php.net/get/dbase-7.1.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-dbase-lib = %{version}-%{release}
Requires: php-dbase-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the php-dbase package.
Group: Libraries
Requires: php-dbase-license = %{version}-%{release}

%description lib
lib components for the php-dbase package.


%package license
Summary: license components for the php-dbase package.
Group: Default

%description license
license components for the php-dbase package.


%prep
%setup -q -n dbase-7.1.1
cd %{_builddir}/dbase-7.1.1
pushd ..
cp -a dbase-7.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-dbase
cp %{_builddir}/dbase-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-dbase/23cb6fa873d559515b754db54720962118c95899 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/dbase.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-dbase/23cb6fa873d559515b754db54720962118c95899
