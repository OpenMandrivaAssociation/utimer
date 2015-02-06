%define name	utimer
%define version 0.4
%define release 2

Summary:	Multifunction command-line timer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		File tools
Url:		https://launchpad.net/utimer
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel, intltool

%description
µTimer ("utimer", pronounced "micro-timer") is a multifunction timer
(command-line only). It provides a timer (e.g. count from 0 to 4
minutes), a countdown (e.g. count from 10 minutes to 0), and a
stopwatch.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%_bindir/utimer
%_mandir/man1/utimer.*


%changelog
* Wed Sep 14 2011 Lev Givon <lev@mandriva.org> 0.4-1mdv2011.0
+ Revision: 699725
- imported package utimer

