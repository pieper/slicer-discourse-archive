# Error of cleaver while using segmentmesher

**Topic ID**: 16128
**Date**: 2021-02-22
**URL**: https://discourse.slicer.org/t/error-of-cleaver-while-using-segmentmesher/16128

---

## Post #1 by @Aep93 (2021-02-22 06:41 UTC)

<p>Hello all,<br>
I am trying to mesh my model using segmentmesher (cleaver). When the resolution of model is high, I can do meshing without any problems; however, when I decrease the resolution of my segmentations, I get an error while my segmentation quality is still very good. This is the error I get:</p>
<p>"Nrrd file read error: No zero crossing in indicator function. Not a valid file or need a lower sigma value.</p>
<p>Command ‘cleaver-cli’ returned non-zero exit status 11."</p>
<p>I do not understand what problem in my segmentation can cause this error. Can you give me some cases that can lead to this error or help me to solve this problem?<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2021-02-22 13:31 UTC)

<p>[quote=“Aep93, post:1, topic:16128”]<br>
"Nrrd file read error: No zero crossing in indicator function. Not a valid file or need a lower sigma value.<br>
[/quote]s</p>
<p>This means that the method gets an empty segment, most likely because there is a small structure that gets completely removed during preprocessing steps (sampling and Gaussian smoothing). You can either hide the segment to exclude from meshing, increase sampling rate, or lower blending function sigma (by specifying <code>--blend_sigma 0.5</code> as additional command line option).</p>

---

## Post #3 by @Aep93 (2021-02-22 20:07 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I understood that this problem happens when I scale down my segmentation. So, I have a segmentation for which I can produce mesh without any problems. Then I  use the transform module to make my segmentation smaller. Then I get this error when I want to mesh my scaled segmentation even though the resolution of the scaled segmentation is the same as the original one and only the dimensions have changed.<br>
Am I missing anything during scaling? should I do additional steps to complete my scaling?</p>

---

## Post #4 by @lassoan (2021-02-22 22:11 UTC)

<p>What do you mean by scaling down? Changing unit from mm to cm or inches? Or decrease the number of elements?</p>

---

## Post #5 by @Aep93 (2021-02-22 22:13 UTC)

<p>I enter a value smaller than 1 in the diagonal elements of first three columns in the transfer module and use this transformation to make my segmentation smaller. (I do it for changing units)</p>

---

## Post #6 by @lassoan (2021-02-22 22:39 UTC)

<p>I would recommend to not change units. If you must change units then do it as the very last step (transform the output of Segment mesher), just before saving the mesh.</p>

---

## Post #7 by @Aep93 (2021-02-22 22:42 UTC)

<p>OK <a class="mention" href="/u/lassoan">@lassoan</a>, I will convert the units in my last step then. Thanks for your response.</p>

---

## Post #8 by @lassoan (2023-08-19 09:13 UTC)

<p>A post was merged into an existing topic: <a href="/t/segmentmesher-error-command-cleaver-cli-exe-returned-non-zero-exit-status-3221226505/31172">SegmentMesher, Error: Command ‘cleaver-cli.exe’ returned non-zero exit status 3221226505</a></p>

---
