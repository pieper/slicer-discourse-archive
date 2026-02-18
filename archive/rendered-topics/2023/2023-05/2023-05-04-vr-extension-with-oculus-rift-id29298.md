# VR extension with oculus rift

**Topic ID**: 29298
**Date**: 2023-05-04
**URL**: https://discourse.slicer.org/t/vr-extension-with-oculus-rift/29298

---

## Post #1 by @Gonzalo_Rojas_Costa (2023-05-04 17:22 UTC)

<p>Hi:</p>
<p>I configure my oculus rift in my notebook. The games runs perfectly. Then, I install 3D slicer (version 5.2.2. in Windows) with VR extension, but when I select the VR glasses icon in 3D Slicer, in some seconds appears a red cross over it?. Why?</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @rbumm (2023-05-04 18:23 UTC)

<p>Unfortunately, the VR extension of 3D Slicer is still broken. All my recent tests with the Oculus Quest2  failed with 5.x Slicer versions. The last working session I can remember was with 4.11.</p>

---

## Post #3 by @Gonzalo_Rojas_Costa (2023-05-04 19:59 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="2" data-topic="29298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Unfortunately, the VR extension of 3D Slicer is still broken.</p>
</blockquote>
</aside>
<p>Do you know if exist any idea to upgrade it for 3D Slicer 5.x ?</p>

---

## Post #4 by @cpinter (2023-05-11 10:33 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Can you please share detaills about how it is broken? It works for me in 5.3 except the two-handed gesture.</p>
<p>The one issue is you have to copy the manifest json files manually next to the Slicer executable. <a class="mention" href="/u/jcfr">@jcfr</a> I’m not sure, do we have some guidelines about it or any way to make this easy for the user?</p>

---

## Post #5 by @rbumm (2023-05-11 12:11 UTC)

<p>That’s correct! The Oculus Quest 2’s right-handed joystick allows you to manipulate objects in 3D space. By using the joystick, you can move the object around, and you can adjust the direction of movement by tilting the right controller.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dc33c5b880a6e867c9e7f8f6e443355eb17b11d.jpeg" data-download-href="/uploads/short-url/1XKuREe6ZVNbNIWTVaR6O2Icm8R.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dc33c5b880a6e867c9e7f8f6e443355eb17b11d.jpeg" alt="image" data-base62-sha1="1XKuREe6ZVNbNIWTVaR6O2Icm8R" width="674" height="500" data-dominant-color="807A77"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">688×510 73.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To ensure proper functionality, one must make sure that the manifest JSON files are located in the same directory as the Slicer.exe file.</p>
<p>In version 4.11, you could grab an object by simultaneously pressing both grab triggers, and then rotate and tilt the object as desired. However, this feature is currently broken in version 5. When attempting this action, the object disappears from the 3D space.</p>

---

## Post #6 by @cpinter (2023-05-11 12:19 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="29298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>In version 4.11, you could grab an object by simultaneously pressing both grab triggers, and then rotate and tilt the object as desired.</p>
</blockquote>
</aside>
<p>What you could grab in 4.11 was the “world” and not the object, this is an important difference from what you say. So the object stayed the same in RAS, but the camera and the scaling of the world changed (just try it with multiple objects in the scene and you’ll see).<br>
That said, I miss this feature very much, because it is super convenient to navigate that way. I don’t have funding for this, and unfortunately also don’t have free time these months, so the same as you, I can only wait. However, I’m trying to be present in the efforts that do have funding (although it is targeted only tangentially because it’s for AR), and whenever I see that I have a day to work on this I’ll coordinate with them and get this done finally.</p>

---

## Post #7 by @rbumm (2023-05-11 12:29 UTC)

<p>Ok, I understand. Do you know where the camera position adjustment is made in the Slicer VR source code and which VTK function would be responsible for moving the camera?</p>

---

## Post #8 by @cpinter (2023-05-11 12:51 UTC)

<p>You can find the details of our findings on this page, and at the links pointed from it: <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW38_2023_GranCanaria/Projects/SlicerVRInteractions/README.md" class="inline-onebox">ProjectWeek/README.md at master · NA-MIC/ProjectWeek · GitHub</a></p>
<p>Basically where this two-handed gesture is managed is the <code>RecognizeComplexGesture</code> function (mentioned in some of the pull requests referenced). The setting of the camera transform as I remember was in the VR interactor style class. If you want further details please don’t hesitate to ask.</p>

