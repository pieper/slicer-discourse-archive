# Volume Rendering not working

**Topic ID**: 4018
**Date**: 2018-09-07
**URL**: https://discourse.slicer.org/t/volume-rendering-not-working/4018

---

## Post #1 by @cwietholt (2018-09-07 14:26 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1<br>
Expected behavior: I am following the <a href="https://www.dropbox.com/s/9jcjpl33qfh5pi6/3DVisualizationDICOM_Slicer4.8_SoniaPujol.pdf?dl=0" rel="nofollow noopener">CT Thorax Abdomen tutorial</a> to have a first look at volume rendering. The expected behavior is described in the tutorial.</p>
<p>Actual behavior: When I click on the eye-icon in the Volume Rendering module, all I see is that the bounding box changes color to white, and a coordinate system appears. There is no rendering of the data. I tried using CPU or GPU rendering, nothing changed. I also made sure in the NVIDIA driver settings that Slicer is using the GPU and not the integrated chip. I am using a Dell Precision mobile workstation with a Quadro M1200 GPU.</p>
<p>Any thoughts?</p>
<p>Christian</p>

---

## Post #2 by @cpinter (2018-09-07 14:30 UTC)

<p>The default transfer functions might not show your data. Try many presets and see if any of them displays your data.<br>
What is the volume’s scalar range? You can check it in the Volumes module.</p>

---

## Post #3 by @pieper (2018-09-07 14:40 UTC)

<p>Also try the current nightly build, which has a very different volume rendering back end and probably works differently.</p>

---

## Post #4 by @cwietholt (2018-09-07 19:34 UTC)

<p>Thanks for the quick replies, it was as usual a user error. I clicked on the wrong eye icon. Sorry, I am new to 3D Slicer.</p>

---

## Post #5 by @cpinter (2018-09-07 19:45 UTC)

<p>If you have any suggestions about how to make it more straightforward for new users we’d be glad to hear it.</p>

---

## Post #6 by @cwietholt (2018-09-07 21:02 UTC)

<p>Sure!</p>
<p>One pitfall is that the eye icon is very small and easily looked over. It kind of blends in with the down arrows that are in the same column if there are any sub-menus. I just didn’t even look there for the icon. Even when it was pointed at in the tutorial I linked, it didn’t occur to me that is where the eye icon would be. In addition, the eye icon for display ROI is in a different column, but that one has a label.</p>
<p>Also, when I select the Volume Rendering module, and it auto-selects a volume to be displayed, I would expect that it displays automatically, as soon as I select the module. Of course here it is important to have a good preset transfer function selected. You can maybe use a simple ramp that uses the histogram to set min and max values, e.g. 10% - 90% of the histogram.</p>
<p>Just some ideas.</p>

---

## Post #7 by @pieper (2018-09-07 21:40 UTC)

<p>By the way <a class="mention" href="/u/cpinter">@cpinter</a>, I love the ability to do the multiple volume rendering, but now I find it hard to toggle between two volumes using the Volume Rendering module (you need to select one, turn it off, then select the other and turn it on).  I was thinking that perhaps now the Data (Subject Hierarchy) tab would be able to control the volume visibility.</p>
<p>And with multiple visible volumes it’s easy to get confused about which volume’s rendering properties are selected for editing so you can mess up your settings by accident.</p>
<p>If you have more cycles to work on that module GUI I have more ideas <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=6" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #8 by @muratmaga (2018-09-07 22:52 UTC)

