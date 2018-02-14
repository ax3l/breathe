#!/usr/bin/env python

#
# Generated Tue Feb 13 19:16:46 2018 by generateDS.py version 2.29.5.
# Python 2.7.13 (default, Nov 24 2017, 17:33:09)  [GCC 6.3.0 20170516]
#
# Command line options:
#   ('-f', '')
#   ('-o', 'compound.py')
#   ('-s', 'compoundsuper.py')
#   ('--super', 'compoundsuper')
#
# Command line arguments:
#   /home/axel/src/picongpu/docs/xml/compound.xsd
#
# Command line:
#   /home/axel/.local/bin/generateDS.py -f -o "compound.py" -s "compoundsuper.py" --super="compoundsuper" /home/axel/src/picongpu/docs/xml/compound.xsd
#
# Current working directory (os.getcwd()):
#   parser
#

import sys
from lxml import etree as etree_

import compoundsuper as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class DoxygenTypeSub(supermod.DoxygenType):

    node_type = "doxygendef"

    def __init__(self, version=None, compounddef=None):
        super(DoxygenTypeSub, self).__init__(version, compounddef, )
supermod.DoxygenType.subclass = DoxygenTypeSub
# end class DoxygenTypeSub


class compounddefTypeSub(supermod.compounddefType):

    node_type = "compounddef"

    def __init__(self, id=None, kind=None, language=None, prot=None, final=None, sealed=None, abstract=None, compoundname=None, title=None, basecompoundref=None, derivedcompoundref=None, includes=None, includedby=None, incdepgraph=None, invincdepgraph=None, innerdir=None, innerfile=None, innerclass=None, innernamespace=None, innerpage=None, innergroup=None, templateparamlist=None, sectiondef=None, briefdescription=None, detaileddescription=None, inheritancegraph=None, collaborationgraph=None, programlisting=None, location=None, listofallmembers=None):
        super(compounddefTypeSub, self).__init__(id, kind, language, prot, final, sealed, abstract, compoundname, title, basecompoundref, derivedcompoundref, includes, includedby, incdepgraph, invincdepgraph, innerdir, innerfile, innerclass, innernamespace, innerpage, innergroup, templateparamlist, sectiondef, briefdescription, detaileddescription, inheritancegraph, collaborationgraph, programlisting, location, listofallmembers, )
supermod.compounddefType.subclass = compounddefTypeSub
# end class compounddefTypeSub


class listofallmembersTypeSub(supermod.listofallmembersType):

    node_type = "listofallmembers"

    def __init__(self, member=None):
        super(listofallmembersTypeSub, self).__init__(member, )
supermod.listofallmembersType.subclass = listofallmembersTypeSub
# end class listofallmembersTypeSub


class memberRefTypeSub(supermod.memberRefType):

    node_type = "memberref"

    def __init__(self, refid=None, prot=None, virt=None, ambiguityscope=None, scope=None, name=None):
        super(memberRefTypeSub, self).__init__(refid, prot, virt, ambiguityscope, scope, name, )
supermod.memberRefType.subclass = memberRefTypeSub
# end class memberRefTypeSub


class compoundRefTypeSub(supermod.compoundRefType):

    node_type = "compoundref"

    def __init__(self, refid=None, prot=None, virt=None, valueOf_=None):
        super(compoundRefTypeSub, self).__init__(refid, prot, virt, valueOf_, )
supermod.compoundRefType.subclass = compoundRefTypeSub
# end class compoundRefTypeSub


class reimplementTypeSub(supermod.reimplementType):

    node_type = "reimplement"

    def __init__(self, refid=None, valueOf_=None):
        super(reimplementTypeSub, self).__init__(refid, valueOf_, )
supermod.reimplementType.subclass = reimplementTypeSub
# end class reimplementTypeSub


class incTypeSub(supermod.incType):

    node_type = "inc"

    def __init__(self, refid=None, local=None, valueOf_=None):
        super(incTypeSub, self).__init__(refid, local, valueOf_, )
supermod.incType.subclass = incTypeSub
# end class incTypeSub


class refTypeSub(supermod.refType):

    node_type = "ref"

    def __init__(self, node_name, refid=None, prot=None, valueOf_=None):
        super(refTypeSub, self).__init__(refid, prot, valueOf_, )
