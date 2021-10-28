#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "HK Transfield"
# ---------------------------------------------------------------------------
"""
Main method, runs the entire application. Allows for different configurations
with respect to the type of emulation the user would like to run and the
length of qubits they want to send
"""
# ---------------------------------------------------------------------------

from QKE.Emulation import QKEEmulator

emulator = None
run_type_dict = {"1": "standard", "2": "intercept", "3": "attack"}
qubit_length_dict = {"1": 16, "2": 256, "3": 1048}

if __name__ == "__main__":
    print("\nQuantum-Key Exchange Emulator, by Harmon Transfield")
    print("------------------------------------------------------\n")

    # Configure what type of emulation the user wants to run
    while True:
        run_type_input = input(
            "What type of QKE do you want to run?\n1. Standard QKE\n2. Intercept and Resend\n3. MITM Attack\nEnter (1, 2, 3): "
        )

        # Just add some very basic validation
        if run_type_input not in ('1', '2', '3'):
            print("Invalid input, please enter 1, 2, or 3")
        else:
            break

    # Configure how many qubits the stream length will be
    while True:
        qubit_length_input = input(
            "\nHow many Qubits do you want to use?\n1. 16\n2. 256 \n3. 1048\nEnter (1, 2, 3): "
        )

        # More basic validation
        if run_type_input not in ('1', '2', '3'):
            print("Invalid input, please enter 1, 2, or 3")
        else:
            break

    # Set a message length
    while True:
        message_length_input = int(
            input("\nEnter the length of the message (16 - 4096): "))

        # More basic validation
        if message_length_input < 16 or message_length_input > 4096:
            print("Invalid input, please enter a number ")
        else:
            break

    # Create a new emulation session
    emulator = QKEEmulator(run_type=run_type_dict[run_type_input],
                           message_length=message_length_input,
                           qubit_length=qubit_length_dict[qubit_length_input])

    # We need to generate some keys first before attempting encryption
    QKE_session = emulator.run_QKE()
    if QKE_session:
        print("The emulation successfully performed a QKE!")
    else:
        print("The emulation could not produce matching keys")

    # Keys have been generated, we can now perform a symmetric encryption
    encryption_session = emulator.run_symmetric_encryption()
    if encryption_session:
        print("The emulation successfully performed a symmetric encryption")
    else:
        print("The emulation could not perform a symmetric encyption")
