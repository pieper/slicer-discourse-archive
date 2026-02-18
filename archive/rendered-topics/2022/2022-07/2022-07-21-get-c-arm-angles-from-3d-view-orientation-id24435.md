# Get C-arm angles from 3D view orientation

**Topic ID**: 24435
**Date**: 2022-07-21
**URL**: https://discourse.slicer.org/t/get-c-arm-angles-from-3d-view-orientation/24435

---

## Post #1 by @donghmu (2022-07-21 17:24 UTC)

<p>Hi. I am an interventional cardiologist. Currently I am interested in pre-planning for my intervention. In detail, I want to determine the optimal angles for setting the X-ray views.<br>
Is there any extension, or Python codes for displaying these parameter (as I show in the following image).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/591ad2835fd5b293accbcd4a551d47e33ef73249.jpeg" data-download-href="/uploads/short-url/cIfXBH9kBoBSrTIBblU6cy0RGzf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/591ad2835fd5b293accbcd4a551d47e33ef73249_2_332x500.jpeg" alt="image" data-base62-sha1="cIfXBH9kBoBSrTIBblU6cy0RGzf" width="332" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/591ad2835fd5b293accbcd4a551d47e33ef73249_2_332x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/591ad2835fd5b293accbcd4a551d47e33ef73249_2_498x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/591ad2835fd5b293accbcd4a551d47e33ef73249.jpeg 2x" data-dominant-color="29241E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">641×963 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Instead of only displaying the cube (for orientation), can we read the detail information about the related angles?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d42cf48f7a8e1b8903f00404595c6bfa3db3b24b.jpeg" data-download-href="/uploads/short-url/ugZxtXupZBpkWwcnLMbFIA8JNLd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d42cf48f7a8e1b8903f00404595c6bfa3db3b24b_2_574x500.jpeg" alt="image" data-base62-sha1="ugZxtXupZBpkWwcnLMbFIA8JNLd" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d42cf48f7a8e1b8903f00404595c6bfa3db3b24b_2_574x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d42cf48f7a8e1b8903f00404595c6bfa3db3b24b_2_861x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d42cf48f7a8e1b8903f00404595c6bfa3db3b24b.jpeg 2x" data-dominant-color="A2978E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">999×869 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks in advanced!</p>

---

## Post #2 by @pieper (2022-07-21 17:29 UTC)

<p>There isn’t a dedicated planning tool that I’m aware of.  You may want to just use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html">Markups Angles</a> to design your imaging plan and then match the device as best you can.</p>

---

## Post #3 by @lassoan (2022-07-21 19:03 UTC)

<p>You can copy-paste this code snippet to the Python console to show the anatomical angles (LAO/RAO, CRA/CAU) of the C-arm in the corner of a 3D view:</p>
<pre><code class="lang-python">threeDViewIndex = 0  # change this to show angles in a different 3D view

def positionerAngleFromViewNormal(viewNormal):
    # According to https://www5.informatik.uni-erlangen.de/Forschung/Publikationen/2014/Koch14-OVA.pdf
    nx = -viewNormal[0]  # L
    ny = -viewNormal[1]  # P
    nz =  viewNormal[2]  # S
    import math
    if abs(ny) &gt; 1e-6:
        primaryAngleDeg = math.atan(-nx/ny) * 180.0 / math.pi
    elif nx &gt;= 0:
        primaryAngleDeg = 90.0
    else:
        primaryAngleDeg = -90.0
    secondaryAngleDeg = math.asin(nz) * 180.0 / math.pi
    return [primaryAngleDeg, secondaryAngleDeg]

def formatPositionerAngle(positionerAngles):
    primaryAngleDeg, secondaryAngleDeg = positionerAngles
    text =  f'{"RAO" if primaryAngleDeg &lt; 0 else "LAO"} {abs(primaryAngleDeg):.1f}\n'
    text += f'{"CRA" if secondaryAngleDeg &lt; 0 else "CAU"} {abs(secondaryAngleDeg):.1f}'
    return text

def cameraUpdated(cameraNode, view):
    viewNormal = cameraNode.GetCamera().GetDirectionOfProjection()
    positionerAngleText = formatPositionerAngle(positionerAngleFromViewNormal(viewNormal))
    view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight, positionerAngleText)
    view.cornerAnnotation().GetTextProperty().SetColor(1,1,0)  # yellow
    view.scheduleRender()

layoutManager = slicer.app.layoutManager()
view = layoutManager.threeDWidget(threeDViewIndex).threeDView()
threeDViewNode = view.mrmlViewNode()
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)
cameraObservation = cameraNode.AddObserver(vtk.vtkCommand.ModifiedEvent, lambda caller, event, view=view: cameraUpdated(caller, view))

