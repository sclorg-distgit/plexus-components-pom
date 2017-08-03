%{?scl:%scl_package %{short_name}-pom}
%{!?scl:%global pkg_name %{name}}

%global short_name plexus-components

Name:           %{?scl_prefix}%{short_name}-pom
Version:        1.3.1
Release:        8.2%{?dist}
Summary:        Plexus Components POM
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-components
BuildArch:      noarch

Source0:        http://repo.maven.apache.org/maven2/org/codehaus/plexus/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus:pom:)

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

%prep
%setup -n %{pkg_name}-%{version} -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.3.1-8.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.3.1-8.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-7
- Regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-4
- Update upstream URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-2
- Rebuild to regenerate Maven auto-requires

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-1
- Update to upstream version 1.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Dec  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-4
- Build with xmvn

* Tue Nov 13 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-3
- Add missing BR/R: plexus-pom

* Mon Nov 12 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-2
- Install LICENSE file

* Wed Oct 31 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Initial packaging
