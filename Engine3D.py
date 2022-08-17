from gl import Renderer, color, V3, V2
from texture import Texture
<<<<<<< HEAD
from shaders import flat, gourad, toon2, negative
=======
from shaders import flat, unlit, gourad, toon, glow, textureBlend
>>>>>>> e29b462cea9726fb3a4a248b7dea2c8149026542

width = 960
height = 540

rend = Renderer(width, height)

<<<<<<< HEAD
rend.active_shader = negative
rend.active_texture = Texture("models/bullTexture.bmp")

rend.dirLight = V3(0.5, 0, -0.5)
rend.glLoadModel("models/bull.obj",
                 translate = V3(0, -1, -8),
                 scale = V3(0.2,0.2,0.2),
                 rotate = V3(35,0,0))

rend.glFinish("Outputs/output1.bmp")

#high angle
''' rend.active_shader = gourad
rend.active_texture = Texture("bullTexture.bmp")

rend.dirLight = V3(0.5, 0, -0.5)
rend.glLoadModel("bull.obj",
                 translate = V3(0, -1.7, -8),
                 scale = V3(0.2,0.2,0.2),
                 rotate = V3(-35,0,0))

rend.glFinish("output.bmp") '''


#Low angle
''' rend.active_shader = gourad
rend.active_texture = Texture("bullTexture.bmp")

rend.dirLight = V3(0, -1, 0)
rend.glLoadModel("bull.obj",
                 translate = V3(0, -1.5, -7),
                 scale = V3(0.3,0.3,0.3),
                 rotate = V3(-30,0,0))
=======
rend.dirLight = V3(1,0,0)

rend.active_texture = Texture("models/earthDay.bmp")
rend.active_texture2 = Texture("models/earthNight.bmp")
rend.active_shader = textureBlend

rend.glLoadModel("models/earth.obj",
                 translate = V3(0, 0, -10),
                 scale = V3(0.01,0.01,0.01),
                 rotate = V3(0,90,0))



#rend.active_texture = Texture("models/model.bmp")
#rend.active_shader = gourad
#rend.glLoadModel("models/model.obj",
#                 translate = V3(-4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = toon
#rend.glLoadModel("models/model.obj",
#                 translate = V3(0, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = glow
#rend.glLoadModel("models/model.obj",
#                 translate = V3(4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))


>>>>>>> e29b462cea9726fb3a4a248b7dea2c8149026542

rend.glFinish("output.bmp")
 '''
