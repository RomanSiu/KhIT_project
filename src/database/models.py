from sqlalchemy import String, DateTime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from datetime import datetime

Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[String] = mapped_column(String(30))
    surname: Mapped[String] = mapped_column(String(40))
    email: Mapped[String] = mapped_column(String(40), nullable=True)
    phone: Mapped[String] = mapped_column(String(30), nullable=True)
    address: Mapped[String] = mapped_column(String(100), nullable=True)
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=True)
