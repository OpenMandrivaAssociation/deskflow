# When build locally there was a library componet that the ABF did not create. Leaving left overs in case this oddity becomes an issue.

#define major 1
#define libname %mklibname deskflow
#define devname %mklibname deskflow -d

Name:		deskflow
Version:	1.26.0
Release:	1
Source0:	https://github.com/deskflow/deskflow/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	Share a single keyboard and mouse between multiple computers
URL:		https://github.com/deskflow/deskflow
License:	GPLv2
Group:		Applications/Productivity

BuildSystem:	cmake
BuildRequires:	pkgconfig(xtst)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  doxygen
BuildRequires:  pkgconfig(libportal)
BuildRequires:  cli11-devel
BuildRequires:  help2man
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gtest)

%description
Share a single keyboard and mouse between multiple computers

#%package -n %{libname}
#Summary:	Share a single keyboard and mouse between multiple computers
#Group:		System/Libraries

#%description -n %{libname}
#Share a single keyboard and mouse between multiple computers

#%package -n %{devname}
#Summary:	Development files for %{name}
#Group:		Development/C
#Requires:	%{libname} = %{EVRD}

#%description -n %{devname}
#Development files (Headers etc.) for %{name}.


%prep
%autosetup -p1

%files
%license LICENSE
%{_datadir}/licenses/deskflow/LICENSE_EXCEPTION
%doc %{_docdir}/deskflow/html/
%exclude %{_docdir}/deskflow/html/search/pages_*.js
%{_bindir}/deskflow*
%{_datadir}/applications/org.deskflow.deskflow.desktop
%{_iconsdir}/hicolor/512x512/apps/org.deskflow.deskflow.png
%{_mandir}/man1/deskflow*
%{_datadir}/metainfo/org.deskflow.deskflow.metainfo.xml

#%files -n %{libname}
#%{_libdir}/*.so.*%{major}*

#%files -n %{devname}
#%{_includedir}/*
#%{_libdir}/*.so
#%{_libdir}/pkgconfig/*
#%{_libdir}/cmake/*
