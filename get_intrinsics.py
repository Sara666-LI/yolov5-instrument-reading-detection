# Get the intrinsics to convert the pixel coordinates to world coordinates
import pyrealsense2 as rs

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 15)
profile = pipeline.start(config)
frames = pipeline.wait_for_frames()
depth = frames.get_depth_frame()
color = frames.get_color_frame()
# 获取内参
depth_profile = depth.get_profile()
print(depth_profile)
# <pyrealsense2.video_stream_profile: 1(0) 640x480 @ 30fps 1>
print(type(depth_profile))
# <class 'pyrealsense2.pyrealsense2.stream_profile'>
print(depth_profile.fps())
# 30
print(depth_profile.stream_index())
# 0
print(depth_profile.stream_name())
# Depth
print(depth_profile.stream_type())
# stream.depth
print('', depth_profile.unique_id)
# <bound method PyCapsule.unique_id of <pyrealsense2.video_stream_profile: 1(0) 640x480 @ 30fps 1>>

color_profile = color.get_profile()
print(color_profile)
# <pyrealsense2.video_stream_profile: 2(0) 640x480 @ 30fps 6>
print(type(color_profile))
# <class 'pyrealsense2.pyrealsense2.stream_profile'>
print(depth_profile.fps())
# 30
print(depth_profile.stream_index())
# 0

cvsprofile = rs.video_stream_profile(color_profile)
dvsprofile = rs.video_stream_profile(depth_profile)

color_intrin = cvsprofile.get_intrinsics()
print("color_intrin:", color_intrin)
# width: 640, height: 480, ppx: 318.482, ppy: 241.167, fx: 616.591, fy: 616.765, model: 2, coeffs: [0, 0, 0, 0, 0]
depth_intrin = dvsprofile.get_intrinsics()
print("depth_intrin:", depth_intrin)
# width: 640, height: 480, ppx: 317.78, ppy: 236.709, fx: 382.544, fy: 382.544, model: 4, coeffs: [0, 0, 0, 0, 0]
extrin = depth_profile.get_extrinsics_to(color_profile)
print("depth_extrin:", extrin)
# rotation: [0.999984, -0.00420567, -0.00380472, 0.00420863, 0.999991, 0.00076919, 0.00380145, -0.00078519, 0.999992]
# translation: [0.0147755, 0.000203265, 0.00051274]

