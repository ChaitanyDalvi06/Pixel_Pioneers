import pygame
import sys

# Define some constants
from classes.constants import WIDTH, HEIGHT, BLACK, WHITE, RED
GREY = (200, 200, 200)
GOLD = (255, 215, 0)

# Organize items by category
ITEMS = {
    "Skins": [
        {"image": "images/PurplePlayer.png", "name": "Purple Skin", "price": 5000},
        {"image": "images/YellowPlayer.png", "name": "Yellow Skin", "price": 4500},
        {"image": "images/GreenPlayer.png", "name": "Green Model", "price": 4000},
        {"image": "images/BluePlayer.png", "name": "Blue Model", "price": 3000},
    ],
    "Skills": [
        {"image": "images/shield1.png", "name": "Shield", "price": 5000},
        {"image": "images/Boost.png", "name": "Speed Boost", "price": 4500},
    ],
    "Models": [
        {"image": "images/Helicopter.png", "name": "Helicopter", "price": 5000},
        {"image": "images/UFO.png", "name": "UFO", "price": 6000},
    ]
}

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shop")

# Load background image
mainmenu_img = pygame.image.load('images/mainmenu.jpg').convert()
mainmenu_img = pygame.transform.scale(mainmenu_img, (WIDTH, HEIGHT))

# Set initial category
selected_category = "Skins"

def draw_shop():
    """Draw the shop UI with categories and items."""
    screen.blit(mainmenu_img, (0, 0))  # Draw background image

    # Draw category buttons
    font = pygame.font.SysFont("Arial", 30)
    categories = list(ITEMS.keys())
    for i, category in enumerate(categories):
        rect = pygame.Rect(20, 100 + i * 100, 250, 50)
        color = BLACK if category != selected_category else RED
        pygame.draw.rect(screen, color, rect, border_radius=10)
        text = font.render(category, True, GREY)
        screen.blit(text, text.get_rect(center=rect.center))

    # Draw items in the selected category
    item_font = pygame.font.SysFont("Arial", 20)
    item_padding = 50  # Padding between items
    start_x, start_y = 300, 150  # Starting coordinates for items
    item_width, item_height = 250, 250  # Width and height of each item box
    
    items = ITEMS[selected_category]  # Get items in the selected category
    for i, item in enumerate(items):
        # Calculate x and y positions with spacing
        x = start_x + (i % 2) * (item_width + item_padding)
        y = start_y + (i // 2) * (item_height + item_padding)
        
        # Draw item box
        rect = pygame.Rect(x, y, item_width, item_height)
        pygame.draw.rect(screen, BLACK, rect, border_radius=10)

        # Load and draw item image
        item_image = pygame.image.load(item["image"]).convert_alpha()
        item_image = pygame.transform.scale(item_image, (150, 150))
        screen.blit(item_image, item_image.get_rect(center=(x + item_width // 2, y + 100)))

        # Display item name
        name_text = item_font.render(item["name"], True, WHITE)
        screen.blit(name_text, (x + 75, y + 200))

        # Display item price
        price_text = item_font.render(f"Buy {item['price']}", True, GOLD)
        screen.blit(price_text, (x + 85, y + 220))

        # Draw the back button
        back_rect = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, RED, back_rect, border_radius=10)
        back_text = font.render("Back", True, WHITE)
        screen.blit(back_text, back_text.get_rect(center=back_rect.center))

    return back_rect

def shop_loop():
    """Main loop for the shop."""
    global selected_category
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Exit the shop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check if category buttons are clicked
                for i, category in enumerate(ITEMS.keys()):
                    if pygame.Rect(20, 100 + i * 100, 150, 50).collidepoint(x, y):
                        selected_category = category  # Change selected category
                # Check if back button is clicked
                if draw_shop().collidepoint(x, y):
                    running = False  # Return to the main menu

        # Draw shop UI
        draw_shop()
        pygame.display.flip()

        clock = pygame.time.Clock()
        clock.tick(60)

# Run the shop loop if this is the main file
if __name__ == "__main__":
    shop_loop()
