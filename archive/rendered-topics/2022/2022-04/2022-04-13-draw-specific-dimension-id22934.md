# Draw specific dimension

**Topic ID**: 22934
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/draw-specific-dimension/22934

---

## Post #1 by @BORIPHAT (2022-04-13 12:19 UTC)

<p>Hello all,<br>
How can I draw two specific dimension on CT image? Could you please give me some advice? Thank you very much.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67cf63b81dc5f44af7041523ef5892489c85db0a.jpeg" data-download-href="/uploads/short-url/eOlvApdGzhDWnnHyrYKNOHyNcro.jpeg?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67cf63b81dc5f44af7041523ef5892489c85db0a_2_690x445.jpeg" alt="Picture1" data-base62-sha1="eOlvApdGzhDWnnHyrYKNOHyNcro" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67cf63b81dc5f44af7041523ef5892489c85db0a_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67cf63b81dc5f44af7041523ef5892489c85db0a_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67cf63b81dc5f44af7041523ef5892489c85db0a_2_1380x890.jpeg 2x" data-dominant-color="464544"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">1920×1240 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @chir.set (2022-04-13 14:23 UTC)

<p>Tough not exactly what you are showing, you can use the ‘Scissors’ tool of Segment Editor to get close to your picture. Choose Fill inside/ Circle/ Centered/ Symmetric (1.0 mm) to draw a circular segment. You won’t be able to specify an arbitrary diameter numerically.</p>
<p>For more precise drawing, have a look at <a href="https://vtk.org/doc/nightly/html/classvtkDiskSource.html" rel="noopener nofollow ugc">vtkDiskSource</a>. Of course, a new interactive tool should be created if you want to draw with the mouse, or even if you want to specify a center with a fiducial point and a radius with a slider.</p>
<p>Since such a tool does not already exist, it’s usefulness in Slicer’s realm is probably questionable.</p>

---

## Post #3 by @jamesobutler (2022-04-13 14:30 UTC)

<p>Various markups exist for simple measurements such as “Line” for linear measurement, “Angle” for measuring degrees and others for area measurements such as “Closed Curve” and “ROI”, but there is not a markup for creating circles to then get radius values.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html?highlight=markups#place-new-markups" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html?highlight=markups#place-new-markups</a></p>

---

## Post #4 by @lassoan (2022-04-13 18:06 UTC)

<p>For any measurement types that are not supported already by an existing markup, you can create your own custom markup by a little Python scripting. The idea is that you use markups to position models. You can add an observer to the markup so that if a control point position is changed then you get notified and you update the model.</p>
<p>There are a few simple examples in the script repository, as <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">this</a>. There is a more complex example here:</p>
<aside class="quote quote-modified" data-post="3" data-topic="20387">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/drawing-circle-on-ct-image/20387/3">Drawing Circle on CT Image</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can also use 2 points of a markups fiducial node to specify a circle by copy-pasting a few lines of code to into the Python console as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">this example</a>. 
I’ve created a modified script that allows you to place 2 circles by specifying 6 points on the circumference: <a href="https://gist.github.com/lassoan/99514fb5edf98e1e3dda926253dc9742" class="inline-onebox">Compute bone axis in 3D Slicer by specifying two circles. · GitHub</a> 
You can use this by placing one fiducial list containing 6 points then copy-pasting into the Python console: 

  <a href="https://www.youtube.com/watch?v=1DG3y1TqWvw" target="_blank" rel="noopener">
    [Custom interactive measurement using P…</a>
  </blockquote>
</aside>

<p>I would recommend using a vtkSphereSource for drawing a circle because then you don’t need to worry about orientation.</p>

---

## Post #5 by @BORIPHAT (2022-04-14 05:12 UTC)

<p>Thank you very much for your suggestion.</p>

---

## Post #6 by @BORIPHAT (2022-04-14 05:17 UTC)

<p>Thank you very much for your guidance. It was very useful, and now I did it.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/542dcf0f45e40963736e275575f201e86648c25d.png" alt="Picture5" data-base62-sha1="c0GfEwdw7aCqvPGdEqfyCHiIbud" width="657" height="351"></p>

---

## Post #7 by @BORIPHAT (2022-04-14 05:18 UTC)

<p>Thank you very much for your suggestion.</p>

---
