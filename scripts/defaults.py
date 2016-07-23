# Modified by scripts.function.preferences.generate.main
defaults = {
  'name panel': {
    'pin active object': True,
    'hide search': True,
    'hide find & replace': True,
    'filters': False,
    'options': False,
    'display names': False,
    'search': '',
    'regex': False,
    'mode': 'SELECTED',
    'groups': False,
    'action': False,
    'grease pencil': False,
    'constraints': False,
    'modifiers': False,
    'bone groups': False,
    'bone constraints': False,
    'vertex groups': False,
    'shapekeys': False,
    'uvs': False,
    'vertex colors': False,
    'materials': False,
    'textures': False,
    'particle systems': False,
    'bone mode': 'SELECTED',
    'display bones': False,
  },

  'shared': {
    'sort': True,
    'link': False,
    'pad': 0,
    'start': 1,
    'step': 1,
    'separator': '.',
    'ignore': False
  },

  'auto name': {
    'mode': 'SELECTED',
    'objects': False,
    'constraints': False,
    'modifiers': False,
    'object data': False,
    'bone constraints': False,
    'object type': 'ALL',
    'constraint type': 'ALL',
    'modifier type': 'ALL',

    'object names': {
      'prefix': False,
      'mesh': 'Mesh',
      'curve': 'Curve',
      'surface': 'Surface',
      'meta': 'Meta',
      'font': 'Text',
      'armature': 'Armature',
      'lattice': 'Lattice',
      'empty': 'Empty',
      'speaker': 'Speaker',
      'camera': 'Camera',
      'lamp': 'Lamp',
    },

    'constraint names': {
      'prefix': False,
      'camera solver': 'Camera Solver',
      'follow track': 'Follow Track',
      'object solver': 'Object Solver',
      'copy location': 'Copy Location',
      'copy rotation': 'Copy Rotation',
      'copy scale': 'Copy Scale',
      'copy transforms': 'Copy Transforms',
      'limit distance': 'Limit Distance',
      'limit location': 'Limit Location',
      'limit rotation': 'Limit Rotation',
      'limit scale': 'Limit Scale',
      'maintain volume': 'Maintain Volume',
      'transform': 'Transform',
      'clamp to': 'Clamp To',
      'damped track': 'Damped Track',
      'inverse kinematics': 'Inverse Kinematics',
      'locked track': 'Locked Track',
      'spline inverse kinematics': 'Spline Inverse Kinematics',
      'stretch to': 'Stretch To',
      'track to': 'Track To',
      'action': 'Action',
      'child of': 'Child Of',
      'floor': 'Floor',
      'follow path': 'Follow Path',
      'pivot': 'Pivot',
      'rigid body joint': 'Rigid Body Joint',
      'shrinkwrap': 'Shrinkwrap',
    },

    'modifier names': {
      'prefix': False,
      'data transfer': 'Data Transfer',
      'mesh cache': 'Mesh Cache',
      'normal edit': 'Normal Edit',
      'uv project': 'UV Project',
      'uv warp': 'UV Warp',
      'vertex weight edit': 'Vertex Weight Edit',
      'vertex weight mix': 'Vertex Weight Mix',
      'vertex weight proximity': 'Vertex Weight Proximity',
      'array': 'Array',
      'bevel': 'Bevel',
      'boolean': 'Boolean',
      'build': 'Build',
      'decimate': 'Decimate',
      'edge split': 'Edge Split',
      'mask': 'Mask',
      'mirror': 'Mirror',
      'multiresolution': 'Multiresolution',
      'remesh': 'Remesh',
      'screw': 'Screw',
      'skin': 'Skin',
      'solidify': 'Solidify',
      'subdivision surface': 'Subdivision Surface',
      'triangulate': 'Triangulate',
      'wireframe': 'Wireframe',
      'armature': 'Armature',
      'cast': 'Cast',
      'corrective smooth': 'Corrective Smooth',
      'curve': 'Curve',
      'displace': 'Displace',
      'hook': 'Hook',
      'laplacian smooth': 'Laplacian Smooth',
      'laplacian deform': 'Laplacian Deform',
      'lattice': 'Lattice',
      'mesh deform': 'Mesh Deform',
      'shrinkwrap': 'Shrinkwrap',
      'simple deform': 'Simple Deform',
      'smooth': 'Smooth',
      'warp': 'Warp',
      'wave': 'Wave',
      'cloth': 'Cloth',
      'collision': 'Collision',
      'dynamic paint': 'Dynamic Paint',
      'explode': 'Explode',
      'fluid simulation': 'Fluid Simulation',
      'ocean': 'Ocean',
      'particle instance': 'Particle Instance',
      'particle system': 'Particle System',
      'smoke': 'Smoke',
      'soft body': 'Soft Body',
    },

    'object data names': {
      'prefix': False,
      'mesh': 'Mesh',
      'curve': 'Curve',
      'surface': 'Surface',
      'meta': 'Meta',
      'font': 'Text',
      'armature': 'Armature',
      'lattice': 'Lattice',
      'empty': 'Empty',
      'speaker': 'Speaker',
      'camera': 'Camera',
      'lamp': 'Lamp',
    },
  },

  'batch name': {
    'mode': 'SELECTED',
    'actions': False,
    'action groups': False,
    'grease pencil': False,
    'pencil layers': False,
    'objects': False,
    'groups': False,
    'constraints': False,
    'modifiers': False,
    'object data': False,
    'bone groups': False,
    'bones': False,
    'bone constraints': False,
    'vertex groups': False,
    'shapekeys': False,
    'uvs': False,
    'vertex colors': False,
    'materials': False,
    'textures': False,
    'particle systems': False,
    'particle settings': False,
    'object type': 'ALL',
    'constraint type': 'ALL',
    'modifier type': 'ALL',
    'sensors': False,
    'controllers': False,
    'actuators': False,
    'line sets': False,
    'linestyles': False,
    'linestyle modifiers': False,
    'linestyle modifier type': 'ALL',
    'scenes': False,
    'render layers': False,
    'worlds': False,
    'libraries': False,
    'images': False,
    'masks': False,
    'sequences': False,
    'movie clips': False,
    'sounds': False,
    'screens': False,
    'keying sets': False,
    'palettes': False,
    'brushes': False,
    'nodes': False,
    'node labels': False,
    'frame nodes': False,
    'node groups': False,
    'texts': False,
    'ignore action': False,
    'ignore grease pencil': False,
    'ignore object': False,
    'ignore group': False,
    'ignore constraint': False,
    'ignore modifier': False,
    'ignore bone': False,
    'ignore bone group': False,
    'ignore bone constraint': False,
    'ignore object data': False,
    'ignore vertex group': False,
    'ignore shapekey': False,
    'ignore uv': False,
    'ignore vertex color': False,
    'ignore material': False,
    'ignore texture': False,
    'ignore particle system': False,
    'ignore particle setting': False,
    'custom name': '',
    'find': '',
    'regex': False,
    'replace': '',
    'prefix': '',
    'suffix': '',
    'suffix last': False,
    'trim start': 0,
    'trim end': 0,
    'cut start': 0,
    'cut amount': 0,
  },

  'copy name': {
    'mode': 'SELECTED',
    'source': 'OBJECT',
    'objects': False,
    'object data': False,
    'materials': False,
    'textures': False,
    'particle systems': False,
    'particle settings': False,
    'use active object': False,
  },
}
