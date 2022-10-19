from typing import Tuple, Dict, List, Any
from sys import argv


class Simulator:
    help_program = """Simulador AFD y MT\n
    Para la ejecución proporcione el programa y la cita, de esta forma:
    python simulador.py programa.txt cintas.txt
    """

    def __init__(self):
        self.dict_program: Dict[Tuple[str, str], Any]
        self.tapes_lines: List[str]
        self.type_program: str

    def _manage_input(self) -> Tuple[str, str]:
        """
        ensures that the correct parameters come in the execution of the program
        """
        if "--help" in argv:
            print(self.help_program)
            exit()

        try:
            program = argv[1]
        except IndexError:
            print("Debe ingresar el parametro: programa.txt")
            exit()

        try:
            tapes = argv[2]
        except IndexError:
            print("Debe ingresar el parametro: cintas.txt")
            exit()

        return program, tapes

    def _read_files(self, program: str, tapes: str) -> Tuple[list, list]:
        program_lines = []
        with open(program, 'r') as f:
            program_lines = f.readlines()

        tapes_lines = []
        with open(tapes, 'r') as f:
            tapes_lines = f.readlines()

        return program_lines, tapes_lines

    def __input_afd(self, line: List[str]) -> Dict[Tuple[str, str], str]:
        # TODO validar los caracteres que vengan
        final_value = {
            (line[0].strip(), line[1].strip()): line[2].strip()
        }
        return final_value

    def __input_mt(self, line: List[str]) -> Dict[Tuple[str, str], Tuple[str, str, str]]:
        # TODO validar los caracteres que vengan
        final_value = {
            (line[0].strip(), line[1].strip()): (line[2].strip(), line[3].strip(), line[4].strip())
        }
        return final_value

    def _serialize_values(self, program_lines: list, tapes_lines: list):
        dict_program = {}
        mt = 0
        afd = 0
        for i, values in enumerate(program_lines):
            line = values.split(" ")

            if len(line) == 5 and afd:
                print(
                    f"Hey!! MT o AFD?\nEn programa.txt, en la linea: {i+1}\nDato invalido: {values}"
                )
                exit()
            elif len(line) == 3 and mt:
                print(
                    f"Hey!! AFD o MT?\nEn programa.txt, en la linea: {i+1}\nDato invalido: {values}"
                )
                exit()
            elif len(line) == 5 and mt:
                dict_program.update(self.__input_mt(line))

            elif len(line) == 3 and afd:
                dict_program.update(self.__input_afd(line))

            elif len(line) == 5:
                mt = 1
                dict_program.update(self.__input_mt(line))

            elif len(line) == 3:
                afd = 1
                dict_program.update(self.__input_afd(line))

            else:
                print(
                    f"Entrada no admitida en programa.txt, en la linea: {i+1}\nDato invalido: {values}"
                )
                exit()

        self.type_program = "afd" if afd else "mt"
        self.dict_program = dict_program
        self.tapes_lines = [i.strip() for i in tapes_lines]

    def run_simulator(self):
        params = self._manage_input()
        values = self._read_files(*params)
        self._serialize_values(*values)
        if self.type_program == "afd":
            self.run_afd()
        elif self.type_program == "mt":
            self.run_mt()

    def run_afd(self):
        mensaje = {True: 'Aceptada', False: 'Rechazada'}

        def AFD(d, q0, F, tape):
            q = q0
            for symbol in tape:
                q = d[q, symbol]
            return q in F

        for line in self.tapes_lines:
            print(
                'La entrada', line, "es", mensaje[
                    AFD(self.dict_program, '0', {'3'}, line) # TODO arreglar para saber el conjunto F
                ]
            )

    def run_mt(self):
        print("run_mt")
        print(self.dict_program, self.tapes_lines)


def main():
    sm = Simulator()
    sm.run_simulator()


if __name__ == "__main__":
    main()
