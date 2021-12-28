import numpy as np
import open3d as o3d
import os

file_name = "000048.bin"
# Load binary point cloud

bin_pcd = np.fromfile(file_name, dtype=np.float32)

# Reshape and drop reflection values
points = bin_pcd.reshape((-1, 4))[:, 0:3]

# Convert to Open3D point cloud
o3d_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))

# Save to whatever format you like
# o3d.io.write_point_cloud("pointcloud.pcd", o3d_pcd)


# Load .pcd file and Visualization
# pc = o3d.io.read_point_cloud("pointcloud.pcd")
# print(pc)
# print(np.asarray(pc.points))
o3d.visualization.draw_geometries([o3d_pcd])