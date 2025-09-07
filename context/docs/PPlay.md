## Tree for PPlay
```
├── mouse.py
├── collision.py
├── __init__.py
├── animation.py
├── sound.py
├── sprite.py
├── gameimage.py
├── point.py
├── keyboard.py
├── gameobject.py
└── window.py
```

## File: mouse.py
```python
# coding= utf-8

import pygame
from pygame.locals import *
from .point import *

# -*- coding: utf-8 -*-

# Initializes pygame's modules
pygame.init()

class Mouse():
    def __init__(self):
        self.BUTTON_LEFT = 1
        self.BUTTON_MIDDLE = 2
        self.BUTTON_RIGHT = 3
        self.WHEEL_UP = 4
        self.WHEEL_DOWN = 5
        
        self.visibility = True

    """Returns the mouse position."""
    def get_position(self):
        return pygame.mouse.get_pos()

    """Defines the mouse's new position."""
    def set_position(self, x, y):
        pygame.mouse.set_pos([x,y])

    """Hides the mouse."""
    def hide(self):
        pygame.mouse.set_visible(False)
        self.visibility = False

    """Unhides the mouse."""
    def unhide(self):
        pygame.mouse.set_visible(True)
        self.visibility = True

    """Return if the mouse is currently visible or not."""
    def is_visible(self):
        return self.visibility

    """
    Returns True or False if the respective button was pressed.
    BUTTON_LEFT = 1
    BUTTON_MIDDLE = 2
    BUTTON_RIGHT = 3
    WHEEL_UP = 4
    WHEEL_DOWN = 5
    """
    def is_button_pressed(self, button):
        pressed_buttons = pygame.mouse.get_pressed()
        if(pressed_buttons[button-1] == 1):
            return True
        else:
            return False            

    """Returns a boolean if the mouse is over an area."""
    def is_over_area(self, start_point, end_point):
        mouse_pos = self.get_position()
        mouse_point = Point(mouse_pos[0], mouse_pos[1])
        start_point = Point(start_point[0], start_point[1])
        end_point = Point(end_point[0], end_point[1])
        
        if((mouse_point.x < start_point.x) or
           (mouse_point.y < start_point.y) or
           (mouse_point.x > end_point.x) or
           (mouse_point.y > end_point.y)):
            return False
        else:
            return True
        
    """Returns if the mouse is over a game_object."""
    def is_over_object(self, game_object):
        return self.is_over_area([game_object.x, game_object.y],
                            [game_object.x + game_object.width,
                             game_object.y + game_object.height])

    """Returns a boolean if the mouse is over the game screen."""
    def is_on_screen(self):
        return pygame.mouse.get_focused()

    """Returns a boolean if the mouse is NOT over the game screen."""
    def is_off_screen(self):
        return (not pygame.mouse.get_focused())

    """
    Returns the amount of mouse relative-movement since
    the previous call to this function.
    """
    def delta_movement(self):
        return pygame.mouse.get_rel()

    # Mouse drag?
```
## File: collision.py
```python
# coding= utf-8

# Modules import
from . import point
import pygame

# -*- coding: utf-8 -*-

"""A simple class to deal with basic collision methods"""
"""
Must note that the collision is inclusive, i.e.,
occurs when one enters the other effectively,
not only when over the same position of the edge.
"""
class Collision():
    """
    minN: the Point of the top left of the N rect
    maxN: the Point of the bottom right of the N rect
    """
    @classmethod
    def collided_rect(cls, min1, max1, min2, max2):
        if(min1.x >= max2.x or max1.x <= min2.x):
            return False
        if(min1.y >= max2.y or max1.y <= min2.y):
            return False
        return True

    """
    args[0]: the origin GameObject
    args[1]: the target GameObject
    """
    @classmethod
    def collided(cls, *args):
        """
        if(len(args) == 2
        and isinstance(args[0], GameObject)
        and isinstance(args[1], GameObject)):
        """
        game_object1_min = point.Point(args[0].x, args[0].y)
        game_object1_max = point.Point(args[0].x + args[0].width,
                                 args[0].y + args[0].height)

        game_object2_min = point.Point(args[1].x, args[1].y)
        game_object2_max = point.Point(args[1].x + args[1].width,
                                 args[1].y + args[1].height)

        return (Collision.collided_rect(game_object1_min, game_object1_max,
                                        game_object2_min, game_object2_max))

    """
    Perfect-pixel collision using masks.
    """
    @classmethod
    def perfect_collision(cls, gameimage1, gameimage2):
        """
        Both objects must extend a GameImage, 
        since it has the pygame.mask and pygame.Rect
        """
        offset_x = (gameimage2.rect.left - gameimage1.rect.left)
        offset_y = (gameimage2.rect.top - gameimage1.rect.top)
        
        mask_1 = pygame.mask.from_surface(gameimage1.image)
        mask_2 = pygame.mask.from_surface(gameimage2.image)
        
        if(mask_1.overlap(mask_2, (offset_x, offset_y)) != None):
            return True
        return False

    """
    Perfect collision aux - is called by GameImage
    """
    @classmethod
    def collided_perfect(cls, gameimage1, gameimage2):
        return (Collision.perfect_collision(gameimage1, gameimage2))
```
## File: __init__.py
```python
__all__ =   [
            "animation",
            "collision",
            "gameimage",
            "gameobject",
            "keyboard",
            #"mouse",
            "point",
            #"sound",
            "sprite",
            "window"
            ]
```
## File: animation.py
```python
# coding= utf-8

# Pygame and System Modules
import sys
import time
import pygame
from . import window
from . import gameimage
from pygame.locals import *

# Initializes pygame's modules
pygame.init()

"""An Animation class for frame-control."""
class Animation(gameimage.GameImage):
    """
    Creates an Animation that is composed by N frames.
    The method set_sequence_time must be called right after.
    Must note that the nnumber of frames will be automatically
    computated: if the image has 100px width and total_frames = 10,
    each frame will have 10px width.
    """
    def __init__(self, image_file, total_frames, loop=True):
        # Parent's constructor must be first-called
        gameimage.GameImage.__init__(self, image_file)

        # A Cast to force it to be a float division
        self.width = self.width/float(total_frames)  # The width of each frame
        self.height = self.height

        # Playing Control
        self.playing = True
        self.drawable = True
        self.loop = loop

        self.total_frames = total_frames
        self.initial_frame = 0
        self.curr_frame = 0
        self.final_frame = total_frames

        # The duration of each frame
        self.frame_duration = []
        self.total_duration = 0

        # The actual time in ms
        self.last_time = int(round(time.time() * 1000))

        self.set_sequence(0, self.total_frames, self.loop)

        
    #-----------------------SEQUENCE SETTERS-----------------
    """
    Sets some aspects of the sequence, init/final frame, loop..
    """
    def set_sequence(self, initial_frame, final_frame, loop=True):
        self.set_initial_frame(initial_frame)
        self.set_curr_frame(initial_frame)
        self.set_final_frame(final_frame)
        self.set_loop(loop)

    """Defines each frame duration and the sequence (time / total_frames)."""
    def set_sequence_time(self, initial_frame, final_frame,
                          total_duration, loop=True):
        self.set_sequence(initial_frame, final_frame, loop)
        time_ms = int(round(total_duration / float(final_frame - initial_frame + 1)))
        for x in range(initial_frame, final_frame):
            self.frame_duration.append(total_duration)

    """Sets the time for all frames."""
    def set_total_duration(self, time_ms):
        time_frame = float(time_ms) / self.total_frames
        self.total_duration = time_frame * self.total_frames
        for x in range(0, self.total_frames):
            self.frame_duration.append(time_frame)

    #-----------------------DRAW&UPDATE METHODS--------------------
    """Method responsible for performing the change of frames."""
    def update(self):
        if(self.playing):
            time_ms = int(round(time.time() * 1000)) #gets the curr time in ms
            if((time_ms - self.last_time > self.frame_duration[self.curr_frame])
               and (self.final_frame != 0)):
                self.curr_frame += 1
                self.last_time = time_ms
            if((self.curr_frame == self.final_frame) and (self.loop)):
                self.curr_frame = self.initial_frame
            else:
                if((not self.loop) and (self.curr_frame + 1 >= self.final_frame)):
                    self.curr_frame = self.final_frame - 1
                    self.playing = False
            
    """Draws the current frame on the screen."""
    def draw(self):
        if(self.drawable):
            # Clips the frame (rect on the image)
            clip_rect = pygame.Rect(self.curr_frame*self.width,
                                    0,
                                    self.width,
                                    self.height
                                    )

            # Updates the pygame rect based on new positions values
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

            # Blits the image with the rect and clip_rect clipped
            window.Window.get_screen().blit(self.image, self.rect, area=clip_rect)
        
    
    #----------------------PLAYING CONTROL METHODS----------------------
    """Stops execution and puts the initial frame as the current frame."""
    def stop(self):
        self.curr_frame = self.initial_frame
        self.playing = False

    """Method responsible for starting the execution of the animation."""
    def play(self):
        self.playing = True

    """Method responsible fo pausing the Animation."""
    def pause(self):
        self.playing = False
        
    """Returns true if the Animation is being executed."""
    def is_playing(self):
        return self.playing

    """Returns if the Animation is looping."""
    def is_looping(self):
        return self.loop

    """Sets if the Animation will loop or not."""
    def set_loop(self, loop):
        self.loop = loop

    """Does not allow the Animation to be drawn on the screen."""
    def hide(self):
        self.drawable = False

    """Allows the Animation to be drawn on the screen."""
    def unhide(self):
        self.drawable = True

    #----------------GETTER&SETTER METHODS----------------       
    """Gets the total duration - sum of all time frames."""
    def get_total_duration(self):
        return self.total_duration
    
    """Sets the initial frame of the sequence of frames."""
    def set_initial_frame(self, frame):
        self.initial_frame = frame

    """Returns the initial frame of the sequence."""
    def get_initial_frame(self):
        return self.initial_frame

    """Sets the final frame of the sequence of frames."""
    def set_final_frame(self, frame):
        self.final_frame = frame

    """Returns the number of final frame of the sequence."""
    def get_final_frame(self):
        return self.final_frame

    """Sets the current frame that will be drawn."""
    def set_curr_frame(self, frame):
        self.curr_frame = frame

    """Gets the current frame that will be drawn."""
    def get_curr_frame(self):
        return self.curr_frame
```
## File: sound.py
```python
# coding= utf-8

import pygame
import pygame.mixer

# Initizalizes pygame's modules
"""Sound é uma classe de controle dos sons do jogo - efeitos, música"""
class Sound():
    """ATENÇÃO! O arquivo passado deve ser .OGG!!! Se não pode gerar problemas."""
    def __init__(self, sound_file):
        self.loop = False
        self.sound_file = sound_file
        self.volume = 50
        self.sound = pygame.mixer.Sound(sound_file)
        self.set_volume(self.volume)

        # To reduce audio delay
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

    def load(self, sound_file):
        if(pygame.mixer):
            return pygame.mixer.Sound(sound_file)

    """Value deve ser um valor entre 0 e 100"""
    def set_volume(self, value):
        if(value >= 100):
            value = 100
        if(value <= 0):
            value = 0

        self.volume = value
        self.sound.set_volume(float(value)/100)

    def increase_volume(self, value):
        self.set_volume(self.volume + value)

    def decrease_volume(self, value):
        self.set_volume(self.volume - value)

    def is_playing(self):
        if(pygame.mixer.get_busy()):
            return True
        else:
            return False

    def pause(self):
        pygame.mixer.pause()

    def unpause(self):
        pygame.mixer.unpause()

    def play(self):
        if(self.loop):
            self.sound.play(-1)
        else:
            self.sound.play()

    def stop(self):
        self.sound.stop()

    def set_repeat(self, repeat):
        self.loop = repeat

    def fadeout(self, time_ms):
       self.sound.fadeout(time_ms)
```
## File: sprite.py
```python
# coding= utf-8

# Modules
import sys
import time
import pygame
from . import window
from . import animation
from pygame.locals import *

# Initializes pygame's modules
pygame.init()

"""Sprite é uma animação que pode ser movida por input, é o "ator" do jogo"""
class Sprite(animation.Animation):
    """
    Caso seja dado apenas o nome da imagem, será criada uma Animation
    com 1 frame apenas.
    """
    def __init__(self, image_file, frames=1):
        # Parent's constructor must be first-called
        animation.Animation.__init__(self, image_file, frames)

    """Permite a movimentação com o teclado no eixo X"""
    def move_key_x(self, speed):
        if(window.Window.get_keyboard().key_pressed("left")):
            self.set_position(self.x - speed, self.y)
            
        if(window.Window.get_keyboard().key_pressed("right")):
            self.set_position(self.x + speed, self.y)

    """Permite a movimentação com o telado no eixo Y"""
    def move_key_y(self, speed):
        if(window.Window.get_keyboard().key_pressed("up")):
            self.set_position(self.x, self.y - speed)
            
        if(window.Window.get_keyboard().key_pressed("down")):
            self.set_position(self.x, self.y + speed)

    """Move o Sprite no eixo X (sem input)"""
    def move_x(self, speed):
        self.x += speed
        self.set_position(self.x, self.y)

    """Move o Sprite no eixo Y (sem input)"""
    def move_y(self, speed):
        self.y += speed
        self.set_position(self.x, self.y)
```
## File: gameimage.py
```python
# Pygame and system modules
import sys
import pygame
from pygame.locals import *
from . import window
from . import gameobject

# Initializes pygame's modules
pygame.init()

# Loads an image (with colorkey and alpha)
def load_image(name, colorkey=None, alpha=False):
    """loads an image into memory"""
    image = pygame.image.load(name)
    if alpha:image = image.convert_alpha()
    else:image=image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
        
"""GameImage is the base class to deal with images"""
class GameImage(gameobject.GameObject):
    """
    Creates a GameImage from the specified file.
    The width and height are obtained based on the image file.
    """
    def __init__(self, image_file):
        # Parent constructor must be called first
        gameobject.GameObject.__init__(self)
        
        # Loads image from the source, converts to fast-blitting format
        self.image = pygame.image.load(image_file).convert_alpha()
        # Gets the image pygame.Rect
        self.rect = self.image.get_rect()
        
        # Size
        self.width = self.rect.width
        self.height = self.rect.height

        
        

    """Draws the image on the screen"""
    def draw(self):
        # A instance of the Window screen
        # Window object must've been instatiated
        # draw_rect is necessary to readjust the image position given .x and .y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        window.Window.get_screen().blit(self.image, self.rect)

    """Sets the (X,Y) image position on the screen"""
    def set_position(self, x, y):
        self.x = x
        self.y = y

    """Checks collision with hitmask"""
    def collided_perfect(self, target):
        # Module import
        from . import collision

        return collision.Collision.collided_perfect(self, target)
```
## File: point.py
```python
# coding= utf-8

"""A Point class"""
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
```
## File: keyboard.py
```python
# coding= utf-8

import pygame
from pygame.locals import *

# Initializes pygame's modules
pygame.init()

class Keyboard():
    """
    Returns True if the key IS pressed, it means
    the press-check occurs every frame
    """
    def key_pressed(self, key):
        key = self.to_pattern(key)
        keys = pygame.key.get_pressed()
        if(keys[key]):
            return True

        return False
    
    """Shows the int code of the key"""
    def show_key_pressed(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                print(event.key)
                
    def to_pattern(self, key):
        if((key=="LEFT") or (key=="left")):
            return pygame.K_LEFT
        elif((key=="RIGHT") or (key=="right")):
            return pygame.K_RIGHT
        elif((key=="UP") or (key=="up")):
            return pygame.K_UP
        elif((key=="DOWN") or (key=="down")):
            return pygame.K_DOWN
        elif((key=="ENTER") or (key=="enter") or
             (key=="RETURN") or (key=="return")):
            return pygame.K_RETURN
        elif((key=="ESCAPE") or (key=="escape") or
             (key=="ESC") or (key=="esc")):
            return pygame.K_ESCAPE
        elif((key=="SPACE") or (key=="space")):
            return pygame.K_SPACE
        elif((key=="LEFT_CONTROL") or (key=="left_control")):
            return pygame.K_LCTRL
        elif((key=="LEFT_SHIFT") or (key=="left_shift")):
            return pygame.K_LSHIFT
        elif(((key >= "A") and (key <= "Z")) or
             ((key  >= "a") and (key <= "z"))):
            return getattr(pygame, "K_" + key.lower())
        elif((key >= "0") and (key <= "9")):
            return getattr(pygame, "K_" + key)
        return key
```
## File: gameobject.py
```python
# coding= utf-8

"""The most basic game class"""
class GameObject():
    """Creates a GameObject in X, Y co-ords, with Width x Height"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0


    def collided(self, obj):
        # Module import
        from . import collision

        return collision.Collision.collided(self, obj)

    def load_sound(self, sound_file):
        # Module import
        from . import sound

        self.sound = sound.Sound(sound_file)
```
## File: window.py
```python
# coding= utf-8

# Pygame and system modules
import sys
import pygame
from pygame.locals import *
from . import keyboard
from . import mouse

# Initializes pygame's modules
pygame.init()
    
"""A simple Window class, it's the primary Surface(from pygame).
All the other game's renderable objects will be drawn on it. """
class Window():
    #A class attribute in Python, this case is similar to Java statics
    screen = None
    
    """Initialize a Window (width x height)"""
    def __init__(self, width, height):
        # Input controllers
        Window.keyboard = keyboard.Keyboard()
        Window.mouse = mouse.Mouse()
        
        # Size
        self.width = width
        self.height = height

        # Pattern color
        self.color = [0,0,0]  # Black

        # Pattern Title
        self.title = "Title"

        # Time Control
        self.curr_time = 0  # current frame time
        self.last_time = 0  # last frame time 
        self.total_time = 0  # += curr-last(delta_time), update()

        # Creates the screen (pygame.Surface)
        # There are some useful flags (look pygame's docs)
        # It's like a static attribute in Java
        Window.screen = pygame.display.set_mode([self.width, self.height])
        # ? Why is it possible to do w.screen?

        # Sets pattern starting conditions
        self.set_background_color(self.color)
        self.set_title(self.title)

        # Updates the entire screen if no arguments are passed
        # Can be used to update portions of the screen (Rect list)
        pygame.display.update()

#------------------------TODO - VIDEO RESIZE METHODS----------------------
    """Not implemented yet - Sets the Window to Fullscreen"""
    # Unfortunately, it must save the old screen (buffer) and
    # blit (transfer, see pygame doc) to the new FSCREEN
    def set_fullscreen(self): pass
    # TODO

    """Not implemented yet - Disable the full display mode"""
    # Yeah.. guess what..
    def restoreScreen(self): pass
    # TODO

    """Not implemented yet - Sets the Window resolution"""
    # The same problem as fullscreen
    def set_resolution(self, width, height): pass
    # TODO
    
#-----------------------CONTROL METHODS---------------------------
    """Refreshes the Window - makes changes visible, AND updates the Time"""
    def update(self):
        pygame.display.update()  # refresh
        
        for event in pygame.event.get():  # necessary to not get errors
            if event.type==QUIT:
                self.close()
        self.last_time = self.curr_time  # set last frame time
        self.curr_time = pygame.time.get_ticks()  # since pygame.init()  
        self.total_time += (self.curr_time - self.last_time)  # == curr_time
        # curr_time should be the REAL current time, but in Python
        # the method returns the time in seconds.
        # And we DO WANT MILLIseconds :P
        # While REAL time is not necessary, yet..

    """Paints the screen - White - and update"""
    def clear(self):
        self.set_background_color([255,255,255])
        self.update()

    """
    Closes the Window and stops the program - throws an exception
    """
    def close(self):
        pygame.quit()
        sys.exit()
        
#---------------------GETTERS AND SETTERS METHODS-----------------
    """
    Changes background color - receives a vector [R, G, B] value
    Example: set_background_color([0,0,0]) -> black
    or set_background_color([255,255,255]) -> white
    """
    def set_background_color(self, RGB):
        self.color = RGB
        Window.screen.fill(self.color)
    # !Implement later possible strings values, such as:
    # "red","green","blue"..!

    """Gets the color attribute (background)"""
    def get_background_color(self):
        return self.color

    """Sets the title of the Window"""
    def set_title(self, title):
        self.title = title
        pygame.display.set_caption(title)

    """Gets the title of the Window"""
    def get_title(self):
        return self.title

#----------------------TIME CONTROL METHODS--------------------------
        
    """Pause the program for an amount of time - milliseconds"""
    # Uses the processor to make delay accurate instead of
    # pygame.time.wait that SLEEPS the proccess
    def delay(self, time_ms):
        pygame.time.delay(time_ms)

    """
    Returns the time passed between
    the last and the current frame - SECONDS
    """
    def delta_time(self):
        return (self.curr_time - self.last_time)/1000.0

    """Returns the total time passed since the Window was created"""
    def time_elapsed(self):
        return self.total_time

#------------------------DRAW METHODS-------------------------------
    """
    Draw a text on the screen at X and Y co-ords, using [R, G, B] color
    [with the specified font,
           [with the specified size,
                   [Bold,
                         [Italic]]]]
    """
    def draw_text(self, text, x, y, size=12, color=(0,0,0),
                 font_name="Arial", bold=False, italic=False):
        # Creates a Font from the system fonts
        # SysFont(name, size, bold=False, italic=False) -> Font
        font = pygame.font.SysFont(font_name, size, bold, italic)

        # Creates a pygame.Surface with the text rendered on it
        # render(text, antialias, color, background=None)->Surface
        font_surface = font.render(text, True, color)
        # That's because pygame does NOT provide a way
        # to directly draw text on an existing Surface.
        # So you must use Font.render() -> Surface and BLIT
        
        # Finally! BLIT!
        self.screen.blit(font_surface, [x, y])

#---------------------CLASS METHODS--------------------------
    """Returns the drawing surface"""
    @classmethod
    def get_screen(cls):
        return cls.screen

    """Returns the keyboard input"""
    @classmethod
    def get_keyboard(cls):
        return cls.keyboard

    """Returns the mouse input"""
    @classmethod
    def get_mouse(cls):
        return cls.mouse
```
