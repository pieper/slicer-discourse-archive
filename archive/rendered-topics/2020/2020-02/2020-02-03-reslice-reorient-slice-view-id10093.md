---
topic_id: 10093
title: "Reslice Reorient Slice View"
date: 2020-02-03
url: https://discourse.slicer.org/t/10093
---

# Reslice / Reorient Slice view

**Topic ID**: 10093
**Date**: 2020-02-03
**URL**: https://discourse.slicer.org/t/reslice-reorient-slice-view/10093

---

## Post #1 by @manjula (2020-02-03 19:51 UTC)

<p>I have some micro CT data of dental implants. However the implants are not vertical in slice view and we need to define a ROI of in the micro thread area only.  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b7131cb6ff8f623ff5094ec5576571bad938d27.jpeg" data-download-href="/uploads/short-url/jTySXKLWYWRyDyH7zSc8sHUDkNh.jpeg?dl=1" title="Original" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b7131cb6ff8f623ff5094ec5576571bad938d27_2_690x461.jpeg" alt="Original" data-base62-sha1="jTySXKLWYWRyDyH7zSc8sHUDkNh" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b7131cb6ff8f623ff5094ec5576571bad938d27_2_690x461.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b7131cb6ff8f623ff5094ec5576571bad938d27_2_1035x691.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b7131cb6ff8f623ff5094ec5576571bad938d27.jpeg 2x" data-dominant-color="2D2D2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Original</span><span class="informations">1332×890 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I wanted to define the ROI as follows <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e3236ff2707832eefd5db81126727ac8b12ecde.jpeg" data-download-href="/uploads/short-url/fIQ6BuFam7VvOLhOC2zQQ7JC54i.jpeg?dl=1" title="neededROI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e3236ff2707832eefd5db81126727ac8b12ecde_2_690x461.jpeg" alt="neededROI" data-base62-sha1="fIQ6BuFam7VvOLhOC2zQQ7JC54i" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e3236ff2707832eefd5db81126727ac8b12ecde_2_690x461.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e3236ff2707832eefd5db81126727ac8b12ecde_2_1035x691.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e3236ff2707832eefd5db81126727ac8b12ecde.jpeg 2x" data-dominant-color="2F2A28"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">neededROI</span><span class="informations">1332×890 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But since there is tilt if i transform the image or the ROI in one slice  (e.g. Yellow) the ROI is either too much or too little in the green slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7919c452a9783db3b150a09f9dd27b7db0c10655.jpeg" data-download-href="/uploads/short-url/hhiYI8q3nUY9cLfqPdV1fup7glD.jpeg?dl=1" title="transformROI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7919c452a9783db3b150a09f9dd27b7db0c10655_2_633x500.jpeg" alt="transformROI" data-base62-sha1="hhiYI8q3nUY9cLfqPdV1fup7glD" width="633" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7919c452a9783db3b150a09f9dd27b7db0c10655_2_633x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7919c452a9783db3b150a09f9dd27b7db0c10655_2_949x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7919c452a9783db3b150a09f9dd27b7db0c10655.jpeg 2x" data-dominant-color="262523"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">transformROI</span><span class="informations">1128×890 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So if i select the area in one slice (green ) we can see the that area selected is extended from the top and short from bottom.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f934b0161f8f66b5991f75e0cc48c61f5a3aed8.png" data-download-href="/uploads/short-url/ku7QPhgv28FKQRXgpnRUjKMn6uQ.png?dl=1" title="Scissor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f934b0161f8f66b5991f75e0cc48c61f5a3aed8_2_574x500.png" alt="Scissor" data-base62-sha1="ku7QPhgv28FKQRXgpnRUjKMn6uQ" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f934b0161f8f66b5991f75e0cc48c61f5a3aed8_2_574x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f934b0161f8f66b5991f75e0cc48c61f5a3aed8_2_861x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f934b0161f8f66b5991f75e0cc48c61f5a3aed8.png 2x" data-dominant-color="292C27"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Scissor</span><span class="informations">1022×890 336 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried with transform and reslice module with no luck. Is there a way to get this ROI and crop the volume by straightening the implant ?  Apart from manually segmenting.</p>
<p>What are the ways to achieve this ?</p>

---