supermod.refType.subclass = refTypeSub

        self.node_name = node_name
# end class refTypeSub


class refTextTypeSub(supermod.refTextType):

    node_type = "reftex"

    def __init__(self, refid=None, kindref=None, external=None, tooltip=None, valueOf_=None):
        super(refTextTypeSub, self).__init__(refid, kindref, external, tooltip, valueOf_, )
supermod.refTextType.subclass = refTextTypeSub
# end class refTextTypeSub


class sectiondefTypeSub(supermod.sectiondefType):

    node_type = "sectiondef"

    def __init__(self, kind=None, header=None, description=None, memberdef=None):
        super(sectiondefTypeSub, self).__init__(kind, header, description, memberdef, )
supermod.sectiondefType.subclass = sectiondefTypeSub
# end class sectiondefTypeSub


class memberdefTypeSub(supermod.memberdefType):

    node_type = "memberdef"

    def __init__(self, kind=None, id=None, prot=None, static=None, const=None, explicit=None, inline=None, refqual=None, virt=None, volatile=None, mutable=None, readable=None, writable=None, initonly=None, settable=None, gettable=None, final=None, sealed=None, new=None, add=None, remove=None, raise_=None, optional=None, required=None, accessor=None, attribute=None, property=None, readonly=None, bound=None, removable=None, contrained=None, transient=None, maybevoid=None, maybedefault=None, maybeambiguous=None, templateparamlist=None, type_=None, definition=None, argsstring=None, name=None, read=None, write=None, bitfield=None, reimplements=None, reimplementedby=None, param=None, enumvalue=None, initializer=None, exceptions=None, briefdescription=None, detaileddescription=None, inbodydescription=None, location=None, references=None, referencedby=None):
        super(memberdefTypeSub, self).__init__(kind, id, prot, static, const, explicit, inline, refqual, virt, volatile, mutable, readable, writable, initonly, settable, gettable, final, sealed, new, add, remove, raise_, optional, required, accessor, attribute, property, readonly, bound, removable, contrained, transient, maybevoid, maybedefault, maybeambiguous, templateparamlist, type_, definition, argsstring, name, read, write, bitfield, reimplements, reimplementedby, param, enumvalue, initializer, exceptions, briefdescription, detaileddescription, inbodydescription, location, references, referencedby, )
supermod.memberdefType.subclass = memberdefTypeSub

        self.parameterlist = supermod.docParamListType.factory()
        self.parameterlist.kind = "param"

# end class memberdefTypeSub


class descriptionTypeSub(supermod.descriptionType):

    node_type = "description"

    def __init__(self, title=None, para=None, sect1=None, internal=None, valueOf_=None, mixedclass_=None, content_=None):
        super(descriptionTypeSub, self).__init__(title, para, sect1, internal, valueOf_, mixedclass_, content_, )
supermod.descriptionType.subclass = descriptionTypeSub
# end class descriptionTypeSub


class enumvalueTypeSub(supermod.enumvalueType):

    node_type = "enumvalue"

    def __init__(self, id=None, prot=None, name=None, initializer=None, briefdescription=None, detaileddescription=None, valueOf_=None, mixedclass_=None, content_=None):
        super(enumvalueTypeSub, self).__init__(id, prot, name, initializer, briefdescription, detaileddescription, valueOf_, mixedclass_, content_, )
supermod.enumvalueType.subclass = enumvalueTypeSub
# end class enumvalueTypeSub


class templateparamlistTypeSub(supermod.templateparamlistType):

    node_type = "templateparamlist"

    def __init__(self, param=None):
        super(templateparamlistTypeSub, self).__init__(param, )
supermod.templateparamlistType.subclass = templateparamlistTypeSub
# end class templateparamlistTypeSub


class paramTypeSub(supermod.paramType):

    node_type = "param"

    def __init__(self, type_=None, declname=None, defname=None, array=None, defval=None, typeconstraint=None, briefdescription=None):
        super(paramTypeSub, self).__init__(type_, declname, defname, array, defval, typeconstraint, briefdescription, )
supermod.paramType.subclass = paramTypeSub
# end class paramTypeSub


class linkedTextTypeSub(supermod.linkedTextType):

    node_type = "linkedtext"

    def __init__(self, ref=None, valueOf_=None, mixedclass_=None, content_=None):
        super(linkedTextTypeSub, self).__init__(ref, valueOf_, mixedclass_, content_, )
