Summary:	A powerful open source data analysis software
Name:		scicraft
Version:	1.0.2
Release:	%mkrel 1
License:	GPL
Group:		Sciences/Other
URL:		http://www.scicraft.org/
Source0:	http://www.scicraft.org/files/%{name}-ng_%{version}.tar.bz2
BuildRequires:	python-devel
BuildRequires:  tetex-dvipdfm
BuildRequires:  latex2html
BuildRequires:  perl
BuildRequires:  imagemagick
BuildRequires:  dos2unix

Requires:	python
Requires:       python-qwt
Requires:       octave 
Requires:       python-vtk
Requires: python-rpy python-gtk python-gobject python-gtk-glade python-gnome python-gtk python-matplotlib python-scipy
Requires:	PyQt
Requires:	R-base
Obsoletes: scicraft-examples

BuildArch:	noarch
# for tests
# BuildRequires:	python-qwt pymol python-rpy

%description
SciCraft is a powerful open source data analysis software with an easy-to-use
graphical user interface

Many of todays scientists face the following problem: They need to integrate a
substantial number of computational tools to solve problems. 

SciCraft is a software designed to make software and method integration easier.
It is also designed to make different computational tools easily available to
the user. In theory SciCraft can be used to integrate any type of software, but
we have in particular focused on the integration and availability of data
analysis methods which originate from fields such as bioinformatics,
statistics, chemometrics and artificial intelligence. One reason for this focus
is that irrespective of the scientific field in question, there is almost
always a need to perform data analysis.

%prep
%setup -qn %{name}-ng-%{version}
# %patch0
#find -type f -exec dos2unix -U {} \;

%build

%install
rm -rf %buildroot

%makeinstall_std
#make install DESTDIR=%buildroot

%check
# X display needed
#make test

%clean
rm -rf %buildroot

%files
%defattr(0644, root, root, 0755)
%attr(0755, root, root) %{_bindir}/*
%{_prefix}/lib/*
%{_datadir}/doc/%{name}-ng
