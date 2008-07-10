Summary:	SCSI utilities
Summary(pl.UTF-8):	Narzędzia do SCSI
Name:		scsiinfo
Version:	1.7
Release:	1
License:	GPL v2
Group:		Applications/System
# formerly ftp://tsx-11.mit.edu/pub/linux/ALPHA/scsi/
Source0:	ftp://ftp.iavsc.org/pub/linux/ALPHA/scsi/%{name}-%{version}.tar.gz
# Source0-md5:	1d7a9a42e84430d14b2fbfee342a950c
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-misc.patch
Patch3:		%{name}-tmpdir.patch
Patch4:		%{name}-llh.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
A collection of useful tools for users of SCSI systems:
- scsiinfo: Allows to access some internals of SCSI devices, such as
  defect lists or the so-called mode pages, which control e.g. the
  behaviour of the device's cache or error management.
- scsiformat: A low-level formatting tool for SCSI disks.

Note: scsiinfo comes with a graphical user interface which can be
found in the scsiinfo-tk package.

%description -l pl.UTF-8
Zestaw użytecznych narzędzi dla użytkowników systemów SCSI:
- scsiinfo: pozwala na dostęp do niektórych informacji wewnętrznych
  SCSI, takich jak listy defektów, strony trybów (kontrolujących
  zachowanie cache urządzenia i obsługę błędów).
- scsiformat: narzędzie do niskopoziomowego formatowania dysków SCSI.

Dostępny jest interfejs graficzny do scsiinfo - znajduje się w
pakiecie scsiinfo-tk.

%package tk
Summary:	Tk graphical frontend for scsiinfo
Summary(pl.UTF-8):	Graficzny frontend do scsiinfo oparty o Tk
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	tk
Obsoletes:	scsiutils-tk

%description tk
For visualization and manipulation of SCSI mode pages, scsiinfo comes
with graphical interface.

%description tk -l pl.UTF-8
Graficzny interfejs do scsiinfo, służący do wizualizacji i operacji na
stronach trybów SCSI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} clean
%{__make} \
	CC="%{__cc} -DCONFIG_BLOCK=1" \
	LDFLAGS="%{rpmldflags}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 0-CHANGES 0-README.first 0-TODO
%attr(755,root,root) %{_bindir}/scsiformat
%attr(755,root,root) %{_bindir}/scsiinfo
%attr(755,root,root) %{_sbindir}/sgcheck
%{_mandir}/man8/scsiformat.8*
%{_mandir}/man8/scsiinfo.8*

%files tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/scsi-config
%attr(755,root,root) %{_bindir}/tk_scsiformat
%dir %{_ulibdir}/scsi
%attr(755,root,root) %{_ulibdir}/scsi/cache
%attr(755,root,root) %{_ulibdir}/scsi/control
%attr(755,root,root) %{_ulibdir}/scsi/disconnect
%attr(755,root,root) %{_ulibdir}/scsi/error
%attr(755,root,root) %{_ulibdir}/scsi/format
%{_ulibdir}/scsi/generic
%attr(755,root,root) %{_ulibdir}/scsi/inquiry
%attr(755,root,root) %{_ulibdir}/scsi/notch
%attr(755,root,root) %{_ulibdir}/scsi/overview
%attr(755,root,root) %{_ulibdir}/scsi/peripheral
%attr(755,root,root) %{_ulibdir}/scsi/rigid
%attr(755,root,root) %{_ulibdir}/scsi/save-changes
%attr(755,root,root) %{_ulibdir}/scsi/save-file
%attr(755,root,root) %{_ulibdir}/scsi/tworands
%attr(755,root,root) %{_ulibdir}/scsi/verify
%{_mandir}/man8/scsi-config.8*
%{_mandir}/man8/tk_scsiformat.8*
