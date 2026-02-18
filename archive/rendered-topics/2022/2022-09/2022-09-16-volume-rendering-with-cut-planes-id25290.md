# Volume Rendering with cut planes

**Topic ID**: 25290
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/volume-rendering-with-cut-planes/25290

---

## Post #1 by @SteveRobbins (2022-09-16 04:52 UTC)

<p>I have loaded a DICOM series, can see the volume rendering.  I can use the ROI and crop to the box.    What I wanted to do is place the three orthogonal (red,green,yellow) planes and use them to cut the volume.  Image below shows the effect I wanted to create.  Is that possible in Slicer 5?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f9d126ccf5609f3509c733af9bf56be4af80427.png" alt="image" data-base62-sha1="6NcXUj0mvNegYyg6aC3L9JIxRLp" width="256" height="256"></p>

---

## Post #2 by @lassoan (2022-09-16 05:03 UTC)

<p>Yes, you can set up this visualization in Slicer. It is not volume rendering (raycasting), just a simple display of the slice views in 3D (with slice region outside the head masked out) and also showing a skin surface model (clipped with the slice view planes).</p>
<p>          <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e6d24c90190c1e4315521adc7bae274d303e861e.gif" target="_blank" rel="noopener" class="onebox">
            <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e6d24c90190c1e4315521adc7bae274d303e861e.gif" width="555" height="500">
          </a>
</p>
<p>See more information in these posts:</p>
<aside class="quote quote-modified" data-post="7" data-topic="118">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/hide-data-inside-roi-when-volume-rendering/118/7">Hide data inside ROI when Volume Rendering</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Also note that you can get almost the same result by showing slice views (with thresholding enabled for the volume, to remove black borders) and a skin surface model (slice clipping enabled to be able to see inside the head). 
Example (<a href="https://1drv.ms/u/s!Arm_AFxB9yqHr5BI0Hag1rewSdETWg">download the scene from here</a>): 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e6d24c90190c1e4315521adc7bae274d303e861e.gif" data-download-href="/uploads/short-url/wVWnFZhfQCwWyiXKAJMVk58R6OO.gif?dl=1" title="ClipIntoBrainS.gif">[image]</a>
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="2" data-topic="1406">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/partial-texture-effect-like-this/1406/2">Partial texture effect like this</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can create images like this in Slicer: 

Use Swiss skull stripper to remove the skull (or use Segment editor to do it manually)
Use slice view controllers to show slices in 3D
In Volumes module, enable thresholding to not show the black boundary around the slice; select a colormap that you like (you can also tune any existing colormap in Colors module)
Create a segment of the brain surface using Segment editor
Export segment to model using Segmentations module
Hide the segmentation (so that …
  </blockquote>
</aside>


---

## Post #3 by @SteveRobbins (2022-09-16 13:35 UTC)

<p>Hello.  I appreciate your help immensely.  You are right that the skin surface model + cut planes produces the image I reference.  That’s a great tip.  I may end up going in that direction.</p>
<p>I originally thought it would be do-able with volume rendering.  Indeed, after your response, I went back and tried some more.  I just noticed the Volume Clip module doc has a picture using ROI Box – <a href="https://www.slicer.org/w/index.php/Documentation/Nightly/Extensions/VolumeClip#/media/File:VolumeClipScreenshot3.png" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Extensions/VolumeClip - Slicer Wiki</a>   That picture gave me the clue what I was doing wrong!</p>
<p>In the module, I had selected “Create New ROI” which then changed to “MarkupsROI”.  I made a box but nothing would happen when I clicked Apply.  It turns out that when I created the ROI it was named “R” and things started working once I went back to the clip module and changed “Clipping ROI” to “R”.</p>

---
