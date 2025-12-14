# scripts/generate_smpl_poses.py

import os
import numpy as np

POSE_DIR = "assets/poses"
os.makedirs(POSE_DIR, exist_ok=True)


def save_pose(name: str, pose: np.ndarray):
    path = os.path.join(POSE_DIR, f"{name}.npy")
    np.save(path, pose.astype(np.float32))
    print(f"Saved {path}")


def main():
    # Neutral pose: all zeros
    neutral = np.zeros(72)
    save_pose("neutral", neutral)

    # T-pose: arms straight out
    t_pose = np.zeros(72)
    t_pose[15 * 3 + 0] = np.pi / 2     # left shoulder
    t_pose[18 * 3 + 0] = -np.pi / 2    # right shoulder
    save_pose("t_pose", t_pose)

    # A-pose: arms slightly down
    a_pose = np.zeros(72)
    a_pose[15 * 3 + 0] = np.pi / 6     # left shoulder
    a_pose[18 * 3 + 0] = -np.pi / 6    # right shoulder
    save_pose("a_pose", a_pose)


if __name__ == "__main__":
    main()
