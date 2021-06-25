from ..db import db

class Game(db.Model):
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

    def to_dict(self):
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