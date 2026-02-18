# Zoom factor quantification

**Topic ID**: 20603
**Date**: 2021-11-12
**URL**: https://discourse.slicer.org/t/zoom-factor-quantification/20603

---

## Post #1 by @CETUS (2021-11-12 17:17 UTC)

<p>Hi, I was curious to ask, is there a specific module or window in 3D slicer that displays the zoom factor changed by the mouse as a percentage, or allows it to be set to a specific percentage? (for example, I have 3 scans of 3 different individuals I will be manually segmenting the same structure out of, and I want to be able to set all at 200% as the zoom level to avoid error in my visual recognition of the dimensions of the structures between individuals). Using Slicer 4.11. Thank you for your help!</p>

---

## Post #2 by @DIV (2021-11-15 07:13 UTC)

<p>Hello, Cetus.  Good question.</p>
<p>I don’t know an answer to your specific question in terms of percentages, but perhaps for your purposes you could use the <em>Field of view</em> setting that I found in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/viewcontrollers.html#panels-and-their-use" rel="noopener nofollow ugc"><strong>View Controllers</strong></a> module?  If you link all of the views (with the linked rings button), then you might be able to quickly set all views to the same magnification?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1f5a1eeaefe2d6da7ad05e060d8f8374c19990a.png" data-download-href="/uploads/short-url/poiMd0nHdma9FIOHctHPgqSeK4G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1f5a1eeaefe2d6da7ad05e060d8f8374c19990a_2_360x500.png" alt="image" data-base62-sha1="poiMd0nHdma9FIOHctHPgqSeK4G" width="360" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1f5a1eeaefe2d6da7ad05e060d8f8374c19990a_2_360x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1f5a1eeaefe2d6da7ad05e060d8f8374c19990a_2_540x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1f5a1eeaefe2d6da7ad05e060d8f8374c19990a.png 2x" data-dominant-color="EEEEEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">683×948 58.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m not entirely certain of precisely what the <em>Field of view</em> setting means, because I noticed that if I drag to increase the size of the module pane (on the LHS of the GUI), thereby shrinking the viewport sizes, the <em>Field of view</em> setting is unchanged;  in so doing the magnification doesn’t change, but less of the slice can be seen horizontally on screen.  On the other hand, if I switch from a <code>Four-Up Table</code> layout to a <code>Four-Up</code> layout, thereby expanding the viewport sizes, the <em>Field of view</em> setting increased (from 22.00 to ~36.1);  in so doing the magnification doesn’t change, but more of the slice can be seen vertically on screen.<br>
So, based on that, I suppose it is linked to how much a slice can be seen (on screen) in the relevant viewport, measured vertically (in the on-screen direction).<br>
Then I guess it should be comparable across different scans if you retain the same layout for each scan.</p>
<p>When it comes to a percentage magnification, I suppose that strictly speaking the size of the computer monitor would also be relevant.</p>
<p>—DIV</p>

---
