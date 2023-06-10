from enum import Enum
from pydantic import BaseModel


class URLType(str, Enum):
    website = "website"
    linkedin = "linkedin"
    twitter = "twitter"


class URL(BaseModel):
    type: URLType
    link_map = {
        URLType.website: lambda : "https://"
    }
    @property
    def link(self):
        """The link property."""
        return self.link_map.get(self.type, lambda: "")()
