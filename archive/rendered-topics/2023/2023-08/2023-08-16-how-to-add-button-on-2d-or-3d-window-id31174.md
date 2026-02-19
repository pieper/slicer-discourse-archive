---
topic_id: 31174
title: "How To Add Button On 2D Or 3D Window"
date: 2023-08-16
url: https://discourse.slicer.org/t/31174
---

# How to add button on 2d or 3d window?

**Topic ID**: 31174
**Date**: 2023-08-16
**URL**: https://discourse.slicer.org/t/how-to-add-button-on-2d-or-3d-window/31174

---

## Post #1 by @jay1987 (2023-08-16 12:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ac450b7300d117664e438b1a7f7e02863c6db8.jpeg" data-download-href="/uploads/short-url/3wgxOE5IbxzHAuZqe89zcIE1Jva.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ac450b7300d117664e438b1a7f7e02863c6db8.jpeg" alt="image" data-base62-sha1="3wgxOE5IbxzHAuZqe89zcIE1Jva" width="454" height="500" data-dominant-color="5E554E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">617×679 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
hello community,like the picture above, i want to add three pushbutton on the right bottom part of 2d window,how to do the work?</p>

---

## Post #2 by @pieper (2023-08-16 15:02 UTC)

<p>Good question - this code seems to work.  You’d need to add some extra code if you want to have it show up in the lower right corner and track window resizes and things.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; sliceButton = qt.QPushButton("Slice")
&gt;&gt;&gt; sliceButton.setParent(slicer.app.layoutManager().sliceWidget("Red"))
&gt;&gt;&gt; sliceButton.geometry = qt.QRect(0,0,200,200)
&gt;&gt;&gt; sliceButton.show()
&gt;&gt;&gt; 
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c54542a96ae92de0579391f23d68793ac03ac01.png" data-download-href="/uploads/short-url/miX9R1SJPi8R861GTx51pdmPKCJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c54542a96ae92de0579391f23d68793ac03ac01_2_690x466.png" alt="image" data-base62-sha1="miX9R1SJPi8R861GTx51pdmPKCJ" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c54542a96ae92de0579391f23d68793ac03ac01_2_690x466.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c54542a96ae92de0579391f23d68793ac03ac01_2_1035x699.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c54542a96ae92de0579391f23d68793ac03ac01.png 2x" data-dominant-color="656466"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×774 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @jay1987 (2023-08-17 05:05 UTC)

<p>thank you pieper! the code is very useful!</p>

---
