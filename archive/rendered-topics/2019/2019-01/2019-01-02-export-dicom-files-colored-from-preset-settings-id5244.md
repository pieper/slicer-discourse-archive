# Export dicom files colored from preset settings

**Topic ID**: 5244
**Date**: 2019-01-02
**URL**: https://discourse.slicer.org/t/export-dicom-files-colored-from-preset-settings/5244

---

## Post #1 by @Canube (2019-01-02 02:33 UTC)

<p>Dear Slicer team,</p>
<p>Best wishes for 2019!</p>
<p>The preset that Slicer offers automatically adds colors to the loaded dicom files. These colored presets, I would like to export and visualize in Virtual Reality. I have a tool for that which stacks the dicom files and visualizes the images in VR.</p>
<p>Currently, the dicom files are still black, grey and white when I export them with a selected preset. Is it possible to get an export of the dicom files colored?</p>
<p>I also tried to color the scans through the editor mode and then export the dicom files, but there I unfortunately also get a colored export.</p>
<p>Can someone please help me get colored dicom output?</p>
<p>On another note, if anybody has any tips or tricks they want to share concerning virtual reality, please let me know!</p>
<p>Look forward to receiving a response.</p>
<p>Kind regards,<br>
Chris</p>

---

## Post #2 by @lassoan (2019-01-02 03:13 UTC)

<p>You can show images (even 4D volumes, replayed in real-time) using volume rendering and you can interact with the scene, move objects, etc. directly in Slicer, using SlicerVirtualReality extension. See more information here: <a href="https://github.com/KitwareMedical/SlicerVirtualReality" rel="nofollow noopener">https://github.com/KitwareMedical/SlicerVirtualReality</a></p>
<div class="lazyYT" data-youtube-id="F_UBoE4FaoY" data-youtube-title="Pedicle screw insertion in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>More features are added continuously, but if you need any specific functionality then let us know. Also, any contribution would be very welcome.</p>
<p>If you want to just show segmented models in virtual reality (you can segment all that you need and the extra effort required for segmentation is acceptable) then you could use any software (Unity, Unreal, etc) or implement native applications from scratch. You can even add volume rendering. However, if you are considering implementing virtual reality applications for medical imaging, then Slicer is by far the most powerful and versatile platform for that.</p>

---

## Post #3 by @Canube (2019-01-02 15:59 UTC)

<p>Dear Andras,</p>
<p>Many thanks for your quick response. Great to hear that Slicer offers these extensive VR applications. Will definitely dive into those options.</p>
<p>If I would like to have coloured exports based on the presets, is that possible? It would really be of added value to me and I am willing to financially contribute.</p>
<p>Thanks in advance,</p>
<p>Chris</p>

---

## Post #4 by @lassoan (2019-01-02 16:20 UTC)

<aside class="quote no-group" data-username="Canube" data-post="3" data-topic="5244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/57b2e6/48.png" class="avatar"> Canube:</div>
<blockquote>
<p>If I would like to have coloured exports based on the presets, is that possible?</p>
</blockquote>
</aside>
<p>This is discussed extensively here: <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524/14" class="inline-onebox">Save volume rendering as STL file - #14 by maxabernathy</a>. In short, volume is saved as is (with single-component scalar values) and you color it using transfer functions (scalar opacity transfer function, scalar color transfer function, and sometimes also gradient opacity transfer function). Transfer functions are saved in a .vp file when you save the scene (simple text file that list number of points in the transfer functions, followed by the point coordinates). You can find information about these transfer functions and how they are used for volume rendering in <a href="https://lorensen.github.io/VTKExamples/site/VTKBook/07Chapter7/#73-volume-rendering">VTK textbook</a>.</p>

---

## Post #5 by @Amir_y (2019-01-03 06:29 UTC)

<p>Hello, and happy 2019!!<br>
I am also interested in viewing volume rendering in mix reality HMD, specifically I am trying to get the Magic Leap AR Headset connected to Slicer. Any general advice about the path I should take?</p>
<p>many thanks<br>
Amir</p>

---

## Post #6 by @lassoan (2019-01-03 15:31 UTC)

