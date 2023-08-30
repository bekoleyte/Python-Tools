import socket
import tkinter as tk
from tkinter import messagebox


def scan_ports(target, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports


def scan_button_clicked():
    target_ip = target_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())

    open_ports = scan_ports(target_ip, start_port, end_port)

    if open_ports:
        messagebox.showinfo("Sonuç", f"Açık portlar: {open_ports}")
    else:
        messagebox.showinfo("Sonuç", "Açık port bulunamadı.")


# GUI oluşturma
root = tk.Tk()
root.title("Port Tarama Aracı")

target_label = tk.Label(root, text="Hedef IP Adresi:")
target_label.pack()

target_entry = tk.Entry(root)
target_entry.pack()

start_port_label = tk.Label(root, text="Başlangıç Portu:")
start_port_label.pack()

start_port_entry = tk.Entry(root)
start_port_entry.pack()

end_port_label = tk.Label(root, text="Bitiş Portu:")
end_port_label.pack()

end_port_entry = tk.Entry(root)
end_port_entry.pack()

scan_button = tk.Button(root, text="Tarama Yap", command=scan_button_clicked)
scan_button.pack()

root.mainloop()