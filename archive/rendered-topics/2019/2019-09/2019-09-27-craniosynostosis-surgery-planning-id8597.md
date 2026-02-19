---
topic_id: 8597
title: "Craniosynostosis Surgery Planning"
date: 2019-09-27
url: https://discourse.slicer.org/t/8597
---

# Craniosynostosis surgery planning

**Topic ID**: 8597
**Date**: 2019-09-27
**URL**: https://discourse.slicer.org/t/craniosynostosis-surgery-planning/8597

---

## Post #1 by @martig (2019-09-27 22:18 UTC)

<p>Hi,</p>
<p>I’m trying to do craniosynostosis surgery planning in Slicer. Basically I need to accurately define two intersecting planes by fiducials and then separate a piece of the skull like on the first image → <img src="http://craniofacialteamtexas.com/wp-content/uploads/2015/07/Distraction-Osteogenesis-Bone-Lengthening-500x275.jpg" alt="" role="presentation" width="500" height="275"><br>
So far I have not managed to figure out how to do it in a manner that allows easily modifying the cut planes.<br>
I have tried this python script → <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a><br>
But I have not figured out how to use it for defining two planes. It would be perfect if I could define two intersecting surfaces with 4 fiducials.<br>
Also, the Angle Planes module seems to almost do just what I need, but I can’t use the planes it generates to cut the model.</p>
<p>The last time I did it in Meshmixer. Not much fun, but the cut planes are easy to manipulate at least.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6782abdabb1f1511f393bf63569a6d8a9606dcab.jpeg" data-download-href="/uploads/short-url/eLH8LGQhfce3ntRGtt1uAyESIPh.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6782abdabb1f1511f393bf63569a6d8a9606dcab_2_588x500.jpeg" alt="PNG" data-base62-sha1="eLH8LGQhfce3ntRGtt1uAyESIPh" width="588" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6782abdabb1f1511f393bf63569a6d8a9606dcab_2_588x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6782abdabb1f1511f393bf63569a6d8a9606dcab_2_882x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6782abdabb1f1511f393bf63569a6d8a9606dcab.jpeg 2x" data-dominant-color="646363"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">891×757 87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Do you have any ideas on how to do it Slicer?</p>
<p>Best Regards,<br>
Martin</p>

---

## Post #2 by @lassoan (2019-09-28 16:00 UTC)

<p>Maybe <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/EasyClip" rel="nofollow noopener">Easy clip extension</a> can fulfill all your requirements.</p>
<p>If you prefer to position planes using markup fiducials then the script needs only a small modification to place 2 planes using 4 fiducials:</p>
<pre><code class="lang-python"># Update plane from fiducial points
def UpdateSlicePlane(param1=None, param2=None):
  # Get point positions as numpy array
  import numpy as np
  nOfFiduciallPoints = markups.GetNumberOfFiducials()
  if nOfFiduciallPoints &lt; 3:
    return  # not enough points
  points = np.zeros([3,nOfFiduciallPoints])
  for i in range(0, nOfFiduciallPoints):
    markups.GetNthFiducialPosition(i, points[:,i])
  # Compute plane1 position and normal
  planePosition = points[:,0]
  planeX = points[:,1] - points[:,0]
  planeNormal1 = np.cross(points[:,1] - points[:,0], points[:,2] - points[:,0])
  sliceNode1.SetSliceToRASByNTP(planeNormal1[0], planeNormal1[1], planeNormal1[2],
    planeX[0], planeX[1], planeX[2],
    planePosition[0], planePosition[1], planePosition[2], 0)
  if nOfFiduciallPoints&gt;3:
    planeNormal2 = np.cross(points[:,1] - points[:,0], points[:,3] - points[:,0])
    sliceNode2.SetSliceToRASByNTP(planeNormal2[0], planeNormal2[1], planeNormal2[2],
        planeX[0], planeX[1], planeX[2],
        planePosition[0], planePosition[1], planePosition[2], 0)

# Get markup node from scene
sliceNode1 = slicer.app.layoutManager().sliceWidget('Red').mrmlSliceNode()
sliceNode2 = slicer.app.layoutManager().sliceWidget('Green').mrmlSliceNode()
markups = slicer.util.getNode('F')

# Update slice plane manually
UpdateSlicePlane()

# Update slice plane automatically whenever points are changed
markupObservation = [markups, markups.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, UpdateSlicePlane, 2)]
</code></pre>
<p>If you cut solid objects then you can use Segment editor module’s Scissors effect. Scissors effect has the option to restrict the cut to one side of the current slice. You can also use Scissors effect to separate segments along arbitrarily drawn lines, not just planes.</p>

---

## Post #3 by @martig (2019-10-02 06:58 UTC)

<p>Andras,</p>
<p>Thank you for the suggestions and the modification to the script. The 4 fiducials for 2 planes work perfectly. The issue with Easy Clip is that it’s quite difficult to exactly position the planes in relation to features of the skull. For me it is easiest if the edges of the planes pass through the points I have defined.</p>
<p>Best Regards,<br>
Martin</p>

---

## Post #4 by @martig (2019-10-03 10:28 UTC)

<p>Do you know if its possible to export the result of Clipping Planes feature under the Models module?<br>
This is exactly what I would need as output.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59ce8969250f7c3431a962ca886844ac8264cfa1.png" data-download-href="/uploads/short-url/cOsZRGVDQVQDEsOIP7S90W6DU9H.png?dl=1" title="model_clip" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59ce8969250f7c3431a962ca886844ac8264cfa1_2_690x256.png" alt="model_clip" data-base62-sha1="cOsZRGVDQVQDEsOIP7S90W6DU9H" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59ce8969250f7c3431a962ca886844ac8264cfa1_2_690x256.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59ce8969250f7c3431a962ca886844ac8264cfa1_2_1035x384.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59ce8969250f7c3431a962ca886844ac8264cfa1.png 2x" data-dominant-color="C9C5C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model_clip</span><span class="informations">1204×447 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I noticed that the Easy Clip planes and the planes generated by the Python script can go out of sync. Is it possible to resynchronise them?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/933b6b14d0b024b9bc858695c4444ebe00fa49d6.png" data-download-href="/uploads/short-url/l0tusm16qNTcFYcePBcBpylAHHg.png?dl=1" title="easy_clip_sync" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/933b6b14d0b024b9bc858695c4444ebe00fa49d6_2_498x500.png" alt="easy_clip_sync" data-base62-sha1="l0tusm16qNTcFYcePBcBpylAHHg" width="498" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/933b6b14d0b024b9bc858695c4444ebe00fa49d6_2_498x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/933b6b14d0b024b9bc858695c4444ebe00fa49d6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/933b6b14d0b024b9bc858695c4444ebe00fa49d6.png 2x" data-dominant-color="A39FBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">easy_clip_sync</span><span class="informations">616×618 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best Regards,<br>
Martin</p>

---
