import socket

HOST = '0.0.0.0'
PORT = 65432
flag = "Master}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        conn.sendall(b"This is another program being run from your docker container,\n")
        conn.sendall(b"Do you want the second part of the flag?\n")
        conn.sendall(b"You could input something, maybe that will work.\n> ")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            try:
                result = str(eval(data.decode()))
                conn.sendall(result.encode() + b"\n> ")

            except Exception as e:
                error_msg = f"Error: {e}\n> "
                conn.sendall(error_msg.encode())
