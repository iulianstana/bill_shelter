from app import db


class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), index=True)
    bath_index = db.Column(db.Float)
    kitchen_index = db.Column(db.Float)
    datetime = db.Column(db.DateTime)

    def __repr__(self):
        return '<Notice %r:%r>' % (self.type, self.datetime.strftime("%B %Y"))


class MonthNotice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    cold_notice = db.Column(db.Integer, db.ForeignKey('notice.id'))
    hot_notice = db.Column(db.Integer, db.ForeignKey('notice.id'))

    def __repr__(self):
        return '<MonthNotice %r>' % self.datetime.strftime("%B %Y")
