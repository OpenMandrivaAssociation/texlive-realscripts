Name:		texlive-realscripts
Version:	56594
Release:	2
Summary:	Access OpenType subscript and superscript glyphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/realscripts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/realscripts
%doc %{_texmfdistdir}/doc/latex/realscripts
#- source
%doc %{_texmfdistdir}/source/latex/realscripts

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