supermod.linkedTextType.subclass = linkedTextTypeSub
# end class linkedTextTypeSub


class graphTypeSub(supermod.graphType):

    node_type = "graph"

    def __init__(self, node=None):
        super(graphTypeSub, self).__init__(node, )
supermod.graphType.subclass = graphTypeSub
# end class graphTypeSub


class nodeTypeSub(supermod.nodeType):

    node_type = "node"

    def __init__(self, id=None, label=None, link=None, childnode=None):
        super(nodeTypeSub, self).__init__(id, label, link, childnode, )
supermod.nodeType.subclass = nodeTypeSub
# end class nodeTypeSub


class childnodeTypeSub(supermod.childnodeType):

    node_type = "childnode"

    def __init__(self, refid=None, relation=None, edgelabel=None):
        super(childnodeTypeSub, self).__init__(refid, relation, edgelabel, )
supermod.childnodeType.subclass = childnodeTypeSub
# end class childnodeTypeSub


class linkTypeSub(supermod.linkType):

    node_type = "link"

    def __init__(self, refid=None, external=None):
        super(linkTypeSub, self).__init__(refid, external, )
supermod.linkType.subclass = linkTypeSub
# end class linkTypeSub


class listingTypeSub(supermod.listingType):

    node_type = "listing"

    def __init__(self, codeline=None):
        super(listingTypeSub, self).__init__(codeline, )
supermod.listingType.subclass = listingTypeSub
# end class listingTypeSub


class codelineTypeSub(supermod.codelineType):

    node_type = "codeline"

    def __init__(self, lineno=None, refid=None, refkind=None, external=None, highlight=None):
        super(codelineTypeSub, self).__init__(lineno, refid, refkind, external, highlight, )
supermod.codelineType.subclass = codelineTypeSub
# end class codelineTypeSub


class highlightTypeSub(supermod.highlightType):

    node_type = "highlight"

    def __init__(self, class_=None, sp=None, ref=None, valueOf_=None, mixedclass_=None, content_=None):
        super(highlightTypeSub, self).__init__(class_, sp, ref, valueOf_, mixedclass_, content_, )
supermod.highlightType.subclass = highlightTypeSub
# end class highlightTypeSub


class referenceTypeSub(supermod.referenceType):

    node_type = "reference"

    def __init__(self, refid=None, compoundref=None, startline=None, endline=None, valueOf_=None, mixedclass_=None, content_=None):
        super(referenceTypeSub, self).__init__(refid, compoundref, startline, endline, valueOf_, mixedclass_, content_, )
supermod.referenceType.subclass = referenceTypeSub
# end class referenceTypeSub


class locationTypeSub(supermod.locationType):

    node_type = "location"

    def __init__(self, file=None, line=None, column=None, bodyfile=None, bodystart=None, bodyend=None):
        super(locationTypeSub, self).__init__(file, line, column, bodyfile, bodystart, bodyend, )
supermod.locationType.subclass = locationTypeSub
# end class locationTypeSub


class docSect1TypeSub(supermod.docSect1Type):

    node_type = "docsect1"

    def __init__(self, id=None, title=None, para=None, sect2=None, internal=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docSect1TypeSub, self).__init__(id, title, para, sect2, internal, valueOf_, mixedclass_, content_, )
supermod.docSect1Type.subclass = docSect1TypeSub
# end class docSect1TypeSub


class docSect2TypeSub(supermod.docSect2Type):

    node_type = "docsect2"

    def __init__(self, id=None, title=None, para=None, sect3=None, internal=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docSect2TypeSub, self).__init__(id, title, para, sect3, internal, valueOf_, mixedclass_, content_, )
supermod.docSect2Type.subclass = docSect2TypeSub
# end class docSect2TypeSub


class docSect3TypeSub(supermod.docSect3Type):

    node_type = "docsect3"

    def __init__(self, id=None, title=None, para=None, sect4=None, internal=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docSect3TypeSub, self).__init__(id, title, para, sect4, internal, valueOf_, mixedclass_, content_, )
supermod.docSect3Type.subclass = docSect3TypeSub
# end class docSect3TypeSub


