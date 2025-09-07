# token_animator.py

"""
This file defines the TokenAnimator class, which is responsible for animating
a player's token sprite from a starting board position to an ending position.
It calculates the path and moves the token incrementally each frame.
"""

import math
from pplay.sprite import Sprite
from typing import List, Tuple

class TokenAnimator:
    """
    Manages the smooth movement animation of a single token sprite.
    """
    def __init__(self,
                 sprite: Sprite,
                 start_pos_idx: int,
                 end_pos_idx: int,
                 space_coords: List[Tuple[int, int]],
                 speed: float = 200.0):
        """
        Initializes the animator.

        Args:
            sprite (Sprite): The token sprite to be animated.
            start_pos_idx (int): The starting board space index.
            end_pos_idx (int): The ending board space index.
            space_coords (List[Tuple[int, int]]): A list of all space coordinates.
            speed (float): The speed of the token in pixels per second.
        """
        self.sprite = sprite
        self.space_coords = space_coords
        self.speed = speed
        self.is_finished = False

        self.path = self._calculate_path(start_pos_idx, end_pos_idx)
        self.target_node_idx = 0
        self._set_next_target()

    def _calculate_path(self, start_idx: int, end_idx: int) -> List[Tuple[int, int]]:
        """Calculates the sequence of coordinates the token must travel through."""
        path_coords = []
        current_idx = start_idx
        while current_idx != end_idx:
            current_idx = (current_idx + 1) % len(self.space_coords)
            path_coords.append(self.space_coords[current_idx])
        
        # If the list is empty, it means we are not moving
        if not path_coords:
            path_coords.append(self.space_coords[start_idx])

        return path_coords

    def _set_next_target(self):
        """Sets the next coordinate in the path as the current target."""
        if self.target_node_idx >= len(self.path):
            self.is_finished = True
            return

        self.target_x, self.target_y = self.path[self.target_node_idx]
        self.target_node_idx += 1

    def update(self, delta_time: float):
        """
        Updates the token's position. This should be called every frame.

        Args:
            delta_time (float): The time elapsed since the last frame.
        """
        if self.is_finished:
            return

        # Calculate vector towards target
        dx = self.target_x - self.sprite.x
        dy = self.target_y - self.sprite.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < 1.0:
            # Reached the target node, set the next one
            self.sprite.set_position(self.target_x, self.target_y)
            self._set_next_target()
            return

        # Move sprite towards target
        move_dist = self.speed * delta_time
        if move_dist > distance:
            move_dist = distance

        self.sprite.x += (dx / distance) * move_dist
        self.sprite.y += (dy / distance) * move_dist
