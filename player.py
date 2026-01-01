import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, deltatime):
        self.rotation += (deltatime * PLAYER_TURN_SPEED)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

    def move(self, delta_time):
        unit_verctor = pygame.Vector2(0, 1)
        rotate_vector = unit_verctor.rotate(self.rotation)
        rotated_with_speed_vector = rotate_vector * PLAYER_SPEED * delta_time
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        if self.shoot_cooldown > 0:
            # I don't know shit.
            pass
        else:
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1)
            shot.velocity =  shot.velocity.rotate(self.rotation)
            shot.velocity *= PLAYER_SHOOT_SPEED
       