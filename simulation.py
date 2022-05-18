import pyglet

from ecosystem import Ecosystem
from neurons import InputLifetime, MiddleNeuron, OutputMovementX
from organism import Organism

if __name__ == '__main__':

    input_neurons = (InputLifetime,)
    middle_neurons = (MiddleNeuron,)
    output_neurons = (OutputMovementX,)

    Organism.set_input_neurons = input_neurons
    Organism.set_middle_neurons = middle_neurons
    Organism.set_output_neurons = output_neurons

    ecosystem = Ecosystem(1000, 10, (100, 100), 0.05)

    window = pyglet.window.Window()

    @window.event
    def on_draw():

        window.clear()

    pyglet.app.run()
