---
topic_id: 35107
title: "Scissorss Fill Inside Operation Issue"
date: 2024-03-26
url: https://discourse.slicer.org/t/35107
---

# Scissors's Fill Inside operation issue

**Topic ID**: 35107
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/scissorss-fill-inside-operation-issue/35107

---

## Post #1 by @MJamal (2024-03-26 16:36 UTC)

<p>Hello again,</p>
<p>I have applied the scissors’ fill-inside operation to segment 1, but I am encountering the following issues:</p>
<ol>
<li>At minute 0:52, you will notice that the operation is not entirely applied to the part where it is scissored. Some gaps are still visible.</li>
<li>From minute 1:00 to 1:05, why does the output of the operation blink rapidly?</li>
<li>Starting from minute 1:22, the output of the operation almost disappears intermittently.</li>
</ol>
<p>Slicer version: Preview Release 5.7.0</p>
<p>Please find the attached video link:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1r78TqbET2B-7II55E4JrnhPJwtsE8Lcd/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1r78TqbET2B-7II55E4JrnhPJwtsE8Lcd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1r78TqbET2B-7II55E4JrnhPJwtsE8Lcd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1r78TqbET2B-7II55E4JrnhPJwtsE8Lcd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Scissor.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @muratmaga (2024-03-26 16:57 UTC)

<p>Did you check the slices? Your screenshot only shows the 3D rendering. It is possible that slight smoothing differences makes one model appear on top of the other.<br>
In my test (with 5.6.1) the cross sectional slices shows the correct behavior.</p>
<p>BTW, if your goal is to split the segment_1 into two mutually exclusive segments, then you shouldn’t use “allow overlap”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0ff4eae2e30f766653da11ff4306ab0354c40ce.jpeg" data-download-href="/uploads/short-url/rxkFoZeVGdXn8LNY1MFjULY31TM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ff4eae2e30f766653da11ff4306ab0354c40ce_2_690x300.jpeg" alt="image" data-base62-sha1="rxkFoZeVGdXn8LNY1MFjULY31TM" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ff4eae2e30f766653da11ff4306ab0354c40ce_2_690x300.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ff4eae2e30f766653da11ff4306ab0354c40ce_2_1035x450.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ff4eae2e30f766653da11ff4306ab0354c40ce_2_1380x600.jpeg 2x" data-dominant-color="6F7370"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×835 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @MJamal (2024-04-03 03:22 UTC)

