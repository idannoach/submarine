from dataclasses import dataclass

@dataclass
class Submarine:
    '''
        A class for storing a submarine's characteristics such as legnth and rotation.
        The default submarine's length is 1, and its rotation is 0 (straight)

    '''
    length  :   int =   1   # Length of submarine
    rotation:   int =   0   # Rotation flag '0' means not rotated, '1' means rotated   

