self.in_start_screen = True

def draw_start_screen(self):
    self.screen.fill(self.black)

    font = pygame.font.SysFont(None, 48)
    title_text = font.render("Welcome to TurnBase!", True, self.white)
    prompt_text = font.render("Press SPACE to start", True, self.white)

    title_rect = title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 40))
    prompt_rect = prompt_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 40))

    self.screen.blit(title_text, title_rect)
    self.screen.blit(prompt_text, prompt_rect)

    pygame.display.flip()

def run(self):
    """Main game loop."""
    while self.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if self.in_start_screen and event.key == pygame.K_SPACE:
                    self.in_start_screen = False

        if self.in_start_screen:
            self.draw_start_screen()
        else:
            self.screen.fill(self.black)
            self.draw_connections()
            self.draw_circles()
            pygame.display.flip()

    pygame.quit()
