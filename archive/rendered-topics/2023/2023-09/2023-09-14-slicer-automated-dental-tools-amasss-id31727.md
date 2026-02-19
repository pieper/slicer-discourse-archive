---
topic_id: 31727
title: "Slicer Automated Dental Tools Amasss"
date: 2023-09-14
url: https://discourse.slicer.org/t/31727
---

# Slicer automated dental tools AMASSS

**Topic ID**: 31727
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/slicer-automated-dental-tools-amasss/31727

---

## Post #1 by @manjula (2023-09-14 20:31 UTC)

<p>hi,</p>
<p>Any one has got the Slicer automated dental tools to work ?</p>
<p>I am using the Slicer 5.5.0-2023-09-13 r32175 / 23bf4eb on Garuda Linux (6.4.12-zen1-1-zen (64-bit))</p>
<p>I have downloaded test scans and latest models and when i run the prediction it stops after few seconds<br>
This is the message i get,</p>
<p>========= ERROR =========</p>
<p>CLI execution failed:</p>
<p>In the future <code>np.bool</code> will be defined as the corresponding NumPy scalar.<br>
In the future <code>np.bool</code> will be defined as the corresponding NumPy scalar.<br>
Traceback (most recent call last):<br>
File “/home/manjula/Documents/Software/Slicer-5.5.0-2023-09-13-linux-amd64/slicer.org/Extensions-32175/SlicerAutomatedDentalTools/lib/Slicer-5.5/cli-modules/AMASSS_CLI.py”, line 99, in <br>
import itk<br>
File “/home/manjula/Documents/Software/Slicer-5.5.0-2023-09-13-linux-amd64/lib/Python/lib/python3.9/site-packages/itk/<strong>init</strong>.py”, line 28, in <br>
from itk.support.extras import *<br>
File “/home/manjula/Documents/Software/Slicer-5.5.0-2023-09-13-linux-amd64/lib/Python/lib/python3.9/site-packages/itk/support/extras.py”, line 35, in <br>
import itk.support.types as itkt<br>
File “/home/manjula/Documents/Software/Slicer-5.5.0-2023-09-13-linux-amd64/lib/Python/lib/python3.9/site-packages/itk/support/types.py”, line 175, in <br>
) = itkCType.initialize_c_types_once()<br>
File “/home/manjula/Documents/Software/Slicer-5.5.0-2023-09-13-linux-amd64/lib/Python/lib/python3.9/site-packages/itk/support/types.py”, line 140, in initialize_c_types_once<br>
_B: “itkCType” = itkCType(“bool”, “B”, np.bool)<br>
File “/home/manjula/Documents/Software/Slicer-5.5.0-2023-09-13-linux-amd64/lib/Python/lib/python3.9/site-packages/numpy/<strong>init</strong>.py”, line 313, in <strong>getattr</strong><br>
raise AttributeError(<strong>former_attrs</strong>[attr])<br>
AttributeError: module ‘numpy’ has no attribute ‘bool’.<br>
<code>np.bool</code> was a deprecated alias for the builtin <code>bool</code>. To avoid this error in existing code, use <code>bool</code> by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use <code>np.bool_</code> here.<br>
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:<br>
<a href="https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations" class="inline-onebox" rel="noopener nofollow ugc">NumPy 1.20.0 Release Notes — NumPy v2.0.dev0 Manual</a></p>
<p>Thank you</p>

---

## Post #2 by @manjula (2023-09-22 15:44 UTC)

<p>Ok Figure out the issue with the Slicer automated dental tools.</p>
<p>It works only on the stable release.  I was trying it on the latest versions.</p>

---

## Post #3 by @mau_igna_06 (2023-09-23 15:05 UTC)

<p>Can you explain more your context (how did you make it work) and share results?<br>
I’be interested on trying this myself</p>
<p>Thanks a lot,<br>
Mauro</p>

---

## Post #4 by @manjula (2023-09-23 19:38 UTC)

