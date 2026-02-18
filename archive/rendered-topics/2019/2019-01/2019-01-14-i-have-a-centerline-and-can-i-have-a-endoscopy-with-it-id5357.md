# I have a centerline and Can I have a endoscopy with it

**Topic ID**: 5357
**Date**: 2019-01-14
**URL**: https://discourse.slicer.org/t/i-have-a-centerline-and-can-i-have-a-endoscopy-with-it/5357

---

## Post #1 by @timeanddoctor (2019-01-14 14:40 UTC)

<p>I have a centerline and Can I get a endoscopy with it.</p>

---

## Post #2 by @pieper (2019-01-14 18:25 UTC)

<p>There’s no particular interface for that right now - but if you create fiducials from some of the centerline points it should work.</p>

---

## Post #3 by @wpgao (2019-01-15 01:32 UTC)

<p>The trajectory of the endoscopy is described using a list of fiducials. If you want to let the endoscopy move along it, you should represent the centerline with a list of fiducials!</p>

---

## Post #4 by @lassoan (2019-01-15 04:38 UTC)

<p>There will be soon a markup “curve” node available soon (within 1-2 months), mostly based on current markup “fiducial” node, so representing curves using fiducials is the right way to go.</p>

---

## Post #5 by @timeanddoctor (2019-01-15 05:33 UTC)

<p>OK, Thanks,<br>
And I get a “makeup” but with a wrong order. Can I change the order of points with CLI?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b74082e99f0d698f4eccbbb52b9c4ecd3794daa8.jpeg" alt="360%E6%88%AA%E5%9B%BE-181744937" data-base62-sha1="q97AHXnd1u6KM6smrtWZ9EV0Aw8" width="493" height="297"></p>

---

## Post #6 by @lassoan (2019-01-15 05:51 UTC)

<p>There are a couple of options. CLIs can read/write markup lists, so you can make any changes.</p>
<p>MarkupsToModel extension contains code that can automatically reorder markups to make up the most reasonable curve.</p>

---

## Post #7 by @timeanddoctor (2019-01-15 08:51 UTC)

<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerIGT/SlicerMarkupsToModel/tree/master/MarkupsToModel">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerMarkupsToModel/tree/master/MarkupsToModel" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerIGT/SlicerMarkupsToModel/tree/master/MarkupsToModel" target="_blank" rel="noopener nofollow ugc">SlicerMarkupsToModel/MarkupsToModel at master · SlicerIGT/SlicerMarkupsToModel</a></h3>

  <p><a href="https://github.com/SlicerIGT/SlicerMarkupsToModel/tree/master/MarkupsToModel" target="_blank" rel="noopener nofollow ugc">master/MarkupsToModel</a></p>

  <p><span class="label1">3D Slicer extension to create tube or closed surface model from markup fiducials</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
I just studied python myself, but the above code of MarkupsToModel  seems not python language…</p>
<p>My fiducials generated from extra-skeleton with a reverse order not suitable for endoscopy timer.<br>
so I went reorder just like the picture below（I need the right column from [C-1,C-2,C-3,] to [,C-3，C-2，C-1]）<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/240c7911ac853dd6a351e7d2d5963fe933639c01.jpeg" alt="360%E6%88%AA%E5%9B%BE20190115163846999" data-base62-sha1="58TUxWEHoNi1VZd5eok8hCdQloJ" width="140" height="181"></p>

---

## Post #8 by @timeanddoctor (2019-01-15 08:56 UTC)

<p>Can I have a script to deal with that problem?</p>

---

## Post #9 by @lassoan (2019-01-15 13:11 UTC)

<p>Yes, of course. You can manipulate markups directly in Python (by modifying the MRML node), or by using Python-wrapped <em>Markups</em> or <em>Markups to model</em> module logic classes.</p>

---

## Post #10 by @szhang (2020-06-15 11:50 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="5357" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>if you create fiducials from some of the centerline points it should work.</p>
</blockquote>
</aside>
<p>Hello <a class="mention" href="/u/pieper">@pieper</a>, to follow up on this topic, is there a way to convert centerline in the format of Surface Mesh (vtkpolydata) into markup fiducial points? Thank you!</p>

---

## Post #11 by @pieper (2020-06-15 15:53 UTC)

<p>Hi <a class="mention" href="/u/szhang">@szhang</a> - if you do the extraction to Markup Curves that will work with Endoscopy.  What method did you use to create the vtkPolyData?</p>

---

## Post #12 by @szhang (2020-06-15 16:25 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, I used VMTK to extract the centerline as vtkPolyData, which can be represented as Points in 3D Display, but then how to convert these points in vtkPolyData into 1) fiducial points to make curves or 2) directly into Markup Curves ?</p>

---

## Post #13 by @pieper (2020-06-15 17:28 UTC)

<p>I see, yes, makes sense but I haven’t done it myself.  <a class="mention" href="/u/lassoan">@lassoan</a> must have done that for his curve tree work.</p>

---

## Post #14 by @lassoan (2020-06-15 18:03 UTC)

<p>In latest SliverPreview releases, you have the option to specify output markups curve node. If you specify that node then you’ll get centerline as curve node(s) as well. You can use these curve nodes in endoscopy module to create flythrough videos.</p>

---
