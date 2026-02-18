# Sequence recording shifting while scrolling through 2D slices

**Topic ID**: 5644
**Date**: 2019-02-05
**URL**: https://discourse.slicer.org/t/sequence-recording-shifting-while-scrolling-through-2d-slices/5644

---

## Post #1 by @athanell (2019-02-05 18:12 UTC)

<p>Hello 3D Slicer users,</p>
<p>I am using the sequence browser, trying to record a slice scrolling through a head CT volume as you can see in the following screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c84a4d172539a588f6fda44d16171169a29ce16.jpeg" data-download-href="/uploads/short-url/44hyy3QxmfInmp7jOxADZ0uYDbg.jpeg?dl=1" title="sequence_browser_slicer3D_screebshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c84a4d172539a588f6fda44d16171169a29ce16_2_689x355.jpeg" alt="sequence_browser_slicer3D_screebshot" data-base62-sha1="44hyy3QxmfInmp7jOxADZ0uYDbg" width="689" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c84a4d172539a588f6fda44d16171169a29ce16_2_689x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c84a4d172539a588f6fda44d16171169a29ce16_2_1033x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c84a4d172539a588f6fda44d16171169a29ce16_2_1378x710.jpeg 2x" data-dominant-color="838091"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sequence_browser_slicer3D_screebshot</span><span class="informations">2388×1230 468 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Red viewer: An axial reformatted CT with an overlayed segmentation.<br>
Yellow viewer: The same reformatted CT without the segmentation.</p>
<p>During the recording all views (Red, Yellow, 3D) are linked and synchronized. But during the playback the Red and Yellow views seem to be out of sync with a shift of one slice in the Yellow viewer as you can see in the next screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/234c4b18bfbaaee64b75d8e05665173744dbc4b1.jpeg" data-download-href="/uploads/short-url/52gauqE2pfN1Q99O8Fz0K0v8RI5.jpeg?dl=1" title="sequence_browser_slicer3D_screebshot_shifted" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/234c4b18bfbaaee64b75d8e05665173744dbc4b1_2_690x348.jpeg" alt="sequence_browser_slicer3D_screebshot_shifted" data-base62-sha1="52gauqE2pfN1Q99O8Fz0K0v8RI5" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/234c4b18bfbaaee64b75d8e05665173744dbc4b1_2_690x348.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/234c4b18bfbaaee64b75d8e05665173744dbc4b1_2_1035x522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/234c4b18bfbaaee64b75d8e05665173744dbc4b1_2_1380x696.jpeg 2x" data-dominant-color="7F7C8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sequence_browser_slicer3D_screebshot_shifted</span><span class="informations">2467×1247 467 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This shifting is more clearly manifested in the following video:<br>
<a href="https://hcpanywhere.hus.fi/u/xQCbyWIAm9_XAJvI/3D%20Slicer%20sequence%20browser%20module%20time%20shift_forum1.mp4?l" rel="noopener nofollow ugc">screen_recording.mp4</a></p>
<p>At 00:45 recording with sequence browser<br>
At 01:20 the playback where the shifting is observed.</p>
<p>Do you know why such shifting takes place and how it could be avoided?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-02-05 18:59 UTC)

<p>Slice link only synchronizes slice views when the interaction is finished, so recording may capture transient events. Enable hot-link by long-clicking on the “Link/unlink the slice controls” button to force strong synchronization of views.</p>

---
