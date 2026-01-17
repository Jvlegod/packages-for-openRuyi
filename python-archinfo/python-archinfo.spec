# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname archinfo

Name:           python-%{srcname}
Version:        9.2.193
Release:        %autorelease
Summary:        Collection of classes that contain architecture-specific information
License:        BSD
URL:            https://github.com/angr/archinfo
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname}
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname} -l

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%{?autochangelog}
