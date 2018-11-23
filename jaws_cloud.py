from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import os

word_list = ['ok','https imgur','now','going','got','go','gifv','im','oh','lot','yet','bad','ill','gifv','https','https instagram','imgur','haha','hahaha','today','think','day',
            'want','good','well','work','still','one','done','will','time','back','right','see','getting','really','facebook',
            'wiki']
##Lets create a function to do this.

def border_wordcloud(words, img, background_color = 'white', border_size = 1.2,stopwords = set(STOPWORDS), 
                     can_display = False, color_function = None, color_map = 'viridis'):
#     Takes in words and an image and displays the word cloud in a border around the image
#     Params
#         words: list of all the words you supplying to the word cloud
#         image: the image you wish to display your word cloud around
    
#     Returns
#         cloud_image: the image with the word cloud around it

#     Create initial Image array
    image_array = np.array(img)
    
    width = int(image_array.shape[0]*border_size)
    height = int(image_array.shape[1]*border_size)
    
    ##create the white background
    background_image = Image.fromarray((np.ones((width,height,image_array.shape[2]),np.uint8))*255,'RGB')
    
    ##Set position to paste
    position = ((int(round(background_image.width - img.width)/2)),int(round(background_image.height-img.height)/2))

    ##Paste it, save and display the images
    background_image.paste(img, position)
    
    ##Create the mask
    mask = np.array(background_image)

    ##Set up the transformed mask
    transformed_mask = np.ndarray((mask.shape[0],mask.shape[1], mask.shape[2]), np.int32)

    ##Create the white array
    white_array = np.array([255,255,255])

    ##Alter the mask so all the white is black and all the images are white
    for i in range(len(mask)):
        transformed_mask[i] = list(map(lambda x: [0,0,0] if ((x == white_array).sum() ==3) else white_array, mask[i]))
    
    ##Create the word cloud with said mask
    word_cloud = WordCloud(width = 800, height = 800,
                    background_color = background_color,
                    stopwords = stopwords,
                    collocations = False,
                    max_words = 100,
                    mask = transformed_mask,
                    min_font_size = 10,
                    contour_width = 3,
                     contour_color = 'green',
                          color_func = color_function,
                          colormap = color_map).generate(words)

    ##Save the wordcloud to a file
    cloud_image = word_cloud.to_image()
    new_position = ((int(round(cloud_image.width - img.width)/2)),int(round(cloud_image.height-img.height)/2))
    cloud_image.paste(img,new_position)
    if can_display:
        display(cloud_image)
    return cloud_image

# os.chdir('C:\\Users\\jfalh\\Desktop\\Jawsem SMS Project\\Final_images')

# for img in os.listdir(os.getcwd()):
#     im = Image.open(img)
#     rgb_im = im.convert('RGB')
#     print(img)
#     name = str(img).replace('.png','')
#     rgb_im.save(name+'.jpg')
