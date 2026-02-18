# Quesition about 3D slicer capacity

**Topic ID**: 38244
**Date**: 2024-09-05
**URL**: https://discourse.slicer.org/t/quesition-about-3d-slicer-capacity/38244

---

## Post #1 by @Hussam (2024-09-05 17:46 UTC)

<p>I have couple of questions I would like to ask about:</p>
<p>-I would like to use 3D slicer using AI models in transnational cancer imaging, including registration and radiomics. Do you mind me asking if 3D slicer has such models, for example register_scan,  warp_scan and warp_structures with AI models?</p>
<p>-I have two gamma knife dose distributions. I opened them in 3D slicerRT to get the profiles at 100 cm. Can you tell me how I can do this?</p>
<p>Yours sincerely</p>
<ul>
<li></li>
</ul>

---

## Post #2 by @Hussam (2024-09-06 09:36 UTC)

<p>Further to question above, I loaded “Sandbox extension”, but I can export the output as an "<em>.svg</em>.</p>
<p>Can you tell me how I export dose profile as “*.Xls”?</p>
<p>Yours sincerely</p>

---

## Post #3 by @lassoan (2024-09-06 13:41 UTC)

<aside class="quote no-group" data-username="Hussam" data-post="1" data-topic="38244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hussam/48/78858_2.png" class="avatar"> Hussam:</div>
<blockquote>
<p>I would like to use 3D slicer using AI models in transnational cancer imaging, including registration and radiomics. Do you mind me asking if 3D slicer has such models, for example register_scan, warp_scan and warp_structures with AI models?</p>
</blockquote>
</aside>
<p>Yes, Slicer has lots of classic and AI tools for fully automatic segmentation, registration, and warping images or structures.</p>
<aside class="quote no-group" data-username="Hussam" data-post="1" data-topic="38244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hussam/48/78858_2.png" class="avatar"> Hussam:</div>
<blockquote>
<p>I have two gamma knife dose distributions. I opened them in 3D slicerRT to get the profiles at 100 cm. Can you tell me how I can do this?</p>
</blockquote>
</aside>
<p>You can get any slice of the dose distribution at any position and orientation. You can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">reformat widget</a> or interactive slice intersections (or set the slice position/orientation using Python scripting).</p>
<aside class="quote no-group" data-username="Hussam" data-post="2" data-topic="38244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hussam/48/78858_2.png" class="avatar"> Hussam:</div>
<blockquote>
<p>I can export the output as an "<em>.svg</em>.</p>
</blockquote>
</aside>
<p>What output would you like to save as .svg?<br>
If you are interested in plots, then no, Slicer currently does not provide SVG output for plots. However, it should be straighforward to load the .csv file that Slicer saves into Excel or into any Python plotting package and render to a vector file format.</p>
<aside class="quote no-group" data-username="Hussam" data-post="2" data-topic="38244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hussam/48/78858_2.png" class="avatar"> Hussam:</div>
<blockquote>
<p>Can you tell me how I export dose profile as “*.Xls”?</p>
</blockquote>
</aside>
<p>You can save as .csv that you can load into Excel.</p>

---

## Post #4 by @Hussam (2024-09-06 14:23 UTC)

<p>Thank you for your prompt reply!<br>
I would like to export dose profile as excel data.</p>

---
