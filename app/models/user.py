from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    is_admin: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )

    is_verified: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False
    )