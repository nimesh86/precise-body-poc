import os
import hashlib
from PIL import Image, ImageDraw, ImageFont

from backend.core.models.artifacts import MeshArtifact, RenderArtifact


OUTPUT_IMAGE_DIR = "outputs/images"
IMAGE_SIZE = (512, 512)
BACKGROUND_COLOR = (230, 230, 230)
TEXT_COLOR = (40, 40, 40)


def render_preview(mesh: MeshArtifact) -> RenderArtifact:
    """
    RENDERER v1 (POC)
    -----------------
    Generates a deterministic placeholder preview image
    for a given mesh artifact.

    This renderer does NOT visualize geometry.
    It only proves the rendering pipeline.
    """

    os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)

    image_id = _deterministic_image_id(mesh.mesh_path)
    image_path = os.path.join(OUTPUT_IMAGE_DIR, f"{image_id}.png")

    _render_placeholder(image_path, mesh.mesh_path)

    return RenderArtifact(image_path=image_path)


def _deterministic_image_id(mesh_path: str) -> str:
    """
    Same mesh path -> same image filename
    """
    return hashlib.sha256(mesh_path.encode()).hexdigest()[:16]


def _render_placeholder(path: str, mesh_path: str) -> None:
    img = Image.new("RGB", IMAGE_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    text = [
        "RENDERER v1 (POC)",
        "",
        "Placeholder Preview",
        "",
        f"Mesh:",
        os.path.basename(mesh_path),
    ]

    y = 180
    for line in text:
        draw.text((40, y), line, fill=TEXT_COLOR)
        y += 32

    img.save(path)
