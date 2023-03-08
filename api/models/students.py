from ..utils import db

# Create the student model
class Student(db.Model):
  __tablename__ = 'students'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(45), nullable=False, unique=True)
  email = db.Column(db.String(50), nullable=False, unique=True)
  password_hash = db.Column(db.Text(), nullable=False)


  def __repr__(self):
      return f"<Student {self.name}>"

  def save(self):
      """
      Create this function on all object instance
      """
      db.session.add(self)
      db.session.commit()

  @classmethod
  def get_by_id(self, id):
      """
      Get the order by id
      """
      return self.query.get_or_404(id)