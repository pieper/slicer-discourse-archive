---
topic_id: 10997
title: "Mirroring A Rotation Around The Axis For A Transform Node"
date: 2020-04-05
url: https://discourse.slicer.org/t/10997
---

# Mirroring a rotation around the axis for a transform node

**Topic ID**: 10997
**Date**: 2020-04-05
**URL**: https://discourse.slicer.org/t/mirroring-a-rotation-around-the-axis-for-a-transform-node/10997

---

## Post #1 by @Mik (2020-04-05 05:44 UTC)

<p>Is it possible to mirror a rotation around the axis in a simple way (not making negative specific elements of the matrix) for a transform node?</p>
<p>For example the code:</p>
<p><code>vtkMRMLLinearTransformNode* gantryToFixedReferenceTransformNode =</code><br>
<code>     this-&gt;GetTransformNodeBetween(Gantry, FixedReference);</code><br>
<code>   vtkTransform* gantryToFixedReferenceTransform = vtkTransform::SafeDownCast(gantryToFixedReferenceTransformNode-&gt;GetTransformToParent());</code><br>
<code>   gantryToFixedReferenceTransform-&gt;Identity();</code><br>
<code>   gantryToFixedReferenceTransform-&gt;RotateY(beamNode-&gt;GetGantryAngle());</code><br>
<code>   gantryToFixedReferenceTransform-&gt;Modified();</code><br>
<code>... some other code ...</code><br>
<code> gantryToFixedReferenceTransform-&gt;MirrorY();  // mirror the rotation</code><br>
<code>gantryToFixedReferenceTransform-&gt;Modified();</code></p>
<p>Without mirror (not very good):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21e8f71e9a416d17ce128798e929390517a7fe75.png" data-download-href="/uploads/short-url/4PYSHWSEk7RmlipKMI7f7LwzTKJ.png?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21e8f71e9a416d17ce128798e929390517a7fe75.png" alt="Screenshot_2" data-base62-sha1="4PYSHWSEk7RmlipKMI7f7LwzTKJ" width="690" height="414" data-dominant-color="989BC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">754×453 21.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With mirror (much better):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9b86c815d3390189297c2b3cca6cb9d3ad261ca.png" data-download-href="/uploads/short-url/v42JIpTbgffBVHJGyOphf6K8PEK.png?dl=1" title="Screenshot_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9b86c815d3390189297c2b3cca6cb9d3ad261ca.png" alt="Screenshot_3" data-base62-sha1="v42JIpTbgffBVHJGyOphf6K8PEK" width="690" height="414" data-dominant-color="9598B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_3</span><span class="informations">754×453 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-04-05 17:15 UTC)

<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="10997">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>Is it possible to mirror a rotation around the axis in a simple way (not making negative specific elements of the matrix) for a transform node?</p>
</blockquote>
</aside>
<p>You can mirror by calling <code>vtkTransform::Scale</code>. Use <code>-1</code> as scale factor for the axes you want to mirror around and <code>1</code> for other axes. Note that for moving physical objects it should not be ever necessary to mirror (as you cannot mirror physical objects in real life either), but you can achieve all physically possible displacements by translate and rotate methods.</p>

---

## Post #3 by @Mik (2020-04-05 18:11 UTC)

<p>It’s safer use rotation on a negative angle for a simple task, i think.</p>
<p><code>transform-&gt;Identity();</code><br>
<code>transform-&gt;RotateY(angle);</code><br>
<code>transform-&gt;Modified();</code><br>
<code>... some other code ...</code><br>
<code>transform-&gt;Identity(); </code><br>
<code>transform-&gt;RotateY(-1. * angle);  // mirror the rotation </code><br>
<code> transform-&gt;Modified();</code></p>

---
