# Proposed custom module for the extension repository

**Topic ID**: 13134
**Date**: 2020-08-22
**URL**: https://discourse.slicer.org/t/proposed-custom-module-for-the-extension-repository/13134

---

## Post #1 by @chir.set (2020-08-22 19:47 UTC)

<p>I hereby propose the <a href="https://github.com/chir-set/PathReformat" rel="noopener nofollow ugc">Path Reformat</a> custom scripted module for bundling in the extension repository.</p>
<p>It is described there, repeating its objects would be superfluous in this post.</p>
<p>I believe it may be of interest for any physician dealing with vascular pathology. The primary intent is visual evaluation of cross-section of arterial segments that are not along the orthogonal axes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ececf14fc683fdcaff26db6e2c4bcb6d4c1d335.jpeg" data-download-href="/uploads/short-url/knkSZ5cx31OOWAKor9UW6iYHMbz.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ececf14fc683fdcaff26db6e2c4bcb6d4c1d335_2_621x499.jpeg" alt="Screenshot" data-base62-sha1="knkSZ5cx31OOWAKor9UW6iYHMbz" width="621" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ececf14fc683fdcaff26db6e2c4bcb6d4c1d335_2_621x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ececf14fc683fdcaff26db6e2c4bcb6d4c1d335_2_931x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ececf14fc683fdcaff26db6e2c4bcb6d4c1d335.jpeg 2x" data-dominant-color="1D1A16"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1164×937 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I insist that this step is <em>not</em> self-promotional.</p>
<p>The code is not written in stone, it may be changed as per your evaluation, within the limits of my coding skills.</p>
<p>I could not find an official way to propose a module or I missed it, so here it goes in the forum.</p>
<p>Lastly, the module dealt in <a href="https://discourse.slicer.org/t/path-explorer-slicer-igt-does-not-save-trajectory/13132/3">this topic</a> suggested me that this custom module may not be disregarded. But I won’t mind if you consider that it’s not worthwhile.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2020-08-22 20:07 UTC)

<p>Thank you, this will be a very useful module. I would add it to the SlicerVMTK extension, as this feature is most commonly needed for vascular applications.</p>
<p>If you can send a pull request that adds this to SlicerVMTK extension then it’s great. If you don’t know how to do that then just let me know and I can do it for you.</p>
<p>We will need to decide on the final module name. “Path” word is not great, as we actually mean “curve”. It would be also useful to include “cross-section” in the name. Something like “Cross-section analysis” would be more clear, but if we find a simple and short bane that somehow includes “curve” as well then it is even better.</p>

---

## Post #3 by @chir.set (2020-08-22 20:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you can send a pull request</p>
</blockquote>
</aside>
<p>I can manage that and will do it tomorrow morning.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>“Path” word is not great</p>
</blockquote>
</aside>
<p>Well I chose ‘Path’ because it deals with marksups curves and VMTK centerlines, two different object types. We’ll change this module’s name. To which one… don’t know yet. Does it need to be changed before or after the pull request ?</p>

---

## Post #4 by @chir.set (2020-08-23 07:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the final module name</p>
</blockquote>
</aside>
<p>How about :</p>
<ul>
<li>Curve orthogonal {flow, analysis, navigation, reformat}</li>
<li>Curve {flow, analysis, navigation, reformat}</li>
<li>Cross-section {flow, analysis, navigation, reformat} ?</li>
</ul>
<p>My preferred is Curve orthogonal navigation.</p>
<p>Would it need a complete change in file names and class names ? Or just self.parent.title ?</p>
<p>Last, I think it’s better to change everything before the pull request.</p>

---

## Post #5 by @lassoan (2020-08-23 13:40 UTC)

<p>Yes, name change is quite invasive (module name, folder name, class name, various file names), so let’s finalize that before the pull request.</p>
<p>Slicer can do actual vascular navigation (with electromagnetically tracked catheters, using SlicerIGT extension), so I would reserve “navigation” word for that. It would also limit the module’s purpose to only navigate/view, and not to do any quantification or analysis.</p>
<p>I think flow is too restrictive (the tool can be used for things that don’t flow, such as bones, nerves, …).</p>
<p>Reformat and analysis both sound OK. Analysis may be better if we want to add more features not just reformat. For example defining points along the curve and measure distances between those points, computing optimal C-arm rotation angles (see requirements <a href="https://discourse.slicer.org/t/how-to-make-fiducial-points-placed-in-curved-planar-reformatted-image-appear-in-the-original-image/12189/8">here</a>), measuring cross-section area, minimum/maximum radius (not just circular cross-section area), finding position of minimum/maximum diameter cross-sections, etc.</p>
<p>If we use “analysis” as last word then then I think only the “Cross-section” prefix would work with it (“Curve orthogonal analysis” would be a bit too confusing, and “Curve analysis” would be too general).</p>
<p>So, from the proposed combination, “Cross-section analysis” seems to be the most appropriate name. It is a bit broad, but the module will eventually do more than just position/orient slice view.</p>

---

## Post #6 by @chir.set (2020-08-23 13:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="13134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Cross-section analysis</p>
</blockquote>
</aside>
<p>OK, I’ll rename as such and do the pull request.</p>

---

## Post #7 by @Romeo_Guevara (2020-08-25 00:14 UTC)

<p>Good evening, the module sounds fantastic, is it already in the Slicer module menu? good night</p>

---

## Post #8 by @chir.set (2020-08-25 06:49 UTC)

<aside class="quote no-group" data-username="Romeo_Guevara" data-post="7" data-topic="13134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/romeo_guevara/48/3539_2.png" class="avatar"> Romeo_Guevara:</div>
<blockquote>
<p>is it already in the Slicer module menu</p>
</blockquote>
</aside>
<p>No, it is still being worked on in a pull request.</p>

---

## Post #9 by @lassoan (2020-10-19 13:59 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-make-my-module-available-in-the-extension-manager/14138">How to make my module available in the Extension manager?</a></p>

---
