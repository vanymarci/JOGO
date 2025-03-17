import pygame
import sys
from datetime import datetime

from pygame import Surface, Rect, KEYDOWN, K_BACKSPACE, K_RETURN, K_ESCAPE
from pygame import font
from util.DBProxy import DBProxy

from util.Const import COLOR_BLUE, SCORE_POS, MENU_OPTION, COLOR_WHITE

class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode=str, player_score=list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(text_size= 48, text='YOU WIN!!!', text_color=COLOR_BLUE, text_pos=SCORE_POS['Title'])
            text = 'Enter your name (4 characters):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            self.score_text(text_size= 20, text=text, text_color=COLOR_WHITE, text_pos=SCORE_POS['EnterName'])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name':name,'score':score,'date':get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1] 
                    else:
                        if len(name) < 4:
                            name += event.unicode
            
            self.score_text(text_size= 20, text=name, text_color=COLOR_WHITE, text_pos=SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(text_size= 48, text='TOP 10 SCORE', text_color=COLOR_BLUE, text_pos=SCORE_POS['Title'])
        self.score_text(text_size= 20, text='NAME       SCORE       DATE      ', text_color=COLOR_BLUE, text_pos=SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(text_size= 20, text=f'    {name}          {score:04d}          {date}', text_color=COLOR_WHITE, text_pos=SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size= int, text= str, text_color= tuple, text_pos= tuple):
        text_font: font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"