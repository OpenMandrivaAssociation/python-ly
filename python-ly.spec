%define	pypi_name python-ly

Summary:		Tool and library for manipulating LilyPond files
Name:	%{pypi_name}
Version:	0.9.9
Release:	1
License:	GPLv2+
Group:	Development/Python
Url:	https://github.com/frescobaldi/python-ly
Source0:	https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRequires:		pkgconfig(python)
BuildRequires:		python3dist(pyproject-api)
BuildRequires:		python3dist(setuptools)
BuildRequires:		python3dist(wheel)
BuildRequires:		python3dist(hatchling)
BuildRequires:		python3dist(sphinx)
BuildRequires:		python3dist(sphinx-rtd-theme)
BuildArch:		noarch

%description
This package provides a Python library ly containing various Python modules
to parse, manipulate or create documents in LilyPond format. A command line
program ly is also provided that can be used to do various manipulations with
LilyPond files.

%files
%doc README.rst CHANGELOG.md
%doc doc/build/html
%{_bindir}/ly
%{_bindir}/ly-server
%{py_puresitedir}/ly
%{py_puresitedir}/python_ly-%{version}.dist-info
%{_mandir}/man1/ly*.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%py_build

# Make docs and man pages
pushd doc
	make html
	make man
popd


%install
%py_install

# Install man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/

# Fix perms and shebang
chmod +x %{buildroot}%{py_puresitedir}/ly/data/makeschemedata.py
sed -i '1s|^#!/usr/bin/env python|#!%{__python}|' %{buildroot}%{py_puresitedir}/ly/data/makeschemedata.py

# Drop useless hidden file
rm -f doc/build/html/.buildinfo
