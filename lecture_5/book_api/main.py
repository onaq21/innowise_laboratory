from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from pydantic import BaseModel

from db.database import Base, engine, get_db
from db.table import Book

Base.metadata.create_all(bind=engine)
app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int]

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]

class BookRead(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int]

    class Config:
        orm_mode = True

@app.post("/books/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)) -> BookRead:
    """Create a new book"""
    db_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=List[BookRead])
def read_books(db : Session = Depends(get_db)) -> List[BookRead]:
    """Get all books"""
    return db.query(Book).all()

@app.delete("/books/{id}", response_model=Optional[BookRead])
def delete_book(id : int, db: Session = Depends(get_db)) -> Optional[BookRead]:
    """Delete a book by ID"""
    book = db.query(Book).filter(Book.id == id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

@app.put("/books/{id}", response_model=Optional[BookRead])
def update_book(id: int, updated_book: BookUpdate, db: Session = Depends(get_db)) -> Optional[BookRead]:
    """Update a book data by ID"""
    book = db.query(Book).filter(Book.id == id).first()
    if book:
        if updated_book.title:
            book.title = updated_book.title
        if updated_book.author:
            book.author = updated_book.author
        if updated_book.year:
            book.year = updated_book.year
        db.commit()
        db.refresh(book)
    return book

@app.get("/books/search", response_model=List[BookRead])
def search_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db)
) -> List[BookRead]:
    """Search a book by title, author or year.
        All parameters are optional"""
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == (year))
    return query.all()