class docSect4TypeSub(supermod.docSect4Type):

    node_type = "docsect4"

    def __init__(self, id=None, title=None, para=None, internal=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docSect4TypeSub, self).__init__(id, title, para, internal, valueOf_, mixedclass_, content_, )
supermod.docSect4Type.subclass = docSect4TypeSub
# end class docSect4TypeSub


class docInternalTypeSub(supermod.docInternalType):

    node_type = "docinternal"

    def __init__(self, para=None, sect1=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docInternalTypeSub, self).__init__(para, sect1, valueOf_, mixedclass_, content_, )
supermod.docInternalType.subclass = docInternalTypeSub
# end class docInternalTypeSub


class docInternalS1TypeSub(supermod.docInternalS1Type):

    node_type = "docinternals1"

    def __init__(self, para=None, sect2=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docInternalS1TypeSub, self).__init__(para, sect2, valueOf_, mixedclass_, content_, )
supermod.docInternalS1Type.subclass = docInternalS1TypeSub
# end class docInternalS1TypeSub


class docInternalS2TypeSub(supermod.docInternalS2Type):

    node_type = "docinternals2"

    def __init__(self, para=None, sect3=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docInternalS2TypeSub, self).__init__(para, sect3, valueOf_, mixedclass_, content_, )
supermod.docInternalS2Type.subclass = docInternalS2TypeSub
# end class docInternalS2TypeSub


class docInternalS3TypeSub(supermod.docInternalS3Type):

    node_type = "docinternals3"

    def __init__(self, para=None, sect3=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docInternalS3TypeSub, self).__init__(para, sect3, valueOf_, mixedclass_, content_, )
supermod.docInternalS3Type.subclass = docInternalS3TypeSub
# end class docInternalS3TypeSub


class docInternalS4TypeSub(supermod.docInternalS4Type):

    node_type = "docinternals4"

    def __init__(self, para=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docInternalS4TypeSub, self).__init__(para, valueOf_, mixedclass_, content_, )
supermod.docInternalS4Type.subclass = docInternalS4TypeSub
# end class docInternalS4TypeSub


class docTitleTypeSub(supermod.docTitleType):

    node_type = "doctitle"

    def __init__(self, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, valueOf_, mixedclass_, content_, )
        super(docTitleTypeSub, self).__init__(*arglist_)
supermod.docTitleType.subclass = docTitleTypeSub
# end class docTitleTypeSub


class docParaTypeSub(supermod.docParaType):

    node_type = "docpara"

    def __init__(self, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, linebreak=None, hruler=None, preformatted=None, programlisting=None, verbatim=None, indexentry=None, orderedlist=None, itemizedlist=None, simplesect=None, title=None, variablelist=None, table=None, heading=None, image=None, dotfile=None, mscfile=None, diafile=None, toclist=None, language=None, parameterlist=None, xrefsect=None, copydoc=None, blockquote=None, parblock=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, linebreak, hruler, preformatted, programlisting, verbatim, indexentry, orderedlist, itemizedlist, simplesect, title, variablelist, table, heading, image, dotfile, mscfile, diafile, toclist, language, parameterlist, xrefsect, copydoc, blockquote, parblock, valueOf_, mixedclass_, content_, )
        super(docParaTypeSub, self).__init__(*arglist_)
supermod.docParaType.subclass = docParaTypeSub
# end class docParaTypeSub


class docMarkupTypeSub(supermod.docMarkupType):

    node_type = "docmarkup"

    def __init__(self, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, linebreak=None, hruler=None, preformatted=None, programlisting=None, verbatim=None, indexentry=None, orderedlist=None, itemizedlist=None, simplesect=None, title=None, variablelist=None, table=None, heading=None, image=None, dotfile=None, mscfile=None, diafile=None, toclist=None, language=None, parameterlist=None, xrefsect=None, copydoc=None, blockquote=None, parblock=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, linebreak, hruler, preformatted, programlisting, verbatim, indexentry, orderedlist, itemizedlist, simplesect, title, variablelist, table, heading, image, dotfile, mscfile, diafile, toclist, language, parameterlist, xrefsect, copydoc, blockquote, parblock, valueOf_, mixedclass_, content_, )
        super(docMarkupTypeSub, self).__init__(*arglist_)
