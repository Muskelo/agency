class BaseMixin():
    """ Base Mixin

    include base methods to work with SQLAlchemy models """

    @classmethod
    def get_(cls, **kwargs):
        """ Get item by fitlers """

        item = cls.query.filter_by(**kwargs).first()

        return item

    
    @classmethod
    def get_all_(cls, **kwargs):
        """ Get item by fitlers """

        items = cls.query.filter_by(**kwargs).all()

        return items