## Post #2 by @lassoan (2020-02-03 20:27 UTC)

<p>There are many ways to reorient slice views and ROIs. What would be the overall goal?</p>

---

## Post #3 by @manjula (2020-02-03 20:45 UTC)

<p>It is to isolate the micro-thread region only and segment it out.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f5afa8a743e7945110c6c8fc7e1b85927807a52.png" alt="Implantium-implant-Dentium-Co-Seoul-Korea" data-base62-sha1="bk0DKiPW2qrIr2oGAVztC7oIO1c" width="454" height="321"></p>
<p>Something like this. This was one of the better oriented scans and more or less the implant was upright. but still there is a slant.</p>
<p>Since these files are larger than &gt;3GB we want to first crop the volume isolating the micro threads afterwards to work on the segmentation and calculations.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e14cc841a3a1ee3367369f1e2e990c28bcef1b6.png" data-download-href="/uploads/short-url/b8JNR0CbtrzeFmq8HwhDmm99hJ4.png?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e14cc841a3a1ee3367369f1e2e990c28bcef1b6_2_574x500.png" alt="Screenshot_1" data-base62-sha1="b8JNR0CbtrzeFmq8HwhDmm99hJ4" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e14cc841a3a1ee3367369f1e2e990c28bcef1b6_2_574x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e14cc841a3a1ee3367369f1e2e990c28bcef1b6_2_861x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e14cc841a3a1ee3367369f1e2e990c28bcef1b6.png 2x" data-dominant-color="65687A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1022×890 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-02-04 00:33 UTC)

<p>If the goal is just cropping then approximate alignment is good enough. Probably you don’t even need to rotate the ROI (since it should not matter that you include a little bit more in the cropped image), but if you want to rotate then apply a transform and use the sliders.</p>
<p>You can align slice view with the implant by showing the implant using volume rendering and then dropping 3 markups fiducial point on the top surface and copy-pasting <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Fit_slice_plane_to_markup_fiducials">this code</a> into the Python console.</p>
<p>In tomorrow’s Slicer Preview Release, we’ll add computation of principal axes directions of segmented objects, so you’ll be able to get the implant long axis automatically from there. You can crop&amp;downsample the volume before segmentation if you find that that the segmenting the whole implant is too computationally demanding.</p>

---

## Post #5 by @manjula (2020-02-04 09:47 UTC)

<p>I tried the way Prof <a class="mention" href="/u/lassoan">@lassoan</a> described but the results are not quite what i expected.</p>
<p>This is close to the ROI i want to have uniformly around the implant.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6fbb1e20cd2a45c2cbc350f85979ca7a8e7b415.png" data-download-href="/uploads/short-url/wXn4syjo055CjxfWUKnxqAjgFtX.png?dl=1" title="oneSide" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6fbb1e20cd2a45c2cbc350f85979ca7a8e7b415_2_690x298.png" alt="oneSide" data-base62-sha1="wXn4syjo055CjxfWUKnxqAjgFtX" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6fbb1e20cd2a45c2cbc350f85979ca7a8e7b415_2_690x298.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6fbb1e20cd2a45c2cbc350f85979ca7a8e7b415.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6fbb1e20cd2a45c2cbc350f85979ca7a8e7b415.png 2x" data-dominant-color="8994AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">oneSide</span><span class="informations">722×312 82.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when i have good ROI in one side other side looks like this,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05cca75688279ce5a8db87e2ac5be4e17e8e6031.jpeg" data-download-href="/uploads/short-url/PiR3IoAzoAGt0QcJHCe6EeXuhj.jpeg?dl=1" title="ROI-Otherside" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05cca75688279ce5a8db87e2ac5be4e17e8e6031_2_690x423.jpeg" alt="ROI-Otherside" data-base62-sha1="PiR3IoAzoAGt0QcJHCe6EeXuhj" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05cca75688279ce5a8db87e2ac5be4e17e8e6031_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05cca75688279ce5a8db87e2ac5be4e17e8e6031_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05cca75688279ce5a8db87e2ac5be4e17e8e6031_2_1380x846.jpeg 2x" data-dominant-color="6E7386"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROI-Otherside</span><span class="informations">1433×880 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>if there is a way of dragging the 8 corners of the ROI box independently the problem will be solved i guess if that is possible. or if there is a way of transforming the ROI box around the center of the segment.</p>
<p>if there is way of orienting this plane,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/368aec08251d12a789d15089e960cde3905257f0.jpeg" data-download-href="/uploads/short-url/7MvqbLkc5iGLVwl5tiWo6clQSe4.jpeg?dl=1" title="Screenshot from 2020-02-04 09-51-25" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/368aec08251d12a789d15089e960cde3905257f0_2_661x500.jpeg" alt="Screenshot from 2020-02-04 09-51-25" data-base62-sha1="7MvqbLkc5iGLVwl5tiWo6clQSe4" width="661" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/368aec08251d12a789d15089e960cde3905257f0_2_661x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/368aec08251d12a789d15089e960cde3905257f0_2_991x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/368aec08251d12a789d15089e960cde3905257f0_2_1322x1000.jpeg 2x" data-dominant-color="656A7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-04 09-51-25</span><span class="informations">1423×1075 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried the script and i am not sure what exactly happens. I can see the difference in the Red Slice when i put the script.</p>
<p>I made a small video to highlight the problem with the plan and what happens.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="RAJ95v692LI" data-video-title="out 4" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=RAJ95v692LI" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/RAJ95v692LI/maxresdefault.jpg" title="out 4" width="" height="">
  </a>
