---
topic_id: 20875
title: "Extract Hounsfield Units Of Segmentation And Save"
date: 2021-12-02
url: https://discourse.slicer.org/t/20875
---

# Extract HounsField Units of Segmentation and Save

**Topic ID**: 20875
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/extract-hounsfield-units-of-segmentation-and-save/20875

---

## Post #1 by @kookoo9999 (2021-12-02 05:56 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a><br>
Hello lassoan ,<br>
I read <a href="https://discourse.slicer.org/t/export-hounsfield-unit-values-as-a-table-from-each-segmentation/18296/15">this</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" rel="noopener nofollow ugc">this</a> too. And I tried to extract HounsField Units and checked saved file when I clicked “Reload and Test” button.<br>
These are result.csv and script code.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a8d1832621cac17f3a046b90a255e344ce9139.png" data-download-href="/uploads/short-url/wLF20WhQZy9MdmQ6hNHjPDJi5XX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5a8d1832621cac17f3a046b90a255e344ce9139_2_682x500.png" alt="image" data-base62-sha1="wLF20WhQZy9MdmQ6hNHjPDJi5XX" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5a8d1832621cac17f3a046b90a255e344ce9139_2_682x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a8d1832621cac17f3a046b90a255e344ce9139.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a8d1832621cac17f3a046b90a255e344ce9139.png 2x" data-dominant-color="303131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">949×695 71.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe6f0512d042894de5c3be8cfc9bb9489e1b892c.png" data-download-href="/uploads/short-url/AiP8s9SXFaOSmPbHgJLyNRw4nOQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe6f0512d042894de5c3be8cfc9bb9489e1b892c.png" alt="image" data-base62-sha1="AiP8s9SXFaOSmPbHgJLyNRw4nOQ" width="637" height="500" data-dominant-color="2F2F2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×626 50.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b11ddf250780ed146ef7ca6b9d51efaac4b58a63.png" data-download-href="/uploads/short-url/pgQvK8HT4T23rBmqhZQWqbcRXhx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b11ddf250780ed146ef7ca6b9d51efaac4b58a63.png" alt="image" data-base62-sha1="pgQvK8HT4T23rBmqhZQWqbcRXhx" width="264" height="500" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">396×748 9.09 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Next day I reboot my local pc then reload and test my module, permission error is appear.<br>
after a few minutes, When I retry there was no error…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/634b42005486b70651367ea07ed336fdae320c44.png" data-download-href="/uploads/short-url/eaovxsCB7ORmxlqhLLTrMnzrdFG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/634b42005486b70651367ea07ed336fdae320c44.png" alt="image" data-base62-sha1="eaovxsCB7ORmxlqhLLTrMnzrdFG" width="689" height="131" data-dominant-color="FEF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1209×230 13.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to obtain HU values for outputs made through the Segment editor, How do I set <code>masterVolumeNode</code> , <code>segmentationNode</code> , <code>labelValue</code> ???<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6187321e21ba6e13d8e4ce8628811c45466b225.png" data-download-href="/uploads/short-url/sgqVbXwA8LDFBJkDSqjfRI2aOq1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6187321e21ba6e13d8e4ce8628811c45466b225_2_493x500.png" alt="image" data-base62-sha1="sgqVbXwA8LDFBJkDSqjfRI2aOq1" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6187321e21ba6e13d8e4ce8628811c45466b225_2_493x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6187321e21ba6e13d8e4ce8628811c45466b225_2_739x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6187321e21ba6e13d8e4ce8628811c45466b225_2_986x1000.png 2x" data-dominant-color="9598A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×1003 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for reading!!</p>

---

## Post #2 by @kookoo9999 (2021-12-02 15:29 UTC)

