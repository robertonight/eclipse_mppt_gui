from model import Nucleo, Pcb

UART_PORT = "COM3"  # port de série
BAUD_RATE = 115200  # vitesse configurée dans code STM32


def main():
    pcb: Pcb = Nucleo(UART_PORT, BAUD_RATE)
    pcb.read_data_from_emitter()


if __name__ == "__main__":
    main()
