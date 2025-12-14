from backend.core.body_engine.body_generator import generate_body
from backend.core.models.engine import EngineBodyParams
from backend.core.rendering.mesh_renderer import MeshRenderer

# 1. Prepare engine-level parameters (same as used internally)
engine_params = EngineBodyParams(
    engine_gender="male",
    engine_scale=0.5,
    engine_shape_vector=[0.0] * 10,  # or whatever your SMPL betas length is
    engine_pose="neutral"
)

# 2. Generate SMPL mesh via PUBLIC API
mesh_artifact = generate_body(
    engine_type="smpl",
    engine_params=engine_params
)

# 3. Render mesh visually
renderer = MeshRenderer()
output_path = "outputs/images/smpl_visual_neutral.png"

renderer.render(mesh_artifact, output_path)

print("Rendered:", output_path)