<p>On that note, when I switch to multi-volume rendering from GPU raycasting, for my data it goes from being like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78b864fae9188f2deef61522ca01f5f1eabb9157.jpeg" data-download-href="/uploads/short-url/hdWmiSbyo0iFRq2RII3RKLIGthR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78b864fae9188f2deef61522ca01f5f1eabb9157_2_469x500.jpeg" alt="image" data-base62-sha1="hdWmiSbyo0iFRq2RII3RKLIGthR" width="469" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78b864fae9188f2deef61522ca01f5f1eabb9157_2_469x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78b864fae9188f2deef61522ca01f5f1eabb9157.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78b864fae9188f2deef61522ca01f5f1eabb9157.jpeg 2x" data-dominant-color="7C7D9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">586×624 89.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
to this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/073d5f858b9c73d693fe46f0c4ac5fdf4568f290.jpeg" data-download-href="/uploads/short-url/122PGrcXv7Zw0W3tPRegHZeKbQY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/073d5f858b9c73d693fe46f0c4ac5fdf4568f290_2_449x500.jpeg" alt="image" data-base62-sha1="122PGrcXv7Zw0W3tPRegHZeKbQY" width="449" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/073d5f858b9c73d693fe46f0c4ac5fdf4568f290_2_449x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/073d5f858b9c73d693fe46f0c4ac5fdf4568f290.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/073d5f858b9c73d693fe46f0c4ac5fdf4568f290.jpeg 2x" data-dominant-color="999BC4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">618×687 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
with todays nightly. Whatever I try with the ramp doesn’t fix this.</p>

---

## Post #9 by @lassoan (2018-09-08 00:15 UTC)

<p>There is no shading implemented yet in multi-volume rendering so you won’t be able to get an image like the one above. By looking at the difference between the renderings, there also seems to be a difference in sampling distance. We can get back to this after shading is implemented.</p>
<p>If proper multi-volume rendering (with shading) is important for you then it could be useful to let Kitware folks know. There is a better chance that it will be implemented sooner if there is a confirmed need from the community. Of course it is even better if they get some small funding for the remaining tasks (which should not be that much).</p>

---

## Post #10 by @lassoan (2018-09-09 22:57 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="4018">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I find it hard to toggle between two volumes using the Volume Rendering module</p>
</blockquote>
</aside>
<p>I guess we did not want to promote multi-volume rendering very much until shading is implemented, to avoid disappointing users. Once multi-volume rendering can produce images comparable to single-volume rendering, we can add a tree view with eye icons in volume renderer module (and also make volume rendering easier to access from subject hierarchy tree).</p>
<p>It would be useful to implement an intelligent default preset selection (we could guess from voxel unit, scalar range, etc.) because then clicking the eye icon would show nice rendering without the need to select a preset and tune intensity offset.</p>

---

## Post #11 by @rkikinis (2018-09-10 05:40 UTC)

<p>In the current VR, we use w/l settings and the LUT associated with the volume to initialize the transfer function. The assumption was that people would look at the slices first and adjust their appearance before going into the volume rendering module.</p>

---

## Post #12 by @rkikinis (2018-09-10 06:32 UTC)

<p>In my experience that heuristic works in general but the lower<br>
threshold ends up showing too much of the background noise<br>
Ron</p>

---

## Post #13 by @pieper (2018-09-10 12:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,  the problem I’m referring to is that the changed behavior of visibility management happens for all rendering modes, not just the multi-volume rendering.  Previously (e.g. 4.8.1), the volume selector acted like a radiobutton, where selecting a volume made it visible and the others invisible, which makes sense for renderers that don’t support multiple volume rendering.  Now, visibility is sticky with the volume, which makes sense for the multi-volume mode but not for the other modes.</p>

---

## Post #14 by @cpinter (2018-09-10 15:07 UTC)

<p>There are definitely things to improve in volume rendering. Multi-volume rendering is still experimental (does not render correctly with the regular mappers, and there is no shading with the multi-volume mapper), and cannot be considered complete. I could add an altered subject hierarchy tree view that shows/hides volume rendering with the eye icon, but as Andras says it may be a bit premature. Maybe I coud implement the old way of functioning until then and add an option for that in Application Settings? Also you can show/hide volume rendering in the Data module (SH tree) by right-clicking the eye icon and toggle volume rendering.</p>

---

