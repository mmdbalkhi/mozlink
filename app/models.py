from config import SECRET_KEY
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids
from werkzeug.urls import url_fix

db = SQLAlchemy()
hashids = Hashids(min_length=3, salt=SECRET_KEY)


class Urls(db.Model):
    """urls table on db

    inherited from :class:`flask_sqlalchemy.SQLAlchemy`

    coumns::
        id (`int`): primary key
        original_url (`str`): url to shorten

    """

    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """url representation

        :returns:
            `str`: url representation
        """
        return f"Url({self.id}, '{self.original_url}')"

    def save(self):
        """save url to db

        :returns:
            `int`: url id
        """
        self.original_url = url_fix(self.original_url)
        db.session.add(self)
        db.session.commit()
        return self.id

    def get(self, id: str):
        """get url from db

        :args:
            id (`str`): url id

        :returns:
            `str`: url to redirect
        """
        return Urls.query.get(hashids.decode(id)[0])

    @staticmethod
    def normalise_url(url: str):
        """normalise url to add `http://` if not present and
        fix url with :func:`werkzeug.urls.url_fix`

        :args:
            ``url`` (`str`): url to normalise

        :returns:
            `str`: normalised url
        """
        if not url.startswith("http://"):
            url = f"http://{url}"
        return url_fix(url)
