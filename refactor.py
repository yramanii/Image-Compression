def compress_me(key, download_path, resized_path, upload_path_thumbnail):
    """
    Compress the images.
    Input: str -> download_path, str -> resized_path
    Output: int -> compression percentage
    """
    
    
    try:
        picture = Image.open(download_path)
        print(key)
        
        Thumbnail_Dimensions = (400, 450)
        Picture_Dimensions = (1000, 1000)
        if picture.size > (1200,1200) and  ".png" in key.lower():

            new_size = picture.resize(Picture_Dimensions)
            compressed = new_size.convert("P", palette=Image.ADAPTIVE, colors=256)
            compressed.save(resized_path, "PNG", optimize=True, quality=85)
            
            picture.thumbnail(Thumbnail_Dimensions)
            picture.save(upload_path_thumbnail, "PNG",optimize=True,quality=85)

        elif picture.size < (1200,1200) and  ".png" in key.lower():
            compressed = picture.convert("P", palette=Image.ADAPTIVE, colors=256)
            compressed.save(resized_path, "PNG", optimize=True, quality=85)
            
            picture.thumbnail(Thumbnail_Dimensions)
            picture.save(upload_path_thumbnail, "PNG",optimize=True,quality=85)
            
            
        else:
            new_size.save(resized_path, "JPEG", optimize=True, quality=85)
            
            picture.thumbnail(Thumbnail_Dimensions)
            picture.save(upload_path_thumbnail, "JPEG",optimize=True,quality=85)
                
            
            picture.save(resized_path, "JPEG", optimize=True, quality=85)
            
            picture.thumbnail(Thumbnail_Dimensions)
            picture.save(upload_path_thumbnail, "JPEG",optimize=True,quality=85)
            return "success"
        
        
    except Exception as e:
        return f"compression failed with error: {str(e)}"