</div>

<p>I can share the data as well if that would help in solving the problem.</p>
<p>thank you.</p>

---

## Post #6 by @manjula (2020-02-04 11:14 UTC)

<p>Also please note that micro-thread is a helix so there is a pitch and it will never be the same but need to be as close as possible.</p>

---

## Post #7 by @lassoan (2020-02-04 14:59 UTC)

<p>When you copy-paste the Python code snippet then it should make the red slice view coplanar with the 3 markups fiducial points. I’ve slightly modified the code (it used integer vectors instead of floating-point vectors), please try again.</p>

---

## Post #8 by @manjula (2020-02-04 17:45 UTC)

<p>Dear Prof Lasso,</p>
<p>Many thanks for helping me with this and the modified script worked perfectly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e62bf49b4707191ec8af45c8584f1664db41257d.png" data-download-href="/uploads/short-url/wQbZwQqehBjvM7TOwkB4VHCTvXL.png?dl=1" title="Screenshot from 2020-02-04 18-24-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e62bf49b4707191ec8af45c8584f1664db41257d_2_690x360.png" alt="Screenshot from 2020-02-04 18-24-14" data-base62-sha1="wQbZwQqehBjvM7TOwkB4VHCTvXL" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e62bf49b4707191ec8af45c8584f1664db41257d_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e62bf49b4707191ec8af45c8584f1664db41257d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e62bf49b4707191ec8af45c8584f1664db41257d.png 2x" data-dominant-color="74779C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-04 18-24-14</span><span class="informations">921×481 99.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However i still want to select the ROI from that slice to a slice in the middle. I have attached the screenshots. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eea4c7e4c867cb36e7da1d6dc85ef04f725fa15.png" data-download-href="/uploads/short-url/4puj22p94bYRjspviwXdJ5oSQyp.png?dl=1" title="UpTohere" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eea4c7e4c867cb36e7da1d6dc85ef04f725fa15_2_531x500.png" alt="UpTohere" data-base62-sha1="4puj22p94bYRjspviwXdJ5oSQyp" width="531" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eea4c7e4c867cb36e7da1d6dc85ef04f725fa15_2_531x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eea4c7e4c867cb36e7da1d6dc85ef04f725fa15_2_796x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eea4c7e4c867cb36e7da1d6dc85ef04f725fa15.png 2x" data-dominant-color="535564"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">UpTohere</span><span class="informations">946×890 304 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How do i cut this volume alone these two planes in red slice ?  ROI box still behaves the same way as it was. So I just want to isolate the volume from the top slice to the middle slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f763f350f0d20548ac676fdf69cb5267f0810c7d.png" data-download-href="/uploads/short-url/ziw4Q41nFFBSObpYA5id4vn7MbX.png?dl=1" title="Screenshot from 2020-02-04 18-47-38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f763f350f0d20548ac676fdf69cb5267f0810c7d_2_554x500.png" alt="Screenshot from 2020-02-04 18-47-38" data-base62-sha1="ziw4Q41nFFBSObpYA5id4vn7MbX" width="554" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f763f350f0d20548ac676fdf69cb5267f0810c7d_2_554x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f763f350f0d20548ac676fdf69cb5267f0810c7d_2_831x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f763f350f0d20548ac676fdf69cb5267f0810c7d.png 2x" data-dominant-color="5C5F6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-04 18-47-38</span><span class="informations">964×869 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What is the best way to crop this volume ? is there a way of like snapping the ROI box to the F1,F2 and F3 ???</p>

