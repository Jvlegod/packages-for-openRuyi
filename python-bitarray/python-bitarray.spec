# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bitarray

Name:           python-%{srcname}
Version:        3.8.0
Release:        %autorelease
Summary:        Efficient arrays of booleans for Python
License:        PSF-2.0
URL:            https://github.com/ilanschnell/bitarray
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  gcc

BuildSystem:    pyproject

%description
bitarray provides an object type which efficiently represents an array of booleans.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%{?autochangelog}