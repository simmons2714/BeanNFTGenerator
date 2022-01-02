import numpy as np
from matplotlib import pyplot as plt
import random
from PIL import Image
import glob
import argparse

def coolbean():
    colors = tuple(round(random.random(),1) for _ in range(3))

    #t = np.arange(0, 2*np.pi, .01)[1:]
    t = np.linspace(-np.pi/1.5, np.pi/2,500)[1:]


    x = 16 * np.cos(t)*((np.sin(t)**3) + np.cos(t)**3)
    y = 13 * np.sin(t)*((np.sin(t)**3) + np.cos(t)**3)



    fig = plt.figure(figsize = (5, 5), dpi=720)
    ax = fig.add_subplot(polar = False)

    #ax.plot(x, y, c=(1,0.2,0.5),lw=5)
    ax.fill(np.r_[x * 1.01, x[::-1] * 0.93], np.r_[y * 1.01, y[::-1] * 0.93],  c=colors)
    plt.axis('off')
    #plt.show()
    plt.savefig("bean.png", format = 'png', dpi=720, transparent = True)

def defaultbean():
    colors = tuple(round(random.random(),1) for _ in range(3))
    #t = np.arange(0, 2*np.pi, .01)[1:]
    t = np.linspace(-np.pi/1.5, np.pi/2,500)[1:]
    #t = np.linspace(0,2*np.pi,100)

    x = 16 * np.cos(t)*((np.sin(t)**3) + np.cos(t)**3)
    y = 13 * np.sin(t)*((np.sin(t)**3) + np.cos(t)**3)



    fig = plt.figure(figsize = (5, 5), dpi=720)
    ax = fig.add_subplot(polar = False)

    ax.plot(x, y, c=colors,lw=5)
    #ax.fill(np.r_[x * 1.01, x[::-1] * 0.93], np.r_[y * 1.01, y[::-1] * 0.93],  c=(1, 0.2, 0.5))
    plt.axis('off')
    #plt.show()
    plt.savefig("bean.png", format = 'png', dpi=720, transparent = True)


def gen_background():
    bg_color = tuple(np.random.choice(range(256), size=3))

    im = Image.new("RGB", (3600,3600), bg_color)
    im.save( "bg_color.png")

def merge_image():
    background = Image.open("bg_color.png")
    foreground = Image.open("bean.png")

    png_count = len(glob.glob1('.',"*.png"))
    png_count -= 2

    background.paste(foreground, (0, 0), foreground.convert('RGBA'))
    background.save('bean_nft_' + str(png_count) +'.png')

parser = argparse.ArgumentParser(description="AI Generated NFT's")
parser.add_argument('--cool', '-c',
                    action='store_true',
                    help='Cool Bean')
parser.add_argument('--default', '-d',
                    action='store_true',
                    help='Default Bean')
parser.add_argument('amount',
                    metavar='amount',
                    type=int,
                    nargs='?',
                    help='amount of nft beans to make')
parser.add_argument('--mixed', '-m',
                    action='store_true',
                    help='Cool Bean and Default Bean')
args = parser.parse_args()

if(args.cool):
    for i in range(args.amount):
        coolbean()
        gen_background()
        merge_image()
elif(args.default):
    for i in range(args.amount):
        defaultbean()
        gen_background()
        merge_image()
elif(args.mixed):
    for i in range((args.amount)//2):
        coolbean()
        gen_background()
        merge_image()
    for i in range (args.amount - (args.amount//2)):
        defaultbean()
        gen_background()
        merge_image()



"""
defaultbean()
gen_background()
merge_image()
"""