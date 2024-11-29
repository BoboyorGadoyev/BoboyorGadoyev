import math
import matplotlib.pyplot as plt

def multivibrator_frequency(R2, R3, C1, C2):

    t1 = math.log(2) * R2 * C1
    t2 = math.log(2) * R3 * C2
    T = t1 + t2
    f = 1 / T
    return t1, t2, T, f

def plot_multivibrator_waveform(R2, R3, C1, C2, duration=0.01):

    t1, t2, T, f = multivibrator_frequency(R2, R3, C1, C2)

    time = []
    signal = []
    t = 0
    value = 1

    while t < duration:
        if value == 1:
            for _ in range(int(t1 * 10000)):
                time.append(t)
                signal.append(value)
                t += 0.0001
        else:
            for _ in range(int(t2 * 10000)):
                time.append(t)
                signal.append(value)
                t += 0.0001
        value = 1 - value

    plt.figure(figsize=(10, 4))
    plt.plot(time, signal, label="Multivibrator to'lqini", color="blue")
    plt.title("Multivibrator to'lqini (to'rtburchak signal)")
    plt.xlabel("Vaqt (s)")
    plt.ylabel("Signal darajasi")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    print("Multivibrator chastotasini hisoblash dasturi")
    print("---------------------------------------------------")

    try:
        R2 = float(input("R2 (Ohm) qiymatini kiriting: "))
        R3 = float(input("R3 (Ohm) qiymatini kiriting: "))
        C1 = float(input("C1 (Farad) qiymatini kiriting: "))
        C2 = float(input("C2 (Farad) qiymatini kiriting: "))
    except ValueError:
        print("Xato! Faqat sonli qiymatlarni kiriting.")
        return

    t1, t2, T, f = multivibrator_frequency(R2, R3, C1, C2)

    print("\nHisoblash natijalari:")
    print(f"Bir qism davomiyligi (t1): {t1:.6e} s")
    print(f"Ikkinchi qism davomiyligi (t2): {t2:.6e} s")
    print(f"To'liq davr davomiyligi (T): {T:.6e} s")
    print(f"Multivibrator chastotasi (f): {f:.2f} Hz")

    plot_multivibrator_waveform(R2, R3, C1, C2)


if __name__ == "__main__":
    main()
