import time
from datetime import datetime, date


class Date:
    """A class representing a date with validation and comparison operators."""
    
    MONTHS = {
        1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр',
        5: 'май', 6: 'июн', 7: 'июл', 8: 'авг',
        9: 'сен', 10: 'окт', 11: 'ноя', 12: 'дек'
    }
    
    def __init__(self, date_str: str) -> None:
        """
        Initialize a Date object with a string in format "dd.mm.yyyy".
        
        Args:
            date_str (str): Date string in format "dd.mm.yyyy".
        """
        self.__date = None
        self.date = date_str 
    
    @property
    def date(self):
        """
        Get the date in formatted string "d mmm yyyy г.".
        
        Returns:
            str: Formatted date string or None if date is invalid.
        """
        if self.__date is None:
            return None
        
        day = self.__date.day
        month = self.MONTHS[self.__date.month]
        year = self.__date.year
        return f"{day} {month} {year} г."
    
    @date.setter
    def date(self, value: str) -> None:
        """
        Set the date from a string in format "dd.mm.yyyy".
        
        Args:
            value (str): Date string in format "dd.mm.yyyy".
        """
        if not isinstance(value, str):
            print("ошибка")
            self.__date = None
            return
        
        try:
            day, month, year = map(int, value.split('.'))
            
            self.__date = datetime(year, month, day)
        except (ValueError, AttributeError, TypeError):
            print("ошибка")
            self.__date = None
    
    def to_timestamp(self) -> int | None:
        """
        Convert the date to Unix timestamp (seconds since 01.01.1970).
        
        Returns:
            int | None: Number of seconds since 1970-01-01, or None if date is invalid.
        """
        if self.__date is None:
            return None

        timestamp = int(self.__date.timestamp())
        return timestamp
    
    def _get_datetime(self):
        """
        Get the internal datetime object for comparisons.
        
        Returns:
            datetime | None: The datetime object or None if invalid.
        """
        return self.__date

    def __eq__(self, other) -> bool:
        """Check if two dates are equal."""
        if not isinstance(other, Date):
            return False
        if self.__date is None or other._get_datetime() is None:
            return False
        return self.__date == other._get_datetime()
    
    def __ne__(self, other) -> bool:
        """Check if two dates are not equal."""
        if not isinstance(other, Date):
            return True
        if self.__date is None or other._get_datetime() is None:
            return True
        return self.__date != other._get_datetime()
    
    def __lt__(self, other) -> bool:
        """Check if this date is earlier than another date."""
        if not isinstance(other, Date):
            return NotImplemented
        if self.__date is None or other._get_datetime() is None:
            return False
        return self.__date < other._get_datetime()
    
    def __le__(self, other) -> bool:
        """Check if this date is earlier than or equal to another date."""
        if not isinstance(other, Date):
            return NotImplemented
        if self.__date is None or other._get_datetime() is None:
            return False
        return self.__date <= other._get_datetime()
    
    def __gt__(self, other) -> bool:
        """Check if this date is later than another date."""
        if not isinstance(other, Date):
            return NotImplemented
        if self.__date is None or other._get_datetime() is None:
            return False
        return self.__date > other._get_datetime()
    
    def __ge__(self, other) -> bool:
        """Check if this date is later than or equal to another date."""
        if not isinstance(other, Date):
            return NotImplemented
        if self.__date is None or other._get_datetime() is None:
            return False
        return self.__date >= other._get_datetime()
    
    def __str__(self) -> str:
        """Return string representation of the date."""
        if self.__date is None:
            return "None"
        return self.date


def main() -> None:
    """
    The main function demonstrating the Date class functionality.
    """
    d1 = Date('07.12.2021')
    print(d1.date)          
    d1.date = '14.02.2022'
    print(d1.date)          
    print(d1.to_timestamp())
    d2 = Date('32.14.2020')
    print(d2.date)         
    d2.date = '29.02.2021'
    print(d2)               
    d2.date = '29.02.2020'
    print(d2.date)         
    
    if d1 < d2:
        print('YES')
    else:
        print('NO')          
    
    print(d1 >= d2)          
    print(d1 != Date('01.01.2023')) 
    print(d1 <= d2)         


if __name__ == "__main__":
    main()
