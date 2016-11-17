from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.ndimage


#Semantic colors
semantic_colors = dict([
('hair', (0, 86, 185, 255)),
('skin' , (255, 250, 80, 255)),
('eyebrows' , (198, 69, 111, 255)),
('eyes', (127, 127, 127, 255)),  #(137, 180, 83, 255)),
('nose', (88, 27, 108, 255)),
('beard', (235, 61, 0, 255)),
('ears', (71, 104, 33, 255)),
('mouth', (0, 158, 194, 255)),        
('clothe', (0, 0, 0, 255)),
('background', (255, 255, 255, 255))
])
    
semantic_positions = dict([
('hair', []),
('skin', []),
('eyebrows', []),
('eyes', []),
('nose', []),
('beard', []),
('ears', []),
('mouth', []),        
('clothe', []),
('background', [])
])


class FaceTransfer():
    
    
    def __init__(self, content, style):
   
        #Load original images RGB and semantic maps RGBA
        
        self.content, self.content_map = scipy.ndimage.imread(content + '.jpg'), scipy.ndimage.imread(content + '_sem' + '.png')
        self.style, self.style_map = scipy.ndimage.imread(style + '.jpg'), scipy.ndimage.imread(style + '_sem' + '.png')
        
        self.output_image = self.content         
        scipy.misc.imsave('./images/output.jpg', self.output_image)               
                    
        #Get the positions of all regions on the semantic map
        self.semantic_position() 
        print(semantic_positions['eyes'])
        
    def semantic_position(self):
            
        #Clear the semantic_positions    
        for key, value in semantic_positions.items():
            semantic_positions[key] = []

        #Create new semantic_positions
        h, w ,d = tuple(self.content_map.shape)                
        map_colors = np.reshape(self.content_map, (h*w, d))        
        for idx in np.ndindex(*map_colors.shape[:1]):                        
            if (map_colors[idx] == semantic_colors['hair']).all():
                semantic_positions['hair'].append(idx)                            
            elif (map_colors[idx] == semantic_colors['skin']).all():
                semantic_positions['skin'].append(idx)    
            elif (map_colors[idx] == semantic_colors['eyebrows']).all():
                semantic_positions['eyebrows'].append(idx)    
            elif (map_colors[idx] == semantic_colors['eyes']).all():
                semantic_positions['eyes'].append(idx)        
            elif (map_colors[idx] == semantic_colors['nose']).all():
                semantic_positions['nose'].append(idx)    
            elif (map_colors[idx] == semantic_colors['beard']).all():
                semantic_positions['beard'].append(idx)    
            elif (map_colors[idx] == semantic_colors['ears']).all():
                semantic_positions['ears'].append(idx)    
            elif (map_colors[idx] == semantic_colors['mouth']).all():
                semantic_positions['mouth'].append(idx)    
            elif (map_colors[idx] == semantic_colors['clothe']).all():
                semantic_positions['clothe'].append(idx)    
            elif (map_colors[idx] == semantic_colors['background']).all():
                semantic_positions['background'].append(idx)    
                
    def new_style(self, region, value, content, style):        
  
        content = content.split('/')[-1]
        style = style.split('/')[-1]
        new_style_image = scipy.ndimage.imread('./images/' + content + 'As' + style + str(value) + '.jpg')        
        h, w ,d = tuple(self.output_image.shape)    
        self.output_image = np.reshape(self.output_image, (h*w,d))
        new_style_image = np.reshape(new_style_image, (h*w,d))
        #Update region
        for position in semantic_positions[region]:
            self.output_image[position] = new_style_image[position] 
        self.output_image = np.reshape(self.output_image, (h,w,d))
        scipy.misc.imsave('./images/output.jpg', self.output_image)                                      