<p><em>Short answer:</em></p>
<ul>
<li>If possible, use virtual reality instead of augmented reality: it is already well supported within Slicer and much more mature in general.</li>
<li>Augmented reality is not ready for real-world use yet, but you can implement quick prototypes using Unity for early feasibility tests. Slicer can be used to create surface models that these prototypes can use and. We plan to have OpenIGTLink-based real-time transfer of meshes from Slicer to Unity-based applications (not ready yet, contributions are welcome).</li>
</ul>
<p><em>Long answer:</em></p>
<p><strong>First question is why would you connect a HoloLens (or a Magic Leap, which can do essentially the same) to Slicer. What application for augmented reality do you have in mind?</strong></p>
<p>We’ve been evaluating HoloLens for various clinical applications for 2 years (burr hole location planning - currently tested in a study in the OR on patient cases, surgical skill training, anatomical training for needle insertion, etc.) and we find that while the technology is very promising, current headsets have still very significant limitations. The most promising use of augmented reality would be in situ visualization within arm-length distance, but unfortunately none of the current headsets (HoloLens, Magic Leap, Meta, etc.) can do that, due to focal plane placed at around 100-300cm in instead of 40-70cm: you cannot see virtual objects and real objects at the same time (you lose sense of depth, so you cannot align shapes in 6dof). There are secondary issues, such as instability of virtual objects (you often get errors of 3-5mm error when you move around an object), size and weight of headset, and lack of computational power on untethered devices.</p>
<p>HTC Vive Pro has video pass-through capabilities, which allows using all the virtual reality infrastructure for augmented reality (SlicerVirtualReality could be used for this). However, image quality, lag, fixed focal distance, dynamic range under strong focused OR lighting might be problematic on video pass-through augmented reality.</p>
<p><strong>Can you use virtual reality instead?</strong></p>
<p>If you don’t need in-situ visualization at arm-length distance then you may just as well use virtual reality. It does not have any of the limitations listed above, they are ready-to-use for several end-user applications, inexpensive, and a single software interface (OpenVR) can be used for all major headsets (HTC Vive, Windows MR, Oculus Rift).</p>
<p><strong>What visualization would you need?</strong></p>
<p>If you only need rendering of surface meshes then you can use simple Unity applications to render them and implement simple interactions. Since headsets are not yet ready for real-world use anyway, these quick throw-away prototypes are appropriate. We’ve been working on implementing OpenIGTLink interface for sending over segmented models from Slicer to Unity-based applications (so that you don’t need to build and deploy a new application for each patient case), but it’s not ready yet.</p>
<p>Volume rendering is feasible, too, you can buy volume renderer from the Unity asset store for a few ten $. Computational capabilities of untethered headsets are limited and these volume renderers are not as sophisticated as VTK’s volume renderer, but might be OK for some applications.</p>

---

## Post #7 by @Amir_y (2019-01-03 17:38 UTC)

<p>Many thanks for the informative answer.<br>
We are using Magic Leap to build a prototype for Needle Insertion .</p>
<p>We want real time Ultra Sound 3D Volume projected via the magic leap on the insertion area.</p>
<p>Are you sure we will have focal distance limit with the magic leap?</p>
<p>thanks!</p>

---

## Post #8 by @lassoan (2019-01-04 02:44 UTC)

<aside class="quote no-group" data-username="Amir_y" data-post="7" data-topic="5244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ecae2f/48.png" class="avatar"> Amir_y:</div>
<blockquote>
<p>Are you sure we will have focal distance limit with the magic leap?</p>
</blockquote>
</aside>
<p>Magic Leap has a focal plane at 1m and 3m, so you won’t be able to align a needle with a displayed trajectory in 3D while holding the needle in your hand at 50cm distance. Of course, try it and see it for yourself. You don’t need to develop any custom software, just show a static model of a tube and try to align a needle with it.</p>
<p>What we do now as a workaround is that we let the user easily show/hide the virtual needle trajectory by pressing a button. The user looks at the hologram (focusing at a distant plane) then quickly hides the trajectory and looks at the physical object (focusing on the object). We’ve found that overall these virtual guides help, but we need a headset with focal plane at 50cm if we want these virtual guides to work at least as well as laser guides (that you can see continuously, while looking at the patient and needle).</p>
<p>Hopefully the HoloLens2 or some other headsets in the near future will come with a much closer focal plane. There may be additional problems to be solved for high-quality, stable hologram visualization at arm-length distance, since tracking errors may be more visible, view may be more occluded, etc., so maybe this won’t be available very soon.</p>

---

## Post #9 by @Canube (2019-01-27 11:19 UTC)

<p>Dear Andras,</p>
<p>Many thanks for your response.</p>
<p>The tutorial for Segmentation for 3D printing requires to make specific segmentations before you can download them. I would like to see if I can download the preset (in full colors) like below to see if I can view them in Unity.</p>
<p>If I select the preset and then export, I logically export an empty .stl file. Can you please tell me how I can export the preset?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8ff08cb8b36f841fe7951716c3cbf55857b8be5e.png" alt="image" data-base62-sha1="kxlEwuOyJlmieh5DCP1oitRQPsW" width="460" height="350"></p>
<p>How can I make a financial contribution to your team?</p>
<p>Kind regards,<br>
Chris</p>

---

## Post #10 by @jcfr (2019-01-28 18:47 UTC)

<aside class="quote no-group" data-username="Canube" data-post="9" data-topic="5244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/57b2e6/48.png" class="avatar"> Canube:</div>
<blockquote>
<p>Can you please tell me how I can export the preset?</p>
</blockquote>
</aside>
<p>The presets are described in the following files. See <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/Resources/presets.xml" class="inline-onebox">Slicer/Modules/Loadable/VolumeRendering/Resources/presets.xml at main · Slicer/Slicer · GitHub</a></p>

---

## Post #11 by @jcfr (2019-01-28 18:54 UTC)

<aside class="quote no-group" data-username="Canube" data-post="9" data-topic="5244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/57b2e6/48.png" class="avatar"> Canube:</div>
<blockquote>
<p>How can I make a financial contribution to your team?</p>
</blockquote>
</aside>
<p>If you are looking to work with a team to implement a specific functionality, you could have a look at the list of commercial partners. See <a href="https://www.slicer.org/wiki/CommercialUse#Commercial_Partners" class="inline-onebox">CommercialUse - Slicer Wiki</a></p>
<p>Or are you looking to make a “donation” to help us maintain the infrastructure and support the project overall ?</p>

---