<p>Yes, I checked the slices, and the effect was clearly visible on them, just as in your screenshot.</p>
<p>Regarding the smoothing difference, I achieved the desired results after disabling surface smoothing:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5eed53a99001f1b45ccfce98b96382855502f02.jpeg" data-download-href="/uploads/short-url/nFUtKnorz7W7Ht1O2UodqxX20TM.jpeg?dl=1" title="image (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5eed53a99001f1b45ccfce98b96382855502f02_2_345x195.jpeg" alt="image (1)" data-base62-sha1="nFUtKnorz7W7Ht1O2UodqxX20TM" width="345" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5eed53a99001f1b45ccfce98b96382855502f02_2_345x195.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5eed53a99001f1b45ccfce98b96382855502f02_2_517x292.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5eed53a99001f1b45ccfce98b96382855502f02_2_690x390.jpeg 2x" data-dominant-color="9296B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (1)</span><span class="informations">1118×633 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, the rendering issue, particularly surface glitching/blinking, still persists when i rotate the model.</p>

---

## Post #4 by @MJamal (2024-04-03 03:32 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="3" data-topic="35107">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>when i rotate the model.</p>
</blockquote>
</aside>
<p>At some point, the overlapped segment just completely disappears.</p>

---

## Post #5 by @MJamal (2024-04-05 06:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, Could you please confirm this is really a rendering bug?</p>

---

## Post #6 by @pieper (2024-04-05 12:03 UTC)

<p>If you have coincident surfaces then yes, you would expect rendering issues.</p>

---

## Post #7 by @lassoan (2024-04-05 14:33 UTC)

<p>With the cutting you created a sharp edge that the smoothing reduces, which causes the band near the cut. Since the binary labelmap representation has finite resolution, if you want to produce smooth surface output then there will be always gaps or overlaps.</p>
<p>You can choose between flying edges + Windowed sinc smoothing / surface net algorithms, depending on what is better suited for your application:</p>
<p>Flying edges, no smoothing, showing binary labelmap representation in slice view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afcc0e6bfd41db78fa07730862411cfc0afa3dca.jpeg" data-download-href="/uploads/short-url/p5aKfFdTAEODwlxZQv3zWeRpZgK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afcc0e6bfd41db78fa07730862411cfc0afa3dca_2_690x234.jpeg" alt="image" data-base62-sha1="p5aKfFdTAEODwlxZQv3zWeRpZgK" width="690" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afcc0e6bfd41db78fa07730862411cfc0afa3dca_2_690x234.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afcc0e6bfd41db78fa07730862411cfc0afa3dca_2_1035x351.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afcc0e6bfd41db78fa07730862411cfc0afa3dca_2_1380x468.jpeg 2x" data-dominant-color="8B8B76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×652 84.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Flying edges with smoothing, showing closed surface representation in slice view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/535a6e174e0df233a9be6386a664cda170f34449.jpeg" data-download-href="/uploads/short-url/bTnnhvbCZYQutO2o45sTleJI4Ah.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/535a6e174e0df233a9be6386a664cda170f34449_2_690x234.jpeg" alt="image" data-base62-sha1="bTnnhvbCZYQutO2o45sTleJI4Ah" width="690" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/535a6e174e0df233a9be6386a664cda170f34449_2_690x234.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/535a6e174e0df233a9be6386a664cda170f34449_2_1035x351.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/535a6e174e0df233a9be6386a664cda170f34449_2_1380x468.jpeg 2x" data-dominant-color="868874"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×653 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Surface nets with smoothing, showing closed surface representation in slice view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc8de407e21df02b25594119deab572e40224016.jpeg" data-download-href="/uploads/short-url/tbzp11hSwuE9rWh3mpPsKr4REbk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8de407e21df02b25594119deab572e40224016_2_690x233.jpeg" alt="image" data-base62-sha1="tbzp11hSwuE9rWh3mpPsKr4REbk" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8de407e21df02b25594119deab572e40224016_2_690x233.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8de407e21df02b25594119deab572e40224016_2_1035x349.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8de407e21df02b25594119deab572e40224016_2_1380x466.jpeg 2x" data-dominant-color="888975"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×651 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>All these differences are fraction of a voxel’s size. If such small changes matter in your specific application then you can increase the resolution of the binary labelmap representation.</p>
<hr>
<p>Farther away from the cut, the two surfaces are the same, which causes the flickering known, which is a rendering phenomenon known as Z fighting (a screen pixel randomly gets rendered by one surface or the other).</p>
<hr>
<p>These discussions are interesting and it may be useful in understanding capabilities and limitations of various processing and rendering algorithms. However, if your goal is to prove substantial equivalence between different software for a 510k submission then at some point you will have to specify clinically acceptable tolerance. You can then ignore all differences that are much smaller than this tolerance.</p>

---

## Post #8 by @MJamal (2025-05-16 05:56 UTC)

<p>Thank you — this is very helpful. Just to clarify: when using flying edges with windowed sinc smoothing, is there a recommended smoothing kernel size or pass count to minimize the banding effect without introducing noticeable geometric distortion?</p>
<p>Also, regarding surface nets — do you find that they generally introduce fewer overlaps/gaps when used at the native resolution of the labelmap, or is increasing resolution still the preferred approach for critical accuracy?</p>

---

## Post #9 by @lassoan (2025-05-18 12:31 UTC)

<p>Increasing resolution is still needed if you want to significantly improve accuracy. If course, it generally does not make sense to go way beyond your input data resolution (but the answer is not easy when your input image resolution is highly anisotropic).</p>

---
