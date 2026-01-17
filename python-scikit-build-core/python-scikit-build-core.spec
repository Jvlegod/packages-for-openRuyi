# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scikit-build-core
%global _with_tests 0

Name:           python-%{srcname}
Version:        0.11.6
Release:        %autorelease
Summary:        Build backend for CMake based projects
License:        Apache-2.0
URL:            https://github.com/scikit-build/scikit-build-core
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/scikit_build_core-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-pytest

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc
BuildRequires:  gcc-c++

%global _description %{expand:
A next generation Python CMake adapter and Python API for plugins
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       cmake
Recommends:     ninja
Provides:       python3dist(%{srcname}) = %{version}-%{release}
%description -n python3-%{srcname} %_description

%pyproject_extras_subpkg -n python3-%{srcname} pyproject

%prep
%autosetup -n scikit_build_core-%{version}

%generate_buildrequires
%pyproject_buildrequires -x pyproject

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files scikit_build_core

%check
:
# We've temporarily commented out `pytest` and
# declared `with_tests 0` because these tests
# can cause many unnecessary dependency issues.
# pytest -m "not network"

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%{?autochangelog}