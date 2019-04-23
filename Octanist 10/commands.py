import bpy

#region Rendering Jobs
def render_s(sock):
    '''
    Render single frame with viewport display
    
    Tips
    ----
    When use_viewport is false, image renders in background.
    '''
    sock.send(bytes('RENDER_INIT', 'utf-8'))
    bpy.ops.render.render(use_viewport=True, write_still=True) # Without use_viewport, render in background
    sock.send(bytes('RENDER_COMPLETE', 'utf-8'))

def render_a(sock):
    '''
    Render full animation with viewport display
    '''
    sock.send(bytes('RENDER_INIT', 'utf-8'))
    bpy.ops.render.render(animation=True, use_viewport=True, write_still=True)
    sock.send(bytes('RENDER_COMPLETE', 'utf-8'))
#endregion

commands = {
    'RENDER_S': render_s,
    'RENDER_A': render_a
}