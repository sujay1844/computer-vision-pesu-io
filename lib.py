import matplotlib.pyplot as plt

def compare_imgs_with_figsize(figsize):

    def compare_images(*args, figsize=figsize, grid_shape=None):

        if len(args) % 2 != 0:
            raise ValueError("Number of titles should match the number of images.")
        
        plt.figure(figsize=figsize)
        
        if grid_shape:
            num_rows, num_cols = grid_shape
        else:
            num_rows, num_cols = 1, len(args) // 2
        
        for i in range(0, len(args), 2):
            img, title = args[i], args[i + 1]
            
            plt.subplot(num_rows, num_cols, i // 2 + 1)
                
            plt.imshow(img, cmap='gray')
            plt.title(title)
            plt.axis('off')
        
        plt.show()

    return compare_images
