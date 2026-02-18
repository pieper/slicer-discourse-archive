# How to convert raw rotational CT scan data into 3d data

**Topic ID**: 42865
**Date**: 2025-05-10
**URL**: https://discourse.slicer.org/t/how-to-convert-raw-rotational-ct-scan-data-into-3d-data/42865

---

## Post #1 by @Samino (2025-05-10 11:44 UTC)

<p>Hi there,<br>
Question from a newbie, coming from marine biology.</p>
<p>I have raw image data in tiff format, of the subject (mollusc) being rotated in the micro CT scanner.<br>
How do I convert this into 3D dicom data that can be used in 3D slicer?</p>
<p>Any pointers would be very much appreciated.</p>
<p>Sam</p>

---

## Post #2 by @pieper (2025-05-10 13:01 UTC)

<p>Usually it’s best to use the software that came with the scanner that acquired the data, since it may be optimized for the hardware.  If that’s not possible, you can try <a href="https://www.openrtk.org/">https://www.openrtk.org/</a>.  You’ll need to know parameters about the scan to get a dimensionally accurate 3D reconstruction.</p>

---

## Post #3 by @muratmaga (2025-05-11 18:05 UTC)

<p>It is not clear what you mean by the “raw image”. I think you will benefit from reading this section, and getting familiar about microCT imaging and downstream processes.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/microCT#what-is-microct-imaging">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/microCT#what-is-microct-imaging" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/microCT#what-is-microct-imaging" target="_blank" rel="noopener nofollow ugc">Tutorials/microCT at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Samino (2025-05-13 08:20 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> thank you this is a very useful overview.<br>
The images I have are the original shadow images of the subject as it is rotated in the scanner.<br>
I was hoping to reconstruct these to make slices.</p>

---

## Post #5 by @Samino (2025-05-13 08:22 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thank you for the information.<br>
So is the reconstruction usually carried out by the CT scanner technicians?</p>

---

## Post #6 by @pieper (2025-05-13 12:21 UTC)

<aside class="quote no-group" data-username="Samino" data-post="5" data-topic="42865">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/samino/48/80166_2.png" class="avatar"> Samino:</div>
<blockquote>
<p>So is the reconstruction usually carried out by the CT scanner technicians?</p>
</blockquote>
</aside>
<p>Yes, this is the typical way.</p>

---

## Post #7 by @Samino (2025-05-14 08:25 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> I’ll see if they can help me.</p>

---
