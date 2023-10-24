from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from app.database import get_db
from .. import models, schemas
from typing import List

app = APIRouter()

@app.post('/create', status_code=status.HTTP_201_CREATED, response_model=schemas.StudentResponse)
def create(student: schemas.Student, db: Session = Depends(get_db)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get('/get_info', response_model=List[schemas.StudentResponse])
def get_student(db: Session = Depends(get_db)):
    all_students = list(db.query(models.Student).all())
    return all_students

@app.get('/get_info/{id}', response_model=schemas.StudentResponse)
def get_student_by_id(id: int, db: Session = Depends(get_db)):
    get_student = db.query(models.Student).filter(models.Student.id == id).first()
    if get_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'student with id {id} not found')
    return get_student

@app.put('/update_info/{id}', response_model=schemas.StudentResponse)
def update_student(id: int, student: schemas.Student, db: Session = Depends(get_db)):
    update_query = db.query(models.Student).filter(models.Student.id == id)
    update_student = update_query.first()
    if update_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id {id} not found')
    update_query.update(student.dict(), synchronize_session=False)
    db.commit()
    return update_query.first()

@app.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def delete_info(id: int, db: Session = Depends(get_db)):
    delete_query = db.query(models.Student).filter(models.Student.id == id)
    delete_info = delete_query.first()
    if delete_info == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'student with id {id} not found')
    delete_query.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Student with id {id} sucessfully deleted"}