cameraUpdated(cameraNode, view)

# Execute the next line to stop updating the positioner angles in the view corner
# cameraNode.RemoveObserver(cameraObservation)
</code></pre>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe59764902aeb19599d558cd3b73a7ac4fbecf1a.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe59764902aeb19599d558cd3b73a7ac4fbecf1a.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe59764902aeb19599d558cd3b73a7ac4fbecf1a.mp4</a>
    </source></video>
  </div><p></p>
<p>We are developing a fluoro simulator module for interventional cardiology as part of the SlicerHeart project. The module will be able to display not just the angles but simulated fluoro images and compute optimal viewing angles, etc. We’ll release it when the results are first published - probably within a year.</p>

---

## Post #4 by @donghmu (2022-07-22 01:26 UTC)

<p>Kindly thanks for your super helpful reply <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"><br>
Hope to see your module soon.<br>
Thank you so much!</p>

---

## Post #5 by @cloudman (2023-04-13 06:52 UTC)

<p>Hi, my image is XA, I want to display the anatomical angles of the C-arm (LAO/RAO, CRA/CAU) in the corner of the red slice viewer, I try to modify your code, but an error is reported when running, how do I modify it?</p>
<pre><code class="lang-auto">def positionerAngleFromViewNormal(viewNormal):
    # According to https://www5.informatik.uni-erlangen.de/Forschung/Publikationen/2014/Koch14-OVA.pdf
    nx = -viewNormal[0]  # L
    ny = -viewNormal[1]  # P
    nz =  viewNormal[2]  # S
    import math
    if abs(ny) &gt; 1e-6:
        primaryAngleDeg = math.atan(-nx/ny) * 180.0 / math.pi
    elif nx &gt;= 0:
        primaryAngleDeg = 90.0
    else:
        primaryAngleDeg = -90.0
    secondaryAngleDeg = math.asin(nz) * 180.0 / math.pi
    return [primaryAngleDeg, secondaryAngleDeg]

def formatPositionerAngle(positionerAngles):
    primaryAngleDeg, secondaryAngleDeg = positionerAngles
    text =  f'{"RAO" if primaryAngleDeg &lt; 0 else "LAO"} {abs(primaryAngleDeg):.1f}\n'
    text += f'{"CRA" if secondaryAngleDeg &lt; 0 else "CAU"} {abs(secondaryAngleDeg):.1f}'
    return text

def cameraUpdated(cameraNode, view):
    viewNormal = cameraNode.GetCamera().GetDirectionOfProjection()
    positionerAngleText = formatPositionerAngle(positionerAngleFromViewNormal(viewNormal))
    view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight, positionerAngleText)
    view.cornerAnnotation().GetTextProperty().SetColor(1,1,0)  # yellow
    view.scheduleRender()

layoutManager = slicer.app.layoutManager()
sliceViewName = layoutManager.sliceViewNames()[0]
view = layoutManager.sliceWidget(sliceViewName).sliceView()
sliceViewNode = view.mrmlViewNode()
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(sliceViewNode)
cameraObservation = cameraNode.AddObserver(vtk.vtkCommand.ModifiedEvent, lambda caller, event, view=view: cameraUpdated(caller, view))

cameraUpdated(cameraNode, view)
</code></pre>

---

## Post #6 by @lassoan (2023-04-19 11:31 UTC)

<aside class="quote no-group" data-username="cloudman" data-post="5" data-topic="24435">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/41988e/48.png" class="avatar"> cloudman:</div>
<blockquote>
<p>but an error is reported</p>
</blockquote>
</aside>
<p>What is the error? What Slicer version do you use?</p>

---

## Post #7 by @cloudman (2023-04-21 07:52 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> The error is:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; sliceViewNode = view.mrmlViewNode()
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: qMRMLSliceView has no attribute named 'mrmlViewNode'
</code></pre>
<p>I need to display angles in red slice viewer, the image is 2D, so I modified your 3D viewer code, but it is wrong, I don’t know how to modify it.</p>

---

## Post #8 by @lassoan (2023-04-23 12:26 UTC)

<p>The script above solves a more complex task: computing C-arm angles from the camera viewpoint in a 3D view. You can use it to find a good angulation that you can just on your C-arm.</p>
<p>If you already have an X-ray angiography image sequence then the C-arm angles are already stored in the DICOM series for each frame, we just need to display it.</p>
<p>For a dynamic acquisition - for showing angles changing throughout the series - we would need to create a somewhat complex script. For showing angles for a static-gantry image we could easily just change the DICOM importer to include th C-arm angle in the node name.</p>
<p>What is your overall goal? How do you plan to use XA images in Slicer?</p>

