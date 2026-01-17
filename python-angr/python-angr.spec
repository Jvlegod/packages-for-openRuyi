# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname angr

Name:           python-%{srcname}
Version:        9.2.193
Release:        %autorelease
Summary:        a multi-architecture binary analysis toolkit
License:        BSD-2-Clause
URL:            https://github.com/angr/angr
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(openssl)
BuildSystem:    pyproject

%description
angr is a multi-architecture binary analysis toolkit, with the ability 
to perform dynamic symbolic execution and various static analyses on binaries.

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
%doc README.md

%changelog
%{?autochangelog}
