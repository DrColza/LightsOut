"""
    Example program to show using an array to back a grid on-screen.

    Sample Python/Pygame Programs
    Simpson College Computer Science
    http://programarcadegames.com/
    http://simpson.edu/computer-science/

    Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import src.levels as levels


class LightsOut:
    GREY = "#757575"
    WHITE = (255, 255, 255)
    PINK = "#d582e0"
    RED = (255, 0, 0)  # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 50
    HEIGHT = 50
    MARGIN = 5
    grid = []
    GRID_SIZE = 5

    def __init__(self):
        self.level = 1
        self.grid = levels.STARTING_MATRIX[self.level]
        pygame.init()
        pygame.display.set_caption("Lights Out")
        WINDOW_SIZE = [280, 280]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.screen.fill(self.GREY)
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.start_game()

    def handle_button_click(self, row, col):
        self.toggle_all_adjacent_buttons(row, col)

    def toggle_all_adjacent_buttons(self, row, col):
        self.toggle_button(row, col)
        self.toggle_button(row - 1, col)
        self.toggle_button(row + 1, col)
        self.toggle_button(row, col - 1)
        self.toggle_button(row, col + 1)

    def toggle_button(self, row, col):
        out_of_bounds = self.check_if_coords_is_out_of_bounds(row, col)
        if out_of_bounds:
            return

        self.grid[row][col] = 1 if self.grid[row][col] == 0 else 0

    def check_if_coords_is_out_of_bounds(self, row, col):
        return (
            row < 0
            or row > (self.GRID_SIZE - 1)
            or col < 0
            or col > (self.GRID_SIZE - 1)
        )

    def go_to_next_level_if_board_is_clear(self):
        if self.grid != levels.STARTING_MATRIX[0]:
            return
        self.level += 1
        self.grid = levels.STARTING_MATRIX[self.level]

    def start_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (self.WIDTH + self.MARGIN)
                    row = pos[1] // (self.HEIGHT + self.MARGIN)

                    self.handle_button_click(row, column)
                    self.go_to_next_level_if_board_is_clear()

            self.draw_the_grid()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()

    def check_board_for_level_completion(self):
        board_has_been_cleared = self.grid == levels.STARTING_MATRIX[0]
        return board_has_been_cleared

    def draw_the_grid(self):
        for row in range(5):
            for column in range(5):
                color = self.WHITE
                if self.grid[row][column] == 1:
                    color = self.PINK
                pygame.draw.rect(
                    self.screen,
                    color,
                    [
                        (self.MARGIN + self.WIDTH) * column + self.MARGIN,
                        (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                        self.WIDTH,
                        self.HEIGHT,
                    ],
                )
        pygame.display.flip()
