from config import db, app, bcrypt
from models import Student, Admin, Course, Module, Message, student_courses, admin_courses
from faker import Faker
import random
from sqlalchemy import func

fake = Faker()

app.app_context().push()

# Function to generate fake data for Student
def generate_fake_student():
    email = fake.email()
    username = fake.user_name()
    password = f"{username}@1234"  # Generating password based on username
    student = Student(email=email, username=username)
    student.password_hash = password
    return student

# Function to generate fake data for Admin
def generate_fake_admin():
    email = fake.email()
    name = fake.name()
    password = f"{name.split()[0]}@1234"  # Generating password based on admin's first name
    admin = Admin(email=email, name=name)
    admin.password_hash = password
    return admin

# Function to generate fake data for Course
def generate_fake_course(admin):
    title = fake.sentence(nb_words=4)
    description = fake.paragraph()
    thumbnail = fake.image_url()
    price = round(random.uniform(10, 100), 2)
    course = Course(title=title, description=description, thumbnail=thumbnail, price=price, admin_id=admin.id)
    return course

# Function to generate fake data for Module
def generate_fake_module(course):
    title = fake.sentence(nb_words=3)
    media = fake.url()  # Using url() to generate a fake URL
    notes = fake.paragraph()
    return Module(title=title, media=media, notes=notes, course=course)

# Function to generate fake data for Message
def generate_fake_message(student):
    title = fake.sentence(nb_words=6)
    content = fake.paragraph(nb_sentences=3)
    return Message(title=title, content=content, student=student)

# Seed function to populate the database
def seed_database():
    try:
        # Delete all existing records
        db.session.query(Student).delete()
        db.session.query(Admin).delete()
        db.session.query(Course).delete()
        db.session.query(Module).delete()
        db.session.query(Message).delete()
        db.session.query(student_courses).delete()
        db.session.query(admin_courses).delete()
        db.session.commit()
        print("✅ Deleted existing records from the database.")

        # Create some fake admins
        admins = [generate_fake_admin() for _ in range(3)]
        db.session.add_all(admins)
        db.session.commit()
        print("✅ Created fake admins.")

        # Create some fake students
        students = [generate_fake_student() for _ in range(5)]
        db.session.add_all(students)
        db.session.commit()
        print("✅ Created fake students.")

        # Create some courses for each admin
        for admin in admins:
            courses = [generate_fake_course(admin) for _ in range(2)]
            db.session.add_all(courses)
            db.session.commit()

            # Establishing relationships between admins and courses
            for course in courses:
                if course not in admin.courses:
                    admin.courses.append(course)
            db.session.commit()
        print("✅ Established relationships between admins and courses.")

        # Create some modules for each course
        for course in Course.query.all():
            modules = [generate_fake_module(course) for _ in range(random.randint(2, 4))]
            db.session.add_all(modules)
            db.session.commit()
        print("✅ Created modules for each course.")

        # Create some messages for each student
        for student in students:
            messages = [generate_fake_message(student) for _ in range(random.randint(1, 3))]  # Generate 1 to 3 messages for each student
            db.session.add_all(messages)
            db.session.commit()
        print("✅ Created messages for each student.")

        # Establishing relationships between students and courses
        for student in students:
            courses = Course.query.order_by(func.random()).limit(2).all()  # Selecting random courses for each student
            for course in courses:
                student.courses.append(course)
            db.session.commit()
        print("✅ Established relationships between students and courses.")

        print("✅ Seeding completed successfully!")

    except Exception as e:
        db.session.rollback()
        print("❌ Seeding failed:", str(e))

if __name__ == '__main__':
    seed_database()
