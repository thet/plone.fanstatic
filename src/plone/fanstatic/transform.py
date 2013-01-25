
import fanstatic

from zope.interface import Interface
from zope.interface import implements
from zope.component import adapts

from lxml import etree
from repoze.xmliter.utils import getHTMLSerializer
from repoze.xmliter.serializer import XMLSerializer

from plone.transformchain.interfaces import ITransform


class FanstaticTransform(object):

    implements(ITransform)
    adapts(Interface, Interface)

    order = 8050
    pretty_print = False  # tests sets this on True

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def transformString(self, result, encoding):
        return self.transformIterable([result], encoding)

    def transformUnicode(self, result, encoding):
        return self.transformIterable([result], encoding)

    def transformIterable(self, result, encoding):
        if not isinstance(result, XMLSerializer):
            getHeader = self.request.response.getHeader

            content_type = getHeader('Content-Type')
            if content_type is None or \
                    not content_type.startswith('text/html'):
                return None

            contentEncoding = getHeader('Content-Encoding')
            if contentEncoding and \
                    contentEncoding in ('zip', 'deflate', 'compress',):
                return None

            try:
                result = getHTMLSerializer(result, encoding=encoding,
                        pretty_print=self.pretty_print)
            except (TypeError, etree.ParseError):
                return None

        resources = fanstatic.init_needed(
                base_url=self.request.getURL(),
                publisher_signature='/++fanstatic++/',
                )

        from plone.fanstatic import groups
        for group in groups:
            group.need()

        resources = etree.HTML(resources.render()).find('head').getchildren()
        head = resources and result.tree.getroot().find('head') or None
        # Ajax are without head...
        if head:
            for item in resources:
                head.append(item)

        return result
