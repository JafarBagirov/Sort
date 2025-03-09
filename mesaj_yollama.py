import pyautogui
import time

message = input('Mesajı daxil et: ')

# İstədiyiniz sayda mesaj göndərmək üçün dövr
num_messages = int(input('Neçə dəfə mesaj göndərmək istəyirsiniz?: '))

# WhatsApp Web-ə daxil olun və mesajın yazılacağı yeri müəyyən edin

for _ in range(num_messages):
    # Mesajı yaz
    pyautogui.write(message)
    
    # Mesajı göndərmək üçün enter düyməsinə bas
    pyautogui.press('enter')
    
    # Hər bir mesaj arasında az bir gecikmə əlavə et ki, WhatsApp Web səhifəsi işləsin
    time.sleep(0.1)  # 2 saniyə gözləyir
