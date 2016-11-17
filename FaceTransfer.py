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
        
        self.content_name = None
        self.style_name = None
        self.load_content(content)
        self.load_style(style)                                            
                        
    def load_content(self, content):
   
        #Contet is just the name
    
        if not(self.content_name == content):
            self.content_name = content
            content_path = './images/' + content + '/originals/image.png' 
            content_map_path = './images/' + content + '/maps/map.png' 

            self.content, self.content_map = scipy.ndimage.imread(content_path), scipy.ndimage.imread(content_map_path)        

            #Save the content as output for display
            self.output_image = self.content         
            scipy.misc.imsave('./images/output.png', self.output_image)               

            #Get the positions of all regions on the semantic map
            self.semantic_position()         
        
    def load_style(self, name):
        
        self.style_name = name  
        self.style_path = './images/' + self.content_name + '/styles/' + name + '/' 
            
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
                
    def change_texture(self, region, value, content, style):        
                          
        change_texture_image = scipy.ndimage.imread(self.style_path + \
        self.content_name + 'As' + self.style_name + str(value) + '.png')        
        h, w ,d = tuple(self.output_image.shape)    
        self.output_image = np.reshape(self.output_image, (h*w,d))
        change_texture_image = np.reshape(change_texture_image, (h*w,d))
        #Update region
        for position in semantic_positions[region]:
            self.output_image[position] = change_texture_image[position] 
        self.output_image = np.reshape(self.output_image, (h,w,d))
        scipy.misc.imsave('./images/output.png', self.output_image) #Change        