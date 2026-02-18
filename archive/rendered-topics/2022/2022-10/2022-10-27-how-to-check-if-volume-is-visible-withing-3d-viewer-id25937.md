# How to check if volume is visible withing 3D Viewer

**Topic ID**: 25937
**Date**: 2022-10-27
**URL**: https://discourse.slicer.org/t/how-to-check-if-volume-is-visible-withing-3d-viewer/25937

---

## Post #1 by @hannahm (2022-10-27 17:00 UTC)

<p>In my custom app, I’ve run into a problem where even if a user has set something as visible, it isnt being shown within the 3D viewer. To remedy this, I’m trying to find whether a volume is currently visible within the 3D viewer and update the display if the volume isnt visible.</p>
<p>I had originally tried to use the <a href="https://vtk.org/doc/nightly/html/classvtkCamera.html#a63ac225662fc7b81628366a7b3b7096c" rel="noopener nofollow ugc"><code>GetFrustumPlanes()</code></a> method with the vtkCamera and check if any of the corners of the volume bounds fall within said bounds.</p>
<pre><code class="lang-auto">        cam = slicer.app.layoutManager().threeDWidget(index).threeDView().cameraNode()

        planes = [0.0]*24
        aspect = cam.GetCamera().GetExplicitAspectRatio()
        cam.GetCamera().GetFrustumPlanes(aspect, planes)

        # Set up frustum planes left,right,bottom,top,far,near
        planes_list = []
        planes_list.append([planes[0],  planes[1],  planes[2],  planes[3]])
        planes_list.append([planes[4],  planes[5],  planes[6],  planes[7]])
        planes_list.append([planes[8],  planes[9],  planes[10], planes[11]])
        planes_list.append([planes[12], planes[13], planes[14], planes[15]])
        planes_list.append([planes[16], planes[17], planes[18], planes[19]])
        planes_list.append([planes[20], planes[21], planes[22], planes[23]])

        # Get Bounds of volume
        bounds = [0] * 6
        volume_node.GetBounds(bounds)

        # Find the corners
        corners = []
        corners.append([bounds[0], bounds[2], bounds[4]])
        corners.append([bounds[0], bounds[2], bounds[5]])
        corners.append([bounds[0], bounds[3], bounds[4]])
        corners.append([bounds[0], bounds[3], bounds[5]])
        corners.append([bounds[1], bounds[2], bounds[4]])
        corners.append([bounds[1], bounds[2], bounds[5]])
        corners.append([bounds[1], bounds[3], bounds[4]])
        corners.append([bounds[1], bounds[3], bounds[5]])

        # All values need to be positive or 0
        in_bounds = False
        for corner in corners:
            if in_bounds:
                break
            for plane in planes_list:
                if in_bounds:
                    break
                res = plane[0] * corner[0] + plane[1] * corner[1] + plane[2] * corner[2] + plane[3]
                logging.debug(f"{plane[0]} * {corner[0]} + {plane[1]} * {corner[1]} + {plane[2]} * {corner[2]} + {plane[3]} = {res}")
                if (res) &gt;= 0:
                    in_bounds = True

        seen = "visible" if in_bounds else "not visible"
        logging.debug(f"I think that the markup is {seen}")
</code></pre>
<p>However, this proved to not work very well, as I could move the volume out of the 3D viewing region and it would still be marked as “visible”.</p>
<p>Is there a good way to check if a volume is currently visible within the 3D viewer?</p>

---