<p>I edit code, but “getNode” is not recognized as a member function. and " *sgmentVoxels" too.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5def41b5af92b0c3fee674be7473bda540421f45.jpeg" data-download-href="/uploads/short-url/doZ0BKJazqkBggfjhPDvbs7go97.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5def41b5af92b0c3fee674be7473bda540421f45_2_690x264.jpeg" alt="image" data-base62-sha1="doZ0BKJazqkBggfjhPDvbs7go97" width="690" height="264" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5def41b5af92b0c3fee674be7473bda540421f45_2_690x264.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5def41b5af92b0c3fee674be7473bda540421f45.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5def41b5af92b0c3fee674be7473bda540421f45.jpeg 2x" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×341 73.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15d3f50a502065e3df04f5693a10c5f264e53e9e.png" data-download-href="/uploads/short-url/3768RVBmoHbAJSNDHcHFPELoEDs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15d3f50a502065e3df04f5693a10c5f264e53e9e.png" alt="image" data-base62-sha1="3768RVBmoHbAJSNDHcHFPELoEDs" width="690" height="55" data-dominant-color="FEF1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">987×80 3.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t want sample data’s Volume(2D View, R,G,Y) , How do I edit code??<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d3973b01c05895af2a6f4be4622882472136c8b.jpeg" data-download-href="/uploads/short-url/4awW4ZPf4vZzfSqPZI9O9VI49f5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d3973b01c05895af2a6f4be4622882472136c8b_2_690x373.jpeg" alt="image" data-base62-sha1="4awW4ZPf4vZzfSqPZI9O9VI49f5" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d3973b01c05895af2a6f4be4622882472136c8b_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d3973b01c05895af2a6f4be4622882472136c8b_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d3973b01c05895af2a6f4be4622882472136c8b.jpeg 2x" data-dominant-color="898A99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1241×671 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @kookoo9999 (2021-12-06 09:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I’m sorry for tagging you. Can you take a look when you have some free time?</p>

---

## Post #4 by @lassoan (2021-12-06 13:37 UTC)

<p>If you have <code>import slicer</code> in your module source code then you can access functions in <code>slicer.util</code> like this: <code>slicer.util.getNode('someNode')</code>.</p>
<p>Note that <code>getNode</code> method is intended for testing and debugging only. In scripted modules you usually don’t know in advance the ID or name of the node that the user will choose, but you get the selected node from a MRML node selector widget.</p>

---

## Post #5 by @kookoo9999 (2021-12-07 00:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/178b4f723ef38aab42eea60fbb50bdb89c71ea71.png" data-download-href="/uploads/short-url/3mhs4IEco8Pu7Ia7yBANqfD9xf3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/178b4f723ef38aab42eea60fbb50bdb89c71ea71.png" alt="image" data-base62-sha1="3mhs4IEco8Pu7Ia7yBANqfD9xf3" width="690" height="302" data-dominant-color="252626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">923×405 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba129e63cebf331466642743498a3a66c38667c5.png" data-download-href="/uploads/short-url/qy4Hormd2tJhlICnkpgVFO1V4kl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba129e63cebf331466642743498a3a66c38667c5_2_683x500.png" alt="image" data-base62-sha1="qy4Hormd2tJhlICnkpgVFO1V4kl" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba129e63cebf331466642743498a3a66c38667c5_2_683x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba129e63cebf331466642743498a3a66c38667c5_2_1024x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba129e63cebf331466642743498a3a66c38667c5.png 2x" data-dominant-color="ACACB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1247×912 89.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2561ebef699cb33d8444c486d6c85ad400fd0c94.png" data-download-href="/uploads/short-url/5kHsFU1DchJnkU3pVWHge6UFvxy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2561ebef699cb33d8444c486d6c85ad400fd0c94_2_690x418.png" alt="image" data-base62-sha1="5kHsFU1DchJnkU3pVWHge6UFvxy" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2561ebef699cb33d8444c486d6c85ad400fd0c94_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2561ebef699cb33d8444c486d6c85ad400fd0c94_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2561ebef699cb33d8444c486d6c85ad400fd0c94.png 2x" data-dominant-color="9FA2AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1247×756 85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I edit the code like capture, but An error has appeared…</p>

---

## Post #6 by @lassoan (2021-12-07 03:40 UTC)

<p>You should get the input <code>segmentationNode</code> and <code>masterVolumeNode</code> from your node selectors - something like <code>segmentationNode = self.ui.segmentationNodeSelector.currentNode()</code>.</p>
<p>You set the output <code>labelmapVolumeNode</code> correctly in the <code>...AddNewNodeByClass...</code> line. The <code>labelmapVolumeNode = slicer.util.getNode...</code> line should be deleted.</p>

---

## Post #7 by @kookoo9999 (2021-12-08 23:59 UTC)

<p>Thanks for reply and sorry to check lately.<br>
I edit segemntationNode,labelmapVolumeNode,masterVolumeNode like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98bb154a9c6f3db0326842166aba1f8a9abd13b4.png" data-download-href="/uploads/short-url/lN7oL6tLIvCWzsVqOvyczRppSAY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98bb154a9c6f3db0326842166aba1f8a9abd13b4.png" alt="image" data-base62-sha1="lN7oL6tLIvCWzsVqOvyczRppSAY" width="690" height="308" data-dominant-color="252626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">924×413 26.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fae91769757905e15789e5896252c149d13f422.png" data-download-href="/uploads/short-url/6NOs0FRujQnX6IWFzUf5FssO4HU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fae91769757905e15789e5896252c149d13f422.png" alt="image" data-base62-sha1="6NOs0FRujQnX6IWFzUf5FssO4HU" width="690" height="121" data-dominant-color="FDF7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1029×181 4.44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to get HU Values, when I click “Get HU Values” . but this error is occured…</p>

---

## Post #8 by @kookoo9999 (2021-12-10 09:06 UTC)

<p>I edit default Button’s code( “Apply”)  like this photo.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d664b17daeaf17c1fc5f25991a78f3f733ccb7fd.png" alt="image" data-base62-sha1="uABUC3VG0TEpuLCtiIQf2qnc6tf" width="529" height="332"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b58a67364fc99e1ba156cc4e8b6a8886a676758a.png" data-download-href="/uploads/short-url/pTYWSbGbInsztARIC8N5LjtOC3o.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b58a67364fc99e1ba156cc4e8b6a8886a676758a.png" alt="image" data-base62-sha1="pTYWSbGbInsztARIC8N5LjtOC3o" width="690" height="351" data-dominant-color="242424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">967×493 22.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17ab07be7e4798786a31912ff0122787cc44270a.png" data-download-href="/uploads/short-url/3nnpzqsQbDSwhp1KPZm1RomJ6hs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17ab07be7e4798786a31912ff0122787cc44270a.png" alt="image" data-base62-sha1="3nnpzqsQbDSwhp1KPZm1RomJ6hs" width="690" height="399" data-dominant-color="252524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">908×526 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07017dd010e0c6bb68819b937a9eb72ee80b5110.png" alt="image" data-base62-sha1="ZYxl0sHI280mRtFmJpyJQlQjT2" width="599" height="153"></p>
<p>And when I click Apply Button, result img and csv file are these .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aaf005d8055da9903b6c47118e3d19a97c7a077.png" data-download-href="/uploads/short-url/8n8DbQmK4HgE6zQbKwXfLAUbQjB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aaf005d8055da9903b6c47118e3d19a97c7a077_2_690x366.png" alt="image" data-base62-sha1="8n8DbQmK4HgE6zQbKwXfLAUbQjB" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aaf005d8055da9903b6c47118e3d19a97c7a077_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aaf005d8055da9903b6c47118e3d19a97c7a077_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aaf005d8055da9903b6c47118e3d19a97c7a077_2_1380x732.png 2x" data-dominant-color="915971"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1386×737 23.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee450bcd69dab8f6b15d6a483feb66f80abc77f6.png" alt="image" data-base62-sha1="xZPzfxTBdDHWnQI9VzziHlvwf6S" width="645" height="400"></p>
<p>Now Volume Display is update, but I can’t find HU Values and don’t want to show Red Circle Volume in Volume Display…</p>

---

## Post #9 by @lassoan (2021-12-10 18:03 UTC)

<p>We cannot review and comment on source code in screenshots. Could you upload your module (including all the files that the Extension Wizard generated) to github and post the link here?</p>

---

## Post #10 by @kookoo9999 (2021-12-12 03:30 UTC)

<p>Thanks for reply.<br>
I uploaded the source at <a href="https://github.com/kookoo9999/HounsFieldUnit" rel="noopener nofollow ugc">here</a>.<br>
Please review it. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #11 by @kookoo9999 (2021-12-13 09:07 UTC)

<p>I want to get the HU Values(x,y,z,HU) from Segment(via 3D Slicer Segmentation Editor’s output).</p>
<p>I tried debugging using VS Code, and I checked that labelmapVolumeNode had no value. And it is also true that we can’t find a way to check the volume and segment.<br>
If you don’t mind, can you show me your source code?</p>

---

## Post #12 by @kookoo9999 (2021-12-21 00:09 UTC)

<p>Hello , <a class="mention" href="/u/lassoan">@lassoan</a><br>
How do I get the Hounsfield Unit Values for the Segment Volume that I made using SegmentEditor? I should like to have the benefit of your advice.<br>
You can check my source code at <a href="https://github.com/kookoo9999/HounsFieldUnit" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #13 by @lassoan (2021-12-21 05:45 UTC)

<p>These <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#quantifying-segments">examples in the script repository</a> should help.</p>

---

## Post #14 by @kookoo9999 (2021-12-21 07:31 UTC)

<p>Thanks for reply!<br>
There was an error that I couldn’t find the getNode, so I modified it to slicer.util.getNode, and this error came out.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d01688e8e05d7db0c896eff08f792f29321d8a3.png" data-download-href="/uploads/short-url/k7ol8iXQr6gxG8Rgjd0uTkpyvGX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d01688e8e05d7db0c896eff08f792f29321d8a3.png" alt="image" data-base62-sha1="k7ol8iXQr6gxG8Rgjd0uTkpyvGX" width="690" height="83" data-dominant-color="232121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1539×187 7.32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @kookoo9999 (2021-12-21 07:54 UTC)

<p>You can see the edit source code <a href="https://github.com/kookoo9999/HounsFieldUnit" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #16 by @kookoo9999 (2022-01-05 23:51 UTC)

<p>I occured this message "AttributeError : ‘MRMLCore.vtkMRMLScalarVolumeNode’  object has no attribute ‘GetSegmentation’ from this line “segmentationNode.GetSegmentation().GetNthSegmentID(0)”  when I clicked the ‘Get HU Values’ button.<br>
You can check ‘Get HU Values’ button’s all source at <a href="https://github.com/kookoo9999/HounsFieldUnit/blob/main/HounsFieldUnit.py" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #17 by @lassoan (2022-01-06 01:13 UTC)

<p>The error message is truncated. Always copy-paste the entire error message <em>text</em> (in addition to that you can also attach screenshots but only if they contain more information than just a textbox).</p>
<p>The error message tells that you passed a volume node as an argument to Segment Statistics module, but it expected that argument to be a segmentation node instead.</p>

---

## Post #18 by @kookoo9999 (2022-01-06 03:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for reply.<br>
This is full error message.<br>
Traceback (most recent call last):<br>
File “C:/Slicer_Module/HounsFiledUnit/src/HounsFieldUnit/HounsFieldUnit/HounsFieldUnit.py”, line 358, in onGetHUButton<br>
segmentId = segmentationNode.GetSegmentation().GetNthSegmentID(0)<br>
AttributeError: ‘MRMLCore.vtkMRMLScalarVolumeNode’ object has no attribute ‘GetSegmentation’</p>
<p>and This is photo of full code of Get HU Buttons.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edb369331a5260e75dba66c00abdaa60161fe85a.png" data-download-href="/uploads/short-url/xUNxTkYfoTTIKzS7GXoCs4iUeCe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edb369331a5260e75dba66c00abdaa60161fe85a.png" alt="image" data-base62-sha1="xUNxTkYfoTTIKzS7GXoCs4iUeCe" width="690" height="254" data-dominant-color="28292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">691×255 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @kookoo9999 (2022-01-07 02:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hello, lassoan<br>
I modified code to this and get result by .csv format.</p>
<blockquote>
<pre><code>segmentationNode = slicer.util.getNode("Segment_1_1")

masterVolumeNode = slicer.util.getNode("Segment")

labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")

slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode,labelmapVolumeNode,masterVolumeNode)



