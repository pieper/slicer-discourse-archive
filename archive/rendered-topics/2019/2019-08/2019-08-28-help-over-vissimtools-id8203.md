# Help over VisSimTools

**Topic ID**: 8203
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/help-over-vissimtools/8203

---

## Post #1 by @Baez (2019-08-28 03:44 UTC)

<p>Hi community.<br>
I have a question, I try to segment the cervical spine with the VisSimTools / Cervical Spine Tools module.<br>
It works well with the Bc11702 data set of the DataStore module.<br>
But wanting to do it with studies of the TCIA Browser I don’t get results.<br>
I can’t find good documentation to help me get better results.<br>
Some good advice to share.<br>
Thaks!</p>

---

## Post #2 by @lassoan (2019-08-28 14:58 UTC)

<p>What is the name of the extension you are using?</p>
<p>If you don’t get relevant answer to your question here for a few days then you may try to directly contact developers of the extension.</p>

---

## Post #3 by @Baez (2019-08-31 00:03 UTC)

<p>Hi.<br>
that excellent tool.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97f4085f2e8b8e207879d01eece8a5ac5489d232.png" data-download-href="/uploads/short-url/lGeW0Nrc0JYWLLoyDYqgdKUtojw.png?dl=1" title="SlicerCervicalSpine" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97f4085f2e8b8e207879d01eece8a5ac5489d232_2_345x193.png" alt="SlicerCervicalSpine" data-base62-sha1="lGeW0Nrc0JYWLLoyDYqgdKUtojw" width="345" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97f4085f2e8b8e207879d01eece8a5ac5489d232_2_345x193.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97f4085f2e8b8e207879d01eece8a5ac5489d232_2_517x289.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97f4085f2e8b8e207879d01eece8a5ac5489d232_2_690x386.png 2x" data-dominant-color="E6EDF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerCervicalSpine</span><span class="informations">1910×1074 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the example, it works very well, but with another volume I am unable to finish the algorithm successfully.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b6784e92ddcc478d625afc843be5a29f0caade7.jpeg" data-download-href="/uploads/short-url/d2BeNk1NrXn7VzmWgoYWGupJUxx.jpeg?dl=1" title="PracticaDelEjemplo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b6784e92ddcc478d625afc843be5a29f0caade7_2_345x193.jpeg" alt="PracticaDelEjemplo" data-base62-sha1="d2BeNk1NrXn7VzmWgoYWGupJUxx" width="345" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b6784e92ddcc478d625afc843be5a29f0caade7_2_345x193.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b6784e92ddcc478d625afc843be5a29f0caade7_2_517x289.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b6784e92ddcc478d625afc843be5a29f0caade7_2_690x386.jpeg 2x" data-dominant-color="72777A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PracticaDelEjemplo</span><span class="informations">1919×1079 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The result was really interesting.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5cb331ab1f62c2283307aed0e74dde24e2cd7c8.jpeg" data-download-href="/uploads/short-url/sdLpIL1uPR0UCXTrrodoka5bxY4.jpeg?dl=1" title="Finlizacion%20del%20algoritmo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5cb331ab1f62c2283307aed0e74dde24e2cd7c8_2_345x194.jpeg" alt="Finlizacion%20del%20algoritmo" data-base62-sha1="sdLpIL1uPR0UCXTrrodoka5bxY4" width="345" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5cb331ab1f62c2283307aed0e74dde24e2cd7c8_2_345x194.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5cb331ab1f62c2283307aed0e74dde24e2cd7c8_2_517x291.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5cb331ab1f62c2283307aed0e74dde24e2cd7c8_2_690x388.jpeg 2x" data-dominant-color="7B8184"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Finlizacion%20del%20algoritmo</span><span class="informations">1918×1079 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I decided to print the example.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59f0b0a034471c01f54e492a98f770d9999c5c87.jpeg" data-download-href="/uploads/short-url/cPEaAa4xmTYNxdcWPcXBYUkLuAf.jpeg?dl=1" title="PostImpresion3DSlicerCervicalTools" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59f0b0a034471c01f54e492a98f770d9999c5c87_2_187x250.jpeg" alt="PostImpresion3DSlicerCervicalTools" data-base62-sha1="cPEaAa4xmTYNxdcWPcXBYUkLuAf" width="187" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59f0b0a034471c01f54e492a98f770d9999c5c87_2_187x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59f0b0a034471c01f54e492a98f770d9999c5c87_2_280x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59f0b0a034471c01f54e492a98f770d9999c5c87_2_374x500.jpeg 2x" data-dominant-color="68635B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PostImpresion3DSlicerCervicalTools</span><span class="informations">720×960 83.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I’m not successful with patients from the clinic, or from TCIA Browser.</p>
<p>Thanks for the time and help.</p>

---

## Post #4 by @Baez (2019-08-31 01:06 UTC)

<p>When i use other vol.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b5beb8def7902b188c7542fec0bf766fe8411c7.png" data-download-href="/uploads/short-url/mamWE2lgfznOjOAlFigMjcoUKgL.png?dl=1" title="InterrupcionDellgoritmo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b5beb8def7902b188c7542fec0bf766fe8411c7_2_690x387.png" alt="InterrupcionDellgoritmo" data-base62-sha1="mamWE2lgfznOjOAlFigMjcoUKgL" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b5beb8def7902b188c7542fec0bf766fe8411c7_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b5beb8def7902b188c7542fec0bf766fe8411c7_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b5beb8def7902b188c7542fec0bf766fe8411c7_2_1380x774.png 2x" data-dominant-color="A5ADAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">InterrupcionDellgoritmo</span><span class="informations">1919×1078 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>.<br>
<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @yf025 (2020-04-23 09:27 UTC)

<p>I meet the same problem，have you figured out？</p>

---
