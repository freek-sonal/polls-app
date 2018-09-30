from moviepy.editor import VideoFileClip
import pygame
import tkinter

pygame.display.set_caption('My video!')

clip = VideoFileClip('hey.mp4')
clip.preview()


# root.update()
pygame.quit()
