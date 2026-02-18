# Can the image slices be made semi-transparent in 3D view?

**Topic ID**: 8713
**Date**: 2019-10-08
**URL**: https://discourse.slicer.org/t/can-the-image-slices-be-made-semi-transparent-in-3d-view/8713

---

## Post #1 by @aptirumalai (2019-10-08 22:34 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @Amine (2019-10-08 23:13 UTC)

<p>Hi, i dont know if it’s possible via the interface<br>
You can paste this code in the python console to set a specific opacity (<code>Red</code> can be changed to <code>Green</code> or <code>Yellow</code>)</p>
<pre><code>opacity = 0.7
Red = getNode("Red Volume Slice")
Red.GetDisplayNode().SetOpacity(opacity)
</code></pre>
<p>This following code is supposed to work too as it allows setting slices to visible models in models module and changing the opacity easily but it does make slicer crash when trying to scroll slices (on both 4.10 and 4.11) <a class="mention" href="/u/lassoan">@lassoan</a> could you please check this out? is this a bug or isn’t it intended to be used? :</p>
<pre><code>Red = getNode("Red Volume Slice")
Red.HideFromEditorsOff()</code></pre>

---

## Post #3 by @aptirumalai (2019-10-08 23:44 UTC)

<aside class="quote no-group quote-modified" data-username="Amine" data-post="2" data-topic="8713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>opacity = 0.7 Red = getNode(“Red Volume Slice”) Red.GetDisplayNode().SetOpacity(opacity)</p>
</blockquote>
</aside>
<p>I tried out your suggestion. It partially works. I can see Fiducials behind a semi-transparent slice. However, a surface model and a trajectory path that I have in my scene do not show through.</p>
<p>Any thoughts? Thanks!</p>

---

## Post #4 by @Amine (2019-10-09 00:12 UTC)

<aside class="quote no-group quote-modified" data-username="Amine" data-post="2" data-topic="8713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>opacity = 0.7 Red = getNode(“Red Volume Slice”) Red.GetDisplayNode().SetOpacity(opacity)</p>
</blockquote>
</aside>
<p>It’s a curious behavior, if you use that code Before enabling the slice visibility in 3d it works fine, try it with a fresh scene (setting it to 1 then again to a lower value seems to cause the problem)</p>

---

## Post #5 by @pieper (2019-10-09 00:21 UTC)

<p>You might also try depth peeling.  Some discussion <a href="https://discourse.slicer.org/t/models-not-transparent-in-slicer-4-10-1/6538">here</a>.</p>

---

## Post #6 by @aptirumalai (2019-10-09 00:42 UTC)

<aside class="quote no-group quote-modified" data-username="Amine" data-post="2" data-topic="8713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>opacity = 0.7 Red = getNode(“Red Volume Slice”) Red.GetDisplayNode().SetOpacity(opacity)</p>
</blockquote>
</aside>
<p>I still have the same issue. I have a model in my scene created from GreyscaleModelMaker. It does not show through the partially transparent slice.</p>

---

## Post #7 by @lassoan (2019-10-09 00:51 UTC)

<p>Textured models (such as slices) are forced to be rendered as opaque if they are shown with opacity = 1.0. There was a slight mistake in the forcing logic that resulted in forced opaque rendering “stuck” after it was once rendered as opaque (this caused the behavior that you had to set opacity before the slice was ever rendered). I have fixed this now (<a href="https://github.com/Slicer/Slicer/commit/da95ecab0cd53226fcec72e71647716be1a097eb">rev28539</a>).</p>
<p>Until a few years ago, VTK did not have a robust way of rendering transparent surfaces, so we had to remove opacity setting option for slice planes and forced the slices to be opaque and rendered last. Now depth peeling in VTK works reasonably well and robustly, so we might consider allowing making slice views transparent. However, there could be rendering issues on some older graphics cards (see <a href="https://issues.slicer.org/view.php?id=4253">bug4253</a>) and point picking may be impacted, too. So, it is probably better to keep it as an experimental feature (can be enabled using Python console only).</p>

---

## Post #8 by @Amine (2019-10-09 19:04 UTC)

<pre><code>Red = getNode("Red Volume Slice")
Red.HideFromEditorsOff()
</code></pre>
<p>Using this on the slice nodes works (allows modification from models module) but makes slicer crash as soon as slices are scrolled even in the new nightly</p>

---

## Post #9 by @aptirumalai (2019-10-09 19:09 UTC)

<p>Amine’s observation that the opacity has to be set to a value like 0.7 in advance does work with models as well. I had created the model with GreyscaleModelMaker which automatically displayed the model in 3D View - before I had modified the opacity. Once I ensured that the first thing I did was to set the opacity to a value smaller than, the slice did become translucent as expected.</p>

---

## Post #10 by @lassoan (2019-10-09 20:49 UTC)

