# Screen Capture features

**Topic ID**: 14860
**Date**: 2020-12-03
**URL**: https://discourse.slicer.org/t/screen-capture-features/14860

---

## Post #1 by @torquil (2020-12-03 09:39 UTC)

<p>Hi!</p>
<p>There are two features that I am missing from the Screen Capture module:</p>
<ol>
<li>Easily select to create a video in the reverse direction, i.e. “reverse yaw” og “reverse pitch”.</li>
<li>Sometimes it is important for me to have create a 360 degree rotate and have full control over the initial/ending camera position. So it would be nice to be able to select the angle specification from 0 to 360 degrees, instead of being forced to use -180 to 180 degrees. As it is now, I’m using trial and error to select the camera position so that the initial camera position in the “yaw”-rotation is correct. It would be quite easy to just be able to select the rotation angle from 0 to 360.</li>
</ol>
<p>Best regards<br>
Torquil Sørensen</p>

---

## Post #2 by @muratmaga (2020-12-04 00:41 UTC)

<p>You can try the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator"><code>Animator</code></a> module in SlicerMorph extenion that gives you a bit more control over the rotation and has the option of changing transfer functions etc.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="oGtvTOhIFtA" data-video-title="SlicerAnimator" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=oGtvTOhIFtA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/oGtvTOhIFtA/maxresdefault.jpg" title="SlicerAnimator" width="" height="">
  </a>
</div>


---

## Post #3 by @lassoan (2020-12-04 06:06 UTC)

<p>ScreenCapture module is fairly simple, so it should not be hard to add these options.</p>
<p>Reverse yaw and Reverse pitch could be two additional options in Rotation axis (and we should probably rename “Rotation axis” to “Rotation direction”).</p>
<p>If the problem is that you don’t see what the start/end orientation is then a simple solution could be to rotate the 3D view in real-time to preview the end position while you are holding down the mouse button, and once you release the button, jump back to the original (center) orientation. To implement this, you can get the <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkRangeWidget.h#L192">ctkDoubleRangeSlider</a> from the ctkDoubleRangeWidget and then connect functions to its <a href="https://github.com/commontk/CTK/blob/18715f18b44fd557106a180a01deeca7f8a89946/Libs/Widgets/ctkDoubleRangeSlider.h#L220-L227">sliderPressed and sliderReleased</a> events (save view position on sliderPressed and restore view position on sliderReleased).</p>

---
