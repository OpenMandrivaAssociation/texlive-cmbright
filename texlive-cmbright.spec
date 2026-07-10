%global tl_name cmbright
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	8.1
Release:	%{tl_revision}.1
Summary:	Computer Modern Bright fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cmbright
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmbright.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmbright.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmbright.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A family of sans serif fonts for TeX and LaTeX, based on Donald Knuth's
CM fonts. It comprises OT1, T1 and TS1 encoded text fonts of various
shapes as well as all the fonts necessary for mathematical typesetting,
including AMS symbols. This collection provides all the necessary files
for using the fonts with LaTeX. Free versions are available, in the cm-
super font bundle (the T1 and TS1 encoded part of the set), and in the
hfbright package (the OT1 encoded part, and the maths fonts).

