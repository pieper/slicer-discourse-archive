---
topic_id: 30189
title: "Slicer To Matlab Igtlink Connection"
date: 2023-06-23
url: https://discourse.slicer.org/t/30189
---

# Slicer to Matlab IGTLink Connection

**Topic ID**: 30189
**Date**: 2023-06-23
**URL**: https://discourse.slicer.org/t/slicer-to-matlab-igtlink-connection/30189

---

## Post #1 by @LauraConnolly1 (2023-06-23 00:29 UTC)

<p>Hi there!</p>
<p>We’re trying to connect 3D Slicer to Matlab using a controller code written in 2018. I’m a bit confused about how to set up the server connection from 3D Slicer to Matlab in the Matlab Commander module. We changed the firewall permissions and try launching the connection from the Matlab side (a GUI that was written in Matlab) but we get an error each time.</p>
<p>We basically want to stream a transform from 3D Slicer to Matlab in the simplest way. The tutorial videos on this page seem to have expired (<a href="http://openigtlink.org/tutorials/matlabigtl.html" class="inline-onebox" rel="noopener nofollow ugc">Tutorials &gt; Matlab/OpenIGTLink</a>) so any pointers to other tutorials would help.</p>
<p>Thanks in advance!!</p>

---

## Post #2 by @lassoan (2023-06-23 00:38 UTC)

<p>Native Matlab implementation of some OpenIGTLink messages are available here: <a href="https://github.com/SlicerIGT/MatlabOpenIGTLink/tree/master/src" class="inline-onebox">MatlabOpenIGTLink/src at master · SlicerIGT/MatlabOpenIGTLink · GitHub</a></p>
<p>A more complete implementation is available in Python in pyigtl package that you may be able to use in Matlab.</p>
<p>In the long term you may consider switching to Python, as it has many advantages over Matlab. We used Matlab heavily until about 10 years ago. Then we moved all out projects to Python and it went very well, we never looked back.</p>

---
