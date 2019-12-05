#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : svg.path
Version  : 4.0.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/63/f9/56781c02bb69f96f0af1644aaabf065bea6cb0e67ffe2b3ca100847f3f82/svg.path-4.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/f9/56781c02bb69f96f0af1644aaabf065bea6cb0e67ffe2b3ca100847f3f82/svg.path-4.0.2.tar.gz
Summary  : SVG path objects and parser
Group    : Development/Tools
License  : MIT
Requires: svg.path-license = %{version}-%{release}
Requires: svg.path-python = %{version}-%{release}
Requires: svg.path-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : util-linux

%description
svg.path
========
svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.

%package license
Summary: license components for the svg.path package.
Group: Default

%description license
license components for the svg.path package.


%package python
Summary: python components for the svg.path package.
Group: Default
Requires: svg.path-python3 = %{version}-%{release}

%description python
python components for the svg.path package.


%package python3
Summary: python3 components for the svg.path package.
Group: Default
Requires: python3-core

%description python3
python3 components for the svg.path package.


%prep
%setup -q -n svg.path-4.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572879113
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/svg.path
cp %{_builddir}/svg.path-4.0.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/svg.path/d14a2577da362843bb255e84ec3c2dd4bfd47f50
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/svg.path/d14a2577da362843bb255e84ec3c2dd4bfd47f50

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
