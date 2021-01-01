from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin(object):

    id = Column(Integer, primary_key=True)

    @declared_attr
    def created_at(cls):
        return Column(DateTime, server_default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, server_default=func.now(), server_onupdate=func.now())