volumeArray = slicer.util.arrayFromVolume(masterVolumeNode)

labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)

labelValue = 1

segmentVoxels = volumeArray[labelArray==labelValue]



import numpy as np

coordinates = np.where(labelArray==labelValue)

hu = volumeArray[coordinates]



coordinateWithHU = np.zeros([len(coordinates[0]),4])

coordinateWithHU[:,0:3] = np.array(coordinates).T

coordinateWithHU[:,3] = hu

slicer.util.pip_install('pandas')

import pandas as pd

pd.DataFrame(coordinateWithHU).to_csv("c:/Extraction_IJK_of_HU.csv")
</code></pre>
</blockquote>
<p>and I know colum ‘A’ means count of voxels, but I don’t know what rows(0,1,2,3) mean.<br>
what is HU Values ??</p>

---

## Post #20 by @kookoo9999 (2022-03-22 06:08 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Hello, My code is <a href="https://github.com/kookoo9999/HounsFieldUnit" rel="noopener nofollow ugc">here</a> and you can check data I used in “data” directory.<br>
After I input the sample directory’s data and occured coordinates(maybe x,y,z,hu) but HU(HounsField Unit) value is number one(1)…<br>
I can’t understand why HU is 1. I think HU get coordinates(x,y,z) each HU values and these values are not same.<br>
Can you review my code??<br>
Thank you.</p>

---
