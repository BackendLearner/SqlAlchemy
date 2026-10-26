from sqlalchemy import create_engine, Integer,Column, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker,relationship

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

student_club = Table(
    "student_club",
    Base.metadata,
    Column("student_id",Integer,ForeignKey("students.id")),
    Column("club_id",Integer,ForeignKey("clubs.id")) 
)

class Branch(Base):

    __tablename__ = "branches"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    students = relationship("Student",back_populates="branch",cascade="all,delete")

    def __repr__(self):
        return f"Branch(name={self.name!r})"

class Student(Base):
    __tablename__= "students"  
    id = Column(Integer, primary_key=True) 
    name = Column(String)
    age = Column(Integer, default=18) 
    branch_id = Column(Integer, ForeignKey("branches.id"),nullable=True)

    branch = relationship("Branch", back_populates="students")

    profile = relationship("Profile", uselist=False, back_populates="student", cascade="all, delete")

    clubs = relationship("Club", secondary=student_club, back_populates="members")

    def __str__(self) :
        return f"{self.name} - {self.branch.name}"

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer,primary_key = True)
    bio = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="profile")

    def __str__(self) :
        return f"{self.student.name}"

class Club(Base):
    __tablename__ = "clubs"
    id =Column(Integer, primary_key = True)
    name = Column(String,unique =True)

    members = relationship("Student", secondary=student_club, back_populates="clubs")

    def __str__(self):
        return f"{self.name}"

Base.metadata.create_all(engine)