---

## Post #9 by @rbumm (2023-05-11 14:08 UTC)

<p>From a clinical point of view it would be absolutely great to have a ROI based crop tool for volume renderings and segmentation in VR.</p>

---

## Post #10 by @Gonzalo_Rojas_Costa (2023-05-12 04:45 UTC)

<p>You used 5.3 version with which glasses? Oculus Rift? Because we are trying to configure our Oculus Rift with 5.3 version, and it doesn’t works.</p>

---

## Post #11 by @cpinter (2023-05-12 08:41 UTC)

<p>I don’t have an Oculus Rift anymore, I tried HTC Vive Pro and HP Reverb 2. I still don’t know what it means for you exactly that “it doesn’t work”. Some detailed information, hopefully screenshots would be useful.</p>

---

## Post #12 by @jcfr (2023-05-13 16:36 UTC)

<blockquote>
<p>one must make sure that the manifest JSON files are located in the same directory as the Slicer.exe file.</p>
</blockquote>
<p>The associated issue <sup class="footnote-ref"><a href="#footnote-94826-1" id="footnote-ref-94826-1">[1]</a></sup> has been fixed<sup class="footnote-ref"><a href="#footnote-94826-2" id="footnote-ref-94826-2">[2]</a></sup> in the <code>SlicerVirtualReality</code> project.</p>
<p>To support configuring the the folder in which the action manifest files are located, the relevant fix from upstream VTK were integrated in our Slicer/VTK fork<sup class="footnote-ref"><a href="#footnote-94826-3" id="footnote-ref-94826-3">[3]</a></sup>.</p>
<p><strong>Question:</strong> Could someone try to download the latest preview build of Slicer and try the SlicerVirtualReality extension ?</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-94826-1" class="footnote-item"><p><a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/112">https://github.com/KitwareMedical/SlicerVirtualReality/issues/112</a> <a href="#footnote-ref-94826-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-94826-2" class="footnote-item"><p><a href="https://github.com/KitwareMedical/SlicerVirtualReality/pull/114">https://github.com/KitwareMedical/SlicerVirtualReality/pull/114</a> <a href="#footnote-ref-94826-2" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-94826-3" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/pull/6967">https://github.com/Slicer/Slicer/pull/6967</a> <a href="#footnote-ref-94826-3" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #13 by @rbumm (2023-05-13 18:50 UTC)

<p>Downloaded the latest preview build of Slicer and installed the SlicerVirtualReality extension.<br>
With or without the JSON files the segmentation is shown in the headset, but none of the keys for manipulation  work (joystick, grab etc) But grabbing with both controllers does not let the object dissapear from the scene.<br>
This was tested with the Quest 2 (it shows a Rift connection) but on an older PC with a GTX 970, still in quite good shape, I will try 4.11 next just to make sure the system generally works.</p>

---

## Post #14 by @rbumm (2023-05-13 19:10 UTC)

<p>4.11 works well on that old system and has all interaction keys active (joystick and both grab triggers).Sidenote: Exiting VR (SteamVR) crashes Slicer.</p>

---

## Post #15 by @cpinter (2023-05-15 14:17 UTC)

<p>Same here with the latest preview. Without copying the jsons I get this, and no interactions work. I didn’t try copying the file as I understand the goal was to check if it works without manual copying.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33d6c05fc6dc05cb071e396c3de607c6384e1623.jpeg" data-download-href="/uploads/short-url/7oAs8HBWZ82ApDSQPGtR0LmUB9x.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33d6c05fc6dc05cb071e396c3de607c6384e1623.jpeg" alt="image" data-base62-sha1="7oAs8HBWZ82ApDSQPGtR0LmUB9x" width="690" height="416" data-dominant-color="20293B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">718×433 46.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for working on this <a class="mention" href="/u/jcfr">@jcfr</a> !</p>

---

## Post #16 by @rbumm (2023-05-16 23:41 UTC)

<p>Interestingly, in my case, I did not get this missing action manifest message in SteamVR this time without the JSONS. On a second try with the JSONS, at least one of the buttons seemed to work (the “B” left controller menu button).</p>

---
