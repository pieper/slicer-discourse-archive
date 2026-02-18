# Glyph text annotation orientation

**Topic ID**: 14590
**Date**: 2020-11-13
**URL**: https://discourse.slicer.org/t/glyph-text-annotation-orientation/14590

---

## Post #1 by @Greydon_Gilmore (2020-11-13 22:26 UTC)

<p>Hello,</p>
<p>Is there a way to change the glyph label orientation? I have a situation where 10 glyphs are inline and the text is overlapping.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc1ab2f837ea33502bc05e3feb5ed5ce38578dfd.jpeg" data-download-href="/uploads/short-url/vp8ffQdfWxS0lMCGuOzuX4FXVpj.jpeg?dl=1" title="Screenshot from 2020-11-13 17-23-34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc1ab2f837ea33502bc05e3feb5ed5ce38578dfd_2_690x464.jpeg" alt="Screenshot from 2020-11-13 17-23-34" data-base62-sha1="vp8ffQdfWxS0lMCGuOzuX4FXVpj" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc1ab2f837ea33502bc05e3feb5ed5ce38578dfd_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc1ab2f837ea33502bc05e3feb5ed5ce38578dfd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc1ab2f837ea33502bc05e3feb5ed5ce38578dfd.jpeg 2x" data-dominant-color="434143"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-11-13 17-23-34</span><span class="informations">835×562 75.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It would be great if I could set the orientation to 90<sup>0</sup>.</p>
<p>Greydon</p>

---

## Post #2 by @lassoan (2020-11-14 05:33 UTC)

<p>You can change the angle of the labels via the markups display node, by typing this into the Python console:</p>
<pre><code>markupsNode = getNode('F')
markupsNode.GetDisplayNode().GetTextProperty().SetOrientation(45.0)
</code></pre>
<p>This property is not saved into the scene, so you need to set it each time you create or load a node. If this feature proves to be useful for you then let us know and we can add it to the GUI and save the information in the scene file.</p>
<p>Note that you can also make labels more visible by rotating the view, adjusting font size, zooming in the view, or making labels shorter.</p>

---

## Post #3 by @Greydon_Gilmore (2020-11-20 18:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> this is a good solution for now, thank you. I think it would be a valuable addition for our clinical team. We use SEEGAssistant to localize SEEG depth electrode contacts. Depending on the number of electrodes and contact spacing it gets quite crowded.</p>
<p>Could this be added to the nightly?</p>

---
