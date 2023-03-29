import pygame
import os
pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")

music_dir = "C:\\VScode_programs\\Python\\lib\\tsis7\\music_folder"
music_files = os.listdir(music_dir)
current_track_index = 0

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))

def play_track():
    pygame.mixer.music.play()

def pause_track():
    pygame.mixer.music.pause()

def stop_track():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))
    pygame.mixer.music.play()

def prev_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))
    pygame.mixer.music.play()

def increase_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 1.0:
        pygame.mixer.music.set_volume(current_volume + 0.1)

def decrease_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume > 0.0:
        pygame.mixer.music.set_volume(current_volume - 0.1)

font = pygame.font.SysFont("Arial", 24)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pause_track()
                else:
                    play_track()
            elif event.key == pygame.K_s:
                stop_track()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()
            elif event.key == pygame.K_UP:
                increase_volume()
            elif event.key == pygame.K_DOWN:
                decrease_volume()
    screen.fill((255, 255, 255))
    current_track_name = music_files[current_track_index]
    current_volume = round(pygame.mixer.music.get_volume(), 2)
    track_label = font.render("Track: " + current_track_name, True, (0, 0, 0))
    volume_label = font.render("Volume: " + str(current_volume), True, (0, 0, 0))
    screen.blit(track_label, (10, 10))
    screen.blit(volume_label, (10, 40))
    pygame.display.update()