---

## Post #9 by @cloudman (2023-04-24 02:14 UTC)

<p>I just want to display the C-arm angles in red slice viewer. I found the angles are in the DICOM tags:(0018,1510) DS PositionerPrimaryAngle, (0018,1511) DS PositionerSecondaryAngle. How can I make it display as (LAO/RAO, CRA/CAU) in the red slice viewer?</p>

---

## Post #10 by @lassoan (2023-04-24 18:05 UTC)

<p>Does the C-arm move during your acquisitions? Is it enough to show the angles of the for frame of the sequence?</p>

---

## Post #11 by @cloudman (2023-04-25 06:51 UTC)

<p>The acquisition process does not move, and each sequence has an angle. I want to display the angle of the sequence after opening a sequence. The angle information is recorded in the Dicom tag, but I don’t know how to display it.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b87fb48487adcd8ada982482d442b304462d4f19.png" alt="20230425145028" data-base62-sha1="qk9sCj8z87K0OPc8cSX6JftWTVf" width="637" height="146"></p>

---

## Post #12 by @lassoan (2023-04-25 11:17 UTC)

<p>Would it be sufficient to include the angles in the node name? You can enable showing the buffer name in the slice view corner annotation.</p>

---

## Post #13 by @cloudman (2023-04-26 03:10 UTC)

<p>Yes, it’s enough, I just want the angle to be displayed.  I don’t know how to get the value of PositionerPrimaryAngle and PositionerSecondaryAngle, and then display it on the red slice viewer. I only know that I can get the angle through the following function by getting those two values:</p>
<pre><code class="lang-auto">def formatPositionerAngle(primaryAngleDeg, secondaryAngleDeg):
    text =  f'{"RAO" if primaryAngleDeg &lt; 0 else "LAO"} {abs(primaryAngleDeg):.1f}\n'
    text += f'{"CRA" if secondaryAngleDeg &lt; 0 else "CAU"} {abs(secondaryAngleDeg):.1f}'
    return text
</code></pre>

---

## Post #14 by @lassoan (2023-05-02 20:12 UTC)

<p>The angles could be added to the name of thr image at the time of DICOM import. The importer is <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMImageSequencePlugin.py">this</a> Python script, you can modify it on your computer.</p>

---

## Post #15 by @cloudman (2023-05-06 07:40 UTC)

<p>It works, Thank you！<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d29b5df656f881f7ac62242bd7f1af2e02e1588.png" alt="QQ截图20230506153341" data-base62-sha1="hRf2Yyx1KYCXcBJRPUIDXXR6lSw" width="672" height="427"></p>

---

## Post #16 by @lassoan (2024-03-26 01:38 UTC)

<p>A post was split to a new topic: <a href="/t/angle-measurement-range/35081">Angle measurement range</a></p>

---

## Post #17 by @davidneustadter (2024-10-27 13:22 UTC)

<p>Andras,</p>
<p>I was wondering if the fluoro simulator module in the SlicerHeart project has been released yet.  I could really use it for my procedure planning!  I was also wondering how accurate the simulated fluoro images will be; for instance, will they take into account the fanning of the x-ray beam and the distance from the x-ray tube focal spot to the anatomy?</p>

---

## Post #18 by @lassoan (2024-10-27 15:38 UTC)

<p>The simulated fluoro image is fully accurate in term of geometry of the cone-beam projection.</p>
<p>The paper about the cathlab simulator is in a very good shape and it will be submitted soon, so it should not take too long to release the module.</p>

---

## Post #19 by @davidneustadter (2024-10-30 08:27 UTC)

<p>Andras,</p>
<p>Thank you very much for the quick reply.  I look forward to trying the fluoro simulator, but if you haven’t submitted the article yet, then there is no telling how long it may take…  I can’t wait that long, so I am working on a poor-man’s version on my own.</p>
<p>I found your code for extracting or defining the c-arm angles, and I figured out how to adjust the colors and opacity to get a reasonable fluoro simulated images, but I am stuck on one issue… the standard fluoro image display shows the projection as viewed from the detector (head up, left side of body on right side of image when at orientation 0,0).  In slicer, the image is as viewed from the camera which mimics the x-ray tube in terms of the perspective.  For this reason the images that I obtain are flipped L-R relative to the standard fluoro display.</p>
<p>Do you have any suggestions of how to solve this?</p>
<p>Thanks,</p>
<p>David</p>

---

## Post #20 by @lassoan (2024-10-30 21:29 UTC)

