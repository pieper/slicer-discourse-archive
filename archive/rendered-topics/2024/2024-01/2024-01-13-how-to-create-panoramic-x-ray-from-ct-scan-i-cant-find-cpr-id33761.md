# How to Create panoramic X-ray from Ct scan , I can't find CPR

**Topic ID**: 33761
**Date**: 2024-01-13
**URL**: https://discourse.slicer.org/t/how-to-create-panoramic-x-ray-from-ct-scan-i-cant-find-cpr/33761

---

## Post #1 by @Mohammad_Talaat (2024-01-13 20:28 UTC)

<p>I 've seen a  post before to create panoramic x-ray from ct scan using curved planner reformat but i couldn’t do it<br>
so if can anyone help . i appreciate much<br>
Thanks<br>
link for previous post</p><aside class="quote quote-modified" data-post="3" data-topic="9456">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-implement-cpr-curved-planar-reconstruction-from-centerline/9456/3">How to implement CPR (curved planar reconstruction) from centerline?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can load a curve from a CSV file that has this structure: 
# Markups fiducial file version = 4.11
# CoordinateSystem = 0
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
1,-48.966353538964675,-101.7065776156342,74.67105263157896,0,0,0,1,1,1,0,MarkupsCurve-1,,
1,-53.75692521242794,-85.6239441404361,66.4605263157895,0,0,0,1,1,1,0,MarkupsCurve-2,,
1,-60.86814580722918,-72.76476934319273,60.7763157894737,0,0,0,1,1,1,0,MarkupsCurve-3,,
1,-65.87663276996875,-62.4254372939…
  </blockquote>
</aside>


---

## Post #2 by @lassoan (2024-01-14 03:41 UTC)

<p>The module is in the Sandbox extension.</p>

---

## Post #3 by @Mohammad_Talaat (2024-01-14 09:24 UTC)

<p>I have a question please , should i draw the curve on the segmented 3d model from the dicom<br>
Or can i draw the curve on the axial cut only<br>
Thanks in advance</p>

---

## Post #4 by @lassoan (2024-01-14 13:47 UTC)

<p>You can draw the curve anywhere, you can even use multiple views: drop a few points in slice views then drop a few in a 3D view on a volume-rendered or segmented surface, and then adjust them in different slice views.</p>

---

## Post #5 by @Mohammad_Talaat (2024-01-14 18:31 UTC)

<p>thanks so much , but the panoramic view became just a slice along the line but not like the panoramic x ray we have in the dental field , do you have a previous recorded video<br>
Thanks in advance .</p>

---

## Post #6 by @muratmaga (2024-01-14 19:12 UTC)

<p>I don’t know much about CPR or dentistry, but all seems to work fine with the sample data in Slicer.</p>
<p>Notice that there are two outputs: A straightened volume, and a projected volume. Projected one is a single X-ray essentially. make sure you are looking at the straightened volume, which looks like a proper 3D volume you can navigate.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33b089b7764485002920cb9c89b975eafb18ff15.jpeg" data-download-href="/uploads/short-url/7ngA4vDTcFdpwpNRgTwx5qeoSQ5.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b089b7764485002920cb9c89b975eafb18ff15_2_690x334.jpeg" alt="image" data-base62-sha1="7ngA4vDTcFdpwpNRgTwx5qeoSQ5" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b089b7764485002920cb9c89b975eafb18ff15_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b089b7764485002920cb9c89b975eafb18ff15_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b089b7764485002920cb9c89b975eafb18ff15_2_1380x668.jpeg 2x" data-dominant-color="7B7A7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4324×2094 715 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Mohammad_Talaat (2024-01-14 19:43 UTC)

<p>thank for your replay , can you clarify more the difference between the red and the green screens</p>

---

## Post #8 by @muratmaga (2024-01-14 20:21 UTC)

<p>In 3D volumes you have 3 planes to look at data. I imagine one is top and one is front on views.</p>

---

## Post #9 by @lassoan (2024-01-15 05:27 UTC)

<p>“Output projected volume” contains the traditional 2D panoramic X-ray projection image. As it is a single-slice volume, it will show up as a 2D image in one slice view, while it will appear as a line in the two other orthogonal slice views.</p>

---
