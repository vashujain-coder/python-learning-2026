from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Payment:
    """Represents a payment received for a project."""
    project_id: int
    amount: float
    id: Optional[int] = None
    currency: str = "INR"
    payment_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    notes: Optional[str] = None

    def __str__(self):
        return (f"{self.id or 'N/A':<3} | Project {self.project_id:<3} | "
                f"{self.currency} {self.amount:>10,.2f} | {self.payment_date}")

    @classmethod
    def from_db_row(cls, row):
        """Create Payment object from database row."""
        return cls(
            id=row[0],
            project_id=row[1],
            amount=row[2],
            currency=row[3],
            payment_date=row[4],
            notes=row[5]
        )