---

## Post #9 by @lassoan (2020-02-04 19:33 UTC)

<p>You can orient slice viewers to orthogonal orthogonal directions by changing the last argument of <code>sliceNode.SetSliceToRASByNTP</code> call from 0 to 1 or 2. Then you can use Scissors effect in rectangle mode to draw an axis-aligned ROI.</p>

---

## Post #10 by @Juicy (2020-02-04 20:17 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a>, maybe as another option you could check out this thread on setting the center of rotation of a transform. I have found this quite useful before.</p>
<p><a href="https://discourse.slicer.org/t/rotation-around-specific-point/9398/11">https://discourse.slicer.org/t/rotation-around-specific-point/9398/11</a></p>

---

## Post #11 by @manjula (2020-02-05 19:05 UTC)

<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/juicy">@Juicy</a></p>
<p>Many thanks.   The way Prof Lasso mentioned worked with segmenting (Scissors) . <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e15ac793c5f4735693a1c598ef7a92029e050d8.png" data-download-href="/uploads/short-url/b8LG3UpxttRvdFG0oV7Oe9tEwTm.png?dl=1" title="Screenshot from 2020-02-05 19-07-54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e15ac793c5f4735693a1c598ef7a92029e050d8_2_690x388.png" alt="Screenshot from 2020-02-05 19-07-54" data-base62-sha1="b8LG3UpxttRvdFG0oV7Oe9tEwTm" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e15ac793c5f4735693a1c598ef7a92029e050d8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e15ac793c5f4735693a1c598ef7a92029e050d8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e15ac793c5f4735693a1c598ef7a92029e050d8_2_1380x776.png 2x" data-dominant-color="AAABB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-05 19-07-54</span><span class="informations">1920×1080 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbe6464cc963aa2933cd873c91b0fe1ee469cd2e.jpeg" data-download-href="/uploads/short-url/zWpcMt6zCqoh87YYhSa2WSlefym.jpeg?dl=1" title="Screenshot from 2020-02-05 19-08-24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbe6464cc963aa2933cd873c91b0fe1ee469cd2e_2_690x388.jpeg" alt="Screenshot from 2020-02-05 19-08-24" data-base62-sha1="zWpcMt6zCqoh87YYhSa2WSlefym" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbe6464cc963aa2933cd873c91b0fe1ee469cd2e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbe6464cc963aa2933cd873c91b0fe1ee469cd2e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbe6464cc963aa2933cd873c91b0fe1ee469cd2e_2_1380x776.jpeg 2x" data-dominant-color="B2B3BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-05 19-08-24</span><span class="informations">1920×1080 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However when I try to do it with ROI box the box was cropping the volume as usual (with the angle) .  I expected it to work the same way as the Scissor but it did not.</p>
<p>However i transform the ROI with “Local” settings and  after some playing around with the slides it managed to crop the volume the way  i wanted to. Otherwise the ROI was still behaving as earlier screenshots unlike the scissor square. If the ROI is working just like the scissor effect things would be much easier for us but we can manage with this way also.</p>
<p>Is there a way of getting the ROI to work the same way as the Scissor square ?</p>
<p>As <a class="mention" href="/u/juicy">@Juicy</a> suggested setting the center of rotation option i am keeping as a last resort because we have about 80 sets of data to analyse and with no easy way of finding the center of implant it would be bit of trouble. But i tried that way also and can get it to work in that way also.</p>
<p>Thank you for the help.</p>

---

## Post #12 by @lassoan (2020-02-05 20:27 UTC)

