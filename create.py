from application import db
from application.models import Animal_Group1, Animal_Group2

db.drop_all()
db.create_all()

g1_animal1 = Animal_Group1(name='Lion')

g2_animal1 = Animal_Group2(name='Tiger')

db.session.add(g1_animal1)
db.session.add(g2_animal1)
db.session.commit()
