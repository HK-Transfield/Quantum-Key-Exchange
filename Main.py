from QKE import Emulation
from QKE.Emulation import QKEEmulator

emulator = None
run_type_dict = {"1": "standard", "2": "intercept", "3": "attack"}
qubit_length_dict = {"1": 16, "2": 256, "3": 1048}

if __name__ == "__main__":
    print("\nQuantum-Key Exchange Emulator, by Harmon Transfield")
    print("------------------------------------------------------\n")

    while True:
        run_type_input = input(
            "What type of QKE do you want to run?\n1. Standard QKE\n2. Intercept and Resend\n3. MITM Attack\nEnter (1, 2, 3): "
        )
        break

    while True:
        qubit_length_input = input(
            "How many Qubits do you want to use?\n1. 16\n2. 256 \n3. 1048\nEnter (1, 2, 3): "
        )
        break

    emulator = QKEEmulator(run_type=run_type_dict[run_type_input],
                           qubit_length=qubit_length_dict[qubit_length_input])

    successful_QKE = emulator.run_QKE()
    successful_encryption = emulator.run_symmetric_encryption()

    if successful_QKE:
        print("The QKE Algorithm performed successfully!")
    else:
        print("Oh no! looks like someone messed up the keys")

    if successful_encryption:
        print("Message sucessfully Ciphered")
