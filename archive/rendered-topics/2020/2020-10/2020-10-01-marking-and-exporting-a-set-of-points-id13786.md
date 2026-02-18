# Marking and exporting a set of points

**Topic ID**: 13786
**Date**: 2020-10-01
**URL**: https://discourse.slicer.org/t/marking-and-exporting-a-set-of-points/13786

---

## Post #1 by @Louis_Kammerer (2020-10-01 06:58 UTC)

<p>Hi, I’m looking for a way to mark a set of points (maybe with fiducials?) on different models to track the movement of changing structures during different stages of growth. Is there a way to mark points and export them with or without the model? All models were created in slicer already.</p>

---

## Post #2 by @pieper (2020-10-01 13:55 UTC)

<p>You may want to put them in a Sequence to manage the time series.  Then each Markups Fiducial list can be exported as can the models.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences" target="_blank" rel="noopener">Documentation/Nightly/Extensions/Sequences - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Louis_Kammerer (2020-10-02 07:02 UTC)

<p>That worked to a degree, I marked the fiducials and made a sequence but the problem is now with alignment, they are all spread out when loaded. All the models are of different sizes but with the same landmarks. Because they are developing embryos the distance between landmarks changes. When I tried to align them with the fiducials then it altered their size to match the landmarks. Aligning them with transforms is long and tedious, is there a smarter way?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/071ef900f00be95126fe18ca33f34d8f3ad3eb14.png" data-download-href="/uploads/short-url/10ZHso8UyI6CvoiTdX16e27nShC.png?dl=1" title="Screenshot (335)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/071ef900f00be95126fe18ca33f34d8f3ad3eb14_2_690x388.png" alt="Screenshot (335)" data-base62-sha1="10ZHso8UyI6CvoiTdX16e27nShC" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/071ef900f00be95126fe18ca33f34d8f3ad3eb14_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/071ef900f00be95126fe18ca33f34d8f3ad3eb14_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/071ef900f00be95126fe18ca33f34d8f3ad3eb14_2_1380x776.png 2x" data-dominant-color="C5C7DC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (335)</span><span class="informations">1920×1080 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2020-10-02 13:44 UTC)

<p>Maybe <a class="mention" href="/u/muratmaga">@muratmaga</a> has tried something similar and can advise.  I’d think you would pick some common feature that exists at all time points and just have everything grow from there.  E.g. if it were a plant you might pick the center of the stalk just where it comes out of the ground; you could use fiducial registration for that and should be able to do just a rigid alignment.</p>

---

## Post #5 by @muratmaga (2020-10-02 15:10 UTC)

<p>If these are embryos of different stages, and if you can put landmarks on them, you can use GPA module to superimpose them and make an animation of the first PC1 (skip the scaling step). You can run a regression to make sure that PC1 is indeed the developmental trajectory but in developmental series it almost always is…</p>
<p>Here is a video of how PC deformations work: <a href="https://www.youtube.com/watch?v=hMMR9GChek8&amp;t=2s" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=hMMR9GChek8&amp;t=2s</a></p>

---
