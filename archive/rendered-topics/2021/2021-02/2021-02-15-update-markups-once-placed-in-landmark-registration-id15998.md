# Update markups once placed in Landmark registration

**Topic ID**: 15998
**Date**: 2021-02-15
**URL**: https://discourse.slicer.org/t/update-markups-once-placed-in-landmark-registration/15998

---

## Post #1 by @LaurennLam (2021-02-15 16:02 UTC)

<p>Hi there,</p>
<p>I’m using the Landmark Registration. But I have some issues when I have to place the landmarks.<br>
When I click to add a new landmark, and then clicking on the fixed image in order to place it, it automatically places the same point (with same coordinate I suppose) in the moving image. But if the two images haven’t the same spacing/extent,… (that’s why I use registration), I have to move the point in the moving image.<br>
But, as I understand, if the landmark is added from the axial view, the only way to move it is to show the other two views and drag/drop it to the correct slice. But it doesn’t seem very accurate.<br>
So I wonder if there is an other way.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2021-02-15 16:05 UTC)

<p>The Landmark Registration module works best when the volumes overlap or are pretty close to begin with.  You could use the Transforms module to get them roughly lined up and then harden the transform before using Landmark Registration.  Then you can use rigid or affine to further refine the registration as needed.</p>

---

## Post #3 by @LaurennLam (2021-02-15 16:12 UTC)

<p>Thanks for the advice.<br>
The main goal is to avoid multiplication of user manipulations.</p>

---

## Post #4 by @lassoan (2021-02-15 16:42 UTC)

<p>I agree that it would be useful to have the option to place the first few landmarks points independently on the two images.</p>
<p>The landmark registration module is just a single Python script, which you can modify with a text editor. <a class="mention" href="/u/laurennlam">@LaurennLam</a> it would be great if you could add a checkbox that would enable/disable automatic placement of the second point (probably 10-20 lines of code) and if it works then contribute the enhancement back to Slicer core.</p>
<p>On Windows, the script is installed by default to <code>c:\Users\&lt;username&gt;\AppData\Local\NA-MIC\Slicer&lt;fullversion&gt;\lib\Slicer-&lt;version&gt;\qt-scripted-modules\LandmarkRegistration.py</code>.</p>

---

## Post #5 by @LaurennLam (2021-02-15 16:45 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> !<br>
I’ll see what I can do.</p>

---
