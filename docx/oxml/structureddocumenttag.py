# encoding: utf-8

"""Custom element classes for structured document tag (CT_Sdt)"""

from .ns import qn
from .xmlchemy import BaseOxmlElement, OxmlElement, ZeroOrMore, ZeroOrOne


class CT_Sdt(BaseOxmlElement):
    """
    ``<w:Sdt>`` element.
    """
    sdtPr = ZeroOrOne('w:sdtPr')
    sdtContent = ZeroOrOne('w:sdtContent')
    sdtEndPr = ZeroOrOne('w:sdtEndPr')

    def clear_content(self):
        """
        Remove all child elements, except the ``<w:pPr>`` element if present.
        """
        for child in self[:]:
            if child.tag == qn('w:sdtPr'):
                continue
            self.remove(child)


class CT_sdtContent(BaseOxmlElement):
    """
    ``<w:sdtContent>`` element, containing the properties and text for a paragraph.
    """
    r = ZeroOrMore('w:r')
    p = ZeroOrMore('w:p')
    sdt = ZeroOrMore('w:sdt')
    tbl = ZeroOrMore('w:tbl')


