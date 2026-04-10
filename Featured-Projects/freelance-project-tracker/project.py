from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Project:
    """Base class for all projects."""
    client_id: int
    title: str
    project_type: str
    platform: str
    id: Optional[int] = None
    status: str = "Active"
    deadline: Optional[str] = None
    completed_date: Optional[str] = None
    created_date: str = ""
    
    def calculate_total(self) -> float:
        raise NotImplementedError("Subclass must implement calculate_total()")

    @property
    def is_overdue(self) -> bool:
        if not self.deadline or self.status != "Active":
            return False
        try:
            return datetime.now() > datetime.strptime(self.deadline, "%Y-%m-%d")
        except ValueError:
            return False

    def __str__(self):
        total = f"₹{self.calculate_total():,.2f}" if self.calculate_total() > 0 else "N/A"
        return (f"{self.id:<3} | {self.client_id:<3} | {self.title:<25} | "
                f"{self.project_type:<8} | {self.platform:<12} | {self.status:<10} | {total}")


@dataclass
class FixedProject(Project):
    fixed_price: float = 0.0

    def calculate_total(self) -> float:
        return self.fixed_price

    @classmethod
    def from_db_row(cls, row):
        return cls(
            id=row[0], client_id=row[1], title=row[2], project_type=row[3],
            platform=row[4], fixed_price=row[5] or 0.0, status=row[8],
            deadline=row[9], created_date=row[10], completed_date=row[11]
        )


@dataclass
class HourlyProject(Project):
    hours: float = 0.0
    hourly_rate: float = 0.0

    def calculate_total(self) -> float:
        return self.hours * self.hourly_rate

    @classmethod
    def from_db_row(cls, row):
        return cls(
            id=row[0], client_id=row[1], title=row[2], project_type=row[3],
            platform=row[4], hours=row[6] or 0.0, hourly_rate=row[7] or 0.0,
            status=row[8], deadline=row[9], created_date=row[10], completed_date=row[11]
        )