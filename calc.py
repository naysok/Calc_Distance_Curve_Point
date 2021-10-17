import math


class Dev():
    

    def line_pts_point_2d(self, p0, p1, point):
        
        """
        Distance (line (p0 to p1) - point)
        Point = [x, y]
        """

        x0 = float(p0[0])
        y0 = float(p0[1])
        x1 = float(p1[0])
        y1 = float(p1[1])
        xx = float(point[0])
        yy = float(point[1])
        
        v0 = abs((y1-y0)*xx - (x1-x0)*yy + x1*y0 -  y1*x0)
        v1 = math.sqrt(math.pow((y1 - y0), 2) + math.pow((x1 - x0), 2))

        d = v0 / v1
        # print(d)

        return d


    def line_pts_points_2d(self, p0, p1, points):
        
        """
        Distance (line (p0 to p1) - points)
        Points = [[x, y], [xx, yy] ...]
        """

        ds = []
        for point in points:
            d = self.line_pts_point_2d(p0, p1, point)
            ds.append(d)

        # print(ds)
        return ds




a = [-4, 2]
b = [3, 5]
c = [5.1, 2]
d = [-3.3, 10]
e = [3.9, 4]


dv = Dev()


d =  dv.line_pts_point_2d(a, b, c)
print(d)

d = dv.line_pts_points_2d(a, b, [c, d, e])
print(d)

