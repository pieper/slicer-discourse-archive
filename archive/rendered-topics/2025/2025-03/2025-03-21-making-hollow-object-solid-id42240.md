---
topic_id: 42240
title: "Making Hollow Object Solid"
date: 2025-03-21
url: https://discourse.slicer.org/t/42240
---

# Making hollow object solid 

**Topic ID**: 42240
**Date**: 2025-03-21
**URL**: https://discourse.slicer.org/t/making-hollow-object-solid/42240

---

## Post #1 by @Jrneal241 (2025-03-21 02:32 UTC)

<p>Hi, I am trying to 3D print a gill raker using a Formlabs resin printer. The gill raker is covered with mineralized structures (denticles), but the middle is completely hollow (b/c connective tissue). Currently, I have tried meshmixer, Blender, and 3D slicer to make the object solid and fill it in, without covering the denticles, but I cannot seem to fix this issue. I have attached an image that will hopefully help. As you can see in the image, some denticles are islands but I want to keep most of them. Thank you for your help!! I appreciate it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f9836df684eaa315efc6dcfc5b43a4471af8e69.jpeg" data-download-href="/uploads/short-url/94Acixtw8iaq0VyRFH69xSDzIql.jpeg?dl=1" title="GillRaker_volumerendering" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f9836df684eaa315efc6dcfc5b43a4471af8e69_2_356x500.jpeg" alt="GillRaker_volumerendering" data-base62-sha1="94Acixtw8iaq0VyRFH69xSDzIql" width="356" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f9836df684eaa315efc6dcfc5b43a4471af8e69_2_356x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f9836df684eaa315efc6dcfc5b43a4471af8e69_2_534x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f9836df684eaa315efc6dcfc5b43a4471af8e69_2_712x1000.jpeg 2x" data-dominant-color="150F0B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GillRaker_volumerendering</span><span class="informations">1039×1456 63.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Arash1 (2025-03-23 02:04 UTC)

<p>Hi. I hope you are doing well.</p>
<p>Few steps could be helpful here.</p>
<ol>
<li>In the Segment Editor, ([Segment editor — 3D Slicer documentation], (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a>), use Islands to remove small parts.</li>
<li>Use the Hollow tool to create a ‘shell’. The shell thickness can fill out the middle part. If this doesn’t work, you can use the Logical Operators, Invert the segment, and use hollow. The difference here would be to use the segment as the outside.</li>
</ol>
<p>The Shell thickness when increased, will fill the hollow  centre.</p>

---

## Post #3 by @Jrneal241 (2025-03-23 15:16 UTC)

<p>Thank you so much! I’ll try <span class="hashtag-raw">#2</span> and see how that works. Thanks again!</p>

---

## Post #4 by @Arash1 (2025-03-23 16:44 UTC)

<p>I would recommend including both steps as those pieces not attached to the main segment may cause challenges with steps 2 and with your 3d printing.</p>

---

## Post #5 by @cpinter (2025-03-24 10:18 UTC)

<p>Have you tried WrapSolidify?</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">
  <header class="source">

      <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/bd602992e35b25ecc43ecf92acc01816/sebastianandress/Slicer-SurfaceWrapSolidify" class="thumbnail">

  <h3><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" target="_blank" rel="noopener">GitHub - sebastianandress/Slicer-SurfaceWrapSolidify: 3D Slicer extension which contains a Segment...</a></h3>

    <p><span class="github-repo-description">3D Slicer extension which contains a Segment Editor Effect that solidifies and extracts the surface of a segmentation</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This extension is for making objects solid. I think the previous answer was about the opposite.</p>

---

## Post #6 by @Arash1 (2025-03-31 23:30 UTC)

<p>Hi.<br>
I believe I didn’t explain adequately, which led to confusion. My apologies. I suggested using the hollow tool because of the nature of the model (lots of grooves and edges). WrapSolidify works fantastic for bone and teeth, but we usually get lots of bleeding for a structure with lots of small details or inconsistencies within the segmentation. We might be doing something wrong for the parameters.<br>
For 3D printing, if the hollow tool is used and the shell thickness is increased, the shell lines will fill the empty space at the centreline. This is pretty much a workaround.</p>

---
