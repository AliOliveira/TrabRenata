import tkinter as tk
from tkinter import messagebox
import random
import time

class Estacionamento:
    def __init__(self):
        self.vagas_carro = 5
        self.vagas_moto = 3
        self.veiculos = {}
        
    def estacionar_veiculo(self, placa, modelo, tipo):
        if not placa or not modelo:
            return "⚠ Informe a placa e o modelo do veículo."
        
        if tipo == "Carro" and self.vagas_carro > 0:
            self.veiculos[placa] = (modelo, tipo, random.randint(1, 5))
            self.vagas_carro -= 1
            time.sleep(0.5)
            return f"✅ Carro {placa} ({modelo}) estacionado com sucesso!"
        elif tipo == "Moto" and self.vagas_moto > 0:
            self.veiculos[placa] = (modelo, tipo, random.randint(1, 5))
            self.vagas_moto -= 1
            time.sleep(0.5)
            return f"✅ Moto {placa} ({modelo}) estacionada com sucesso!"
        else:
            return "❌ Sem vagas disponíveis para esse tipo de veículo."
        
    def remover_veiculo(self, placa):
        if placa in self.veiculos:
            modelo, tipo, horas = self.veiculos.pop(placa)
            preco = 5 * horas if tipo == "Carro" else 3 * horas
            if tipo == "Carro":
                self.vagas_carro += 1
            else:
                self.vagas_moto += 1
            time.sleep(0.5)
            return f"🚗 {tipo} {placa} ({modelo}) removido. ⏳ Tempo: {horas}h. 💰 Valor: R${preco:.2f}"
        else:
            return "❌ Veículo não encontrado."
        
    def listar_veiculos(self):
        time.sleep(0.5)
        if not self.veiculos:
            return "📭 Nenhum veículo estacionado."
        return "\n".join([f"🅿 {placa} - {modelo} ({tipo})" for placa, (modelo, tipo, _) in self.veiculos.items()])


def estacionar():
    placa = entry_placa.get()
    modelo = entry_modelo.get()
    tipo = var_tipo.get()
    if placa and modelo:
        msg = estacionamento.estacionar_veiculo(placa, modelo, tipo)
        root.after(500, lambda: messagebox.showinfo("📌 Informação", msg))
    else:
        messagebox.showwarning("⚠ Atenção", "Por favor, informe a placa e o modelo do veículo!")

def remover():
    placa = entry_placa.get()
    if placa:
        msg = estacionamento.remover_veiculo(placa)
        root.after(500, lambda: messagebox.showinfo("📌 Informação", msg))
    else:
        messagebox.showwarning("⚠ Atenção", "Informe a placa para remover o veículo!")

def listar():
    msg = estacionamento.listar_veiculos()
    root.after(500, lambda: messagebox.showinfo("🚘 Veículos Estacionados", msg))

def sair():
    root.destroy()

estacionamento = Estacionamento()
root = tk.Tk()
root.title("🚗 Sistema de Estacionamento 🏍")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, padx=20, pady=20, bg="#ffffff", relief=tk.RIDGE, borderwidth=2)
frame.pack(pady=20)

tk.Label(frame, text="🚗 Sistema de Estacionamento 🏍", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)

tk.Label(frame, text="🔤 Placa:", bg="#ffffff").pack()
entry_placa = tk.Entry(frame, width=30)
entry_placa.pack(pady=5)

tk.Label(frame, text="🚘 Modelo:", bg="#ffffff").pack()
entry_modelo = tk.Entry(frame, width=30)
entry_modelo.pack(pady=5)

var_tipo = tk.StringVar(value="Carro")
tipo_frame = tk.Frame(frame, bg="#ffffff")
tipo_frame.pack()
tk.Radiobutton(tipo_frame, text="🚗 Carro", variable=var_tipo, value="Carro", bg="#ffffff").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(tipo_frame, text="🏍 Moto", variable=var_tipo, value="Moto", bg="#ffffff").pack(side=tk.LEFT, padx=10)

btn_frame = tk.Frame(frame, bg="#ffffff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="🅿 Estacionar", command=estacionar, width=15, bg="#4CAF50", fg="white").pack(pady=2)
tk.Button(btn_frame, text="❌ Remover", command=remover, width=15, bg="#F44336", fg="white").pack(pady=2)
tk.Button(btn_frame, text="📜 Listar Veículos", command=listar, width=15, bg="#2196F3", fg="white").pack(pady=2)
tk.Button(btn_frame, text="🚪 Sair", command=sair, width=15, bg="#555555", fg="white").pack(pady=2)

root.mainloop()
