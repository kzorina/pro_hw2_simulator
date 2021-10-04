from pyphysx import *
import numpy as np
from pyphysx import ShapeFlag, GeometryType

def get_matrix_dh(theta, d, alpha, a):
    return np.array([[np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a*np.cos(theta)],
                     [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a*np.sin(theta)],
                     [0, np.sin(alpha), np.cos(alpha), d],
                     [0, 0, 0, 1]])

def add_motion_axis_link():
    actor = RigidDynamic()
    shape = Shape.create_box([0.05, 0.05, 0.2], Material(restitution=1.))
    shape.set_flag(ShapeFlag.SIMULATION_SHAPE, False)
    actor.disable_gravity()
    actor.attach_shape(shape)
    return actor