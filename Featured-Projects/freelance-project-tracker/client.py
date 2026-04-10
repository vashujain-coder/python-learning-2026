from dataclasses import dataclass
from typing import Optional


@dataclass
class Client:
    """Represents a freelance client."""
    name: str
    platform: str
    id: Optional[int] = None
    email: Optional[str] = None
    country: Optional[str] = None
    added_date: str = ""

    def __str__(self):
        return (f"{self.id if self.id else 'N/A':<3} | {self.name:<20} | "
                f"{self.email or 'N/A':<30} | {self.country or 'N/A':<15} | "
                f"{self.platform:<15} | {self.added_date}")

    @classmethod
    def from_db_row(cls, row):
        """Create Client object from database row."""
        return cls(
            id=row[0],
            name=row[1],
            email=row[2],
            country=row[3],
            platform=row[4],
            added_date=row[5]
        )