<aside class="quote no-group" data-username="manjula" data-post="11" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>However when I try to do it with ROI box the box was cropping the volume as usual (with the angle)</p>
</blockquote>
</aside>
<p>From the 3 markup points, you can create a transform that rotates the ROI. In fact, you can fully position and rotate the ROI based on a few markup points (e.g., 3 coplanar points to define the position and orientation of the front face of the ROI and a 4th point to define the opposite face).</p>
<p>With latest Slicer Preview release that you download tomorrow or later (rev28754), you can position the ROI on an object automatically as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment">this example</a>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/629440e24c3483477b4d7a817cf7bca15c113090.jpeg" data-download-href="/uploads/short-url/e44qgyzjaQMqEf6xtUJ9PoK7T3i.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/629440e24c3483477b4d7a817cf7bca15c113090_2_690x461.jpeg" alt="image" data-base62-sha1="e44qgyzjaQMqEf6xtUJ9PoK7T3i" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/629440e24c3483477b4d7a817cf7bca15c113090_2_690x461.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/629440e24c3483477b4d7a817cf7bca15c113090_2_1035x691.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/629440e24c3483477b4d7a817cf7bca15c113090_2_1380x922.jpeg 2x" data-dominant-color="605F68"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1381×924 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, you can almost fully automate your workflow by first segmenting the implant using thresholding (if you have multiple implants then you can separate them using Islands / Split islands to segments), run the example script above to place the oriented ROI boxes automatically, then adjust them as needed.</p>

---

## Post #13 by @manjula (2020-02-05 22:04 UTC)

<p>I am looking forward to this new build and this will solve many of our and many of others problem in analyzing. This is very exciting…</p>
<p>What we are trying to do is something similar to this  and for the record <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"> we had the idea independent of this paper before we came across about a week ago.</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/101es3u7QhLVgj-xTkaFothyKl5Eby6vU/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:129/67;"><img src="https://lh3.googleusercontent.com/c6WEI__dL4ZgbZfVp-FGnmOkOkLGfT8og1kbH1tGtjfMX1BuCG2kk41lBJkVZpU=w1200-h630-p" class="thumbnail" width="129" height="67"></div>

<h3><a href="https://drive.google.com/file/d/101es3u7QhLVgj-xTkaFothyKl5Eby6vU/view?usp=sharing" target="_blank" rel="nofollow noopener">nakahara2019.pdf</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>So what we are doing is   this  to analyse the total volume and the bone volume…</p>
<div class="lazyYT" data-youtube-id="pTLfp6Z3DGU" data-youtube-title="trial" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Our other problem is we when we grow the margins our computers are not powerful enough to grow over 0.1 mm on these data sets. We grow each ring 0.1 mm at a time which takes about 2-3 minutes to do that as well. We want to use 0.5 mm rings but when we try to grow at 0…5 mm at the same time the Slicer hangs…</p>
<p>My system is  i7-8550U CPU @ 1.80GHz,  16Gb DDR4 2400 MT/s and NVidia Geforce MTX150 4GB.</p>
<p>But i guess noting can be done apart from upgrading the hardware specs.</p>

---

## Post #14 by @lassoan (2020-02-05 23:02 UTC)

<aside class="quote no-group" data-username="manjula" data-post="13" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Our other problem is we when we grow the margins our computers are not powerful enough to grow over 0.1 mm on these data sets.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> worked on this and there is an almost-complete pull request that speeds up large margin computations by 10x or more:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/1274">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/1274" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/1274" target="_blank" rel="noopener">slice pipeline does not re-execute for changes to label layer image data</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="23:24:02" data-timezone="UTC">11:24PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="23:24:02" data-timezone="UTC">11:24PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=1274). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You may also find “Split Volume” effect useful: if you segment the implants with thresholding, split the segments using Island effect, then Volume Split effect cuts out only the implants (with a predefined padding around it) automatically, to separate small volumes.</p>

---

## Post #15 by @manjula (2020-02-07 14:13 UTC)

