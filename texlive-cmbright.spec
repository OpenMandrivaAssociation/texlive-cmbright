# revision 21107
# category Package
# catalog-ctan /fonts/cmbright
# catalog-date 2007-01-01 00:37:00 +0100
# catalog-license lppl
# catalog-version 8.1
Name:		texlive-cmbright
Version:	8.1
Release:	7
Summary:	Computer Modern Bright fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cmbright
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmbright.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmbright.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmbright.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A family of sans serif fonts for TeX and LaTeX, based on Donald
Knuth's CM fonts. It comprises OT1, T1 and TS1 encoded text
fonts of various shapes as well as all the fonts necessary for
mathematical typesetting, including AMS symbols. This
collection provides all the necessary files for using the fonts
with LaTeX. A commercial-quality Adobe Type 1 version of these
fonts is available from Micropress. Free versions are
available, in the cm-super font bundle (the T1 and TS1 encoded
part of the set), and in the hfbright (the OT1 encoded part,
and the maths fonts).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/cmbright/ams10pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ams8pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ams9pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/baccent.mf
%{_texmfdistdir}/fonts/source/public/cmbright/bgreeku.mf
%{_texmfdistdir}/fonts/source/public/cmbright/bitalms.mf
%{_texmfdistdir}/fonts/source/public/cmbright/bpunct.mf
%{_texmfdistdir}/fonts/source/public/cmbright/br10pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/br17pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/br8pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/br9pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/brmsa.mf
%{_texmfdistdir}/fonts/source/public/cmbright/brmsb.mf
%{_texmfdistdir}/fonts/source/public/cmbright/broman.mf
%{_texmfdistdir}/fonts/source/public/cmbright/bromanl.mf
%{_texmfdistdir}/fonts/source/public/cmbright/bromlig.mf
%{_texmfdistdir}/fonts/source/public/cmbright/bromms.mf
%{_texmfdistdir}/fonts/source/public/cmbright/brs10pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/brs17pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/brs8pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/brs9pt.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbr10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbr17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbr8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbr9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbras10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbras8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbras9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrbs10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrbs8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrbs9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrbx10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrmb10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrmi10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrmi8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrmi9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrsl10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrsl17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrsl8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrsl9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrsy10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrsy8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmbrsy9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmsltl10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/cmtl10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebaccess.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebbase.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebbraces.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebbx10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebmo10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebmo17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebmo8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebmo9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebmr10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebmr17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebmr8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebmr9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebpseudo.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebpunct.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebrleast.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebrlig.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebrligtb.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebrllett.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebrlwest.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebroman.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebso10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebso17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebso8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebso9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebsr10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebsr17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebsr8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebsr9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebtl10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ebto10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/mathsl.mf
%{_texmfdistdir}/fonts/source/public/cmbright/msa.mf
%{_texmfdistdir}/fonts/source/public/cmbright/msb.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbbx10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbmo10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbmo17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbmo8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbmo9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbmr10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbmr17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbmr8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbmr9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbpseudo.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbso10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbso17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbso8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbso9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbsr10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbsr17.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbsr8.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbsr9.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbsymb.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbsymbol.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbtl10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/tbto10.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ttsymb.mf
%{_texmfdistdir}/fonts/source/public/cmbright/ttsymbol.mf
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbras10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbras8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbras9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrbs8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrbs9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrsl17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmbrsy9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmsltl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/cmtl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebmo10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebmo17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebmo8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebmo9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebso10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebso17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebso8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebso9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebsr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebsr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebsr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebsr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebtl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/ebto10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbmo10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbmo17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbmo8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbmo9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbso10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbso17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbso8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbso9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbsr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbsr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbsr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbsr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbtl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmbright/tbto10.tfm
%{_texmfdistdir}/tex/latex/cmbright/cmbright.sty
%{_texmfdistdir}/tex/latex/cmbright/omlcmbr.fd
%{_texmfdistdir}/tex/latex/cmbright/omlcmbrm.fd
%{_texmfdistdir}/tex/latex/cmbright/omscmbr.fd
%{_texmfdistdir}/tex/latex/cmbright/omscmbrs.fd
%{_texmfdistdir}/tex/latex/cmbright/ot1cmbr.fd
%{_texmfdistdir}/tex/latex/cmbright/ot1cmtl.fd
%{_texmfdistdir}/tex/latex/cmbright/t1cmbr.fd
%{_texmfdistdir}/tex/latex/cmbright/t1cmtl.fd
%{_texmfdistdir}/tex/latex/cmbright/ts1cmbr.fd
%{_texmfdistdir}/tex/latex/cmbright/ts1cmtl.fd
%doc %{_texmfdistdir}/doc/fonts/cmbright/LICENSE
%doc %{_texmfdistdir}/doc/fonts/cmbright/README
%doc %{_texmfdistdir}/doc/fonts/cmbright/cmbright.txt
%doc %{_texmfdistdir}/doc/fonts/cmbright/manifest.txt
%doc %{_texmfdistdir}/doc/latex/cmbright/cmbright.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cmbright/cmbright.dtx
%doc %{_texmfdistdir}/source/latex/cmbright/cmbright.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 8.1-2
+ Revision: 750259
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 8.1-1
+ Revision: 718076
- texlive-cmbright
- texlive-cmbright
- texlive-cmbright
- texlive-cmbright
- texlive-cmbright

