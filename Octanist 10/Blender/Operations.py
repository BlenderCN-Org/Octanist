import os
import bpy
from bpy.app.handlers import persistent
from datetime import datetime

TIMER = None

# Events
def clear_render_event():
    bpy.app.handlers.render_init.clear()
    bpy.app.handlers.render_post.clear()
    bpy.app.handlers.render_complete.clear()

def handler_init_render(scene):
    # Set timer
    global TIMER
    TIMER = datetime.now()
    # Get dir of render ouput
    path = bpy.context.scene.render.filepath
    if(path=='/tmp\\'): 
        path = 'C:\\tmp'
    # Send response via socket
    res = {
        'type': 'msg',
        'code': 'init_render',
        'info': {
            'output_path': path
        }
    }
    sock.send(res)

def handler_post_render(scene):
    res = {
        'type': 'msg',
        'code': 'post_render',
        'info': {
            'time_elapsed': datetime.now() - TIMER
        }
    }
    sock.send(res)

def handler_complete_render(scene):
    res = {
        'type': 'msg',
        'code': 'complete_render',
        'info': {
            'time_elapsed': datetime.now() - TIMER
        }
    }
    sock.send(res)

# Operations
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
    # Clean events
    clear_render_event()

    if(animation):
        bpy.ops.render.render(animation=True, write_still=True)
    else:
        bpy.ops.render.render(write_still=True)
    
    # Register events
    bpy.app.handlers.render_init.append(handler_init_render)
    bpy.app.handlers.render_post.append(handler_post_render)
    bpy.app.handlers.render_complete.append(handler_complete_render)

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

