%global pypi_name python-ly

Name:           %{pypi_name}
Version:        0.9.6
Release:        1
Group:          Development/Python
Summary:        Tool and library for manipulating LilyPond files
License:        GPLv2+
URL:            https://github.com/wbsoft/python-ly
Source0:        http://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  pythonegg(setuptools)

%description
This package provides a Python library ly containing various Python
modules to parse, manipulate or create documents in LilyPond format.
A command line program ly is also provided that can be used to do
various manipulations with LilyPond files.

%prep
%setup -q -n %{pypi_name}-%{version}
%autopatch -p1

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%{_bindir}/ly
%{_bindir}/ly-server
%{python_sitelib}/*

