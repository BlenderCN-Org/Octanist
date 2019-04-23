import bpy

#region Rendering Jobs
def render_sv():
    '''
    Render single frame with viewport display
    
    Tips
    ----
    When use_viewport is false, image renders in background.
    '''
    bpy.ops.render.render(use_viewport=True, write_still=True) # Without use_viewport, render in background

def render_av():
    '''
    Render full animation with viewport display
    '''
    bpy.ops.render.render(animation=True, use_viewport=True, write_still=True)

def render_sn():
    '''
    Render single frame without viewport display
    
    Tips
    ----
    When use_viewport is false, image renders in background.
    '''
    bpy.ops.render.render(use_viewport=False, write_still=True) # Without use_viewport, render in background

def render_an():
    '''
    Render full animation without viewport display
    '''
    bpy.ops.render.render(animation=True, use_viewport=False, write_still=True)
#endregion

commands = {
    'RENDER_SV': render_sv,
    'RENDER_AV': render_av,
    'RENDER_SN': render_sn,
    'RENDER_AN': render_an,
}