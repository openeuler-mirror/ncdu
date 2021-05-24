Name:                ncdu
Version:             1.15.1
Release:             1
Summary:             Disk usage analyzer with an ncurses interface
License:             MIT
URL:                 https://dev.yorhel.nl/ncdu/
Source0:             https://dev.yorhel.nl/download/ncdu-%{version}.tar.gz
BuildRequires:       ncurses-devel
%description
It is designed to find space hogs on a remote server where you don't have an
entire graphical setup available,but it is a useful tool even on regular desktop
systems.Ncdu aims to be fast,simple and easy to use,and shold be able to run in
any minimal POSIX-like environment with ncurses installed

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_mandir}/man1/ncdu.1*
%doc ChangeLog COPYING
%{_bindir}/ncdu

%changelog
* Sun June 16 2021 huanghaitao <huanghaitao8@huawei.com> - 1.15.1-1
- package init
