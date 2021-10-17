import math
import numpy as np


class DevNumpy():


    def distance_pt_pts(self, p, points):
        
        p_np = np.array(p, np.float64)
        points_np = np.array(points, np.float64)
        
        ### Define Vector2pt
        u = points_np - p_np
        # print(u)

        ### Get VectorSize ()= Distance)
        d = np.linalg.norm(u, axis=1)
        # print(d)

        return d


    def distance_line_pts_points_2d_np(self, p0, p1, points):
        
        """
        Distance (line (p0 to p1) - points)
        Points = [[xa, ya], [xb, yb], ...]
        Points_Transpose = [[xa, xa, ...], [ya, yb, ...]]
        """

        ### List to NumpyArray with cast
        p0_np = np.array(p0, np.float64)
        p1_np = np.array(p1, np.float64)
        points_np = np.array(points, np.float64)
        
        ### Transpose
        points_np_T = points_np.T
        
        x0 = p0_np[0]
        y0 = p0_np[1]
        x1 = p1_np[0]
        y1 = p1_np[1]
        xx = points_np_T[0]
        yy = points_np_T[1]


        v0 = abs((y1-y0)*xx - (x1-x0)*yy + x1*y0 -  y1*x0)
        v1 = math.sqrt(math.pow((y1 - y0), 2) + math.pow((x1 - x0), 2))
        d = v0 / v1

        # print(d)

        return d




dv = DevNumpy()


################################################################


### Test : Line-Points with Numpy

a = [-4, 2]
b = [3, 5]
c = [5.1, 2]
d = [-3.3, 10]
e = [3.9, 4]

# a = np.array(a)
# print(a)

dd = dv.distance_line_pts_points_2d_np(a, b, [c])
# print(dd)

dd = dv.distance_line_pts_points_2d_np(a, b, [c, d, e])
# print(dd)


################################################################


### Test : Point-Points with Numpy

a = [-4, 2]
b = [3, 5]
c = [5.1, 2]
d = [-3.3, 10]

dd = dv.distance_pt_pts(a, [b, c, d])
print(dd)