<p>Prof <a class="mention" href="/u/lassoan">@lassoan</a></p>
<ol>
<li>
<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment" rel="nofollow noopener">ROI</a> scripts works perfectly how ever I need to “enter”  "twice " for it to draw the box every time. Is this expected ?</p>
</li>
<li>
<p>I downloaded the latest rev 28755 (linux) build but i was not able to figure out to do this without the script as you showed it earlier ? Can you point me in the right direction.</p>
</li>
<li>
<p>As i mentioned earlier due to lack of processing power in our machines, we need to grow the margin 0.1 mm at a time. We need 3 zones each 0- 0.5, 0.5- 1 and a 1 -  1.5 mm bone rings. So at this way we need to do it 15 times in one sample and we looses the count too in the middle <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"><br>
Is it possible to do a loop for  script like grow 0.1mm at a time for 5 times ? It should basically behave the same as manually doing it 5 times  ?</p>
</li>
</ol>
<p>I will make a feature request also for this. If the segment editor have a option to apply the same effect repeatedly for “x” number of times. Even though this looks like a redundant and similar function i think in lower specs computers this will be useful if it works the way i think it would.</p>

---

## Post #16 by @lassoan (2020-02-07 14:25 UTC)

<aside class="quote no-group" data-username="manjula" data-post="15" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment">ROI</a> scripts works perfectly how ever I need to “enter” "twice " for it to draw the box every time. Is this expected ?</p>
</blockquote>
</aside>
<p>It’s not expected and I didn’t experience this. Maybe just a screen refresh issue. You can try forcing re-rendering fixes it.</p>
<aside class="quote no-group" data-username="manjula" data-post="15" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I downloaded the latest rev 28755 (linux) build but i was not able to figure out to do this without the script as you showed it earlier ? Can you point me in the right direction.</p>
</blockquote>
</aside>
<p>I don’t know what you are referring to.</p>
<aside class="quote no-group" data-username="manjula" data-post="15" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>As i mentioned earlier due to lack of processing power in our machines, we need to grow the margin 0.1 mm at a time.</p>
</blockquote>
</aside>
<p>Simply running the method recursively would lead to inaccuracies because if the kernel is small then it does not approximate a sphere perfectly. The pull request by <span class="mention">@sunderlandyl</span> mentioned above will take care of the performance issue in Margin and Hollow effects.</p>

---

## Post #17 by @manjula (2020-02-07 14:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>With latest Slicer Preview release that you download tomorrow or later (rev28754), you can position the ROI on an object automatically as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment" rel="noopener nofollow ugc">this example </a></p>
</blockquote>
</aside>
<p>I am sorry i was referring to this. I was expecting that this ROI positioning can be done without the use of the script from the rev 28754 above.</p>
<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Simply running the method recursively would lead to inaccuracies because if the kernel is small then it does not approximate a sphere perfectly. The pull request by <span class="mention">@sunderlandyl</span> mentioned above will take care of the performance issue in Margin and Hollow effects.</p>
</blockquote>
</aside>
<p>If you think it is not very accurate we will have trouble analyzing the data. Do you have any idea how long the that pull request will take to materialize ?<br>
As the same time is their any work around other than finding a better computer ! we have ordered a workstation but it will take time it seems and we are in  hurry on this one.</p>

---

## Post #18 by @lassoan (2020-02-07 14:42 UTC)

<aside class="quote no-group" data-username="manjula" data-post="17" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I am sorry i was referring to this. I was expecting that this ROI positioning can be done without the use of the script from the rev 28754 above.</p>
</blockquote>
</aside>
<p>The oriented bounding box, principal axes, etc. will most likely be used as part of automated workflows, so I’m not sure if it is worth spending time with converting the script to a module. You need to keep using the script or add it to your own processing module.</p>
<aside class="quote no-group" data-username="manjula" data-post="17" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>If you think it is not very accurate we will have trouble analyzing the data. Do you have any idea how long the that pull request will take to materialize ?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> might be able to give you an estimate. If it’s very urgent for you: since the work-in-progress part of the pull request does not affect core functionality, you can copy the relevant part of the effect (compute distance map and threshold it) into your own script.</p>

---

## Post #19 by @Sunderlandkyl (2020-02-07 15:00 UTC)

<p>I’m working on the pull request currently, and hope to have it finished today.</p>

---

