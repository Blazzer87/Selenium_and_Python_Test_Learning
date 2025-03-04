from pydantic import BaseModel, computed_field
from datetime import date
from dateutil.relativedelta import relativedelta

class User(BaseModel):
    id: int
    name: str
    surname: str
    birthday_date: date

    @computed_field
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    @computed_field
    def age(self) -> str:
        today = date.today()
        delta = relativedelta(today, self.birthday_date)
        return f"{delta.years} лет, {delta.months} месяцев и {delta.days} дней"




alex = User(id=1, name="Алексей", surname="Яковенко", birthday_date="1993-02-19")

print(alex.model_dump())