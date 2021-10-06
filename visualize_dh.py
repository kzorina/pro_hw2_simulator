# from pyphysx import *
from pyphysx_render.meshcat_render import MeshcatViewer
import quaternion as npq
from pyphysx_utils.rate import Rate
from utils import *
import json

dh_dict = json.load(open("hw02.json", 'rb'))
dh_dict['theta0 offset'] = 0
dh_dict['d0'] = 0
dh_dict['alpha0'] = 0
dh_dict['a0'] = 0
""" Construct a scene with various objects """
scene = Scene()
scene.add_actor(RigidStatic.create_plane(material=Material(static_friction=0.1, dynamic_friction=0.1, restitution=0.5)))

""" Add motion axes links to scene """
links = []
n_links = 7
for i in range(n_links):
    link = add_motion_axis_link()
    links.append(link)
    scene.add_actor(link)

""" Compute transformation from DH """
a = np.eye(4)
for i in range(n_links):
    a = a.dot(get_matrix_dh(dh_dict[f'theta{i} offset'], dh_dict[f'd{i}'], dh_dict[f'alpha{i}'], dh_dict[f'a{i}']))
    links[i].set_global_pose((a[:3, 3], npq.from_rotation_matrix(a[:3, :3])))

""" Create a viewer and add the scene into it. """
render = MeshcatViewer(wait_for_open=True, open_meshcat=True, show_frames=True, frame_scale=0.22)
render.add_physx_scene(scene)

""" Simulate. """
rate = Rate(120)
for i in range(50):
    scene.simulate(rate.period())
    render.update()
    rate.sleep()