## Post #15 by @pieper (2018-09-10 21:37 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="14" data-topic="4018">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Maybe I coud implement the old way of functioning</p>
</blockquote>
</aside>
<p>I think this would be the most logical for the near future - it makes no sense currently to have multiple volumes marked as visible when they cannot be composited.</p>
<p>Logic could be: when a new volume is selected in the combo box all other volumes are made invisible unless the multiple-volume renderer is selected.</p>

---

## Post #16 by @lassoan (2018-09-11 18:47 UTC)

<p>I think the current implementation is clear to use (whenever you click the eye icon, a volume is shown) and implement (old behavior was very buggy, render volume often switched randomly when changing parent transform or loading a scene), and allows rendering of multiple volumes (which can work quite well even with simple volume renderer when the volumes are transparent). I think these advantages overweigh the inconvenience of a single extra click and potential user confusion about compositing errors.</p>

---

## Post #17 by @pieper (2018-09-11 19:20 UTC)

<p>The old behavior had some problems, but my original issue with the current behavior still stands: if your goal is to compare to volume renderings it’s multiple confusing clicks (turn off current, select new, turn it on).  And if the currently selected volume isn’t the visible one it’s prone to changing the lookup table and not seeing any update (which is confusing).</p>

---

## Post #18 by @cpinter (2018-09-11 19:23 UTC)

<p>About the accidental lookup table manipulation: we could disable the rest of the panel when the selected volume is not shown.</p>

---

## Post #19 by @lassoan (2018-09-11 21:30 UTC)

<p>The behavior is the same for markups, segmentations, volumes, transforms, plots, etc.: you select a node and then adjust visibility. Models and annotations have a tree instead of a node combobox, which has a direct visibility shortcut as well, but otherwise it works the same way.</p>
<p>Why would we want to invent something new for volume rendering?</p>
<p>Would it help if we replaced the node selector combobox by a tree (similar to models)?</p>
<p>Would it help if we added a special “single” mode to the eye icon in volume rendering module (can be enabled with long click)? It would hide all other volumes when eye icon is clicked. This mode would be a purely GUI-level option - rendering of multiple volumes could be still possible by using Data module, by loading a scene, etc. (or by disabling “single” mode).</p>

---

## Post #20 by @pieper (2018-09-12 12:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="19" data-topic="4018">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Why would we want to invent something new for volume rendering?</p>
</blockquote>
</aside>
<p>The difference, at least now, is that unless the multi-volume renderer is selected, the volumes do not composite correctly so it doesn’t make sense to have them visible at the same time.  I agree that once multivolume rendering is working well it could become the default and then things should be exactly parallel to the model/segmentations/etc interfaces.</p>
<p>As long as the best renderers available only really support single-volume rendering (as in the current CPU and GPU options) then we should have an easy way to use them that is consistent with that limitation.</p>

---

## Post #21 by @Tommaso_Di_Noto (2019-11-28 10:29 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a>!<br>
Are there any updates on the multi-volume rendering shading? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thanks in advance</p>

---

## Post #22 by @lassoan (2019-11-28 14:16 UTC)

<p>He managed to fix some of the issues but not all of them (some stability issues remain unresolved).</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> it would be great if you could post the link to your WIP branch, just in case someone at Kitware or elsewhere would find time to continue.</p>

---

## Post #23 by @cpinter (2019-11-29 16:42 UTC)

<p>This is my branch:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="32" height="32">
      <a href="https://github.com/cpinter/VTK/tree/multi-volume-shading" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/1325980?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/cpinter/VTK/tree/multi-volume-shading" target="_blank">cpinter/VTK</a></h3>

<p>WARNING: This is NOT the official upstream VTK git repository - cpinter/VTK</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Shading with multi-volume rendering works with this branch, however, not every time! Unfortunately about 2/3 of the time there is no shading at all (looks black, as if lighting is not considered whatsoever), but when it shows up, then it looks as it’s supposed to. I haven’t been able to figure out the reason for this undeterministic behavior. Any suggestions are welcome, and I’m happy to answer any questions.</p>

---
