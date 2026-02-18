# How to record vtkCamera transform matrix?

**Topic ID**: 26933
**Date**: 2022-12-27
**URL**: https://discourse.slicer.org/t/how-to-record-vtkcamera-transform-matrix/26933

---

## Post #1 by @StephenLeePeng (2022-12-27 01:37 UTC)

<p>Dear all,<br>
recently I met a problem.<br>
In Volume Rendering module, I created a volume rendering with a vtkMarkupsROI named nodule_roi. The nodule volume is surrounded by nodule_roi.<br>
Firstly, I adjust 3d view controller to A. So in the world coordinate system, the camera is in the axis of negative y (-y).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f870407fd0d4a8d529403e8304ecef36bdc5091.jpeg" data-download-href="/uploads/short-url/blwZnPbEXueXtL6gjjgCEBqpHb3.jpeg?dl=1" title="camera1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f870407fd0d4a8d529403e8304ecef36bdc5091_2_647x500.jpeg" alt="camera1" data-base62-sha1="blwZnPbEXueXtL6gjjgCEBqpHb3" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f870407fd0d4a8d529403e8304ecef36bdc5091_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f870407fd0d4a8d529403e8304ecef36bdc5091_2_970x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f870407fd0d4a8d529403e8304ecef36bdc5091.jpeg 2x" data-dominant-color="512F2A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">camera1</span><span class="informations">1101×850 45.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Secondly, I rotate the nodule volume to any direction. Of course I know, the nodule volume is not rotated anyway in the world, the camera is rotated actually. As the nodule volume and nodule_roi is related, so the nodule volume and nodule_roi seems to be rotated in the same time.<br>
This will cause the front plane of nodule roi is not vertical to the line between the center of nodule volume and camera position.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e966478e44acf551ca1517bde989af9b65e95a8.jpeg" data-download-href="/uploads/short-url/klo0WmLA8dnYfyECv7mDPh7djG8.jpeg?dl=1" title="camera2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e966478e44acf551ca1517bde989af9b65e95a8_2_673x500.jpeg" alt="camera2" data-base62-sha1="klo0WmLA8dnYfyECv7mDPh7djG8" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e966478e44acf551ca1517bde989af9b65e95a8_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e966478e44acf551ca1517bde989af9b65e95a8_2_1009x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e966478e44acf551ca1517bde989af9b65e95a8.jpeg 2x" data-dominant-color="412821"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">camera2</span><span class="informations">1148×852 61.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So, I want to record the transform matrix of camera during the rotation, and apply this transform matrix to the nodule roi, to achieve the front plane of nodule roi is always vertical to the line, between center of nodule volume and current camera position.</p>
<p>This picture is I adjust the nodule roi manually, rotate by three axis, to achieve the result I expected to achieve. But I want to achieved it automatically, by recording the transform matrix of camera, then apply to the nodule roi.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4470d218bbf9f9025ecf879c23610f64f0122d3.jpeg" data-download-href="/uploads/short-url/s0lOh6wsfGWcOxu9dvXx9k4HcqL.jpeg?dl=1" title="camera3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4470d218bbf9f9025ecf879c23610f64f0122d3_2_662x500.jpeg" alt="camera3" data-base62-sha1="s0lOh6wsfGWcOxu9dvXx9k4HcqL" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4470d218bbf9f9025ecf879c23610f64f0122d3_2_662x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4470d218bbf9f9025ecf879c23610f64f0122d3_2_993x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4470d218bbf9f9025ecf879c23610f64f0122d3.jpeg 2x" data-dominant-color="4B2E27"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">camera3</span><span class="informations">1126×850 63.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the method I think, or may be there are more efficient way to achieve this goal.<br>
Any advice will be appreciated! <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2022-12-27 14:56 UTC)

<p>World you like to automatically rotate the volume rendering clung ROI to keep its axes aligned with the camera’s normal and view-up axes?</p>

---

## Post #3 by @StephenLeePeng (2022-12-29 12:21 UTC)

<p>Thank you for your reply.<br>
I upload a picture to show my goal.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f47c1807cdbeabcf59846c6a5099fe3fe55213d.jpeg" data-download-href="/uploads/short-url/2baTH2dQM6lGTR7VOihQBtdjxg1.jpeg?dl=1" title="ROI orientation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f47c1807cdbeabcf59846c6a5099fe3fe55213d_2_457x500.jpeg" alt="ROI orientation" data-base62-sha1="2baTH2dQM6lGTR7VOihQBtdjxg1" width="457" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f47c1807cdbeabcf59846c6a5099fe3fe55213d_2_457x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f47c1807cdbeabcf59846c6a5099fe3fe55213d_2_685x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f47c1807cdbeabcf59846c6a5099fe3fe55213d.jpeg 2x" data-dominant-color="FBF7F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROI orientation</span><span class="informations">794×867 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Actor is as camera, Cube and shpere display volume and nodule, and the plane source represent the front plane of vtkMarkupsROI.</p>
<p>The first picture, the volume rendering is +A, adjust view controller to A.<br>
The second picture, the volume rendering is rotated by user. Now, If I add a button, when I push the button, I hope the vtkMarkupsROI is rotated, and the front plane of ROI is vertical to the line between nodule center and camera pos, not surround the volume  as before.</p>
<p>According test, I find a interface of the camera, which is camera.GetViewTransformMatrix().<br>
If I rotate the volume by any direction, and I called the camera.GetViewTransformMatrix(), I can get a rotation matrix of camera. Then, I transpose the camera view transfrom matrix, and apply the vtkMarkupsROI, then the ROI will rotate, to achieve the front plane of ROI is vertical the line between nodule center and camera.</p>
<p>But the center of ROI is not aligned to nodule center. And I called SetCenter() with the nodule center, then the ROI will moved to the destination as the second picture showed.</p>
<pre><code class="lang-auto">    # Get camera view transform matrix &amp; Matrix transpose
    threeDView = slicer.app.layoutManager().threeDWidget(0).threeDView()
    renderer = threeDView.renderWindow().GetRenderers().GetFirstRenderer()
    camera = renderer.GetActiveCamera()
    camera_trans_matrix = camera.GetViewTransformMatrix()

    matrix_zero = [0] * 16
    origin_matrix.DeepCopy(matrix_zero, origin_matrix)
    camera_trans_reverse = np.array(matrix_zero).reshape(4, 4).transpose()
    roiNode.ApplyTransformMatrix(slicer.util.vtkMatrixFromArray(camera_trans_reverse))
</code></pre>

---

## Post #4 by @lassoan (2022-12-29 14:06 UTC)

<p>I would not recommend to mess with the camera matrices but use the camera’s SetFocalPoint (defines center of rotation), and SetPosition+SetViewUp (defines orientation) methods instead. You can also attach an observer to the camera and keep the ROI node parallel with the camera normal and up vector, if you want to keep the target cut in half from various viewing directions.</p>

---

## Post #5 by @StephenLeePeng (2022-12-30 05:20 UTC)

<p>Thank you for reply and supplied two methods.</p>
<p>Frist method, As the volume and ROI use the single camera. If I called interface of camea, such as SetFocalPoint, SetPosition and SetViewUp, the volume position and orientation displayed will be changed at the same time, which is not to be expected. I only want to rotate the ROI, the volume can not be rotated or moved at the same time.</p>
<p>Second method, could you please show me some example codes, I am not familiar with how to add observer with camera, and applied the camera rotate events to the ROI, to achieve my target.</p>
<p>Any advice will be appreciated!</p>

---
