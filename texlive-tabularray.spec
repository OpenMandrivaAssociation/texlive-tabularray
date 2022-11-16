Name:		texlive-tabularray
Version:	64891
Release:	1
Summary:	Typeset tabulars and arrays with LaTeX3
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabularray
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularray.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularray.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX tables are implemented using TeX commands such as
\halign, \noalign, \span, and \omit. In order to implement new
features, many macro packages have modified the inner table
commands inside LaTeX. This makes package code complicated,
difficult to maintain, and often conflicts with each other. At
present, the LaTeX3 programming layer is basically mature. This
tabularray package will discard the old \halign commands and
directly use LaTeX3 functions to parse the table, and then
typeset the entire table. Under the premise of being compatible
with the basic syntax of LaTeX2 tables, this macro package will
completely separate the content and style of the table, and the
style of the table can be completely set in keyval way.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tabularray
%doc %{_texmfdistdir}/doc/latex/tabularray

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
