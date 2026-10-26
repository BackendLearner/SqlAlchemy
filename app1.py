from app import Base, SessionLocal, Branch, Student, Profile, Club


db = SessionLocal()


# new_branch = Branch(name="DS")
# db.add(new_branch)
# db.commit()

# new_student = Student(name="Swati", age=20, branch_id=1)
# db.add(new_student)
# db.commit()

# s = db.query(Student).filter_by(id=1).first()
# print(s)

branches = db.query(Branch).all()
print(branches)