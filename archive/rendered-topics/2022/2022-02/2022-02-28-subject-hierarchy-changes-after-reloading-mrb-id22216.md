# Subject hierarchy changes after reloading .mrb

**Topic ID**: 22216
**Date**: 2022-02-28
**URL**: https://discourse.slicer.org/t/subject-hierarchy-changes-after-reloading-mrb/22216

---

## Post #1 by @koeglfryderyk (2022-02-28 14:51 UTC)

<p>I have the same issue as described in  <a href="/t/save-subject-hierarchy/8488">Save subject hierarchy</a>, only with volumes and not models.</p>
<ol>
<li>Load some data into Slicer</li>
<li>Create a folder hierarchy</li>
<li>Place the loaded volumes into the folders</li>
<li>Save everything as an .mrb</li>
<li>After reloading the .mrb the hierarchy has changed</li>
</ol>
<p>This is the hierarchy that I am saving:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fd2fc58dd77d977844158262ac1bee81227f9ae.jpeg" data-download-href="/uploads/short-url/bo9KOfRsI5VXZfHJXTE3oKt2jwy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd2fc58dd77d977844158262ac1bee81227f9ae_2_345x113.jpeg" alt="image" data-base62-sha1="bo9KOfRsI5VXZfHJXTE3oKt2jwy" width="345" height="113" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd2fc58dd77d977844158262ac1bee81227f9ae_2_345x113.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd2fc58dd77d977844158262ac1bee81227f9ae_2_517x169.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd2fc58dd77d977844158262ac1bee81227f9ae_2_690x226.jpeg 2x" data-dominant-color="F0F1F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">914×302 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the hierarchy that I get after reloading the .mrb:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fe0c32355d23d434a454cb3d2cf7644e15791b2.jpeg" data-download-href="/uploads/short-url/975D9HeTT7ciexJsm1T9l22Jtcu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fe0c32355d23d434a454cb3d2cf7644e15791b2_2_345x111.jpeg" alt="image" data-base62-sha1="975D9HeTT7ciexJsm1T9l22Jtcu" width="345" height="111" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fe0c32355d23d434a454cb3d2cf7644e15791b2_2_345x111.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fe0c32355d23d434a454cb3d2cf7644e15791b2_2_517x166.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fe0c32355d23d434a454cb3d2cf7644e15791b2_2_690x222.jpeg 2x" data-dominant-color="F0F1F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">912×296 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
(the three US volumes change location)</p>
<p>MacOS. The same issue occurs with the stable release 4.11.20210226 and with several preview releases, including the latest 4.13.0, revision 30657, built 2022-02-26</p>

---

## Post #2 by @cpinter (2022-02-28 17:12 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="22216">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>including the latest 4.13.0, revision 30657, built 2022-02-26</p>
</blockquote>
</aside>
<p>Do you mean that you tried with the latest preview not only to load the scene but also to both save and load?</p>

---

## Post #3 by @koeglfryderyk (2022-02-28 22:03 UTC)

<p>Yes, I tried saving and loading with the stable and preview versions.</p>
<p>I think I narrowed the problem a bit down:<br>
Even though in the tree it looks like the parents are correctly assigned, they are not (this screenshot was of the state that was saved to an .mrb):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbe817021a2526b1132aa5416f0ab06fcb004d59.jpeg" data-download-href="/uploads/short-url/zWt5UwbDv6atDzDK5V9ZfUIaEJz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbe817021a2526b1132aa5416f0ab06fcb004d59_2_312x250.jpeg" alt="image" data-base62-sha1="zWt5UwbDv6atDzDK5V9ZfUIaEJz" width="312" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbe817021a2526b1132aa5416f0ab06fcb004d59_2_312x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbe817021a2526b1132aa5416f0ab06fcb004d59_2_468x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbe817021a2526b1132aa5416f0ab06fcb004d59_2_624x500.jpeg 2x" data-dominant-color="EDEDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">934×748 98.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>it says that the parent of the selected node is the scene, even though in the tree it’s parent is Pre-op imaging</li>
</ul>
<p>It seems that dragging nodes does not update the subject hierarchy properly - or am I doing something wrong?</p>

---

## Post #4 by @cpinter (2022-03-01 10:14 UTC)

<p>Thanks for the further investigation! So it seems that the problem is not on the save/load (i.e. MRML) side but the SH tree widget / model side.</p>
<p>How do you put these volumes under the folder? I know it’s a strange question, but maybe you do something extra we don’t. Also, not sure if you have access to another operating system (Windows or Linux) but if you could try the same thing it would help.</p>

---

## Post #5 by @koeglfryderyk (2022-03-02 15:13 UTC)

<p>I don’t know why, but I cannot reproduce it anymore. If I manage to do it again I’ll describe what I’m doing exactly</p>

---

## Post #6 by @cpinter (2022-03-03 08:58 UTC)

<p>Thanks for the update!</p>

---
