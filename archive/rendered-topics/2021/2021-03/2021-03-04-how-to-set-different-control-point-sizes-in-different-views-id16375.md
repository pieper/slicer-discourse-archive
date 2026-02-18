# How to set different control point sizes in different views?

**Topic ID**: 16375
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/how-to-set-different-control-point-sizes-in-different-views/16375

---

## Post #1 by @akshay_pillai (2021-03-04 18:16 UTC)

<p>Operating system: windows 10<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:<br>
I want the control points in a centerline curve to have different sizes in 3d view and different sizes in sagittal view. I know I can use markups module to change glyph size for different point sizes but that changes it in both 3d view and other views. Is there any way to do this?</p>

---

## Post #2 by @lassoan (2021-03-04 19:01 UTC)

<p>Can you tell a bit more about your use case?<br>
Have you tried both absolute and relative glyph sizing mode?</p>
<p>You can always make nodes appear differently in various views by adding more display nodes and specify for each display node what views they are displayed in.</p>

---

## Post #3 by @akshay_pillai (2021-03-05 15:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>always make nodes appear differently in various views by adding more display nodes and specify for each display node what views they are displayed in</p>
</blockquote>
</aside>
<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a> , yes I did try absolute and relative glyph sizing but that doesn’t apply here.</p>
<p>What I am trying to do is , first create a centerline curve using the vmtk extract centerline module. That gives me a centerline curve, the centerline curve has control points that I can view by toggling view in markups module(control points section). I want to display these control points with 5% glyph size in the 3d view on the centerline , but also 1% glyph size in the other views. So it is just the one vtkMRMLMarkupsCurveNode that I create.</p>

---

## Post #4 by @lassoan (2021-03-05 15:45 UTC)

<p>As I wrote above, just create an additional display node for the 3D view. Set view node IDs in the display nodes select which views they render the markups node in.</p>
<p>Can you attach a screenshot that shows why you need different glyph size in slice and 3D view (how things look with 1% and 5%)? If this is may be a common need then we can address it in the Slicer core with a simpler solution than using multiple display nodes.</p>

---

## Post #5 by @akshay_pillai (2021-03-05 15:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> ok ill try that. Yes I can attach a screenshot once I implement it. Thanks.</p>

---

## Post #6 by @lassoan (2021-03-05 15:50 UTC)

<p>I meant please show how 3D and slice views look with a single display node now (two screenshots, one with 1%, one with 5%).</p>

---

## Post #7 by @akshay_pillai (2021-03-05 15:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="16375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>how how 3D and slice views look with a</p>
</blockquote>
</aside>
<p>Here you go:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43b626791c405a59d726bb97b52748c2ad570560.jpeg" data-download-href="/uploads/short-url/9F0feuQ6XwnOBAX7yJjCk5UqCMo.jpeg?dl=1" title="1%.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43b626791c405a59d726bb97b52748c2ad570560_2_690x498.jpeg" alt="1%.PNG" data-base62-sha1="9F0feuQ6XwnOBAX7yJjCk5UqCMo" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43b626791c405a59d726bb97b52748c2ad570560_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43b626791c405a59d726bb97b52748c2ad570560_2_1035x747.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43b626791c405a59d726bb97b52748c2ad570560.jpeg 2x" data-dominant-color="432E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1%.PNG</span><span class="informations">1277×922 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57569b8042a26cfb9a5323fd5a3aba41792687f3.jpeg" data-download-href="/uploads/short-url/csD5V2jq0ZdX1FLhDWeKAD9zg0r.jpeg?dl=1" title="5%.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57569b8042a26cfb9a5323fd5a3aba41792687f3_2_690x479.jpeg" alt="5%.PNG" data-base62-sha1="csD5V2jq0ZdX1FLhDWeKAD9zg0r" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57569b8042a26cfb9a5323fd5a3aba41792687f3_2_690x479.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57569b8042a26cfb9a5323fd5a3aba41792687f3_2_1035x718.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57569b8042a26cfb9a5323fd5a3aba41792687f3.jpeg 2x" data-dominant-color="483031"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5%.PNG</span><span class="informations">1277×887 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2021-03-05 16:00 UTC)

<p>I see. Size variation in 3D view is a bit higher than usual due to the extreme wide angle field of view. Still the 5% size looks pretty good.</p>
<p>What is the reason for showing the control points? Do you expect your users to move the control points? Or you just want to allow then to click on it to jump to that position?</p>

---

## Post #9 by @akshay_pillai (2021-03-05 16:07 UTC)

<p>Well no, I actually wanted to view control points as I move through the centerline in endoscopy videos both in 3d view and others, but the control points look extremely small and are not visible during the video at 1% but they are in the other views. So I wanted to set it to 5% to make it look better in the endoscopy flythrough as well without changing how it looks in the other views.</p>

---

## Post #10 by @lassoan (2021-03-05 16:09 UTC)

<p>If you don’t need to interact with the points then I would recommend to hide the control points. If you need to interact with them then the 5% looks good to me (but of course you can add the secondary display node if you want).</p>

---

## Post #11 by @akshay_pillai (2021-03-05 16:15 UTC)

<aside class="quote no-group" data-username="akshay_pillai" data-post="9" data-topic="16375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p>n</p>
</blockquote>
</aside>
<p>I’m sorry for not mentioning, but yeah I do think that displaying the control points will give the user additional functionality of jumping between visible points in the 3d view. One more thing: I know that I can set the glyph size using slicer.mrmlScene.GetDefaultNodeByClass(‘vtkMRMLMarkupsDisplayNode’).SetGlyphScale(5), how can I do this for absolute value? and how do I set absolute value to be on as default?</p>

---

## Post #12 by @lassoan (2021-03-05 16:44 UTC)

<aside class="quote no-group" data-username="akshay_pillai" data-post="11" data-topic="16375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p>slicer.mrmlScene.GetDefaultNodeByClass(‘vtkMRMLMarkupsDisplayNode’).SetGlyphScale(5), how can I do this for absolute value? and how do I set absolute value to be on as default?</p>
</blockquote>
</aside>
<p>See documentation here for setting absolute/relative glyph size: <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsDisplayNode.html#a5e452bb436f3b4cfbecef72518ce26a9" class="inline-onebox">Slicer: vtkMRMLMarkupsDisplayNode Class Reference</a></p>
<p>You can change the default properties for new nodes by modifying the default node (<code>slicer.mrmlScene.GetDefaultNodeByClass(...)</code>).</p>

---
