#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : home-assistant
Version  : 0.97.2
Release  : 102
URL      : https://github.com/home-assistant/home-assistant/archive/0.97.2/home-assistant-0.97.2.tar.gz
Source0  : https://github.com/home-assistant/home-assistant/archive/0.97.2/home-assistant-0.97.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: home-assistant-bin = %{version}-%{release}
Requires: home-assistant-license = %{version}-%{release}
Requires: home-assistant-python = %{version}-%{release}
Requires: home-assistant-python3 = %{version}-%{release}
Requires: Jinja2
Requires: PyJWT
Requires: PyQRCode
Requires: SQLAlchemy
Requires: aiohttp
Requires: aiohttp-cors
Requires: astral
Requires: async-timeout
Requires: bcrypt
Requires: distro
Requires: envs
Requires: eternalegypt
Requires: gTTS-token
Requires: home-assistant-frontend
Requires: importlib_metadata
Requires: libstoragemgmt-python3
Requires: mutagen
Requires: netdisco
Requires: pyotp
Requires: python-openzwave
Requires: python-slugify
Requires: ruamel.yaml
Requires: ua-parser
Requires: user-agents
Requires: voluptuous
Requires: voluptuous-serialize
Requires: xmltodict
Requires: zeroconf
BuildRequires : Jinja2
BuildRequires : PyJWT
BuildRequires : PyQRCode
BuildRequires : SQLAlchemy
BuildRequires : aiohttp
BuildRequires : aiohttp-cors
BuildRequires : astral
BuildRequires : async-timeout
BuildRequires : bcrypt
BuildRequires : buildreq-distutils3
BuildRequires : distro
BuildRequires : envs
BuildRequires : eternalegypt
BuildRequires : gTTS-token
BuildRequires : home-assistant-frontend
BuildRequires : mutagen
BuildRequires : netdisco
BuildRequires : pyotp
BuildRequires : python-openzwave
BuildRequires : python-slugify
BuildRequires : ruamel.yaml
BuildRequires : ua-parser
BuildRequires : user-agents
BuildRequires : voluptuous
BuildRequires : voluptuous-serialize
BuildRequires : xmltodict
BuildRequires : zeroconf

%description
Home Assistant |Chat Status|
=================================================================================

%package bin
Summary: bin components for the home-assistant package.
Group: Binaries
Requires: home-assistant-license = %{version}-%{release}

%description bin
bin components for the home-assistant package.


%package license
Summary: license components for the home-assistant package.
Group: Default

%description license
license components for the home-assistant package.


%package python
Summary: python components for the home-assistant package.
Group: Default
Requires: home-assistant-python3 = %{version}-%{release}

%description python
python components for the home-assistant package.


%package python3
Summary: python3 components for the home-assistant package.
Group: Default
Requires: python3-core

%description python3
python3 components for the home-assistant package.


%prep
%setup -q -n home-assistant-0.97.2

%build
## build_prepend content
sed -i 's/==/>=/g' setup.py
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566617992
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/home-assistant
cp LICENSE.md %{buildroot}/usr/share/package-licenses/home-assistant/LICENSE.md
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hass

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/home-assistant/LICENSE.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
