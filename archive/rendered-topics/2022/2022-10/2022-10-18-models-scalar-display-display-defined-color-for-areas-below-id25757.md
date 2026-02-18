# Models / Scalar Display: Display defined color for areas below threshold

**Topic ID**: 25757
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/models-scalar-display-display-defined-color-for-areas-below-threshold/25757

---

## Post #1 by @stephan (2022-10-18 15:32 UTC)

<p>Dear Slicer developers,</p>
<p>may I make a feature request? In the models module, scalars can by displayed on the surface using a custom color palette. Also, there is a threshold function which allows the display only of those parts of the model surface with associated scalar values within the thresholds.<br>
Would it be possible to add an option to this threshold function to not hide the out-of-threshold areas, but display them in a certain color?<br>
In my use case, there is scalar data for each surface vertex. Valid data is usually in the 0.0 to +20.0 range and should be displayed using the rainbow color scale with a range of 0.5 (red) to 1.5 (pink). However, there are vertices where the input data was actuallly invalid, those are encoded as the value -10000 and it would be great if those areas would be displayed gray (independently of the actual range for the valid scalars).<br>
In Slicer &lt;= 4.11.0 I found the workaround to create 2 copies of the model, with the one higher up in the subject hierarchy list being all gray and the second one having the colors and a lower threshold of -9000. Thus, all the -1000 values are invisible and the gray “background model” shines through.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50f9ee14ff432a9f7e30f22d062b37abe1b48e0e.jpeg" data-download-href="/uploads/short-url/bylFyhoongSuXTD64STDgG4RSuq.jpeg?dl=1" title="Slicer 4.11.0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50f9ee14ff432a9f7e30f22d062b37abe1b48e0e_2_690x377.jpeg" alt="Slicer 4.11.0" data-base62-sha1="bylFyhoongSuXTD64STDgG4RSuq" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50f9ee14ff432a9f7e30f22d062b37abe1b48e0e_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50f9ee14ff432a9f7e30f22d062b37abe1b48e0e_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50f9ee14ff432a9f7e30f22d062b37abe1b48e0e_2_1380x754.jpeg 2x" data-dominant-color="3C2B3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer 4.11.0</span><span class="informations">1920×1050 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, starting with v 4.13 and above, there are some flickering artifacts where the background shines through in colored areas.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/264fbd6242fa381022b98749e1c419fdcd2c8566.jpeg" data-download-href="/uploads/short-url/5sUZ6wI4OOqyhPCE62xVO9oYAT4.jpeg?dl=1" title="Slicer 5.0.3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/264fbd6242fa381022b98749e1c419fdcd2c8566_2_690x377.jpeg" alt="Slicer 5.0.3" data-base62-sha1="5sUZ6wI4OOqyhPCE62xVO9oYAT4" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/264fbd6242fa381022b98749e1c419fdcd2c8566_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/264fbd6242fa381022b98749e1c419fdcd2c8566_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/264fbd6242fa381022b98749e1c419fdcd2c8566_2_1380x754.jpeg 2x" data-dominant-color="383139"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer 5.0.3</span><span class="informations">1920×1050 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It would be therefore really helpful if I could retire this workaround with the second copy and simply define a color for areas outside the threshold.<br>
(Simply appending the color scale with 0 = gray does not really work, since I need values between 0 and the lower limit of the range to be red and only those with the exact vallue -1000 to be grey.)</p>
<p>I hope that makes sense?</p>
<p>Thank you and best regards<br>
Stephan</p>

---

## Post #2 by @lassoan (2022-10-18 16:37 UTC)

<aside class="quote no-group" data-username="stephan" data-post="1" data-topic="25757">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>Would it be possible to add an option to this threshold function to not hide the out-of-threshold areas, but display them in a certain color?</p>
</blockquote>
</aside>
<p>You can achieve this by modifying the color table. See these examples:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-table">Create custom color table</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-map-and-display-color-legend">Create custom color map and display color legend</a></li>
</ul>
<aside class="quote no-group" data-username="stephan" data-post="1" data-topic="25757">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>However, starting with v 4.13 and above, there are some flickering artifacts where the background shines through in colored areas.</p>
</blockquote>
</aside>
<p>You can remove the flicker by making the model slightly transparent (0.99 may suffice) and enable depth peeling in the 3D view controller.</p>

---

## Post #3 by @stephan (2022-10-20 19:21 UTC)

<p>Prof. Lasso, thank you for your quick reply.<br>
Probably the creation of a custom color table might be the best thing to do.<br>
The slightly transparent models do not really look the way it should (although the artifacts disappear, there is a surprising amount of background color being mixed into the foreground (color-table defined) color even with .99 transparency.<br>
Thank you<br>
Stephan</p>

---
