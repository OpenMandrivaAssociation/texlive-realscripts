%global tl_name realscripts
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3d
Release:	%{tl_revision}.1
Summary:	Access OpenType subscript and superscript glyphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/realscripts
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/realscripts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package replaces \textsuperscript and \textsubscript commands
by equivalent commands that use OpenType font features to access
appropriate glyphs if possible. The package also patches LaTeX's default
footnote command to use this new \textsuperscript for footnote symbols.
The package requires fontspec running on either XeLaTeX or LuaLaTeX. The
package holds functions that were once parts of the xltxtra package,
which now loads realscripts by default.

