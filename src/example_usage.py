from cave.agent_ascent import entrance, labyrinth, volcano, alien
from cave.models.simple_embed import SimpleEmbed

def run_cave(x):
    model = SimpleEmbed(dim=32)
    s1 = entrance(x)
    s2 = labyrinth(s1)
    s3 = volcano(s2, model)
    s4 = alien(s3)
    return s4

print(run_cave("Renzo discovering latent geometry"))
