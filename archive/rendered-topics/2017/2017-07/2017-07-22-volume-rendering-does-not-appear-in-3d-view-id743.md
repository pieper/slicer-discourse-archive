# Volume rendering does not appear in 3D view

**Topic ID**: 743
**Date**: 2017-07-22
**URL**: https://discourse.slicer.org/t/volume-rendering-does-not-appear-in-3d-view/743

---

## Post #1 by @moselhy (2017-07-22 20:27 UTC)

<p>I can’t seem to get Volume Rendering to work with a Sequence Browser pointing to a volume sequence. Here is a screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/072dbc715e2260457a5c8a94d27b393e8a0979e8.png" data-download-href="/uploads/short-url/11vky4PzkdYvk26NUrcevtSThk4.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/072dbc715e2260457a5c8a94d27b393e8a0979e8_2_690x334.png" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/072dbc715e2260457a5c8a94d27b393e8a0979e8_2_690x334.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/072dbc715e2260457a5c8a94d27b393e8a0979e8_2_1035x501.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/072dbc715e2260457a5c8a94d27b393e8a0979e8_2_1380x668.png 2x" data-dominant-color="9191A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">2048×992 352 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2017-07-22 20:30 UTC)

<p>It is most likely not related to sequences. A few things to check:</p>
<ul>
<li>Try to switch to CPU volume rendering. GPU volume rendering does not work on all configurations.</li>
<li>Click the small box icon (to the right from the pushpin icon) at the top of the 3D view to make sure the volume is in the field of view.</li>
</ul>

---

## Post #3 by @moselhy (2017-07-22 20:35 UTC)

<p>I pressed them in each view and changed to CPU volume rendering but nothing happens…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/2c4c8c2d6323241d5ca861b5a19b99438b738b24.png" data-download-href="/uploads/short-url/6jT0GH4SYWSjtY1mOGxzBVEax7u.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2c4c8c2d6323241d5ca861b5a19b99438b738b24_2_690x333.png" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2c4c8c2d6323241d5ca861b5a19b99438b738b24_2_690x333.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2c4c8c2d6323241d5ca861b5a19b99438b738b24_2_1035x499.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2c4c8c2d6323241d5ca861b5a19b99438b738b24_2_1380x666.png 2x" data-dominant-color="9797AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">2048×990 355 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You are right that it is probably not related to sequences. I did the following steps:</p>
<ol>
<li>saved that one volume frame as a nrrd</li>
<li>closed the scene</li>
<li>opened the saved frame</li>
</ol>
<p>and it did the same thing and nothing showed up.</p>
<p>However, if I do these steps with <a href="http://slicer.kitware.com/midas3/download/item/292313/RegLib_C01_2.nrrd" rel="noopener nofollow ugc">this volume</a> it works just fine</p>
<p>This is the sequence I am using:<br>
<a href="http://slicer.kitware.com/midas3/download/item/299877/CTP-cardio.seq.nrrd" class="onebox" target="_blank" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/download/item/299877/CTP-cardio.seq.nrrd</a></p>

---

## Post #4 by @lassoan (2017-07-22 20:37 UTC)

<p>I’ve tried to visualize this data set and I can confirm that your problem was that the volume was not in 3D view’s field of view by default. The solution was to click the reset FOV button.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/b80dd89c4e5a9d20695717581a308a61278bf582.jpg" data-download-href="/uploads/short-url/qgdwdZMbVrV8caxYWYMSAhOZgSm.jpg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b80dd89c4e5a9d20695717581a308a61278bf582_2_518x500.jpg" width="518" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b80dd89c4e5a9d20695717581a308a61278bf582_2_518x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b80dd89c4e5a9d20695717581a308a61278bf582_2_777x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b80dd89c4e5a9d20695717581a308a61278bf582_2_1036x1000.jpg 2x" data-dominant-color="756E87"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1180×1137 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @moselhy (2017-07-23 03:54 UTC)

<p>Thank you, it works now</p>

---

## Post #6 by @Ulli_Wie (2017-07-29 07:57 UTC)

<p>I cant’t get anything shown in 3D view at all - are there any additional steps than the ones described above?</p>
<p>I tried the dataset mentioned above (<a href="http://slicer.kitware.com/midas3/download/item/299877/CTP-cardio.seq.nrrd" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/download/item/299877/CTP-cardio.seq.nrrd</a>)<br>
and clicked the reset FOV button several times… but still:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d77ad8af401e4bff749f9027240e62bccb87b9e3.jpeg" data-download-href="/uploads/short-url/uKdQUsfc1PHSqqTnKYCmfOCh0PN.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d77ad8af401e4bff749f9027240e62bccb87b9e3_2_690x370.jpg" alt="image" data-base62-sha1="uKdQUsfc1PHSqqTnKYCmfOCh0PN" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d77ad8af401e4bff749f9027240e62bccb87b9e3_2_690x370.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d77ad8af401e4bff749f9027240e62bccb87b9e3_2_1035x555.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d77ad8af401e4bff749f9027240e62bccb87b9e3_2_1380x740.jpg 2x" data-dominant-color="8F8F97"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @Ulli_Wie (2017-07-29 08:10 UTC)

<p>found it in another tutorial:</p>
<p>I did not click on the “eye” Symbol next to “Volume”. Now it works <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7510fce2a44eb0e5a1f19507e324adfd539df8b8.png" alt="image" data-base62-sha1="gHCg8CyPXS6njx9DPkjonjOYpE4" width="445" height="358"></p>

---
