import copy

def css_styles(initial_styles):
    new = copy.deepcopy(initial_styles)

    def add_style(selector, property, value):
        if selector not in new:
            new[selector] = {}
        
        new[selector][property]= value
        return new
        
    return add_style


