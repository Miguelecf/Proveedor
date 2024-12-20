from sqlalchemy.exc import SQLAlchemyError
from entities.base  import Base, SessionLocal, engine
from entities import product,photoURL,size,sizecolor

def init_db():
    try:
        session = SessionLocal()
        Base.metadata.create_all(bind=engine)
        session.commit()
        print("Tablas creadas exitosamente.")
    except SQLAlchemyError as e:
        print(f"Error al crear las tablas: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    init_db()