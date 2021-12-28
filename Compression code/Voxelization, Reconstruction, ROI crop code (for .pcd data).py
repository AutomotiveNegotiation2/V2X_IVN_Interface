import open3d as o3d
import numpy as np
import pcl
import os

# examples/Python/Basic/pointcloud.py
data_path = "F:\예타2세부_데이터\AI 허브\특수환경 자율주행 3D 이미지\Training\[원천]incheon4\drive_1096\lidar"
data_name = "000354.pcd"

file_name = os.path.join(data_path, data_name) #, fragment.pcd, "L515-can.pcd" , "1280_1792.pcd"c
pcd = o3d.io.read_point_cloud(file_name)
print("Origin_pcd_number : ",pcd)
print("Origin_pcd_shape : ",np.asarray(pcd.points).shape)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])

downpcd = pcd.voxel_down_sample(voxel_size=0.9)
print("Down_pcd_number : ",downpcd)
print("Down_pcd_shape : ",np.asarray(downpcd.points).shape)
print(np.asarray(downpcd.points))
o3d.visualization.draw_geometries([downpcd])

'''
# ### Surface Reconstruction
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
# Alpha shapes
# ll = [0.1]#, 0.02,0.025, 0.03,0.05]
# for k in ll:
#     alpha = k
#     mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(downpcd, alpha)
#     mesh.compute_vertex_normals()
#     o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)

# Ball pivoting
# radii = [0.1]#, 0.01, 0.02, 0.04]
# rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(downpcd, o3d.utility.DoubleVector(radii))
# o3d.visualization.draw_geometries([rec_mesh])

# Possion surface reconstruction
# print('run Poisson surface reconstruction')
# with o3d.utility.VerbosityContextManager(
#         o3d.utility.VerbosityLevel.Debug) as cm:
#     mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(downpcd, depth=100)
# print(mesh)
# o3d.visualization.draw_geometries([mesh])
'''

'''
### ROI Crop
print("Load a polygon volume and use it to crop the original point cloud")
vol = o3d.visualization.read_selection_polygon_volume("cropped.json")
chair = vol.crop_point_cloud(downpcd)
print("Crop_pcd_number : ",chair)
print("Crop_pcd_shape : ",np.asarray(chair.points).shape)
o3d.visualization.draw_geometries([chair])

print("Recompute the normal of the downsampled point cloud")
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
    radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([downpcd])

print("Print a normal vector of the 0th point")
print(downpcd.normals[0])
print("Print the normal vectors of the first 10 points")
print(np.asarray(downpcd.normals)[:10, :])
print("")

print("Paint chair")
chair.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([chair])
print("")
'''
