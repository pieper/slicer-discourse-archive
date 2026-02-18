# Color changed in a display but not in data box while loaded by Python script

**Topic ID**: 26459
**Date**: 2022-11-27
**URL**: https://discourse.slicer.org/t/color-changed-in-a-display-but-not-in-data-box-while-loaded-by-python-script/26459

---

## Post #1 by @Jakub_Mitura (2022-11-27 14:40 UTC)

<p>I am loading set of the labels from paths like in code below</p>
<pre><code class="lang-auto">        label= slicer.util.loadSegmentation(labPath.as_posix(),labPath.name) 
        idss=label[1].GetDisplayNode().GetVisibleSegmentIDs()
        colorr= listOfColors[index]
        label[1].GetDisplayNode().SetSegmentOverrideColor(idss[0],*colorr)
</code></pre>
<p>As one can see below  this manages to set the color in the display but the color in the data menu on the left is default green - So i o not know which label is related to which color while displaying - what am I doing wrong ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/996498e0dd48c0c3134473dc92bd3b1e46a18024.jpeg" data-download-href="/uploads/short-url/lSYA34HyYcue4tIkyN64fUR9sZC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/996498e0dd48c0c3134473dc92bd3b1e46a18024_2_690x338.jpeg" alt="image" data-base62-sha1="lSYA34HyYcue4tIkyN64fUR9sZC" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/996498e0dd48c0c3134473dc92bd3b1e46a18024_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/996498e0dd48c0c3134473dc92bd3b1e46a18024.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/996498e0dd48c0c3134473dc92bd3b1e46a18024.jpeg 2x" data-dominant-color="828285"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">852×418 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-11-27 15:58 UTC)

<p><code>SetSegmentOverrideColor</code> method is provided for special cases: when you want to display a segment in a particular view with a different color than the segment’s color specified in</p>
<pre><code>segmentationNode.GetSegmentation().GetSegment(segmentID).SetColor(r,g,b)
</code></pre>
<p>See <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html#af59758179523133bbc04156bd4bb2f34"><code>SetSegmentOverrideColor</code> method documentation</a>:</p>
<blockquote>
<p>Set segment override color by segment ID Override color is used for specifying custom color for a segment in selected views. By default, segment color is invalid (-1,-1,-1), which means that the color stored in <a href="https://apidocs.slicer.org/master/classvtkSegment.html">vtkSegment</a> object will be used. If a valid override color is specified then in the views corresponding to this display node, segment will be colored using the override color.</p>
</blockquote>

---

## Post #3 by @Jakub_Mitura (2022-11-27 16:05 UTC)

<p>Thanks Hovewer for reply Now when I use code as below I get blank indicators in data tab</p>
<pre><code class="lang-auto">        label[1].GetSegmentation().GetSegment(idss[0]).SetColor(colorr[0],colorr[1],colorr[2])
</code></pre>
<p>I am using Slicer in browser using unmodified slicer jupyter docker container<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0e9c44e449594b527bf51281430db1daa4d2205.png" data-download-href="/uploads/short-url/pf2SqE1roPBPsp2Y0Q9mKWwzzyl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0e9c44e449594b527bf51281430db1daa4d2205_2_690x338.png" alt="image" data-base62-sha1="pf2SqE1roPBPsp2Y0Q9mKWwzzyl" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0e9c44e449594b527bf51281430db1daa4d2205_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0e9c44e449594b527bf51281430db1daa4d2205.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0e9c44e449594b527bf51281430db1daa4d2205.png 2x" data-dominant-color="878687"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">852×418 94.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-11-27 16:10 UTC)

<p>You specified white color for the segment (all RGB values were set to values &gt;= 1.0). RGB color in VTK are defined by numbers between 0.0 … 1.0 (not 0 … 255).</p>
<p>If you previously set SegmentOverrideColor, don’t forget to reset it by setting it to (-1,-1,-1).</p>

---

## Post #5 by @Jakub_Mitura (2022-11-27 16:11 UTC)

<p>Yes it was It - thank You !!</p>

---
