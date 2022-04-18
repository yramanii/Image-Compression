import os
from PIL import Image


def compressMe(file):
    # breakpoint()
    '''
    Compress the images.
    Input: str -> filepath
    Output: int -> compression percentage
    '''
    filepath = file

    if file.split('/')[-1].split('.')[-1] in ('jpg', 'jpeg', 'png', 'webp'):
        picture = Image.open(filepath)
        dim1 = (300, 300)

        save_path = filepath.replace('preprod_upload', 'preprod_upload_3')

        os.makedirs(save_path.replace(save_path.split('/')[-1], ''), exist_ok=True)
        new_size = picture.resize(dim1)     # dim2 will affect (picture)
    
        try:

            if '.png' in filepath.lower():
                
                new_size.save(save_path.replace(save_path.split('/')[-1], 'thumbnail_' + save_path.split('/')[-1]), "PNG",optimize=True,quality=85) 

            else:
                
                new_size.save(save_path.replace(save_path.split('/')[-1], 'thumbnail_' + save_path.split('/')[-1]),"JPEG",optimize=True,quality=85)   # dim1 (thumbnail)
        
        except:
            # picture.save(save_path)
            os.system(f'cp {file} {save_path}')
            print(file)

    elif file.split('/')[-1].split('.')[-1] in ('gif'):
        picture = Image.open(filepath)
        save_path = filepath.replace('preprod_upload', 'preprod_upload_3')
        os.makedirs(save_path.replace(save_path.split('/')[-1], ''), exist_ok=True)
        picture.save(save_path)

    else:
        save_path = filepath.replace('preprod_upload', 'preprod_upload_3')
        print('other files: ', file, '\n')

        os.system(f'cp {file} {save_path}')

def main():
    '''
    Invokes the function.
    Input: -
    Output: -
    '''
    # breakpoint()
    directories = ['2017', '2018', '2020', '2021', '2022', 'avatars']
    # directories = ['2019']
    print(directories)
    
    for directory in directories:
        sub_directories = os.listdir(f'/home/yashramani/Desktop/workspace/preprod_upload/{directory}')
        # sub_directories = ['12']
        print(sub_directories)
        for sub_directory in sub_directories:
            print('dir', directory)
            print('sub_dir', sub_directory)
            for file in os.listdir(f'/home/yashramani/Desktop/workspace/preprod_upload/{directory}/{sub_directory}'):
                if os.path.splitext(file)[1].lower():
                    filepath = os.path.join(f'/home/yashramani/Desktop/workspace/preprod_upload/{directory}/{sub_directory}/', file)
                    if os.path.getsize(filepath) > 0:
                        compressMe(filepath)
                # else:
                #     filepath = os.path.join(f'/home/yashramani/Desktop/workspace/preprod_upload/{directory}/{sub_directory}/', file)
                #     compressMe(filepath)
                # else:
                #     f = open(file, "w")
                #     full_path = os.path.join(f'/home/yashramani/Desktop/workspace/preprod_upload_2/{directory}/{sub_directory}/', file)
                #     f.write(full_path)
                #     f.close()

    print ("Done")

if __name__ == "__main__":
    main()
    
