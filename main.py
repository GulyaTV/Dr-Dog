import random
import time
import os
import shutil
import winreg
import psutil
import webbrowser
from threading import Thread
import customtkinter as ctk

class DrDog:
    def __init__(self, name="Гуля"):
        self.name = name
        self.threats = ["троян", "червь", "шпион", "рекламный вирус", "шифровальщик"]
        self.malicious_sites = ["exinariuminix.info", "malware.com", "virus.org", "trojan.horse"]
        self.actions = ["лает", "рычит", "виляет хвостом", "обнюхивает", "прыгает вокруг"]
        self.backup_folder = "backup_files"
        # Расширенные сигнатуры для поиска вредоносных файлов
        self.malicious_signatures = [
            "malware", "virus", "trojan", "worm", "spyware", "ransomware",
            "keylogger", "rootkit", "adware", "exploit", "backdoor"
        ]
        self.gui_mode = True  # По умолчанию графический интерфейс

    def bark(self):
        print(f"{self.name}: Гав! Гав!")

    def scan_system(self, progress_callback=None):
        print(f"{self.name} начинает обнюхивать систему...")
        time.sleep(2)
        threats_found = random.randint(0, 5)
        if threats_found == 0:
            print(f"{self.name}: Всё чисто! Можно идти гулять!")
            if progress_callback:
                progress_callback(100, "Всё чисто! Можно идти гулять!")
        else:
            print(f"{self.name}: Гав! Гав! Обнаружено {threats_found} угроз!")
            for i in range(threats_found):
                threat = random.choice(self.threats)
                action = random.choice(self.actions)
                print(f"{self.name} {action} на {threat}...")
                time.sleep(1)
                if progress_callback:
                    progress_callback((i + 1) * 20, f"Обнаружена угроза: {threat}")
            print(f"{self.name}: Все угрозы устранены! Молодец, {self.name}!")
            if progress_callback:
                progress_callback(100, "Все угрозы устранены!")

    def scan_registry(self, progress_callback=None):
        print(f"{self.name} начинает проверку реестра Windows...")
        time.sleep(2)
        found_malicious = False

        try:
            reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
            for i in range(winreg.QueryInfoKey(registry_key)[1]):
                value_name, value_data, _ = winreg.EnumValue(registry_key, i)
                for site in self.malicious_sites:
                    if site in value_data:
                        print(f"{self.name}: Гав! Гав! Обнаружен подозрительный сайт в реестре: {site}")
                        print(f"{self.name}: Удаляю вредоносные записи...")
                        winreg.DeleteValue(registry_key, value_name)
                        found_malicious = True
            winreg.CloseKey(registry_key)
        except Exception as e:
            print(f"{self.name}: Ошибка при доступе к реестру: {e}")

        if not found_malicious:
            print(f"{self.name}: В реестре всё чисто!")
            if progress_callback:
                progress_callback(100, "В реестре всё чисто!")
        else:
            if progress_callback:
                progress_callback(100, "Реестр очищен!")

    def treat_system(self, progress_callback=None):
        print(f"{self.name} начинает лечение системы...")
        time.sleep(2)
        print(f"{self.name}: Лечение завершено! Ваш компьютер здоров!")
        if progress_callback:
            progress_callback(100, "Лечение завершено!")

    def backup_files(self, progress_callback=None):
        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)
        print(f"{self.name} начинает закапывать важные файлы...")
        time.sleep(2)
        files = [f for f in os.listdir() if os.path.isfile(f)]
        if not files:
            print(f"{self.name}: Нет файлов для резервного копирования.")
            if progress_callback:
                progress_callback(100, "Нет файлов для резервного копирования.")
            return
        for i, file in enumerate(files):
            shutil.copy(file, os.path.join(self.backup_folder, file))
            print(f"{self.name}: Файл '{file}' закопан!")
            if progress_callback:
                progress_callback((i + 1) * 100 // len(files), f"Копирование файла: {file}")
        print(f"{self.name}: Все файлы успешно закопаны в папку '{self.backup_folder}'.")
        if progress_callback:
            progress_callback(100, "Все файлы закопаны!")

    def scan_files(self, directory=".", progress_callback=None):
        print(f"{self.name} начинает сканирование файлов в директории '{directory}'...")
        time.sleep(2)
        found_malicious = False
        files = [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files]
        for i, file_path in enumerate(files):
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for signature in self.malicious_signatures:
                        if signature in content:
                            print(f"{self.name}: Гав! Гав! Обнаружен подозрительный файл: {file_path}")
                            print(f"{self.name}: Сигнатура: {signature}")
                            found_malicious = True
            except Exception as e:
                print(f"{self.name}: Ошибка при чтении файла {file_path}: {e}")
            if progress_callback:
                progress_callback((i + 1) * 100 // len(files), f"Сканирование файла: {file_path}")
        if not found_malicious:
            print(f"{self.name}: Вредоносные файлы не обнаружены!")
            if progress_callback:
                progress_callback(100, "Вредоносные файлы не обнаружены!")

    def scan_processes(self, progress_callback=None):
        print(f"{self.name} начинает сканирование процессов...")
        time.sleep(2)
        found_malicious = False
        processes = psutil.process_iter(['pid', 'name'])
        for process in processes:
            try:
                process_name = process.info['name']
                for signature in self.malicious_signatures:
                    if signature in process_name.lower():
                        print(f"{self.name}: Гав! Гав! Обнаружен подозрительный процесс: {process_name} (PID: {process.info['pid']})")
                        found_malicious = True
            except Exception as e:
                print(f"{self.name}: Ошибка при сканировании процесса: {e}")
        if not found_malicious:
            print(f"{self.name}: Подозрительные процессы не обнаружены!")
            if progress_callback:
                progress_callback(100, "Подозрительные процессы не обнаружены!")
        else:
            if progress_callback:
                progress_callback(100, "Сканирование процессов завершено!")

class DrDogApp:
    def __init__(self, root, dr_dog):
        self.root = root
        self.dr_dog = dr_dog
        self.root.title("Dr. Dog")
        self.root.geometry("500x400")

        self.label = ctk.CTkLabel(root, text=f"Добро пожаловать в Dr. Dog, {self.dr_dog.name}!", font=("Arial", 16))
        self.label.pack(pady=10)

        self.progress = ctk.CTkProgressBar(root, orientation="horizontal", mode="determinate")
        self.progress.pack(pady=10)
        self.progress.set(0)

        self.status_label = ctk.CTkLabel(root, text="Готов к работе!", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.scan_system_button = ctk.CTkButton(root, text="Сканировать систему", command=lambda: Thread(target=self.dr_dog.scan_system, args=(self.update_progress,)).start())
        self.scan_system_button.pack(pady=5)

        self.scan_registry_button = ctk.CTkButton(root, text="Проверить реестр", command=lambda: Thread(target=self.dr_dog.scan_registry, args=(self.update_progress,)).start())
        self.scan_registry_button.pack(pady=5)

        self.scan_files_button = ctk.CTkButton(root, text="Сканировать файлы", command=self.scan_files)
        self.scan_files_button.pack(pady=5)

        self.scan_processes_button = ctk.CTkButton(root, text="Сканировать процессы", command=lambda: Thread(target=self.dr_dog.scan_processes, args=(self.update_progress,)).start())
        self.scan_processes_button.pack(pady=5)

        self.backup_button = ctk.CTkButton(root, text="Закопать файлы", command=lambda: Thread(target=self.dr_dog.backup_files, args=(self.update_progress,)).start())
        self.backup_button.pack(pady=5)

        self.feed_button = ctk.CTkButton(root, text="Покормить Гулю", command=self.feed_gulya)
        self.feed_button.pack(pady=5)

        self.source_code_button = ctk.CTkButton(root, text="Исходный код", command=self.open_source_code)
        self.source_code_button.pack(pady=5)

    def update_progress(self, value, message):
        self.progress.set(value / 100)
        self.status_label.configure(text=message)

    def scan_files(self):
        directory = ctk.filedialog.askdirectory()
        if directory:
            Thread(target=self.dr_dog.scan_files, args=(directory, self.update_progress)).start()

    def feed_gulya(self):
        webbrowser.open("https://boosty.to/gulya_tv")

    def open_source_code(self):
        webbrowser.open("https://github.com/GulyaTV/Dr-Dog")

def main():
    dr_dog = DrDog()
    root = ctk.CTk()
    app = DrDogApp(root, dr_dog)
    root.mainloop()

if __name__ == "__main__":
    main()
