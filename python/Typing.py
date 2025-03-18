# import curses
# from curses import wrapper

# def start(stdscr):
#     stdscr.clear()
    
#     stdscr.addstr("Hızlı yazı yazma oyununa hoş geldiniz!", curses.color_pair(3))
#     stdscr.addstr("\nOyunun amacı, size gösterilen kelimeyi en hızlı şekilde yazmaktır.")
#     stdscr.addstr("\nBaşlamak için herhangi bir tuşa basınız.", curses.color_pair(3))
#     stdscr.refresh()
#     stdscr.getkey()

# def displey_txt(stdscr,target,current,wpm=0):
#     stdscr.addstr(target)
#     for i, char in enumerate(current):
#         correct_char=target[i]
#         color=curses.color_pair(1)
#         if char!=correct_char:
#             color=curses.color_pair(2)
#         stdscr.addstr(0,i, char,curses.color_pair(1))

# def wpm(stdscr):
#     target_txt="Bu alan hizli yazmaya çaliştiğim alan olacak."
#     current_txt = []
#     stdscr.clear()
#     stdscr.addstr(target_txt)
#     stdscr.refresh()
#     while True:
#         key = stdscr.getch()
#         current_txt.append(chr(key))
#         stdscr.clear()
#         stdscr.addstr(target_txt)
#         stdscr.refresh()
#         for char in current_txt:
#             stdscr.addstr(char,curses.color_pair(1))
#         stdscr.refresh()
#         key=stdscr.getch()
#         if key==27:
#             break
#         elif key==263 or key==8 or key==127:
#             if len(current_txt)>0:
#                 current_txt.pop()
#         else:
#             current_txt.append(chr(key))


# def main(stdscr):
#     curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
#     curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
#     curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
#     start(stdscr)
#     wpm(stdscr)
  
    
# wrapper(main)


import curses  
from curses import wrapper  
import time  

def start(stdscr):  
    stdscr.clear()  
    
    stdscr.addstr("Hızlı yazı yazma oyununa hoş geldiniz!", curses.color_pair(3))  
    stdscr.addstr("\nOyunun amacı, size gösterilen kelimeyi en hızlı şekilde yazmaktır.")  
    stdscr.addstr("\nBaşlamak için herhangi bir tuşa basınız.", curses.color_pair(3))  
    stdscr.refresh()  
    stdscr.getkey()  

def display_txt(stdscr, target, current, elapsed_time):  
    stdscr.clear()  
    stdscr.addstr(target)  # Hedef metin  
    stdscr.addstr(1, 0, f"Süre: {elapsed_time:.2f} saniye")  # Süreyi göster  

    # Mevcut metni Hedef metnin üzerine yazma  
    for i, char in enumerate(current):  
        correct_char = target[i]  
        if char == correct_char:  
            stdscr.addstr(0, i, char, curses.color_pair(1))  
        else:  
            stdscr.addstr(0, i, char, curses.color_pair(2))  
    
    stdscr.refresh()  

def wpm(stdscr):  
    target_txt = "Bu alan hızlı yazmaya çalıştığım alan olacak."  
    current_txt = []  
    stdscr.clear()  
    stdscr.addstr(target_txt)  
    stdscr.refresh()  

    start_time = None  # Süreyi başlatma zamanına dair başlangıç noktası  
    while True:  
        key = stdscr.getch()  
        
        if key == 27:  # ESC tuşu  
            break  
        elif key in (263, 8, 127):  # Backspace tuşları  
            if current_txt:  
                current_txt.pop()  
        elif key == 10:  # Enter tuşu (yazmayı bitir)  
            if start_time is not None:  
                elapsed_time = time.time() - start_time  # Geçen süre hesaplama  
                word_count = len(''.join(current_txt).split())  # Yazılan kelime sayısını hesaplama  
                wpm = (word_count / elapsed_time) * 60 if elapsed_time > 0 else 0  # Dakikadaki kelime sayısını hesaplama  
                stdscr.addstr(3, 0, f"Yazma süreniz: {elapsed_time:.2f} saniye")  
                stdscr.addstr(4, 0, f"Dakikada yazdığınız kelime sayısı: {wpm:.2f} kelime.")  
                stdscr.addstr(5, 0, "Devam etmek için herhangi bir tuşa basın...")  
                stdscr.refresh()  
                stdscr.getkey()  # Kullanıcının devam etmesini bekle  
                break  
        else:  
            if start_time is None:  
                start_time = time.time()  # Süreyi başlatma  
            current_txt.append(chr(key))  
        
        # Güncel süreyi göster  
        if start_time is not None:  
            elapsed_time = time.time() - start_time  
            display_txt(stdscr, target_txt, current_txt, elapsed_time)  

def main(stdscr):  
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  
    start(stdscr)  
    wpm(stdscr)  

wrapper(main)  