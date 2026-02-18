# How to map a projector's image to a model(AR) precise?

**Topic ID**: 13569
**Date**: 2020-09-19
**URL**: https://discourse.slicer.org/t/how-to-map-a-projectors-image-to-a-model-ar-precise/13569

---

## Post #1 by @timeanddoctor (2020-09-19 19:54 UTC)

<p>How to map a projector’s image to a 3d printing model of brain(AR) precise?</p>

---

## Post #2 by @timeanddoctor (2020-09-19 20:31 UTC)

<p>Towards portable image guidance and automatic patient registration using an RGB-D camera and video projector</p>
<p>I read this paper and want to project the points to a model but It is not so easy to. The image is too smal and I need to take the projector move to let the image overlap.</p>

---

## Post #3 by @ColtonBarr (2020-09-20 16:00 UTC)

<p>You’ll need some way to determine the pose of the 3D printed object relative to the projector - in the paper we start by finding the pose of the object relative to a depth camera. This requires extracting a point cloud of the object from a depth image (module for that <a href="https://github.com/PerkLab/DepthImageToPointCloud" rel="noopener nofollow ugc">here</a>) and performing ICP registration between a model of the object and the object point cloud (we used the <a href="http://www.slicerigt.org/wp/" rel="noopener nofollow ugc">SlicerIGT</a> Model Registration module). The position of the depth camera relative to the projector can be found using the <a href="https://github.com/bytedeco/procamcalib" rel="noopener nofollow ugc">ProCamCalib</a> tool. Once the target point on the object in the projector’s coordinate system is known, the 3D target point must be converted to 2D pixel coordinates. You can then generate an image with a small circle at this position and send it to the projector.</p>
<p>Let me know if there’s a specific part of the paper’s workflow I can clarify.</p>

---

## Post #4 by @timeanddoctor (2020-09-22 12:24 UTC)

<p>Thank you very much.  I still confused by this:The 3D target point must be converted to 2D pixel coordinates.</p>
<ol>
<li>
<p>I donnot know how to read  (x,y) coordinate in the 3d view(or just simple remove the “z” axis information of the points).</p>
</li>
<li>
<p>And if I get the .xml for the camera and the projector, should I use it by the opencv just like calibrate a picture?</p>
</li>
</ol>

---

## Post #5 by @ColtonBarr (2020-09-23 16:41 UTC)

<p>The projector can be treated as the inverse of a pinhole camera model, so we can make use of the same equations to convert between pixel coordinates and 3D coordinates. Given the point [X Y Z] in the camera’s coordinate system solve for [u v] to get the same point in projector pixel coordinates:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5b2500ed68cbede61697f9d4040f4a128bf74f8.png" alt="image" data-base62-sha1="wLZnbBDh54LQiUyJgr4MCJbWPPi" width="579" height="208"></p>
<p>Further info on this equation <a href="https://docs.opencv.org/2.4.13/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html" rel="noopener nofollow ugc">here</a>.</p>
<p>That’s correct - the camera parameters from the ProCamCalib .xml should be used for camera calibration, and the projector parameters are used in the above equation.</p>

---

## Post #6 by @timeanddoctor (2020-10-02 05:13 UTC)

<p>Dear ColtonBarr:</p>
<p>Thank you very much!</p>
<p>Should I build a vtk sense with a cameraMimicProjector to mimic the real projector first? I get the intrinsics and extrinsics of projector and I don’t know how to define the cameraMimicProjector in vkt/slicer?</p>

---
