%global tl_name tabularray
%global tl_revision 78251

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2025C
Release:	%{tl_revision}.1
Summary:	Typeset tabulars and arrays with LaTeX3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabularray
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularray.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularray.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ninecolors)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX tables are implemented using TeX commands such as \halign,
\noalign, \span, and \omit. In order to implement new features, many
macro packages have modified the inner table commands inside LaTeX. This
makes package code complicated, difficult to maintain, and often
conflicts with each other. At present, the LaTeX3 programming layer is
basically mature. This tabularray package will discard the old \halign
commands and directly use LaTeX3 functions to parse the table, and then
typeset the entire table. Under the premise of being compatible with the
basic syntax of LaTeX2 tables, this macro package will completely
separate the content and style of the table, and the style of the table
can be completely set in keyval way.

