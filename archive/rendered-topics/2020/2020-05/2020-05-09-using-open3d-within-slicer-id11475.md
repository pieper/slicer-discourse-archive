---
topic_id: 11475
title: "Using Open3D Within Slicer"
date: 2020-05-09
url: https://discourse.slicer.org/t/11475
---

# Using open3d within Slicer

**Topic ID**: 11475
**Date**: 2020-05-09
**URL**: https://discourse.slicer.org/t/using-open3d-within-slicer/11475

---

## Post #1 by @agporto (2020-05-09 07:41 UTC)

<p>I recently joined the SlicerMorph team and I have been developing an algorithm that makes heavy use of the open3d library (<a href="https://github.com/intel-isl/Open3D" rel="nofollow noopener">https://github.com/intel-isl/Open3D</a>). I was able to install it within Slicer using pip, but when importing it into Slicer, I get the following error (ImportError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.22’ not found ). It seems to be related to the GNU C Library, I was wondering if there is any hope that this problem could be solved, as it would be great to be able to use open3d within Slicer. Any ideas or directions?  Thanks in advance.</p>

---

## Post #2 by @pieper (2020-05-09 19:38 UTC)

<p>Hi -</p>
<p>The error you are seeing should be fixable at the os level - you can google around for GLIBCXX and libstdc++ and you should find the right instructions for your particular OS version.</p>
<p>On the plus side, I can report that I was able to run <code>pip_install('open3d')</code> and <code>import open3d</code> on both windows and mac and it appears that it will nicely interoperate with Slicer via numpy arrays.</p>
<p>Thanks for pointing out the library - looks super useful.  Let us know if you get it working on your machine and how it works.  I’ll definitely be looking into it too and maybe we can work up some demo code.</p>

---

## Post #3 by @lassoan (2020-05-10 00:59 UTC)

<p>I had a look and Open3D and I’m not impressed at all. It is a small library containing of a handful of random algorithms that are mostly already available in other widely used libraries (OpenCV, PCL, VTK, etc). What feature of Open3D do you use?</p>

---

## Post #4 by @pieper (2020-05-10 01:04 UTC)

<p>Don’t know if it’ll be useful but it does work.</p>
<pre><code class="lang-auto">m = getNode("Segment_1")
p = arrayFromModelPoints(m)
cloud = o3d.geometry.PointCloud()
cloud.points = o3d.utility.Vector3dVector(p)
o3d.visualization.draw_geometries(cloud)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b506778b15ffeb9d56e0fd331f00ca708027bf6.jpeg" data-download-href="/uploads/short-url/1C5w4GqqL2t6q4AmaDhcoHyA59k.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b506778b15ffeb9d56e0fd331f00ca708027bf6_2_649x499.jpeg" alt="image" data-base62-sha1="1C5w4GqqL2t6q4AmaDhcoHyA59k" width="649" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b506778b15ffeb9d56e0fd331f00ca708027bf6_2_649x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b506778b15ffeb9d56e0fd331f00ca708027bf6_2_973x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b506778b15ffeb9d56e0fd331f00ca708027bf6.jpeg 2x" data-dominant-color="9FA1A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1258×968 406 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @agporto (2020-05-10 02:35 UTC)

<p>Dear Steve and Andras.<br>
Thanks so much for the quick responses and thanks Steve to point us in the right direction to get it working. I agree with Andras that it is a small and targeted library. To answer the usage question, this library contains most of what we need for registration and some functions that I couldn’t find in other more comprehensive libraries. For example, the feature -based RANSAC registration (<a href="http://www.open3d.org/docs/release/tutorial/Advanced/global_registration.html#feature-matching" rel="nofollow noopener">http://www.open3d.org/docs/release/tutorial/Advanced/global_registration.html#feature-matching</a>) method is quite useful and I haven’t found a good implementation elsewhere. Similarly, the pose graph functionality is another one that I could not find in other libraries (<a href="http://www.open3d.org/docs/release/tutorial/ReconstructionSystem/register_fragments.html" rel="nofollow noopener">http://www.open3d.org/docs/release/tutorial/ReconstructionSystem/register_fragments.html</a>) that deal with point clouds. All in all, I would also say that this library is quite lightweights (seems to use the memory efficiently), it has very readable syntax and it contains useful callback functions for the visualization. I don’t necessarily expect that it would be useful for the Slicer community at large, but, for our purposes, it seems to work well. I am open to the possibility that other libraries might do a better job at it. I just don’t know another library that contains everything that I would need at this point.<br>
Thanks again,<br>
Arthur</p>

---
