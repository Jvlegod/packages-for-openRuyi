# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyvex
%global libvexversion 421bf0d9ec800df09fe4f8d90a8c13a0c63325e3

Name:           python-%{srcname}
Version:        9.2.193
Release:        %autorelease
Summary:        A Python interface to libvex and VEX IR
License:        BSD-2-Clause and GPL-3.0-or-later and LGPL-2.0-only
URL:            https://github.com/angr/pyvex
#!RemoteAsset
Source0:        https://github.com/angr/pyvex/archive/v%{version}/pyvex-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/angr/vex/archive/%{libvexversion}/vex-%{libvexversion}.tar.gz

%global _description %{expand:
A Python interface to libVEX and the VEX intermediate representation.}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(scikit-build-core) >= 0.11.4
BuildRequires:  python3dist(cffi) >= 1.0.3
BuildRequires:  python3-bitstring

%description %_description

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%prep
%autosetup -p1 -n %{srcname}-%{version}
%ifarch riscv64
sed -i 's/assert kb_end - kb_start < 5000/assert kb_end - kb_start < 50000/' tests/test_pyvex.py
%endif
tar xvf %{SOURCE1}
rm -rf vex
mv vex-%{libvexversion} vex

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
mv pyvex_c/LICENSE LICENSE-pyvex_c
%pyproject_save_files -l pyvex

%check
for f in \
    tests/test_arm_postprocess.py \
    tests/test_gym.py \
    tests/test_irsb_property_caching.py \
    tests/test_lift.py \
    tests/test_mips32_postprocess.py \
    tests/test_pyvex.py \
    tests/test_s390x_exrl.py \
    tests/test_s390x_lochi.py \
    tests/test_s390x_vl.py \
    tests/test_spotter.py \
    tests/test_ud2.py;
do
    %{py3_test_envvars} %{python3} $f
done

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%license LICENSE-pyvex_c

%changelog
%{?autochangelog}