<p>In latest preview release the order of making the slice transparent and showing it in 3D view should not matter anymore.</p>
<p>Models module should not be used to adjust slice properties. Slice view transparency would be added to the view controller, but for now we will not add GUI as this is not ready for users (would need more testing).</p>

---

## Post #11 by @Riccardo_Pappalardo (2022-03-31 20:40 UTC)

<p>Hi Amine I’ve never used the Python console before and can’t get the CT scan coronal plane (in the red slice) to be transparent. When I paste your code (line Red = getNode(“Red Volume Slice”))<br>
into the console i get:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37bbf52adb44b3ea0d93e4c52559910f1f7d1481.png" data-download-href="/uploads/short-url/7X2XpVxIFSQCuYgZOKYwDCnQ5zz.png?dl=1" title="Screenshot 2022-03-31 213859" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37bbf52adb44b3ea0d93e4c52559910f1f7d1481.png" alt="Screenshot 2022-03-31 213859" data-base62-sha1="7X2XpVxIFSQCuYgZOKYwDCnQ5zz" width="690" height="88" data-dominant-color="FCF5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-03-31 213859</span><span class="informations">778×100 3.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>“Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “”, line 12, in getNode<br>
MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘Red Volume Slice’”</p>
<p>I get this error for both the codes you’ve provided.</p>
<p>Is there a solution to this?</p>

---

## Post #12 by @lassoan (2022-03-31 22:45 UTC)

<p>Looking up nodes by name is not robust (node names may change). Instead, you can use node IDs or get the list of slice nodes from the layout manager - see examples <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-vtk-views-renderers-and-cameras">here</a>.</p>

---

## Post #13 by @Riccardo_Pappalardo (2022-04-01 16:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="8713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>list of slice nodes</p>
</blockquote>
</aside>
<p>Thanks so much for your reply.</p>
<p>I have tried that but still unsuccessful:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f34ad0578581da4c14f798f46a3ba170d162631.png" alt="image" data-base62-sha1="918Wahj8zugf5fxz1tEh0cvryU1" width="612" height="358"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21ad9958bcae7ae557715e856887997d0be28a7c.png" data-download-href="/uploads/short-url/4NVGP0wqZXAU4aayIW5onJox9rS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21ad9958bcae7ae557715e856887997d0be28a7c_2_690x78.png" alt="image" data-base62-sha1="4NVGP0wqZXAU4aayIW5onJox9rS" width="690" height="78" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21ad9958bcae7ae557715e856887997d0be28a7c_2_690x78.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21ad9958bcae7ae557715e856887997d0be28a7c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21ad9958bcae7ae557715e856887997d0be28a7c.png 2x" data-dominant-color="FAF2F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">935×107 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Other failed attemps:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/569d46e33a40740b2136bdfc725ddbf55b2e2c76.png" alt="image" data-base62-sha1="cme1EwTVbP7JamFUWag8zYdtHro" width="354" height="91"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db7d6f865429cf08c5793b8835edb90da84e78b6.png" data-download-href="/uploads/short-url/vjHjg9Mras4cJloeF7tFGHlBHOC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db7d6f865429cf08c5793b8835edb90da84e78b6_2_690x78.png" alt="image" data-base62-sha1="vjHjg9Mras4cJloeF7tFGHlBHOC" width="690" height="78" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db7d6f865429cf08c5793b8835edb90da84e78b6_2_690x78.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db7d6f865429cf08c5793b8835edb90da84e78b6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db7d6f865429cf08c5793b8835edb90da84e78b6.png 2x" data-dominant-color="FAF2F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×104 33.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9a7d1d4c17382cff4fefd8f87602f374a4d9fa3.png" data-download-href="/uploads/short-url/sLVwsmzlBtBRQLvIf2tOK4s15Av.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9a7d1d4c17382cff4fefd8f87602f374a4d9fa3_2_690x114.png" alt="image" data-base62-sha1="sLVwsmzlBtBRQLvIf2tOK4s15Av" width="690" height="114" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9a7d1d4c17382cff4fefd8f87602f374a4d9fa3_2_690x114.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9a7d1d4c17382cff4fefd8f87602f374a4d9fa3_2_1035x171.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9a7d1d4c17382cff4fefd8f87602f374a4d9fa3_2_1380x228.png 2x" data-dominant-color="FDF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1423×236 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m quite a beginner so there may be something that I’m missing. Any solution? Thanks so much</p>

---

## Post #14 by @lassoan (2022-04-01 21:10 UTC)

<p>I know, it is quite confusing. There are about 10 objects for each slice view for controlling various aspects - see an overview <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#slice-view-pipeline">here</a>.</p>
<p>You can change opacity of a slice appearing in 3D views by modifying <code>Opacity</code> value in the slice display node.</p>

---
