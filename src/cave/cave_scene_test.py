from cave.multi_agent import CaveAgent
from cave.world.cave_scene import latent_to_scene

agent = CaveAgent("vision")
agent.ascend("image of a cat")

scene = latent_to_scene(agent.latent)

print("Scene:", scene.name)
print("Description:", scene.description)
print("Intensity:", scene.intensity)
print("Color:", scene.color)
print("Symbol:", scene.symbol)
