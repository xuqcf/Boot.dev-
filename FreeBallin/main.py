def new_resizer(max_width, max_height):
    def inner(min_width=0, min_height=0): 
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        
        def innermost(width, height):
            width = max(min_width, min(width, max_width)) # min(width, max_width) if width is above max_width, use max_width, otherwise keep width || max(min_width, result), if width is too small, use min_width otherwise keep result
            height = max(min_height, min(height, max_height))
            return width, height
        
        return innermost
    return inner