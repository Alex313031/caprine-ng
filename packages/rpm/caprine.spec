%define debug_package %{nil}
%global _build_id_links alldebug

Name:           caprine
Version:        2.60.3
Release:        1%{?dist}
Summary:        Elegant Facebook Messenger desktop app

License:        MIT
URL:            https://github.com/Alex313031/caprine-ng
Source0:        https://github.com/Alex313031/caprine-ng/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.desktop

ExclusiveArch:  x86_64
BuildRequires:  npm
BuildRequires:  nodejs >= 16.0.0

%description
Caprine is an unofficial and privacy-focused Facebook Messenger app with many useful features.

%prep
%autosetup

%build
npm install --silent --no-progress
node_modules/.bin/tsc
node_modules/.bin/electron-builder --linux dir

%install
install -d %{buildroot}%{_libdir}/%{name}
cp -r dist/linux-unpacked/* %{buildroot}%{_libdir}/%{name}

install -d %{buildroot}%{_bindir}
ln -sf %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

install -Dm644 build/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -d %{buildroot}%{_datadir}/applications
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d %{buildroot}%{_datadir}/licenses/%{name}
install -Dm644 license %{buildroot}%{_datadir}/licenses/%{name}

%post
/usr/bin/update-desktop-database
/usr/bin/gtk-update-icon-cache

%postun
/usr/bin/update-desktop-database
/usr/bin/gtk-update-icon-cache

%files
%license %{_datadir}/licenses/%{name}/license
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/caprine.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jun 29 2025 Alex313031 <alex313031@gmail.com> - 2.60.3-1
- Update CSS selectors and code maintenance
* Sat Nov 30 2024 dusansimic <dusan.simic1810@gmail.com> - 2.60.2-1
- Update links and desktop entry keywords
* Wed Apr 3 2024 dusansimic <dusan.simic1810@gmail.com> - 2.60.1-1
- Code refactoring
* Tue Mar 5 2024 Alex313031 <alex313031@gmail.com> - 2.60.0-1
- Release 2.60.0
* Tue Feb 29 2024 Alex313031 <alex313031@gmail.com> - 2.59.4-1
- Release 2.59.4
* Tue Feb 20 2024 Alex313031 <alex313031@gmail.com> - 2.59.3-1
- Release 2.59.3
* Mon Jan 15 2024 Alex313031 <alex313031@gmail.com> - 2.59.2-1
- Release 2.59.2
* Mon Oct 09 2023 Alex313031 <alex313031@gmail.com> - 2.59.1-1
- Release 2.59.1
* Wed Sep 27 2023 dusansimic <dusan.simic1810@gmail.com> - 2.59.0-1
- Release 2.59.0
* Mon Sep 25 2023 dusansimic <dusan.simic1810@gmail.com> - 2.58.3-1
- Release 2.58.3
* Fri Aug 22 2023 Alex313031 <alex313031@gmail.com> - 2.58.2-1
- Release 2.58.2
* Fri Aug 11 2023 Alex313031 <alex313031@gmail.com> - 2.58.1-1
- Release 2.58.1
* Fri Jul 20 2023 Alex313031 <alex313031@gmail.com> - 2.57.6-1
- Release 2.57.6
* Fri Jun 6 2023 Alex313031 <alex313031@gmail.com> - 2.57.5-1
- Release 2.57.5
* Sat May 6 2023 dusansimic <dusan.simic1810@gmail.com> - 2.57.4-1
- Release 2.57.4
* Sun Apr 30 2023 dusansimic <dusan.simic1810@gmail.com> - 2.57.3-1
- Release 2.57.3
* Sat Apr 29 2023 dusansimic <dusan.simic1810@gmail.com> - 2.57.2-1
- Release 2.57.2
* Mon Apr 17 2023 dusansimic <dusan.simic1810@gmail.com> - 2.57.1-1
- Release 2.57.1
* Wed Nov 16 2022 dusansimic <dusan.simic1810@gmail.com> - 2.57.0-1
- Release 2.57.0
* Mon Aug 22 2022 dusansimic <dusan.simic1810@gmail.com> - 2.56.1-1
- Release 2.56.1
* Thu Aug 18 2022 dusansimic <dusan.simic1810@gmail.com> - 2.56.0-1
- Release 2.56.0
* Thu Jun 16 2022 dusansimic <dusan.simic1810@gmail.com> - 2.55.7-1
- Release 2.55.7
* Mon Jun 13 2022 dusansimic <dusan.simic1810@gmail.com> - 2.55.6-1
- Release 2.55.6
* Mon May 16 2022 dusansimic <dusan.simic1810@gmail.com> - 2.55.5-1
- Release 2.55.5
* Sun Mar 20 2022 dusansimic <dusan.simic1810@gmail.com> - 2.55.3-1
- Release 2.55.3
* Thu Dec  9 2021 dusansimic <dusan.simic1810@gmail.com> - 2.55.2-1
- Release 2.55.2
* Thu Dec  2 2021 dusansimic <dusan.simic1810@gmail.com> - 2.55.1-1
- Release 2.55.1
* Thu Oct 28 2021 dusansimic <dusan.simic1810@gmail.com> - 2.55.0-1
- Release 2.55.0
* Fri Aug 13 2021 dusansimic <dusan.simic1810@gmail.com> - 2.54.1-1
- Release 2.54.1
* Thu Jul 29 2021 dusansimic <dusan.simic1810@gmail.com> - 2.54.0-1
- Release 2.54.0
* Sat May  8 2021 dusansimic <dusan.simic1810@gmail.com> - 2.53.0-1
- Release 2.53.0
* Mon Apr 26 2021 dusansimic <dusan.simic1810@gmail.com> - 2.52.4-1
- Release 2.52.4
- Removed dependency desktop-file-utils and gtk-update-icon-cache
* Fri Apr  9 2021 dusansimic <dusan.simic1810@gmail.com> - 2.52.3-1
- Release 2.52.3
- Some minor updates to spec file and adding license file to installation
* Thu Mar 25 2021 dusansimic <dusan.simic1810@gmail.com> - 2.52.2-1
- Release 2.52.2