<p>If you want to flip between showing the front or back of the mesh, you can use reverse perspective projection in the renderer camera. We have discussed this a couple of times on the VTK forum (for example, <a href="https://discourse.vtk.org/t/inverted-perspective-divide-in-vtk/13061/16">here</a>).</p>
<p>In the simulator in SlicerHeart we do not support flipping between rendering from the front or back, as we could achieve all visualizations that we needed without implementing this (by rendering 3D content semitransparent). Also, there may be a few things that need to be fixed (one issue that we know about is that currently GPU volume rendering is not compatible with reverse perspective projection).</p>

---

## Post #21 by @davidneustadter (2024-10-31 13:49 UTC)

<p>Andras,</p>
<p>Thanks again for the quick reply.  I am confused by something that you mention both in your recent reply and in the discussion that you linked to in the VTK forum.  In both places you say that you do not need to use reverse perspective for semi-transparent content because you can see through everything so it doesn’t matter what is in front and what is behind.  When simulating fluoro images from a volume (or creating a model view to be overlaid on fluoro images) I believe that the reverse perspective is important event for semi-transparent content because the perspective will be wrong.  Fluoro images are viewed from the perspective of the detector, such that objects closer to the x-ray tube are in the “back” and objects closer to the detector are in the “front”.  For this reason, objects in the back are larger and objects in the front are smaller, which is the opposite of normal visual or camera perspective.  I believe that this is what Daan Baas was trying to correct for, and it also what I am trying to correct for.</p>
<p>Daan Baas says that he found a 2-step solution:<br>
"The solution I ended up with required a combination of two steps:</p>
<ol>
<li>
<p>Setting the camera position to the point exactly opposite of the focal point, as seen from the camera position (i.e. rotating the camera position around the focal point 180 degrees, with the same viewUp). This gives the desired depth inverted perspective scaling, with cells of the 3D model farther away from the original camera position appearing larger than equally-sized cells closer to the camera.</p>
</li>
<li>
<p>Inverting the sign of both the X- and the Z-values in the camera’s projection transform by setting the Camera’s UserTransform matrix to an identity matrix, with -1 on both the X and Z:<br>
-1 0 0 0<br>
0 1 0 0<br>
0 0 -1 0<br>
0 0 0 1<br>
Inverting the sign of X corrects for the Left-Right flip that results from rotating the camera around the focal point.<br>
Inverting the sign of Z places the cells cells in the back our 3D model on the front and vice versa. This corrects for the Front-Back flip that results from rotating the camera around the focal point."</p>
</li>
</ol>
<p>Can you explain to me how to do his step <span class="hashtag-raw">#2</span>?  I could not find anything called “UserTransform matrix”.  Where is this and how can I change it?  (I tried changing the “AppliedTransform” matrix in the cameranode and it did not seem to have any effect")</p>
<p>Thank you so much for your help!!</p>
<p>David</p>

---

## Post #22 by @lassoan (2024-10-31 14:00 UTC)

<blockquote>
<p>In both places you say that you do not need to use reverse perspective for semi-transparent content because you can see through everything so it doesn’t matter what is in front and what is behind. When simulating fluoro images from a volume (or creating a model view to be overlaid on fluoro images) I believe that the reverse perspective is important event for semi-transparent content because the perspective will be wrong.</p>
</blockquote>
<p>Reverse perspective is not needed if the model is transparent, because you can simply place the renderer camera in the X-ray source position and all sizes will be correct. The only (very significant) limitation of this approach is that if you use opaque models then you can always just see the side of the objects that face towards the generator. Cutting the surface can help, too (for example for left atrium ablation it can be quite usable), but it depends on the geometry, so not a general solution.</p>
<aside class="quote no-group" data-username="davidneustadter" data-post="21" data-topic="24435">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davidneustadter/48/78532_2.png" class="avatar"> davidneustadter:</div>
<blockquote>
<p>Can you explain to me how to do his step <span class="hashtag-raw">#2</span>? I could not find anything called “UserTransform matrix”.</p>
</blockquote>
</aside>
<p>This is a method of the vtkCamera. You can access the VTK camera object as shown in examples in the script repository.</p>

---

## Post #23 by @SassanHashemi (2025-05-20 12:17 UTC)

<p>Slicer 5.8.1<br>
Windows 11<br>
Camera Angle Python work inconsistency</p>
<p>Dear Andras,</p>
<p>The Python code for camera angle does not work when I applied to a newly opened saved session. It works only when the Slicer app is opened fresh.</p>
<p>So, my workaround is to open Slicer, apply the Python code and then load the scene from file.</p>
<p>Not a big issue, just an FYI.</p>
<p>Thanks,<br>
Sassan</p>

---
