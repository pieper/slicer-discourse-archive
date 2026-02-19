---
topic_id: 20939
title: "Get Radius And Diameter Inside The Vessels"
date: 2021-12-06
url: https://discourse.slicer.org/t/20939
---

# Get radius and diameter inside the vessels

**Topic ID**: 20939
**Date**: 2021-12-06
**URL**: https://discourse.slicer.org/t/get-radius-and-diameter-inside-the-vessels/20939

---

## Post #1 by @MAURICIO_ALBERTO_LED (2021-12-06 22:51 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Extract de diameter of the vessel  on each point (MarkupsFiducial)<br>
Actual behavior:Tracebak Error</p>
<p>Hello Good Day<br>
I am in a project where we are trying determine the ballistic trajectories of bullets inside the brain and the damage. We need to calculate the damage of vessels by measuring the change of their diameter throughout all the vessels length.</p>
<p>I am using SlicerVMTK module and using the the python environment, and pasting the next code:</p>
<pre><code class="lang-auto">c = getNode('CenterlineComputationModel')
points = slicer.util.arrayFromModelPoints(c)
radii = slicer.util.arrayFromModelPointData(c, 'Radius')
for i, radius in enumerate(radii):
print("Point {0}: position={1}, radius={2}".format(i, points[i], radius))
</code></pre>
<p>Geves me this error:</p>
<pre><code class="lang-auto">Python 3.6.7 (default, Feb 27 2021, 05:09:17) 
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux2
&gt;&gt;&gt; c = getNode('CenterlineComputationModel')
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/mauricio/Desktop/Slicer-4.11.20210226-linux-amd64/bin/Python/slicer/util.py", line 1312, in getNode
    raise MRMLNodeNotFoundException("could not find nodes in the scene by name or id '%s'" % (pattern if (isinstance(pattern, str)) else ""))
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id 'CenterlineComputationModel'
&gt;&gt;&gt; points = slicer.util.arrayFromModelPoints(c)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'c' is not defined
&gt;&gt;&gt; radii = slicer.util.arrayFromModelPointData(c, 'Radius')
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'c' is not defined
&gt;&gt;&gt; for i, radius in enumerate(radii):
...   print("Point {0}: position={1}, radius={2}".format(i, points[i], radius))
...
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73622c457e92bb7985f6603b22986b184aaf06a8.png" data-download-href="/uploads/short-url/gsJf6zAvcbLpP9b8HoDv7ZPRTaU.png?dl=1" title="vessel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73622c457e92bb7985f6603b22986b184aaf06a8_2_690x388.png" alt="vessel" data-base62-sha1="gsJf6zAvcbLpP9b8HoDv7ZPRTaU" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73622c457e92bb7985f6603b22986b184aaf06a8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73622c457e92bb7985f6603b22986b184aaf06a8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73622c457e92bb7985f6603b22986b184aaf06a8_2_1380x776.png 2x" data-dominant-color="4F4F60"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vessel</span><span class="informations">1595×898 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for the help.</p>

---