## Post #20 by @manjula (2020-02-07 15:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The oriented bounding box, principal axes, etc. will most likely be used as part of automated workflows, so I’m not sure if it is worth spending time with converting the script to a module. You need to keep using the script or add it to your own processing module.</p>
</blockquote>
</aside>
<p>Thank you for the clarification. The script works well for our case so nothing much needed from that aspect.</p>
<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> might be able to give you an estimate. If it’s very urgent for you: since the work-in-progress part of the pull request does not affect core functionality, you can copy the relevant part of the effect (compute distance map and threshold it) into your own script.</p>
</blockquote>
</aside>
<p>It is very urgent as we plan to present on this by march. we have around 100 samples of this. If you have some time can you please look at the data if it is nothing too much for ask.</p>
<p><a href="https://drive.google.com/file/d/1cUoeyi0xYrkaRctVPzL6CF845YvmKdVY/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1cUoeyi0xYrkaRctVPzL6CF845YvmKdVY/view?usp=sharing</a></p>
<p>We need to grow three zones (0-0.5 mm, 0.5 - 1mm  &amp; 1- 1.5 mm)  unfortunately we have dont have a way to measure if this is a error in growing 1mmx5 vs 5mmx1.  We want the total volumes of each zone calculated.</p>
<p>If you and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could guide me to add this functionality to a script to enhance performance i am very  in to trying this out.</p>

---

## Post #21 by @manjula (2020-02-08 19:30 UTC)

<p>Prof <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>I was following the discussion at</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="14" data-topic="10093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="https://github.com/Slicer/Slicer/pull/1274" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a></p>
<h4><a href="https://github.com/Slicer/Slicer/pull/1274" rel="noopener nofollow ugc">ENH: Add vtkITK filter for computing label margins</a></h4>
<p><code>Slicer:master</code> ← <code>Sunderlandkyl:vtkitk_margin</code></p>
<p>opened Dec 3, 2019</p>
<p><a href="https://github.com/Sunderlandkyl" rel="noopener nofollow ugc"> <img src="https://avatars3.githubusercontent.com/u/9222709?v=4" alt="Sunderlandkyl" width="20" height="20"> Sunderlandkyl </a></p>
<p><a href="https://github.com/Slicer/Slicer/pull/1274/files" rel="noopener nofollow ugc"> +302 -101</a></p>
</blockquote>
</aside>
<p>At this momement, if we tell to grow the margin by 0.5 mm in a cylinder, is only 0.25 mm is grown on either side ? so if we want 0.5 in one side do we need to grow it by 1 mm ?</p>

---

## Post #22 by @lassoan (2020-02-08 20:16 UTC)

<p>Margin size will mean the how much a boundary will be moved (if you set 1mm as margin then the object will be 2mm wider).</p>

---

## Post #23 by @manjula (2020-02-13 20:03 UTC)

<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/juicy">@Juicy</a></p>
<p>Now as margin growing working perfectly we started working on analysis of data and we  noticed a very minor offset of the ROI.</p>
<p>We expected the Bar of the ROI to align to all the fiducials.   we initially thought it was due to error in placement of marks and we incorporated auto update and played around</p>
<h1><a name="p-35837-update-slice-plane-automatically-whenever-points-are-changed-1" class="anchor" href="#p-35837-update-slice-plane-automatically-whenever-points-are-changed-1" aria-label="Heading link"></a>Update slice plane automatically whenever points are changed</h1>
<p>markupObservation = [markups, markups.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, UpdateSlicePlane, 0)]</p>
<p>In Slice view it is nicely in plane but the ROI does not fit perfectly to that. Is this expected ? Is there something that need to be changed in the ROI code ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a07b942872289d3ab1a1717418ee1e8c0fb35a5.jpeg" data-download-href="/uploads/short-url/hpwNyrQYtzekkOuUC2rwAq7ZLDL.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a07b942872289d3ab1a1717418ee1e8c0fb35a5_2_690x489.jpeg" alt="Screenshot" data-base62-sha1="hpwNyrQYtzekkOuUC2rwAq7ZLDL" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a07b942872289d3ab1a1717418ee1e8c0fb35a5_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a07b942872289d3ab1a1717418ee1e8c0fb35a5_2_1035x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a07b942872289d3ab1a1717418ee1e8c0fb35a5.jpeg 2x" data-dominant-color="7E8792"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1254×890 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/730dac6a30ff2235845bcf519ae00d6f1535af4a.jpeg" data-download-href="/uploads/short-url/gpOcFPt9Vmht8FVTAmrT6Xp378C.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/730dac6a30ff2235845bcf519ae00d6f1535af4a_2_690x489.jpeg" alt="Screenshot_2" data-base62-sha1="gpOcFPt9Vmht8FVTAmrT6Xp378C" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/730dac6a30ff2235845bcf519ae00d6f1535af4a_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/730dac6a30ff2235845bcf519ae00d6f1535af4a_2_1035x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/730dac6a30ff2235845bcf519ae00d6f1535af4a.jpeg 2x" data-dominant-color="7D838E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1254×890 279 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The Coplanar script is working perfectly i think as you can see. It is something wrong with the ROI.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5abef188bf3e2c5713d7e130635c29a39c58ebaa.png" data-download-href="/uploads/short-url/cWM4974pl5Cqdyj3B9me09jUrJ8.png?dl=1" title="Screenshot_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5abef188bf3e2c5713d7e130635c29a39c58ebaa_2_574x500.png" alt="Screenshot_3" data-base62-sha1="cWM4974pl5Cqdyj3B9me09jUrJ8" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5abef188bf3e2c5713d7e130635c29a39c58ebaa_2_574x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5abef188bf3e2c5713d7e130635c29a39c58ebaa_2_861x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5abef188bf3e2c5713d7e130635c29a39c58ebaa.png 2x" data-dominant-color="8A8996"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_3</span><span class="informations">1022×890 318 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @lassoan (2020-02-13 20:24 UTC)

