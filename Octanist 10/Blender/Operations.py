import os

def launch():
    '''
    Launch the Octanist App located in the current directory
    '''
    octanist = os.path.dirname(os.path.realpath(__file__)) + 'Octanist.exe'
    os.startfile(octanist)

def start_render(animation=False):
    '''
    Start rendering the current scene
    
    Parameters
    ----------
    animation : bool
        Render animation or not
    '''
    return None

def cancel_render():
    '''
    Cancel the rendering progress
    '''
    return None

def send_selected_info():
    '''
    Send the info of selected object via socket
    '''
    return None

def send_materials_info():
    '''
    Send the info of all materials in the context via socket
    '''
    return None

def append_material_from_lib(libpath, matname):
    '''
    Append the material from a given library

    Parameters
    ----------
    libpath : str
        The path to the library
    matname : str
        The specific material name
    
    Comments
    --------
    If we copy a material in the library of Octanist App and paste it
        first append_material_from_lib and then cp_material_to
    '''
    return None

def rm_material_from(matname, objnames):
    '''
    Remove a material from the selected object(s)

    Parameters
    ----------
    matname : str
        The specific material name
    objname : list
        Object names
    '''
    return None

def cp_material_to(matname, objnames):
    '''
    Copy a material to the selected object(s)

    Parameters
    ----------
    matname : str
        The specific material name
    objname : list
        Object names
    '''
    return None

def update_env_daylight(power, direction, turbidity, north_offset, sun_size, colors):
    '''
    Update the data of daylight environment

    Parameters
    ----------
    power : float
        bpy.context.scene.world.octane.env_power
    direction : list
        bpy.context.scene.world.octane.env_sundir_{x|y|z}
    turbidity : float
        bpy.context.scene.world.octane.env_turbidity
    north_offset : float
        bpy.context.scene.world.octane.env_northoffset
    sun_size : float
        bpy.context.scene.world.octane.env_sun_size
    colors : list
        bpy.context.scene.world.octane.env_sky_color
        bpy.context.scene.world.octane.env_sunset_color
    '''
    return None

def update_env_texture(imgpath, power, vector):
    '''
    Update the data and material of texture environment

    Parameters
    ----------
    imgpath : str
        The image related to the texture material
    power : float
        bpy.context.scene.world.octane.env_power
    vector : list
        Transformation vector related to the texture material
    '''
    return None

