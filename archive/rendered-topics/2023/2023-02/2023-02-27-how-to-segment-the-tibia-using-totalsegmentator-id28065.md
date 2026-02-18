# How to segment the tibia using TotalSegmentator?

**Topic ID**: 28065
**Date**: 2023-02-27
**URL**: https://discourse.slicer.org/t/how-to-segment-the-tibia-using-totalsegmentator/28065

---

## Post #1 by @zhangliang (2023-02-27 09:22 UTC)

<p>Hello, I can successfully install totalsegmentator. After trying, we couldn’t segment the tibia and surrounding soft tissue. I don’t know what the problem is.</p>

---

## Post #2 by @rbumm (2023-02-27 09:43 UTC)

<p>Tibia and fibula are in the <a href="https://github.com/wasserth/TotalSegmentator#class-details">list of structure classes</a> that TotalSegmentator supports.</p>
<p>Could you provide more detail? What was your input volume?</p>

---

## Post #3 by @zhangliang (2023-02-28 05:26 UTC)

<p>Like this picture, we uploaded a dicom data with mainly tibia, and after running the plugin, it doesn’t show the segmentation result as it should. It should be noted that Task is installed manually, as shown in the figure below.<br>
Also, is there a “filter” for the segmentation results? We don’t need all of them for the display of the results.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/908484d5e0608e14a9ec276b3edea6c59904adf9.png" alt="6fdfa77a580b865f84e18d231e1ad9f" data-base62-sha1="kCsFV8ojKUFuhqjyahg5XivI1GV" width="581" height="394"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26099ae5469ed6af1fa86bfb3e14d28c929dfab9.jpeg" alt="e1ac6bcf76a4227132a204bba9fd9b9" data-base62-sha1="5quINLQ3TCfQOkYhy8Hv1viRBQR" width="407" height="175"></p>

---

## Post #4 by @rbumm (2023-02-28 14:04 UTC)

<p>Just tested the issue with a suitable dataset and can confirm your report.<br>
It seems as if the tibia and phalanges are not yet included in TotalSegmentator 1.5.2, but as I see from <a href="https://github.com/wasserth/TotalSegmentator/issues/66">here</a>, are planned to be supported in one of the next versions.</p>
<p>Maybe <a class="mention" href="/u/wasserth">@wasserth</a> could shortly comment? Thank you.</p>

---
