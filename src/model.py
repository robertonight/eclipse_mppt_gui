import serial


class Pcb:
    def __init__(self, uart_port: str, baud_rate: int):
        print("Initialisation de la carte...")
        self.__uart_port = uart_port
        self.__baud_rate = baud_rate

    def read_data_from_emitter(self):
        pass  # logic will be added later by polymorphism

    @property
    def uart_port(self) -> str:
        return self.__uart_port

    @property
    def baud_rate(self) -> int:
        return self.__baud_rate

    @uart_port.setter
    def uart_port(self, uart_port: str) -> None:
        self.__uart_port = uart_port

    @baud_rate.setter
    def baud_rate(self, baud_rate: int) -> None:
        self.__baud_rate = baud_rate


class Nucleo(Pcb):
    def __init__(self, uart_port: str, baud_rate: int):
        super().__init__(uart_port, baud_rate)

    def read_data_from_emitter(self):
        try:
            # Initialisation de la connexion UART
            with serial.Serial(self.uart_port, self.baud_rate, timeout=1) as ser:
                print(
                    f"Connexion UART ouverte sur {self.uart_port} à {self.baud_rate} bauds."
                )
                print("En attente des données...\n")

                while True:
                    # Lecture des données en provenance de l'UsART
                    myData = ser.readline()
                    print(f"myData: {myData}")
                    data = myData.decode().strip()
                    if data:  # Si des données sont reçues
                        print(f"Données reçues : {data}")

        except serial.SerialException as e:
            print(f"Erreur : Impossible d'ouvrir le port série {self.uart_port}.\n{e}")
        except KeyboardInterrupt:
            print("\nConnexion UART fermée. Programme arrêté.")
        except UnicodeDecodeError as myExcep:
            data = ser.readline().strip("\t")
            print(f"Données reçues : {data[0].decode("utf-8")}")
