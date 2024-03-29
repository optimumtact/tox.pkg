%global _project tox
%global _prefix  /usr/%{_project}

Name:           %{_project}-gcc
Version:        4.9.3
Release:        1
Summary:        The GNU Compiler
License:        GPL-3.0+
Group:          Development/Languages/C and C++
URL:            http://gcc.gnu.org
BuildRequires:  gcc-c++, glibc-devel, binutils, perl, bison, flex, gettext-devel, texinfo, zlib-devel, zip, unzip, dejagnu, gmp-devel, mpfr-devel
Source0:        https://build.opensuse.org/source/home:antonbatenev:tox:tox-gcc/%{name}/%{name}_%{version}.orig.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?centos}
BuildRequires:  compat-glibc, elfutils-devel, libmpc-devel
%else
BuildRequires:  mpc-devel
%endif

%if 0%{?suse_version}
Source1:        https://build.opensuse.org/source/home:antonbatenev:tox:tox-gcc/%{name}/%{name}.rpmlintrc
%endif

%description
Core package for the GNU Compiler Collection, including the C language
frontend.

Language frontends other than C are split to different sub-packages,
namely gcc-ada, gcc-c++, gcc-fortran, gcc-java, gcc-objc and
gcc-obj-c++.


%define debug_package %{nil}


%prep
%setup -q


%build
./configure \
    --prefix=%{_prefix}        \
    --with-treads=posix        \
    --enable-languages=c,c++   \
    --disable-multilib         \
    --disable-profiling        \
    --enable-ld                \
    --disable-libgcj           \
    --disable-java             \
    --disable-gcj              \
    --disable-libgcj-multifile \
    --disable-plugin           \
    --with-tune=generic

make %{?_smp_mflags}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%install
make DESTDIR=%{buildroot} install
find "%{buildroot}" -name 'libstdc++.so*' -delete

%if 0%{?suse_version}
export NO_BRP_CHECK_RPATH="true"
%endif


%files
%defattr(-,root,root,-)

%if 0%{?suse_version}
%dir %{_prefix}
%endif

%{_prefix}


%changelog
* Mon Jun 24 2015 Anton Batenev <antonbatenev@yandex.ru> - 4.9.3-1
- Initial
