# IGT fiducial registration : How to have a fix coordinate system

**Topic ID**: 31448
**Date**: 2023-08-30
**URL**: https://discourse.slicer.org/t/igt-fiducial-registration-how-to-have-a-fix-coordinate-system/31448

---

## Post #1 by @saeedeh_lavasany (2023-08-30 12:54 UTC)

<p>Hello I am trying to use IGT fiducial registration to register a tool that position is tracked by an EMT sensor to a CT model.<br>
I’m using two EM sensors: one is called the “stylus,” and the other is named the “reference.”<br>
I followed the tutorial to register the stylus tip by aligning it with specific markers I selected on the CT scan.<br>
After completing the registration process, I incorporated the “Reference To CT” transformation into the hierarchy.</p>
<p>However, there’s an issue. Even though I attempt to transfer the information from the stylus sensor to the reference sensor, which is securely positioned on the phantom object, the transformation called “Reference To CT” becomes inaccurate when I manipulate the field generator. As a result, I lose the ability to visualize the stylus on the phantom object.</p>
<p>Would you please let me know whats the problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a921966d711a248c8dc4eceee381abaa0c1b7643.png" data-download-href="/uploads/short-url/o8cEwwEBPV6iXZBly3jun8nO5HB.png?dl=1" title="Capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a921966d711a248c8dc4eceee381abaa0c1b7643_2_690x385.png" alt="Capture3" data-base62-sha1="o8cEwwEBPV6iXZBly3jun8nO5HB" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a921966d711a248c8dc4eceee381abaa0c1b7643_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a921966d711a248c8dc4eceee381abaa0c1b7643_2_1035x577.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a921966d711a248c8dc4eceee381abaa0c1b7643_2_1380x770.png 2x" data-dominant-color="FDFBFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture3</span><span class="informations">2605×1454 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dade8638c953ad47f040a5155505e26f5e7e15a9.png" data-download-href="/uploads/short-url/vecQmWZIobwKKkLhfeXYOVRwEhX.png?dl=1" title="Capture4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dade8638c953ad47f040a5155505e26f5e7e15a9_2_690x303.png" alt="Capture4" data-base62-sha1="vecQmWZIobwKKkLhfeXYOVRwEhX" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dade8638c953ad47f040a5155505e26f5e7e15a9_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dade8638c953ad47f040a5155505e26f5e7e15a9_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dade8638c953ad47f040a5155505e26f5e7e15a9_2_1380x606.png 2x" data-dominant-color="FDFCFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture4</span><span class="informations">2523×1110 75.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd5a49c6512b90ca1525f306874c4ec24a1f4431.png" data-download-href="/uploads/short-url/tiDk1xj9m9uZTVdcwPuWBuo3w3f.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd5a49c6512b90ca1525f306874c4ec24a1f4431_2_477x500.png" alt="Capture1" data-base62-sha1="tiDk1xj9m9uZTVdcwPuWBuo3w3f" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd5a49c6512b90ca1525f306874c4ec24a1f4431_2_477x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd5a49c6512b90ca1525f306874c4ec24a1f4431_2_715x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd5a49c6512b90ca1525f306874c4ec24a1f4431_2_954x1000.png 2x" data-dominant-color="E9EEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1051×1100 36.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddf61083b91fbba8234725979f77b619f830a837.png" data-download-href="/uploads/short-url/vFyI7Y33A0ICBFkf2jNLDQREErZ.png?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddf61083b91fbba8234725979f77b619f830a837_2_500x500.png" alt="Capture2" data-base62-sha1="vFyI7Y33A0ICBFkf2jNLDQREErZ" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddf61083b91fbba8234725979f77b619f830a837_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddf61083b91fbba8234725979f77b619f830a837_2_750x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddf61083b91fbba8234725979f77b619f830a837.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">815×815 27.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2023-08-30 18:27 UTC)

<p>ReferenceToTracker is constantly being updated by Plus, overwriting the inverse.<br>
You can add TrackerToReference (or StylusToReference) in the Plus config file, and use one of those to transform the stylus.</p>

---

## Post #3 by @saeedeh_lavasany (2023-08-31 08:37 UTC)

<p>Thank you for your reply. I implemented the transformation, and now everything is working perfectly.</p>

---

## Post #4 by @Dr_Ayush_Shrivastava (2025-02-23 18:23 UTC)

<p>How can i connect you , i need help.</p>

---
