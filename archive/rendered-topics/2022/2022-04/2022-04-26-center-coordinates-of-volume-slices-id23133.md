---
topic_id: 23133
title: "Center Coordinates Of Volume Slices"
date: 2022-04-26
url: https://discourse.slicer.org/t/23133
---

# Center coordinates of volume slices?

**Topic ID**: 23133
**Date**: 2022-04-26
**URL**: https://discourse.slicer.org/t/center-coordinates-of-volume-slices/23133

---

## Post #1 by @rbumm (2022-04-26 19:36 UTC)

<p>How do I get the center coordinates for a volume that is shifted to the left and zoomed in a bit  during maniplations?</p>
<p>Example: from</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/147ac1b9565b50508fb2e0c32f55bc8064d3bb54.jpeg" data-download-href="/uploads/short-url/2VaynuGpRAwlud6MVKkJUTSC7mk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/147ac1b9565b50508fb2e0c32f55bc8064d3bb54.jpeg" alt="image" data-base62-sha1="2VaynuGpRAwlud6MVKkJUTSC7mk" width="690" height="456" data-dominant-color="5D5C5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">701×464 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>to</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/491a480b73ac18f205fc9a7285368eda936d2020.jpeg" data-download-href="/uploads/short-url/aqHa6HWOE5L32xbS8637NpaOm0o.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/491a480b73ac18f205fc9a7285368eda936d2020.jpeg" alt="image" data-base62-sha1="aqHa6HWOE5L32xbS8637NpaOm0o" width="690" height="437" data-dominant-color="6E6C6B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">711×451 41.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am interested in the screen coordinates. Thanks.</p>

---

## Post #2 by @mau_igna_06 (2022-04-26 22:42 UTC)

<p>I think you may need to use <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLSliceNode.html#a8ebef5d6a77bcabc4282ebc59651ac52">this method</a> to get the XYToRASMatrix and invert it, then transform the sliceCenterRAS with it</p>
<p>I’m not 100% sure it will work, hope it helps</p>

---

## Post #3 by @rbumm (2022-04-27 09:18 UTC)

<p>Thanks, Mauro, I think this got me on the right track.</p>
<p>There is a <a href="https://github.com/Slicer/Slicer/blob/55aa11474f67fe1fc7ebef3feab1746da9338772/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation2D.cxx#L161">function in vtkSlicerMarkupsWidgetRepresentation2D</a> which I could use with a world coordinate of 0.,0.,0. to be at the center of the CT volume and receive it’s display coordinate.</p>

---

## Post #4 by @mau_igna_06 (2022-04-27 09:54 UTC)

<p>I think you would need the sliceCenterRAS, that normally is not (0,0,0). You can get it by averaging the bounds on each axis of the corresponding CT volume</p>
<p>Hope it helps</p>

---

## Post #5 by @rbumm (2022-04-29 10:22 UTC)

<p>Sorry, that has not solved it for me yet.</p>
<p>Managed to call GetXYToRAS() and to do the invert. Could anyone explain where the above metioned  “sliceCenterRAS”  is and how it is used?<br>
Or how I could read the centers from the vtkMatrix4x4 matrix?</p>
<p>I would need to get CT volume centers as xy display coordinates for each axial, coronal and saggital 2D view.</p>
<p>Thanks.</p>

---

## Post #6 by @mau_igna_06 (2022-04-29 17:37 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="23133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>I would need to get CT volume centers as xy display coordinates for each axial, coronal and saggital 2D view.</p>
</blockquote>
</aside>
<p>Yes. Sorry, that’s the correct name for the variable volumeCenterRAS, not sliceCenterRAS.</p>
<p>And you can get it like this:</p>
<pre><code class="lang-auto">bounds=[0,0,0,0,0,0]
volume = getNode('myCT')
volume.GetRASBounds(bounds)
volumeCenterRAS = [(bounds[1]+bounds[0])/2,(bounds[3]+bounds[2])/2,(bounds[5]+bounds[4])/2,1]
</code></pre>
<p>I think this should work as RASToXY is a projection matrix:<br>
<code>RASToXY.MultiplyPoint(volumeCenterRAS, sliceCenterXY)</code></p>
<p>Please let me know how it goes</p>

---

## Post #7 by @rbumm (2022-04-29 18:46 UTC)

<p>Thx Mauro, can only try that out next week. I´ll be doing this in C++ and need to see how to get to the volume node reliably in that module I am working on.</p>

---

## Post #8 by @rbumm (2022-05-04 15:57 UTC)

<p>Think I got it working (C++) by</p>
<pre><code class="lang-auto">//----------------------------------------------------------------------
void GetBackgroundVolumeXYCenter(double slicePos[2])
{
    vtkMRMLSliceCompositeNode* compositeNode = nullptr;
    compositeNode = vtkMRMLSliceCompositeNode::SafeDownCast(this-&gt;GetSliceNode()-&gt;GetScene()-&gt;GetFirstNodeByClass("vtkMRMLSliceCompositeNode"));
    const char* backgroundVolumeID = compositeNode-&gt;GetBackgroundVolumeID();

    double volumeBounds[6] = { 0.0 };
    double volumeCenterRAS[4] = { 0.0 };
    double centerPosDisplay[4] = { 0.0 };

    if (backgroundVolumeID)
    {
        vtkMRMLScalarVolumeNode* sliceBackgroundVolumeNode = vtkMRMLScalarVolumeNode::SafeDownCast(this-&gt;GetSliceNode()-&gt;
            GetScene()-&gt;GetNodeByID(backgroundVolumeID));
        if (sliceBackgroundVolumeNode)
        {
            sliceBackgroundVolumeNode-&gt;GetRASBounds(volumeBounds);
            // xmin,ymax,ymin,ymax,zmin,zmax
            volumeCenterRAS[0] = (volumeBounds[1] + volumeBounds[0]) / 2.;
            volumeCenterRAS[1] = (volumeBounds[3] + volumeBounds[2]) / 2.;
            volumeCenterRAS[2] = (volumeBounds[5] + volumeBounds[4]) / 2.;
            volumeCenterRAS[3] = 1.;
            this-&gt;GetWorldToSliceCoordinates(volumeCenterRAS, centerPosDisplay);
        }
    }
    slicePos[0] = centerPosDisplay[0];
    slicePos[1] = centerPosDisplay[1];
}
</code></pre>
<p>This assumes you have a function this-&gt;GetSliceNode() and this-&gt;GetWorldToSliceCoordinates() in your code, as in  <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation2D.cxx">vtkSlicerMarkupsWidgetRepresentation2D</a></p>

---
