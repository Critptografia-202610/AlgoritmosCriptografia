# Algoritmo de Euclides Extendido con impresión de pasos y tabla
# Notación: i, r_i, q_i, s_i, t_i

import sys
from typing import List, Tuple

def euclides_extendido_pasos(a: int, b: int) -> Tuple[int, int, int, List[Tuple]]:
    """
    Calcula d = gcd(a,b) y coeficientes s, t tales que:
        a*s + b*t = d

    Además guarda los pasos del algoritmo y la tabla (i, r_i, q_i, s_i, t_i).
    """
 
    # Inicialización
    r_i_2, r_i_1 = a, b
    s_i_2, s_i_1 = 1, 0
    t_i_2, t_i_1 = 0, 1

    tabla = []
    i = 0

    while r_i_1 != 0:
        q_i = r_i_2 // r_i_1

        r_i = r_i_2 - q_i * r_i_1
        s_i = s_i_2 - q_i * s_i_1
        t_i = t_i_2 - q_i * t_i_1

        tabla.append((i, r_i_2, q_i, s_i_2, t_i_2))

        r_i_2, r_i_1 = r_i_1, r_i
        s_i_2, s_i_1 = s_i_1, s_i
        t_i_2, t_i_1 = t_i_1, t_i

        i += 1

    tabla.append((i, r_i_2, "-", s_i_2, t_i_2))

    d = r_i_2
    s = s_i_2
    t = t_i_2

    return d, s, t, tabla


def imprimir_pasos(a: int, b: int, tabla: List[Tuple]) -> None:
    print("\n>> Pasos del algoritmo de Euclides:\n")

    for fila in tabla[:-1]:
        i, r_i, q_i, _, _ = fila
        r_sig = tabla[i + 1][1]
        r_rest = r_i - q_i * r_sig
        print(f"{r_i} = {q_i}*{r_sig} + {r_rest}")


def imprimir_tabla(tabla: List[Tuple]) -> None:
    print("\n>> Tabla del algoritmo extendido:\n")
    print(f"{'i':>3} {'r_i':>6} {'q_i':>6} {'s_i':>6} {'t_i':>6}")
    print("-" * 33)

    for fila in tabla:
        i, r_i, q_i, s_i, t_i = fila
        print(f"{i:>3} {r_i:>6} {str(q_i):>6} {s_i:>6} {t_i:>6}")


def run() -> None:
    try:
        a = int(input("\n>> Inserte entero a: "))
        b = int(input(">> Inserte entero b: "))

        d, s, t, tabla = euclides_extendido_pasos(a, b)
        imprimir_pasos(a, b, tabla)
        imprimir_tabla(tabla)

        print("\n>> Confirmación final:\n")
        print(f"{a}*({s}) + {b}*({t}) = {a*s + b*t}")

    except KeyboardInterrupt:
        print("\n\n>> Cerrando programa...")
        sys.exit(0)
    except Exception as e:
        print(f"\n>> [ERROR]: {e}")


if __name__ == "__main__":
    print("\nAlgoritmo de Euclides Extendido (con pasos y tabla)")
    print("Presione ^C para salir")
    while True:
        run()
