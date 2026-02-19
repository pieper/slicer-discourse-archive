---
topic_id: 43277
title: "Efficient Segmentation Of Fossil Vertebrae From Matrix In 3D"
date: 2025-06-09
url: https://discourse.slicer.org/t/43277
---

# Efficient Segmentation of Fossil Vertebrae from Matrix in 3D Slicer

**Topic ID**: 43277
**Date**: 2025-06-09
**URL**: https://discourse.slicer.org/t/efficient-segmentation-of-fossil-vertebrae-from-matrix-in-3d-slicer/43277

---

## Post #1 by @Busra_Pullu1 (2025-06-09 19:42 UTC)

<p>Hi all,</p>
<p>I’m working with an undergrad student to segment <strong>individual fossil vertebrae</strong> from a CT-scanned <strong>articulated specimen</strong> (paleontological data). We’re using <strong>3D Slicer</strong>, and the matrix and bone have <strong>very similar densities</strong>, making thresholding difficult.</p>
<p>We’ve managed to get a decent volume rendering using adjusted thresholds, but we’re still struggling with effective <strong>segmentation techniques</strong> to isolate bones cleanly.</p>
<p><strong>Our key challenges:</strong></p>
<ul>
<li>Bone and matrix are hard to distinguish by intensity alone.</li>
<li>We’d like to avoid painstaking slice-by-slice manual painting, if possible.</li>
<li>We’re working with articulated vertebrae, so some separation between elements would be helpful.</li>
</ul>
<p><strong>Questions:</strong></p>
<ol>
<li>Are there any recommended tutorials or workflows specifically for fossil or archaeological materials?</li>
<li>Is there a better way to improve segmentation beyond thresholding — e.g., region growing, AI tools, or semi-automated methods?</li>
<li>Any tips on segmenting <strong>multiple similar elements</strong> (e.g., vertebrae) efficiently?</li>
</ol>
<p>Thanks so much for any guidance! We’ve found medical examples helpful, but fossil data seems to need a different approach.</p>
<p>Best,<br>
B</p>

---

## Post #2 by @muratmaga (2025-06-09 20:02 UTC)

<aside class="quote no-group" data-username="Busra_Pullu1" data-post="1" data-topic="43277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/busra_pullu1/48/79395_2.png" class="avatar"> Busra_Pullu1:</div>
<blockquote>
<p>Is there a better way to improve segmentation beyond thresholding — e.g., region growing, AI tools, or semi-automated methods?</p>
</blockquote>
</aside>
<p>All of those are available in Slicer.</p>
<p>Try painting a few seeds and the use the <code>Grow from the seeds</code> effect in Segment Editor. Lately, I am using the NNInteractive extension with quite a bit of success in similar settings. However, you if you have large volume, you will need to crop the volume into smaller chunks so that NNInteractive works effectively.</p>
<p>See the documentation at: <a href="https://github.com/coendevente/SlicerNNInteractive/blob/main/README.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerNNInteractive/README.md at main · coendevente/SlicerNNInteractive · GitHub</a></p>

---

## Post #3 by @CarlosJWinkler (2025-06-11 09:55 UTC)

<p>Hi dear,</p>
<p>Let me help us whith my knowlegd,<br>
I would like receive CT data in order convert and help do a flow of convertation.<br>
My email is: <a href="mailto:printerize3d@gmail.com">printerize3d@gmail.com</a>.</p>

---
