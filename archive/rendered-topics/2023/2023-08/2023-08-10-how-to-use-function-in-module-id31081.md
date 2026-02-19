---
topic_id: 31081
title: "How To Use Function In Module"
date: 2023-08-10
url: https://discourse.slicer.org/t/31081
---

# How to use function in module

**Topic ID**: 31081
**Date**: 2023-08-10
**URL**: https://discourse.slicer.org/t/how-to-use-function-in-module/31081

---

## Post #1 by @Theo (2023-08-10 08:31 UTC)

<p>i want to use a protected function in “openigtlinkif” module named “startCurrentIGTLConnector(bool)”,so i changed the source code  to set it public and compile successfully, but my project still can’t find it, how to let this function open to my project,thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c01ac3a2dc3d677366f828695ea277c4ab5ad862.png" data-download-href="/uploads/short-url/rpr10V31NQbVZ4VicVIyU15AKvo.png?dl=1" title="1691651824599" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c01ac3a2dc3d677366f828695ea277c4ab5ad862_2_690x477.png" alt="1691651824599" data-base62-sha1="rpr10V31NQbVZ4VicVIyU15AKvo" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c01ac3a2dc3d677366f828695ea277c4ab5ad862_2_690x477.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c01ac3a2dc3d677366f828695ea277c4ab5ad862.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c01ac3a2dc3d677366f828695ea277c4ab5ad862.png 2x" data-dominant-color="262726"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1691651824599</span><span class="informations">937×649 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-08-10 08:41 UTC)

<p>There is no need to change anything in the module’s code. You can add a <code>vtkMRMLIGTLConnectorNode</code> to the scene, set its type, port, hostname (if client), and call its <code>Start()</code> method:</p>
<pre><code class="lang-python">connectorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLIGTLConnectorNode")
connectorNode.SetTypeClient('localhost', 18944)
connectorNode.Start()
</code></pre>

---

## Post #3 by @Theo (2023-08-11 01:33 UTC)

<p>Thanks for your prompt reply, it works</p>

---