supermod.docMarkupType.subclass = docMarkupTypeSub
# end class docMarkupTypeSub


class docURLLinkSub(supermod.docURLLink):

    node_type = "docurllink"

    def __init__(self, url=None, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (url, ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, valueOf_, mixedclass_, content_, )
        super(docURLLinkSub, self).__init__(*arglist_)
supermod.docURLLink.subclass = docURLLinkSub
# end class docURLLinkSub


class docAnchorTypeSub(supermod.docAnchorType):

    node_type = "docanchor"

    def __init__(self, id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docAnchorTypeSub, self).__init__(id, valueOf_, mixedclass_, content_, )
supermod.docAnchorType.subclass = docAnchorTypeSub
# end class docAnchorTypeSub


class docFormulaTypeSub(supermod.docFormulaType):

    node_type = "docformula"

    def __init__(self, id=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docFormulaTypeSub, self).__init__(id, valueOf_, mixedclass_, content_, )
supermod.docFormulaType.subclass = docFormulaTypeSub
# end class docFormulaTypeSub


class docIndexEntryTypeSub(supermod.docIndexEntryType):

    node_type = "docindexentry"

    def __init__(self, primaryie=None, secondaryie=None):
        super(docIndexEntryTypeSub, self).__init__(primaryie, secondaryie, )
supermod.docIndexEntryType.subclass = docIndexEntryTypeSub
# end class docIndexEntryTypeSub


class docListTypeSub(supermod.docListType):

    node_type = "doclist"

    def __init__(self, listitem=None, subtype=""):
        self.node_subtype = "itemized"
        if subtype is not "":
            self.node_subtype = subtype
        super(docListTypeSub, self).__init__(listitem, )
supermod.docListType.subclass = docListTypeSub
# end class docListTypeSub


class docListItemTypeSub(supermod.docListItemType):

    node_type = "doclistitem"

    def __init__(self, para=None):
        super(docListItemTypeSub, self).__init__(para, )
supermod.docListItemType.subclass = docListItemTypeSub
# end class docListItemTypeSub


class docSimpleSectTypeSub(supermod.docSimpleSectType):

    node_type = "docsimplesect"

    def __init__(self, kind=None, title=None, para=None):
        super(docSimpleSectTypeSub, self).__init__(kind, title, para, )
supermod.docSimpleSectType.subclass = docSimpleSectTypeSub
# end class docSimpleSectTypeSub


class docVarListEntryTypeSub(supermod.docVarListEntryType):

    node_type = "docvarlistentry"

    def __init__(self, term=None):
        super(docVarListEntryTypeSub, self).__init__(term, )
supermod.docVarListEntryType.subclass = docVarListEntryTypeSub
# end class docVarListEntryTypeSub


class docVariableListTypeSub(supermod.docVariableListType):

    node_type = "docvarlist"

    def __init__(self, varlistentry=None, listitem=None):
        super(docVariableListTypeSub, self).__init__(varlistentry, listitem, )
supermod.docVariableListType.subclass = docVariableListTypeSub
# end class docVariableListTypeSub


class docRefTextTypeSub(supermod.docRefTextType):

    node_type = "docreftext"

    def __init__(self, refid=None, kindref=None, external=None, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (refid, kindref, external, ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, valueOf_, mixedclass_, content_, )
        super(docRefTextTypeSub, self).__init__(*arglist_)
supermod.docRefTextType.subclass = docRefTextTypeSub
# end class docRefTextTypeSub


class docTableTypeSub(supermod.docTableType):

    node_type = "doctable"

    def __init__(self, rows=None, cols=None, row=None, caption=None):
        super(docTableTypeSub, self).__init__(rows, cols, row, caption, )
supermod.docTableType.subclass = docTableTypeSub
# end class docTableTypeSub


class docRowTypeSub(supermod.docRowType):

    node_type = "docrow"

    def __init__(self, entry=None):
        super(docRowTypeSub, self).__init__(entry, )
supermod.docRowType.subclass = docRowTypeSub
# end class docRowTypeSub


class docEntryTypeSub(supermod.docEntryType):

    node_type = "docentry"

    def __init__(self, thead=None, para=None):
        super(docEntryTypeSub, self).__init__(thead, para, )
supermod.docEntryType.subclass = docEntryTypeSub
# end class docEntryTypeSub


class docCaptionTypeSub(supermod.docCaptionType):

    node_type = "doccaption"

    def __init__(self, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, valueOf_, mixedclass_, content_, )
        super(docCaptionTypeSub, self).__init__(*arglist_)
supermod.docCaptionType.subclass = docCaptionTypeSub
# end class docCaptionTypeSub


class docHeadingTypeSub(supermod.docHeadingType):

    node_type = "docheading"

    def __init__(self, level=None, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (level, ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, valueOf_, mixedclass_, content_, )
        super(docHeadingTypeSub, self).__init__(*arglist_)
supermod.docHeadingType.subclass = docHeadingTypeSub
# end class docHeadingTypeSub


class docImageTypeSub(supermod.docImageType):

    node_type = "docimage"

    def __init__(self, type_=None, name=None, width=None, height=None, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (type_, name, width, height, ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, valueOf_, mixedclass_, content_, )
        super(docImageTypeSub, self).__init__(*arglist_)
supermod.docImageType.subclass = docImageTypeSub
# end class docImageTypeSub


class docFileTypeSub(supermod.docFileType):

    node_type = "docfile"

    def __init__(self, name=None, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (name, ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, valueOf_, mixedclass_, content_, )
        super(docFileTypeSub, self).__init__(*arglist_)
supermod.docFileType.subclass = docFileTypeSub
# end class docFileTypeSub


class docTocItemTypeSub(supermod.docTocItemType):

    node_type = "doctocitem"

    def __init__(self, id=None, ulink=None, bold=None, emphasis=None, computeroutput=None, subscript=None, superscript=None, center=None, small=None, htmlonly=None, manonly=None, xmlonly=None, rtfonly=None, latexonly=None, dot=None, plantuml=None, anchor=None, formula=None, ref=None, nonbreakablespace=None, iexcl=None, cent=None, pound=None, curren=None, yen=None, brvbar=None, sect=None, umlaut=None, copy=None, ordf=None, laquo=None, not_=None, shy=None, registered=None, macr=None, deg=None, plusmn=None, sup2=None, sup3=None, acute=None, micro=None, para=None, middot=None, cedil=None, sup1=None, ordm=None, raquo=None, frac14=None, frac12=None, frac34=None, iquest=None, Agrave=None, Aacute=None, Acirc=None, Atilde=None, Aumlaut=None, Aring=None, AElig=None, Ccedil=None, Egrave=None, Eacute=None, Ecirc=None, Eumlaut=None, Igrave=None, Iacute=None, Icirc=None, Iumlaut=None, ETH=None, Ntilde=None, Ograve=None, Oacute=None, Ocirc=None, Otilde=None, Oumlaut=None, times=None, Oslash=None, Ugrave=None, Uacute=None, Ucirc=None, Uumlaut=None, Yacute=None, THORN=None, szlig=None, agrave=None, aacute=None, acirc=None, atilde=None, aumlaut=None, aring=None, aelig=None, ccedil=None, egrave=None, eacute=None, ecirc=None, eumlaut=None, igrave=None, iacute=None, icirc=None, iumlaut=None, eth=None, ntilde=None, ograve=None, oacute=None, ocirc=None, otilde=None, oumlaut=None, divide=None, oslash=None, ugrave=None, uacute=None, ucirc=None, uumlaut=None, yacute=None, thorn=None, yumlaut=None, fnof=None, Alpha=None, Beta=None, Gamma=None, Delta=None, Epsilon=None, Zeta=None, Eta=None, Theta=None, Iota=None, Kappa=None, Lambda=None, Mu=None, Nu=None, Xi=None, Omicron=None, Pi=None, Rho=None, Sigma=None, Tau=None, Upsilon=None, Phi=None, Chi=None, Psi=None, Omega=None, alpha=None, beta=None, gamma=None, delta=None, epsilon=None, zeta=None, eta=None, theta=None, iota=None, kappa=None, lambda_=None, mu=None, nu=None, xi=None, omicron=None, pi=None, rho=None, sigmaf=None, sigma=None, tau=None, upsilon=None, phi=None, chi=None, psi=None, omega=None, thetasym=None, upsih=None, piv=None, bull=None, hellip=None, prime=None, Prime=None, oline=None, frasl=None, weierp=None, imaginary=None, real=None, trademark=None, alefsym=None, larr=None, uarr=None, rarr=None, darr=None, harr=None, crarr=None, lArr=None, uArr=None, rArr=None, dArr=None, hArr=None, forall=None, part=None, exist=None, empty=None, nabla=None, isin=None, notin=None, ni=None, prod=None, sum=None, minus=None, lowast=None, radic=None, prop=None, infin=None, ang=None, and_=None, or_=None, cap=None, cup=None, int=None, there4=None, sim=None, cong=None, asymp=None, ne=None, equiv=None, le=None, ge=None, sub=None, sup=None, nsub=None, sube=None, supe=None, oplus=None, otimes=None, perp=None, sdot=None, lceil=None, rceil=None, lfloor=None, rfloor=None, lang=None, rang=None, loz=None, spades=None, clubs=None, hearts=None, diams=None, OElig=None, oelig=None, Scaron=None, scaron=None, Yumlaut=None, circ=None, tilde=None, ensp=None, emsp=None, thinsp=None, zwnj=None, zwj=None, lrm=None, rlm=None, ndash=None, mdash=None, lsquo=None, rsquo=None, sbquo=None, ldquo=None, rdquo=None, bdquo=None, dagger=None, Dagger=None, permil=None, lsaquo=None, rsaquo=None, euro=None, tm=None, valueOf_=None, mixedclass_=None, content_=None):
        arglist_ = (id, ulink, bold, emphasis, computeroutput, subscript, superscript, center, small, htmlonly, manonly, xmlonly, rtfonly, latexonly, dot, plantuml, anchor, formula, ref, nonbreakablespace, iexcl, cent, pound, curren, yen, brvbar, sect, umlaut, copy, ordf, laquo, not_, shy, registered, macr, deg, plusmn, sup2, sup3, acute, micro, para, middot, cedil, sup1, ordm, raquo, frac14, frac12, frac34, iquest, Agrave, Aacute, Acirc, Atilde, Aumlaut, Aring, AElig, Ccedil, Egrave, Eacute, Ecirc, Eumlaut, Igrave, Iacute, Icirc, Iumlaut, ETH, Ntilde, Ograve, Oacute, Ocirc, Otilde, Oumlaut, times, Oslash, Ugrave, Uacute, Ucirc, Uumlaut, Yacute, THORN, szlig, agrave, aacute, acirc, atilde, aumlaut, aring, aelig, ccedil, egrave, eacute, ecirc, eumlaut, igrave, iacute, icirc, iumlaut, eth, ntilde, ograve, oacute, ocirc, otilde, oumlaut, divide, oslash, ugrave, uacute, ucirc, uumlaut, yacute, thorn, yumlaut, fnof, Alpha, Beta, Gamma, Delta, Epsilon, Zeta, Eta, Theta, Iota, Kappa, Lambda, Mu, Nu, Xi, Omicron, Pi, Rho, Sigma, Tau, Upsilon, Phi, Chi, Psi, Omega, alpha, beta, gamma, delta, epsilon, zeta, eta, theta, iota, kappa, lambda_, mu, nu, xi, omicron, pi, rho, sigmaf, sigma, tau, upsilon, phi, chi, psi, omega, thetasym, upsih, piv, bull, hellip, prime, Prime, oline, frasl, weierp, imaginary, real, trademark, alefsym, larr, uarr, rarr, darr, harr, crarr, lArr, uArr, rArr, dArr, hArr, forall, part, exist, empty, nabla, isin, notin, ni, prod, sum, minus, lowast, radic, prop, infin, ang, and_, or_, cap, cup, int, there4, sim, cong, asymp, ne, equiv, le, ge, sub, sup, nsub, sube, supe, oplus, otimes, perp, sdot, lceil, rceil, lfloor, rfloor, lang, rang, loz, spades, clubs, hearts, diams, OElig, oelig, Scaron, scaron, Yumlaut, circ, tilde, ensp, emsp, thinsp, zwnj, zwj, lrm, rlm, ndash, mdash, lsquo, rsquo, sbquo, ldquo, rdquo, bdquo, dagger, Dagger, permil, lsaquo, rsaquo, euro, tm, valueOf_, mixedclass_, content_, )
        super(docTocItemTypeSub, self).__init__(*arglist_)
supermod.docTocItemType.subclass = docTocItemTypeSub
# end class docTocItemTypeSub


class docTocListTypeSub(supermod.docTocListType):

    node_type = "doctoclist"

    def __init__(self, tocitem=None):
        super(docTocListTypeSub, self).__init__(tocitem, )
supermod.docTocListType.subclass = docTocListTypeSub
# end class docTocListTypeSub


class docLanguageTypeSub(supermod.docLanguageType):

    node_type = "doclanguage"

    def __init__(self, langid=None, para=None):
        super(docLanguageTypeSub, self).__init__(langid, para, )
supermod.docLanguageType.subclass = docLanguageTypeSub
# end class docLanguageTypeSub


class docParamListTypeSub(supermod.docParamListType):

    node_type = "docparamlist"

    def __init__(self, kind=None, parameteritem=None):
        super(docParamListTypeSub, self).__init__(kind, parameteritem, )
supermod.docParamListType.subclass = docParamListTypeSub
# end class docParamListTypeSub


class docParamListItemSub(supermod.docParamListItem):

    node_type = "docparamlistitem"

    def __init__(self, parameternamelist=None, parameterdescription=None):
        super(docParamListItemSub, self).__init__(parameternamelist, parameterdescription, )
supermod.docParamListItem.subclass = docParamListItemSub
# end class docParamListItemSub


class docParamNameListSub(supermod.docParamNameList):

    node_type = "docparamnamelist"

    def __init__(self, parametertype=None, parametername=None):
        super(docParamNameListSub, self).__init__(parametertype, parametername, )
supermod.docParamNameList.subclass = docParamNameListSub
# end class docParamNameListSub


class docParamTypeSub(supermod.docParamType):

    node_type = "docparam"

    def __init__(self, ref=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docParamTypeSub, self).__init__(ref, valueOf_, mixedclass_, content_, )
supermod.docParamType.subclass = docParamTypeSub
# end class docParamTypeSub


class docParamNameSub(supermod.docParamName):

    node_type = "docparamname"

    def __init__(self, direction=None, ref=None, valueOf_=None, mixedclass_=None, content_=None):
        super(docParamNameSub, self).__init__(direction, ref, valueOf_, mixedclass_, content_, )
supermod.docParamName.subclass = docParamNameSub
# end class docParamNameSub


class docXRefSectTypeSub(supermod.docXRefSectType):

    node_type = "docxrefsect"

    def __init__(self, id=None, xreftitle=None, xrefdescription=None):
        super(docXRefSectTypeSub, self).__init__(id, xreftitle, xrefdescription, )
supermod.docXRefSectType.subclass = docXRefSectTypeSub
# end class docXRefSectTypeSub


class docCopyTypeSub(supermod.docCopyType):

    node_type = "doccopy"

    def __init__(self, link=None, para=None, sect1=None, internal=None):
        super(docCopyTypeSub, self).__init__(link, para, sect1, internal, )
supermod.docCopyType.subclass = docCopyTypeSub
# end class docCopyTypeSub


class docBlockQuoteTypeSub(supermod.docBlockQuoteType):

    node_type = "docblockquote"

    def __init__(self, para=None):
        super(docBlockQuoteTypeSub, self).__init__(para, )
supermod.docBlockQuoteType.subclass = docBlockQuoteTypeSub
# end class docBlockQuoteTypeSub


class docParBlockTypeSub(supermod.docParBlockType):

    node_type = "docparblock"

    def __init__(self, para=None):
        super(docParBlockTypeSub, self).__init__(para, )
supermod.docParBlockType.subclass = docParBlockTypeSub
# end class docParBlockTypeSub


class docEmptyTypeSub(supermod.docEmptyType):

    node_type = "docempty"

    def __init__(self):
        super(docEmptyTypeSub, self).__init__()
supermod.docEmptyType.subclass = docEmptyTypeSub
# end class docEmptyTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=True):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DoxygenType'
        rootClass = supermod.DoxygenType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=True):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DoxygenType'
        rootClass = supermod.DoxygenType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=True):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DoxygenType'
        rootClass = supermod.DoxygenType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=True):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DoxygenType'
        rootClass = supermod.DoxygenType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from compoundsuper import *\n\n')
        sys.stdout.write('import compoundsuper as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
