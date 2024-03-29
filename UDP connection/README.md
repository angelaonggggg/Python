# UDP Client-Server Communication

This Python script demonstrates a simple UDP client-server communication using sockets between 2 parties. The script provides both client and server functionalities, allowing communication between them over a UDP connection.

## Installation

To run the code locally:

1. Download the code.
2. Open a terminal and navigate to the directory containing the script.
3. Ensure that the following files are in the same directory:
   - `connection.py`
   - `Alice.txt`
   - `Bob.txt`

## Usage

1. To execute the Python code, open two terminals on the command prompt and navigate to the directory containing the files.

2. On one terminal, run the following command for Alice (Server):
    ```
    python3 connection.py
    ```

3. The system will prompt the user to enter a file: 
    ```
    Alice.txt
    ```

5. The server will wait for the client to connect before establishing the connection.

6. On the other terminal, run the following command for Bob (Client):
    ```
    python3 connection.py
    ```

7. The system will prompt the user to enter a file:
    ```
    Bob.txt
    ```

8. The server will establish the connection, and Bob can send a message to Alice.

## Language used

Python
