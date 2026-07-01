from cave.models.simple_embed import SimpleEmbed

def compare_agents(a, b):
    model = SimpleEmbed(dim=32)
    z1 = model.encode(a)
    z2 = model.encode(b)
    return model.measure_alignment(z1, z2)
