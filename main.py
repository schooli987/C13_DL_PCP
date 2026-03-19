import pygame
import random
from emotion_ai import detect_emotion
from game import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emotion Match Game")

background = pygame.image.load("assets/bg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

score = 0
misses = 0

WIN_SCORE = 3
MAX_MISSES = 3

emotions = ['angry','disgust','fear','happy','neutral','sad','surprise']

emoji_images = {
    "angry": pygame.image.load("assets/angry.png"),
    "disgust": pygame.image.load("assets/disgusted.jpg"),
    "fear": pygame.image.load("assets/fear.png"),
    "happy": pygame.image.load("assets/happy.png"),
    "neutral": pygame.image.load("assets/neutral.png"),
    "sad": pygame.image.load("assets/sad.png"),
    "surprise": pygame.image.load("assets/surprise.png")
}

# resize emojis
for key in emoji_images:
    emoji_images[key] = pygame.transform.scale(emoji_images[key], (200,200))

# emoji spinner variables
current_emoji = random.choice(emotions)
spin_timer = 0
stop_timer = 0
spinning = True

running = True

while running:

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    user_emotion = detect_emotion()

    # Fast emoji spinning
    if spinning:

        spin_timer += 1

        if spin_timer % 4 == 0:
            current_emoji = random.choice(emotions)

        if spin_timer > 100:
            spinning = False
            stop_timer = 0

    else:

        stop_timer += 1

        if stop_timer > 90:

            if user_emotion == current_emoji:
                score += 1
            else:
                misses += 1

            spinning = True
            spin_timer = 0

    # draw emoji
    emoji_img = emoji_images[current_emoji]
    screen.blit(emoji_img,(WIDTH//2 - 100, HEIGHT//2 - 100))

    # UI
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text,(20,20))

    emotion_text = font.render(f"Your Emotion: {user_emotion}", True, (255,255,255))
    screen.blit(emotion_text,(20,60))

    miss_text = font.render(f"Misses: {misses}", True, (255,0,0))
    screen.blit(miss_text,(20,100))

    # win condition
    if score >= WIN_SCORE:

        win_text = font.render("YOU WIN!", True, (0,255,0))
        screen.blit(win_text,(WIDTH//2 - 80, HEIGHT//2))

        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    # lose condition
    if misses >= MAX_MISSES:

        lose_text = font.render("GAME OVER", True, (255,0,0))
        screen.blit(lose_text,(WIDTH//2 - 100, HEIGHT//2))

        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()