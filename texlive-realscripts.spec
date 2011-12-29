# revision 19976
# category Package
# catalog-ctan /macros/latex/contrib/realscripts
# catalog-date 2010-09-30 22:08:28 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-realscripts
Version:	0.3
Release:	1
Summary:	Access OpenType subscript and superscript glyphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/realscripts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package replaces \textsuperscript and \textsubscript
commands by equivalent commands that use OpenType font features
to access appropriate glyphs if possible. The package also
patches LaTeX's default footnote command to use this new
\textsuperscript for footnote symbols. The package requires
fontspec running on either XeLaTeX or LuaLaTeX. The package
holds functions that were once parts of the xltxtra package,
which now loads realscripts by default.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/realscripts/realscripts.sty
%doc %{_texmfdistdir}/doc/latex/realscripts/README
%doc %{_texmfdistdir}/doc/latex/realscripts/realscripts.pdf
#- source
%doc %{_texmfdistdir}/source/latex/realscripts/realscripts.dtx
%doc %{_texmfdistdir}/source/latex/realscripts/realscripts.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
