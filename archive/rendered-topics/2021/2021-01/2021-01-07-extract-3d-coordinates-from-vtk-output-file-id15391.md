# Extract 3D Coordinates from VTK Output File

**Topic ID**: 15391
**Date**: 2021-01-07
**URL**: https://discourse.slicer.org/t/extract-3d-coordinates-from-vtk-output-file/15391

---

## Post #1 by @Judith (2021-01-07 14:27 UTC)

<p>Hello everybody,</p>
<p>How do you extract de 3D coordinates from a VTK output file? This VTK output file is created using the Model-to-Model Distance module. It does not matter if the coordinates are in the LPS or RAS system, as I need to compare different coordinates. I need to export these coordinates to Excel.</p>
<p>Any suggestions would be really helpful, thankyou in advance.</p>
<p>Kind regards,<br>
Judith</p>

---

## Post #2 by @pieper (2021-01-07 17:11 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/v4.11/developer_guide/slicer.html#slicer.util.arrayFromModelPoints"><code>arrayFromModelPoints</code></a></p>

---

## Post #3 by @lassoan (2021-01-07 17:19 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thanks for providing the link. I’m wondering if we should always use latest tag (<a href="https://slicer.readthedocs.io/en/">https://slicer.readthedocs.io/en/</a><strong>latest</strong>…) instead of a specific version (<a href="https://slicer.readthedocs.io/en/">https://slicer.readthedocs.io/en/</a><strong>v4.11</strong>) in forum posts, because these posts may be read in several months or even years later and by that time specific tags may be outdated. We could also add a “stable” tag to readthedocs.</p>

---

## Post #4 by @pieper (2021-01-07 17:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="15391">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m wondering if we should always use latest tag</p>
</blockquote>
</aside>
<p>Yes, that’s always a tradeoff.  There’s a risk that things will get reformatted and we end up with a dead link.  On the wiki we would have a header that was added to pages when new versions were created; can we easily do the same on readthedocs?</p>
<p>There’s a similar tradeoff with github links to line numbers in branches which can get out of date compared to a link to the commit+line number.</p>

---

## Post #5 by @lassoan (2021-01-07 18:34 UTC)

<p>There is no automatic redirect. Maybe after structure of documentation is stabilized we can establish a policy of never deleting documentation page but add links to pages where content is moved to.</p>

---

## Post #6 by @jsalas424 (2022-07-24 22:03 UTC)

<p>Hi Pieper,</p>
<p>I too need to extract the x,y,z coordinates from a VTK file that I imported to Slicer. I was hoping you could be a little more explicit about how to use arrayFromModelPoints? I have imported the VTK and can see the mesh in the viewer, now what? Sorry if this is a trivial question, I’m relatively new to Slicer.</p>
<p>Here’s what I’m looking at:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3447fbab194d026be780653ed342615c141aba.jpeg" data-download-href="/uploads/short-url/frdzSDbzKSpWDyWSsYkcPh7Wnxw.jpeg?dl=1" title="Screen Shot 2022-07-24 at 6.05.39 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c3447fbab194d026be780653ed342615c141aba_2_690x330.jpeg" alt="Screen Shot 2022-07-24 at 6.05.39 PM" data-base62-sha1="frdzSDbzKSpWDyWSsYkcPh7Wnxw" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c3447fbab194d026be780653ed342615c141aba_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c3447fbab194d026be780653ed342615c141aba_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c3447fbab194d026be780653ed342615c141aba_2_1380x660.jpeg 2x" data-dominant-color="6B6A86"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-07-24 at 6.05.39 PM</span><span class="informations">1920×919 69.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you can see at the bottom, I attempted to run ‘slicer.util.arrayFromModelPoints(mesh)’ since my “Node” is named mesh as far as I can tell. Dead end and I got the error “NameError: name ‘mesh’ is not defined”</p>

---

## Post #7 by @pieper (2022-07-24 22:32 UTC)

<p>You need to use something like:</p>
<pre><code class="lang-auto">meshModelNode = slicer.util.getNode("mesh")
points = slicer.util. arrayFromModelPoints(meshModelNode)
</code></pre>
<p>(you can leave out <code>slicer.util</code> when typing at the console).</p>
<p>To get used to slicer python programming you can have a look at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html">the FAQ</a> and some of <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers">the tutorials</a>.</p>

---
