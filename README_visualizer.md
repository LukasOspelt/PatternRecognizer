```mermaid
classDiagram
    class Visualizer {
        + name: str
        + __init__(name: str)
        + visualize(frame: numpy.ndarray, pattern_list: list): None
    }
    Visualizer --|> object
```