<p>Hi Mauro,</p>
<p>Well, it works perfectly but only on the Slicer stable version ( I tried the ALI and AMASSS). I tried installing the Python libraries manually with the preview release. I haven’t tried the rest.</p>
<p>How it works?</p>
<ol>
<li>Fresh download of the 3D Slicer stable version and extract.</li>
<li>Install only the SlicerAutomatedDentalTools extension</li>
</ol>
<p><strong>ALI</strong></p>
<p>It works well with the test data and <strong>other CBCT</strong>  (I tried)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ce3c67a4009f07503ea2862c040e55f167e2b7.jpeg" data-download-href="/uploads/short-url/ao4eEBRBrGksa53n3cnq3YzdVIz.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ce3c67a4009f07503ea2862c040e55f167e2b7_2_690x473.jpeg" alt="Screenshot" data-base62-sha1="ao4eEBRBrGksa53n3cnq3YzdVIz" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ce3c67a4009f07503ea2862c040e55f167e2b7_2_690x473.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ce3c67a4009f07503ea2862c040e55f167e2b7_2_1035x709.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ce3c67a4009f07503ea2862c040e55f167e2b7_2_1380x946.jpeg 2x" data-dominant-color="A888A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1400×961 71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
With test data</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70538d82caf225bf87895ecfa1ec97ef8f4b454f.png" data-download-href="/uploads/short-url/g1GueG2u50XqgvY8o4T1GdVM3bF.png?dl=1" title="Screenshot2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70538d82caf225bf87895ecfa1ec97ef8f4b454f_2_690x229.png" alt="Screenshot2" data-base62-sha1="g1GueG2u50XqgvY8o4T1GdVM3bF" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70538d82caf225bf87895ecfa1ec97ef8f4b454f_2_690x229.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70538d82caf225bf87895ecfa1ec97ef8f4b454f_2_1035x343.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70538d82caf225bf87895ecfa1ec97ef8f4b454f_2_1380x458.png 2x" data-dominant-color="A28AAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot2</span><span class="informations">1415×470 267 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
with a another CBCT</p>
<p>AMASSS ( It works well with the test data and I did not have time to test other CBCTs)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e559a4bf3838617ead75d654678540f4d2914c10.jpeg" data-download-href="/uploads/short-url/wIVoRYhYjzgoLaNW7sgbqlN6SVG.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e559a4bf3838617ead75d654678540f4d2914c10_2_690x482.jpeg" alt="Screenshot_1" data-base62-sha1="wIVoRYhYjzgoLaNW7sgbqlN6SVG" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e559a4bf3838617ead75d654678540f4d2914c10_2_690x482.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e559a4bf3838617ead75d654678540f4d2914c10_2_1035x723.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e559a4bf3838617ead75d654678540f4d2914c10_2_1380x964.jpeg 2x" data-dominant-color="62647A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1400×978 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried SlicerDentalModelSeg this way and did not work.<br>
The output I get from SlicerDentalModelSeg. Even when I install the missing packages pandas,tqdm etc. using them using    “pip_install(“pandas”)” it finally ends with error messages. this is the first error.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pastebin.com/6491EVnr">
  <header class="source">
      <img src="https://pastebin.com/favicon.ico" class="site-icon" width="" height="">

      <a href="https://pastebin.com/6491EVnr" target="_blank" rel="noopener nofollow ugc">Pastebin</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://pastebin.com/i/facebook.png" class="thumbnail">

<h3><a href="https://pastebin.com/6491EVnr" target="_blank" rel="noopener nofollow ugc">Crown Segmentation - Pastebin.com</a></h3>

  <p>Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However when I install other extensions  (even if I uninstall and reinstall only the Dental tools this does not work and these are the outputs I get.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pastebin.com/ShLBGVcT">
  <header class="source">
      <img src="https://pastebin.com/favicon.ico" class="site-icon" width="" height="">

      <a href="https://pastebin.com/ShLBGVcT" target="_blank" rel="noopener nofollow ugc">Pastebin</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://pastebin.com/i/facebook.png" class="thumbnail">

<h3><a href="https://pastebin.com/ShLBGVcT" target="_blank" rel="noopener nofollow ugc">AMASS Module - Pastebin.com</a></h3>

  <p>Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pastebin.com/X86RLT1g">
  <header class="source">
      <img src="https://pastebin.com/favicon.ico" class="site-icon" width="" height="">

      <a href="https://pastebin.com/X86RLT1g" target="_blank" rel="noopener nofollow ugc">Pastebin</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://pastebin.com/i/facebook.png" class="thumbnail">

<h3><a href="https://pastebin.com/X86RLT1g" target="_blank" rel="noopener nofollow ugc">ALI Module - Pastebin.com</a></h3>

  <p>Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @hortakc (2024-06-20 19:05 UTC)

<p>Hi <a class="mention" href="/u/manjula">@manjula</a> !<br>
Are you still working with ALI and AMASS?<br>
Which version is working well for you?<br>
I am trying the 5.6.2 and they are not working properly</p>

---

## Post #6 by @manjula (2024-06-25 15:33 UTC)

<p>Yes I do and both works.</p>

---
