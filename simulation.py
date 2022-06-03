import pyglet
from pyglet import shapes

from ecosystem import Ecosystem
from neurons import InputLifeTime, MiddleNeuron, OutputMovementX
from organism import Organism

if __name__ == '__main__':

    input_neurons = (InputLifeTime,)
    middle_neurons = (MiddleNeuron,)
    output_neurons = (OutputMovementX,)

    Organism.set_input_neurons(input_neurons)
    Organism.set_middle_neurons(middle_neurons)
    Organism.set_output_neurons(output_neurons)

    Organism.set_genome_size(3)

    ecosystem = Ecosystem(1000, 100, (100, 100), 0.1)
    ecosystem.populate()
    ecosystem.broadcast_event('InputLifeTime',
                              ecosystem.lifetime/ecosystem.lifespan)

    window = pyglet.window.Window()

    @window.event
    def on_draw():

        batch = pyglet.graphics.Batch()

        window.clear()
        # red_sequare = shapes.Rectangle(
        # 150, 240, 200, 20, color=(255, 55, 55), batch=batch)
        batch.draw()

    pyglet.app.run()
