---
topic_id: 21813
title: "Rotational Transformation Matrix After Surface Registration"
date: 2022-02-05
url: https://discourse.slicer.org/t/21813
---

# Rotational transformation matrix after surface registration

**Topic ID**: 21813
**Date**: 2022-02-05
**URL**: https://discourse.slicer.org/t/rotational-transformation-matrix-after-surface-registration/21813

---

## Post #1 by @mdhan (2022-02-05 16:56 UTC)

<p>Hello, I’m rather new to 3D Slicer, and I’d greatly appreciate any advice!</p>
<p>I am interested in obtaining the rotational transformation matrix after registering one model to another. For registration, I used the Slicer CMF module using the surface-based registration method. Are there any ways for me to find out the rotations the moving model underwent?</p>
<p>Thank you very much in advance!!</p>

---

## Post #2 by @ungi (2022-02-06 14:15 UTC)

<p>Hi, in the Surface Registration module, you have selected/created an “Output Transform”. Check the name of that transform. Then go to the Transforms module in Slicer, select the same transform name, and the 4x4 homogeneous transformation matrix will be displayed under Edit/Transform Matrix. The upper left 3x3 part of that matrix defines the rotation. I hope this helps.</p>

---

## Post #3 by @mdhan (2022-02-07 04:44 UTC)

<p>Thank you so much - that was extremely helpful!!</p>

---

## Post #4 by @mdhan (2022-05-30 14:13 UTC)

<p>Hello,</p>
<p>Sorry for troubling you all, but I’d be grateful if you could kindly help with a followup question to my original question.</p>
<p>I’ve been having trouble utilizing the rotational transformation matrix to suit my needs, and wanted to make sure I was interpreting things correctly.</p>
<p>What I am interested in knowing is the rotational transformation matrix in degrees, and I have been using an online calculator (<a href="https://www.andre-gaschler.com/rotationconverter/" class="inline-onebox" rel="noopener nofollow ugc">3D Rotation Converter</a>) to convert the 3x3 part of Slicer’s 4x4 matrix.</p>
<p>As a test, I created a cube on Meshmixer, and duplicated it. Then, I rotated the duplicate 11.1, 22.2, 33.3 degrees in the x, y, and z axes, respectively. After exporting these 2 surfaces, I then used the Slicer CMF registration and got the transformation matrix in the 4x4 matrix format.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53.jpeg" data-download-href="/uploads/short-url/cZCJSIH7g8npqjDZEJgp7x309R9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53_2_638x500.jpeg" alt="image" data-base62-sha1="cZCJSIH7g8npqjDZEJgp7x309R9" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53_2_638x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53_2_957x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53_2_1276x1000.jpeg 2x" data-dominant-color="252722"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1436×1125 91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484.png" data-download-href="/uploads/short-url/4dDWsxjN6XmsDudc8r7lxLtrZ76.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484_2_683x500.png" alt="image" data-base62-sha1="4dDWsxjN6XmsDudc8r7lxLtrZ76" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484_2_683x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484.png 2x" data-dominant-color="A88A8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">808×591 57.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d55047a37ff516b14cd3fe61aa6d57672fb2f24.jpeg" alt="MATRIX" data-base62-sha1="8Kzh2rysVhUggRJgM8c330JS96I" width="483" height="137"></p>
<p>However, when I tried to convert the 3x3 matrix to angles, all of the numbers seemed quite off from the 11.1, 22.2, 33.3 degrees. Even when accounting for possible registration errors, the discrepancies seem quite severe (plus on visual inspection the registration seems accurate).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81437bdcd1847c31bfe9094d3537c1065ddee799.jpeg" data-download-href="/uploads/short-url/irwaYWta5KXV67vRySIFG2uI7Ox.jpeg?dl=1" title="OUTPUT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81437bdcd1847c31bfe9094d3537c1065ddee799_2_690x283.jpeg" alt="OUTPUT" data-base62-sha1="irwaYWta5KXV67vRySIFG2uI7Ox" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81437bdcd1847c31bfe9094d3537c1065ddee799_2_690x283.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81437bdcd1847c31bfe9094d3537c1065ddee799_2_1035x424.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81437bdcd1847c31bfe9094d3537c1065ddee799.jpeg 2x" data-dominant-color="EEEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OUTPUT</span><span class="informations">1329×547 88.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would again be grateful for everyone’s wisdom on this!!</p>

---
