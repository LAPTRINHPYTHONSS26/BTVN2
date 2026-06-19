from abc import ABC, abstractmethod

# Lớp cha: Khuôn mẫu Tướng (Dùng ABC để ép buộc thực thi)
class Hero(ABC):
    @abstractmethod
    def use_ultimate(self):
        pass

# Lớp con 1: Pháp Sư
class Mage(Hero):
    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")

# Lớp con 2: Sát Thủ (Đã sửa lỗi bằng cách ghi đè hàm đúng)
class Assassin(Hero):
    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")

# --- KỊCH BẢN TRẬN ĐẤU ---
print("--- LOADING TRẬN ĐẤU ---")
team_heroes = [Mage(), Assassin()] 
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
for hero in team_heroes:
    hero.use_ultimate()