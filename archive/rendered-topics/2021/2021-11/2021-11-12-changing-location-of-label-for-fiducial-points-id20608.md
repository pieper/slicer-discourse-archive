# Changing location of label for fiducial points

**Topic ID**: 20608
**Date**: 2021-11-12
**URL**: https://discourse.slicer.org/t/changing-location-of-label-for-fiducial-points/20608

---

## Post #1 by @neuralnet (2021-11-12 22:23 UTC)

<p>Hi all,</p>
<p>I’m new to slicer, so apologies if this question is basic. I’ve been reading the documentation, but haven’t been able to figure this out.</p>
<p>I need to annotate an image by marking several points. However, these points are extremely close to each other in the image. When I add points with labels, the labels overlap and become unreadable, no matter how small I make the text.</p>
<p>Is there any way that the label could be moved away from the point itself, perhaps with a line pointing to the marker? Here is an example of what is happening:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/212f80113c88fc07bff92905cad897fa6f07da3f.png" alt="Screen Shot 2021-11-12 at 2.22.31 PM" data-base62-sha1="4Jzwzw8gPlt6xJGp8LlFNPYBFj9" width="476" height="252"></p>

---

## Post #2 by @mikebind (2021-11-13 00:02 UTC)

<p>Controls for this would be great!  I don’t know if they exist, but I run into this problem frequently as well.</p>

---

## Post #3 by @mikebind (2021-11-13 01:08 UTC)

<p>Searching through this site, I found this, which might be helpful for you:</p>
<aside class="quote quote-modified" data-post="1" data-topic="14590">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/glyph-text-annotation-orientation/14590">Glyph text annotation orientation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, 
Is there a way to change the glyph label orientation? I have a situation where 10 glyphs are inline and the text is overlapping. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc1ab2f837ea33502bc05e3feb5ed5ce38578dfd.jpeg" data-download-href="/uploads/short-url/vp8ffQdfWxS0lMCGuOzuX4FXVpj.jpeg?dl=1" title="Screenshot from 2020-11-13 17-23-34" rel="noopener nofollow ugc">[Screenshot from 2020-11-13 17-23-34]</a> 
It would be great if I could set the orientation to 900. 
Greydon
  </blockquote>
</aside>


---

## Post #4 by @mikebind (2021-11-13 01:24 UTC)

<p>Looks like many of the features we might find helpful are implemented through vtkTextProperty (<a href="https://vtk.org/doc/nightly/html/classvtkTextProperty.html" class="inline-onebox">VTK: vtkTextProperty Class Reference</a>)</p>
<p>As noted above, orientation can be set with SetOrientation, distance from point (perpendicular to baseline) set with SetLineOffset, and relative positioning to point set via the following:</p>
<pre><code class="lang-auto">myMarkupNode.GetDisplayNode().GetTextProperty().SetJustificationToCentered()
myMarkupNode.GetDisplayNode().GetTextProperty().SetJustificationToLeft()
myMarkupNode.GetDisplayNode().GetTextProperty().SetJustificationToRight()
myMarkupNode.GetDisplayNode().GetTextProperty().SetVerticalJustificationToCentered()
myMarkupNode.GetDisplayNode().GetTextProperty().SetVerticalJustificationToBottom()
myMarkupNode.GetDisplayNode().GetTextProperty().SetVerticalJustificationToTop()
</code></pre>
<p>None of these will produce a line connecting the label with the point, but otherwise, there is a fair amount of flexibility here.</p>

---

## Post #5 by @lassoan (2021-11-13 14:37 UTC)

<p>Text size is defined in screen space, so you can make the labels non-overlapping by zooming in or reducing the text size.</p>
<p>Making the labels manually movable would be complicated to implement, especially because in each view the labels would need to be moved in different directions. But at some point we are going to implement this.</p>
<p>If you find that changing text orientation makes a big difference then submit a feature request for it at <a href="http://issues.slicer.org">issues.slicer.org</a>.</p>

---

## Post #6 by @DIV (2021-11-15 07:30 UTC)

<p>Hello, neuralnet.<br>
I’m pretty new to Slicer too, so take the following suggestions with a grain of salt…</p>
<p>I’m not sure whether it helps in your case, but I found that sometimes it’s helpful to rotate the 3D view so that features are arranged more in a vertical line (so it ends up looking like bullets on a <em>PowerPoint</em> slide) rather than in a horizontal line.<br>
Perhaps there is a similar trick that would help for a 2D slice?</p>
<p>Other than that, you could possibly add the points to different ‘nodes’, so that it is easier to show only some markers, and easier to give them distinct colours, rather than having them all toggled on (i.e. visible) together and all in the same colour.</p>
<p>One more thing:  you can shrink the size of the points (set <code>Glyph size</code> in the <em>Display</em> panel of the <strong>Markups</strong> module).  From what I can see in your screenshot, this might help a little where the labels are being printed over the top of other points (which are all in the same colour).<br>
[Possibly it might also help if the text could be a different colour from the markers, in your case, but I don’t know whether that can be done in Slicer.]</p>
<p>—DIV</p>

---

## Post #7 by @neuralnet (2021-11-17 00:32 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> wow!! thank you, this is hugely helpful</p>

---

## Post #8 by @neuralnet (2021-11-17 00:33 UTC)

<p>Thank you, Dr. Lasso!</p>

---

## Post #9 by @neuralnet (2021-11-17 00:34 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> thank you!</p>

---

## Post #10 by @neuralnet (2021-11-17 00:34 UTC)

<p>Hi DIV,</p>
<p>This is a great strategy. I will try it out! Thank you!</p>

---

## Post #11 by @Anna_M (2024-03-25 18:05 UTC)

<p>Quick and dirty workaround: add spaces in front of your label name.<br>
(I know this is an old topic, but there’s still no added feature I can see and this is a common problem in my work.)</p>

---

## Post #12 by @muratmaga (2024-03-25 19:52 UTC)

<aside class="quote no-group" data-username="Anna_M" data-post="11" data-topic="20608">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anna_m/48/69762_2.png" class="avatar"> Anna_M:</div>
<blockquote>
<p>Quick and dirty workaround: add spaces in front of your label name.</p>
</blockquote>
</aside>
<p>Original poster was asking about an ability to draw a line pointing to a text, much like you might do in powerpoint. That’s now possible through the ExtraMarkups extension.</p>
<p>However, changing the position of control point labels would be a nice addition.</p>

---
