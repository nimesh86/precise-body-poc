# backend/core/body_engine/base_smpl_engine.py

import os
import numpy as np
import torch


class BaseSMPLFamilyEngine:
    """
    Shared utilities for SMPL / SMPL-X based engines.
    """

    POSE_DIR = "assets/poses"

    def _load_pose(self, pose_name: str) -> torch.Tensor:
        pose_file = os.path.join(self.POSE_DIR, f"{pose_name}.npy")

        if not os.path.exists(pose_file):
            raise FileNotFoundError(f"Pose file not found: {pose_file}")

        pose_vector = np.load(pose_file, allow_pickle=True).astype("float32")

        if pose_vector.shape != (72,):
            raise ValueError("SMPL pose vector must have shape (72,)")

        return torch.tensor(pose_vector).unsqueeze(0)
