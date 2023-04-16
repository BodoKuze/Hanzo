from label import Text
import os
import pygame
from sound import Sound_Effect

class Title:
    def __init__(self,master,yes,up,down) -> None:
        
        self.music_playing = True

        self.courser_x = 0
        self.master = master
        self.inputs = [yes,up,down]
        self.buffer_input = 0
        self.font_path = fr"{os.getcwd()}\font\EndlessBossBattleRegular-v7Ey.ttf"

        self.music_track = 0

        self.courser = Text(master,self.font_path,30,">",290,300,700,300,(255,255,255))
        self.title1 = Text(master,self.font_path,100,"Hanzo",240,100,700,300,(255,255,255))
        self.title2 = Text(master,self.font_path,30,"beta ver.",320,200,700,300,(255,255,255))
        self.music = Text(master,self.font_path,30,"music :",315,300,700,300,(255,255,255))
        self.music2 = Text(master,self.font_path,30,"on",435,300,700,300,(255,255,255))
        self.track = Text(master,self.font_path,30,"track :",315,350,700,300,(255,255,255))
        self.track2 = Text(master,self.font_path,30,"A",435,350,700,300,(255,255,255))
        self.start_game = Text(master,self.font_path,30,"start",315,400,700,300,(255,255,255))
        
        self.arrow_sfx = Sound_Effect("menu")
        self.start_game_sfx = Sound_Effect("start_game")



        self.start = False


    def buffer(self):
        if 0 < self.buffer_input < 10:
            self.buffer_input += 1
        else:
            self.buffer_input = 0



    def update(self,dt):
        
        self.buffer()

        keys = pygame.key.get_pressed()

        if keys[self.inputs[0]] and self.buffer_input == 0:
            self.arrow_sfx.play()
            self.buffer_input = 1
            match self.courser_x :

                case 0:
                    self.music_playing = not self.music_playing

                case 1:
                    self.music_track += 1
                    if self.music_track > 2:
                        self.music_track = 0

                case 2:
                    self.start_game_sfx.play()
                    self.start = True



        if keys[self.inputs[2]] and self.buffer_input == 0:
            self.buffer_input = 1
            self.courser_x += 1
            self.arrow_sfx.play()
        if keys[self.inputs[1]] and self.buffer_input == 0:
            self.buffer_input = 1
            self.courser_x -= 1
            self.arrow_sfx.play()

        if self.courser_x < 0:
            self.courser_x = 2
        if self.courser_x > 2:
            self.courser_x = 0

        match self.courser_x:
            case 0:
                self.courser = Text(self.master,self.font_path,30,">",290,300,700,300,(255,255,255))
            case 1:
                self.courser = Text(self.master,self.font_path,30,">",290,350,700,300,(255,255,255))
            case 2:
                self.courser = Text(self.master,self.font_path,30,">",290,400,700,300,(255,255,255))



        self.update_app(dt)


    def update_app(self,dt):



        if self.music_playing:
            self.music2.update_text("on",(255,255,255))
        else:
            self.music2.update_text("off",(255,100,45))

        match self.music_track:

            case 0:
                self.track2.update_text("A",(255,255,255))
            case 1:
                self.track2.update_text("B",(255,255,255))
            case 2:
                self.track2.update_text("C",(255,255,255))






        if dt % 5 == 0:
            self.title1.update_text("Hanzo",(255,100,100))
            self.title2.update_text("beta ver.",(255,100,100))
        else:
            self.title1.update_text("Hanzo",(255,255,255))
            self.title2.update_text("beta ver.",(255,255,255))

        


        self.title1.update()
        self.title2.update()
        self.music.update()
        self.music2.update()
        self.track.update()
        self.track2.update()
        self.start_game.update()
        self.courser.update()