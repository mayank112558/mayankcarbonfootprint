from database import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    company_name = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    energy_usage = db.relationship('EnergyUsage', backref='user', uselist=False)
    waste = db.relationship('Waste', backref='user', uselist=False)
    business_travel = db.relationship('BusinessTravel', backref='user', uselist=False)

    @property
    def total_energy(self):
        """Returns total energy usage for the user."""
        if self.energy_usage:
            return (self.energy_usage.electricity_bill or 0) + \
                   (self.energy_usage.natural_gas_bill or 0) + \
                   (self.energy_usage.fuel_bill or 0)
        return 0

    @property
    def total_waste(self):
        """Returns total waste generated by the user."""
        return self.waste.waste_generated if self.waste else 0

    @property
    def total_travel(self):
        """Returns total business travel footprint."""
        return self.business_travel.kilometers_traveled if self.business_travel else 0

    @property
    def total_footprint(self):
        """Calculates the total carbon footprint."""
        return self.total_energy + self.total_waste + self.total_travel


class EnergyUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    electricity_bill = db.Column(db.Float, nullable=False)
    natural_gas_bill = db.Column(db.Float, nullable=False)
    fuel_bill = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Waste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    waste_generated = db.Column(db.Float, nullable=False)
    recycling_percentage = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class BusinessTravel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kilometers_traveled = db.Column(db.Float, nullable=False)
    fuel_efficiency = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
