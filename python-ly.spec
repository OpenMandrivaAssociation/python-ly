%define module python-ly
%define oname python_ly

Name:		python-ly
Summary:	Tool and library for manipulating LilyPond files
Version:	0.9.10
Release:	1
License:	GPLv2+
Group:		Development/Python
URL:		https://github.com/frescobaldi/python-ly
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pyproject-api)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphinx-rtd-theme)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package provides a Python library ly containing various Python modules
to parse, manipulate or create documents in LilyPond format. A command line
program ly is also provided that can be used to do various manipulations with
LilyPond files.

%prep -a
# Moving this to prep stage fixes the rpmlint-
# python-bytecode-inconsistent-mtime error during package check stage.
# Fix perms and shebang
chmod +x ly/data/makeschemedata.py
sed -i '1s|^#!/usr/bin/env python|#!%{__python}|' ly/data/makeschemedata.py

%build -a
# Make docs and man pages
pushd doc
	make html
	make man
popd

%install -a
# Install man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/

# Drop useless hidden file
rm -f doc/build/html/.buildinfo

%files
%doc README.rst CHANGELOG.md
%doc doc/build/html
%{_bindir}/ly
%{_bindir}/ly-server
%{py_puresitedir}/ly
%{py_puresitedir}/%{oname}-%{version}.dist-info
%{_mandir}/man1/ly*.1.*