<p>How did you position the ROI? Is it the oriented bounding box provided by Segment statistics?</p>

---

## Post #25 by @manjula (2020-02-13 20:31 UTC)

<p>I could not figure out how to gt the bounding box with the segment statistics.<br>
I did it with the Script in the repository.</p>
<p>segmentationNode = getNode(‘Segmentation’)</p>
<h1>Compute bounding boxes</h1>
<p>import SegmentStatistics<br>
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()<br>
segStatLogic.getParameterNode().SetParameter(“Segmentation”, segmentationNode.GetID())<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_origin_ras.enabled”,str(True))<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_diameter_mm.enabled”,str(True))<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_direction_ras_x.enabled”,str(True))<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_direction_ras_y.enabled”,str(True))<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_direction_ras_z.enabled”,str(True))<br>
segStatLogic.computeStatistics()<br>
stats = segStatLogic.getStatistics()</p>
<h1>Draw ROI for each oriented bounding box</h1>
<p>import numpy as np<br>
for segmentId in stats[‘SegmentIDs’]:<br>
# Get bounding box<br>
obb_origin_ras = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_origin_ras”])<br>
obb_diameter_mm = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_diameter_mm”])<br>
obb_direction_ras_x = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_direction_ras_x”])<br>
obb_direction_ras_y = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_direction_ras_y”])<br>
obb_direction_ras_z = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_direction_ras_z”])<br>
# Create ROI<br>
segment = segmentationNode.GetSegmentation().GetSegment(segmentId)<br>
roi=slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLAnnotationROINode”)<br>
roi.SetName(segment.GetName()+’ bounding box’)<br>
roi.SetXYZ(0.0, 0.0, 0.0)<br>
roi.SetRadiusXYZ(<em>(0.5</em>obb_diameter_mm))<br>
# Position and orient ROI using a transform<br>
obb_center_ras = obb_origin_ras+0.5*(obb_diameter_mm[0] * obb_direction_ras_x + obb_diameter_mm[1] * obb_direction_ras_y + obb_diameter_mm[2] * obb_direction_ras_z)<br>
boundingBoxToRasTransform = np.row_stack((np.column_stack((obb_direction_ras_x, obb_direction_ras_y, obb_direction_ras_z, obb_center_ras)), (0, 0, 0, 1)))<br>
boundingBoxToRasTransformMatrix = slicer.util.vtkMatrixFromArray(boundingBoxToRasTransform)<br>
transformNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLTransformNode’)<br>
transformNode.SetAndObserveMatrixTransformToParent(boundingBoxToRasTransformMatrix)<br>
roi.SetAndObserveTransformNodeID(transformNode.GetID())</p>

---
