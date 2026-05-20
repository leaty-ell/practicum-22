from typing import List


class AirTicket:
    """A class representing an airline ticket."""
    
    def __init__(self, passenger_name: str, _from: str, to: str, date_time: str,
                 flight: str, seat: str, _class: str, gate: str) -> None:
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate
    
    def __str__(self) -> str:
        """
        Return formatted string representation of the ticket.
        
        Returns:
            str: Formatted ticket string matching the table layout.
        """
        class_display = {
            'P': 'P',
            'S': 'S',
            'C': 'C',
            'Premium': 'P',
            'Standard': 'S',
            'Comfort': 'C'
        }
        cls = class_display.get(self._class, self._class)
        
        name = self.passenger_name[:18].ljust(18)
        _from = self._from[:4].ljust(4)
        to = self.to[:2].ljust(2)
        date_time = self.date_time[:16].ljust(16)
        flight = self.flight[:20].ljust(20)
        seat = self.seat[:3].ljust(3)
        gate = self.gate[:4].ljust(4)
        
        return f"|{name}|{_from}|{to}|{date_time}|{flight}|{seat}|{cls}|{gate}|"
    
    def __repr__(self) -> str:
        """Return string representation for debugging."""
        return (f"AirTicket(passenger_name='{self.passenger_name}', _from='{self._from}', "
                f"to='{self.to}', date_time='{self.date_time}', flight='{self.flight}', "
                f"seat='{self.seat}', _class='{self._class}', gate='{self.gate}')")


class Load:
    """A class for loading ticket data from a file."""
    
    data: List[AirTicket] = []
    
    @classmethod
    def write(cls, filename: str) -> List[AirTicket]:
        """
        Load ticket data from a file and store in class attribute.
        
        Args:
            filename (str): Path to the tickets file.
        
        Returns:
            List[AirTicket]: List of AirTicket instances.
        """
        cls.data = []
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(';')
                
                if len(parts) < 8:
                    continue
                
                passenger_name = parts[0].strip()
                _from = parts[1].strip()
                to = parts[2].strip()
                date_time = parts[3].strip()
                flight = parts[4].strip()
                seat = parts[5].strip()
                _class = parts[6].strip()
                gate = parts[7].strip()

                ticket = AirTicket(passenger_name, _from, to, date_time,
                                   flight, seat, _class, gate)
                cls.data.append(ticket)
        
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
        
        return cls.data


def main() -> None:
    """
    The main function demonstrating the AirTicket and Load classes.
    """
    tickets = Load.write('tickets.txt')
    
    print('-' * 79)
    print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
    print('=' * 79)
    
    for item in Load.data:
        print(item)
    
    print('-' * 79)


if __name__ == "__main__":
    main()
