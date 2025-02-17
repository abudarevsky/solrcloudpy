import logging

from solrcloudpy.collection import SolrCollection
from solrcloudpy.connection import SolrConnection
from solrcloudpy.parameters import SearchOptions

logging.basicConfig()

__version__ = "4.0.1-solr8"
__all__ = ["SolrCollection", "SolrConnection", "SearchOptions"]
