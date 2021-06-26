from typing import Any, Dict, List
from ..db import db
# from db import db

class Game(db.Model):
    __tablename__ = "game"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    worth = db.Column(db.String)
    thumbnail = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)
    instructions = db.Column(db.String)
    open_giveaway_url = db.Column(db.String)
    published_date = db.Column(db.String)
    type = db.Column(db.String)
    platforms = db.Column(db.String)
    end_date = db.Column(db.String)
    users = db.Column(db.Integer)
    status = db.Column(db.String)
    gamerpower_url = db.Column(db.String)
    open_giveaway = db.Column(db.String)

    def __init__(self, *args, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.title = kwargs.get("title")
        self.worth = kwargs.get("worth")
        self.thumbnail = kwargs.get("thumbnail")
        self.image = kwargs.get("image")
        self.description = kwargs.get("description")
        self.instructions = kwargs.get("instructions")
        self.open_giveaway_url = kwargs.get("open_giveaway_url")
        self.published_date = kwargs.get("published_date")
        self.type = kwargs.get("type")
        self.platforms = kwargs.get("platforms")
        self.end_date = kwargs.get("end_date")
        self.users = kwargs.get("users")
        self.status = kwargs.get("status")
        self.gamerpower_url = kwargs.get("gamerpower_url")
        self.open_giveaway = kwargs.get("open_giveaway")
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "worth": self.worth,
            "thumbnail": self.thumbnail,
            "image": self.image,
            "description": self.description,
            "instructions": self.instructions,
            "open_giveaway_url": self.open_giveaway_url,
            "published_date": self.published_date,
            "type": self.type,
            "platforms": self.platforms,
            "end_date": self.end_date,
            "users": self.users,
            "status": self.status,
            "gamerpower_url": self.gamerpower_url,
            "open_giveaway": self.open_giveaway
        }
    
    def __str__(self) -> str:
        return f"Game<id: {self.id}, title: {self.title}, worth: {self.worth}>"

    def saveto_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def deletefrom_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def findby_title(cls, title) -> "Game":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def findby_id(cls, id) -> "Game":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["Game"]:
        return cls.query.all()
    