import pygame
import sys
from classes.constants import WIDTH, HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def music_background():
    pygame.mixer.music.load('game_sounds/background_music.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(loops=-1)


def show_game_over(score):
    font = pygame.font.SysFont('Impact', 50)
    font_small = pygame.font.SysFont('Impact', 30)
    text = font.render("GAME OVER", True, (139, 0, 0))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
    score_text = font_small.render(f"Final Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
    # Button properties
    button_font = pygame.font.SysFont('Impact', 30)
    continue_button_rect = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 80, 200, 50)
    exit_button_rect = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 150, 200, 50)

    # Load Game Over sound
    pygame.mixer.music.load('game_sounds/gameover.mp3')
    pygame.mixer.music.play()

    running = True
    while running:
        screen.blit(text, text_rect)
        screen.blit(score_text, score_rect)

        # Draw buttons
        pygame.draw.rect(screen, (0, 0, 0), continue_button_rect)
        pygame.draw.rect(screen, (0, 0, 0), exit_button_rect)
        continue_text = button_font.render("CONTINUE", True, (255, 255, 255))
        exit_text = button_font.render("EXIT", True, (255, 255, 255))
        screen.blit(continue_text, continue_text.get_rect(center=continue_button_rect.center))
        screen.blit(exit_text, exit_text.get_rect(center=exit_button_rect.center))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if continue_button_rect.collidepoint(x, y):
                    running = False
                    return "continue"  # Restart the game with the same score
                elif exit_button_rect.collidepoint(x, y):
                    running = False
                    return "exit"  # Return to main menu

    # Restart background music after exiting the game over screen
    music_background()
    # screen.blit(text, text_rect)
    # screen.blit(score_text, score_rect)
    # pygame.display.flip()
    # pygame.mixer.music.load('game_sounds/gameover.mp3')
    # pygame.mixer.music.play()
    # pygame.time.delay(4000)
    # music_background()


def show_game_win():
    font = pygame.font.SysFont('Impact', 50)
    text = font.render("AWESOME! GO ON!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.mixer.music.load('game_sounds/win.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(1000)
    music_background()
