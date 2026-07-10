from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

class user_fn(BaseModel):
    id:int
    name:str
    age:int


students=[]

@app.get('/students')
def get_students():
    return students

@app.get('/students/{student_id}')
def get_student(student_id:int):
    for student in students:
        if students.id==student_id:
            return student
    from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class user_fn(BaseModel):
    id:int
    name:str
    age:int


students=[]

@app.get('/students')
def get_students():
    return students

@app.get('/students/{student_id}')
def get_student(student_id:int):
    for student in students:
        if students['id']==student_id:
            return student
    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )


@app.post('/students')

def create_student(student:user_fn):
    for s in students:
        if s.id==student.id:
            raise HTTPException(
                status_code=400,
                detail="Student id already exist"
            )

    students.append(student)
    return{
        "message":"Student added",
        "student":student
    }

@app.put('/students/{student_id}')

def update_student(student_id: int,student:user_fn):
    for index,s in enumerate(students):
        if s.id==student_id:
            students[index]=student
            return{
                "message":"Student updated",
                "student":student
            }
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.delete('/students/{student_id}')

def delete_student(student_id:int):
    for index,s in enumerate(students):
        if s.id==student_id:
            students.pop(index)
            return{
                "message":"Student deleted"
            }
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.post('/students')

def create_student(student:user_fn):
    students.append(student)
    return{
        "message":"Student added",
        "student":student
    }

@app.put('/students/{student_id}')

def update_student(student_id: int,student:user_fn):
    for index,s in enumerate(students):
        if s.id==student_id:
            students[index]=student
            return{
                "message":"Student updated",
                "student":student
            }
    return{"message":"student not found"}


@app.delete('/students/{student_id}')

def delete_student(student_id:int):
    for index,s in enumerate(students):
        if s.id==student_id:
            students.pop(index)
            return{
                "message":"Student deleted"
            }
    return{"message":"student not found"}
