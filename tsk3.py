from typing import List, Optional


class Date:
    """A class representing a date for meeting compatibility."""
    
    def __init__(self, date_str: str) -> None:
        self.__date_str = date_str
    
    def get_date_str(self) -> str:
        """Get the date string."""
        return self.__date_str
    
    def __eq__(self, other) -> bool:
        """Compare two dates."""
        if not isinstance(other, Date):
            return False
        return self.__date_str == other.get_date_str()
    
    def __str__(self) -> str:
        """Return string representation of the date."""
        return self.__date_str


class User:
    """A class representing an employee/person."""
    
    def __init__(self, user_id: int, nick_name: str, first_name: str,
                 last_name: str, middle_name: str, gender: str) -> None:
        self.__id = user_id
        self.__nick_name = nick_name
        self.__first_name = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__gender = gender
    
    def get_id(self) -> int:
        """Get user ID."""
        return self.__id
    
    def get_full_name(self) -> str:
        """Get full name of the person."""
        if self.__last_name and self.__first_name:
            return f"{self.__first_name} {self.__last_name}"
        elif self.__nick_name:
            return self.__nick_name
        else:
            return f"{self.__first_name} {self.__middle_name}".strip()
    
    def __str__(self) -> str:
        """Return string representation of the user."""
        return self.get_full_name()


class Meeting:
    """A class representing a work meeting."""
    
    lst_meeting: List['Meeting'] = []
    
    def __init__(self, meeting_id: int, date: Date, title: str) -> None:
        self.__id = meeting_id
        self.__date = date
        self.__title = title
        self.__employees = []
        Meeting.lst_meeting.append(self)
    
    def get_id(self) -> int:
        """Get meeting ID."""
        return self.__id
    
    def get_date(self) -> Date:
        """Get meeting date."""
        return self.__date
    
    def get_title(self) -> str:
        """Get meeting title."""
        return self.__title
    
    def get_employees(self) -> List[User]:
        """Get list of employees attending the meeting."""
        return self.__employees
    
    def add_person(self, person: User) -> None:
        """
        Add a person to the meeting.
        
        Args:
            person (User): The person to add.
        """
        if person not in self.__employees:
            self.__employees.append(person)
    
    def count(self) -> int:
        """
        Count the number of employees attending the meeting.
        
        Returns:
            int: Number of employees.
        """
        return len(self.__employees)
    
    @classmethod
    def count_meeting(cls, date: Date) -> int:
        """
        Count the number of meetings on a specific date.
        
        Args:
            date (Date): The date to check.
        
        Returns:
            int: Number of meetings on that date.
        """
        count = 0
        for meeting in cls.lst_meeting:
            if meeting.get_date() == date:
                count += 1
        return count
    
    @classmethod
    def total(cls) -> int:
        """
        Get the total number of meetings.
        
        Returns:
            int: Total number of meetings.
        """
        return len(cls.lst_meeting)
    
    def __str__(self) -> str:
        """
        Return string representation of the meeting.
        
        Returns:
            str: Formatted meeting information.
        """
        employees_str = ", ".join([str(emp) for emp in self.__employees])
        return f"{self.__id} {self.__date} {self.__title} [{employees_str}]"
    
    def __repr__(self) -> str:
        """Return detailed string representation for debugging."""
        return f"Meeting(id={self.__id}, date={self.__date}, title='{self.__title}')"


class Load:
    """
    A class for loading meeting, person, and registration data from files.
    """
    
    @classmethod
    def write(cls, meetings_file: str, persons_file: str, pers_meetings_file: str) -> None:
        """
        Load data from files and create Meeting and User objects.
        
        Args:
            meetings_file (str): Path to meetings.txt file.
            persons_file (str): Path to persons.txt file.
            pers_meetings_file (str): Path to pers_meetings.txt file.
        """
        Meeting.lst_meeting.clear()

        persons = {}
        try:
            with open(persons_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(';')
                if len(parts) < 6:
                    continue
                
                user_id = int(parts[0].strip())
                nick_name = parts[1].strip()
                first_name = parts[2].strip()
                last_name = parts[3].strip()
                middle_name = parts[4].strip()
                gender = parts[5].strip()
                
                user = User(user_id, nick_name, first_name, last_name, middle_name, gender)
                persons[user_id] = user
        
        except FileNotFoundError:
            print(f"Ошибка: файл '{persons_file}' не найден")
            return
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return
        
        meetings = {}
        try:
            with open(meetings_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(';')
                if len(parts) < 3:
                    continue
                
                meeting_id = int(parts[0].strip())
                date_str = parts[1].strip()
                title = parts[2].strip()
                
                date = Date(date_str)
                meeting = Meeting(meeting_id, date, title)
                meetings[meeting_id] = meeting
        
        except FileNotFoundError:
            print(f"Ошибка: файл '{meetings_file}' не найден")
            return
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return

        try:
            with open(pers_meetings_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(';')
                if len(parts) < 2:
                    continue
                
                meeting_id = int(parts[0].strip())
                person_id = int(parts[1].strip())
                
                if meeting_id in meetings and person_id in persons:
                    meetings[meeting_id].add_person(persons[person_id])
        
        except FileNotFoundError:
            print(f"Ошибка: файл '{pers_meetings_file}' не найден")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")


def main() -> None:
    """
    The main function demonstrating the Meeting, User, and Load classes.
    """
    Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
    
    for item in Meeting.lst_meeting:
        print(item)
    
    print(Meeting.total())
    print(Meeting.count_meeting(Date('21.04.2020')))


if __name__ == "__main__":
    main()
