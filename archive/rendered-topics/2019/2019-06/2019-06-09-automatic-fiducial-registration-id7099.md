# Automatic Fiducial Registration

**Topic ID**: 7099
**Date**: 2019-06-09
**URL**: https://discourse.slicer.org/t/automatic-fiducial-registration/7099

---

## Post #1 by @redsoxfan4 (2019-06-09 21:13 UTC)

<p>Hi All. I would like to build an extension that will automatically pick up MR-visible spheres and place a fiducial in the center of them. Would anyone be able to point me in the write direction for starting this project? I am familiar with python coding but new to developing extensions. Thanks!</p>

---

## Post #2 by @lassoan (2019-06-09 21:49 UTC)

<p>There are many options, including some readily usable fully automatic solutions. To make recommendations, we would need to know a bit more about your application.</p>
<p>Do you need to register patient skin markers or markers embedded in a device? Do you really use sphere markers? (fluid filled tubes and donut shape are much more common) How many markers do you need to register? What is their size? What accuracy and time constraints do you have?</p>

---

## Post #3 by @redsoxfan4 (2019-06-09 22:06 UTC)

<p>Thanks for replying. These would be skin markers that are truly spheres with a homogeneous material (no fluid). I need to register 8-10 and they are 4mm in diameter. I would like the markers to be as accurate as possible, of course, but I envisage .25mm of error to be ok. If you are referring to time constraints for detection, there aren’t any for now.</p>

---

## Post #4 by @lassoan (2019-06-10 13:41 UTC)

<p>I’m not aware of any Slicer extension that would automatically detect spherical fiducials in a random configuration and determine their accurate positions, but it should not be difficult to implement.</p>
<p>First task is detection of fiducial candidates. You can probably do a quick first pass using thresholding, followed by splitting to islands (discarding islands that are much smaller or larger than the expected sphere volumes), then picking the ones with the highest intensity, closest volume, most spherical shape. You can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">Segment Editor effects</a> (or study scripts used in the effects and put it in your own script).</p>
<p>Second task is subpixel accuracy position estimation. For spherical markers, you should be able to get accurate position by performing intensity-based registration between expected image of the fiducial (bright sphere) with the MRI image cropped to a small region around the detected fiducial. You can use rigid transformation, with translation scale set to very high value (so essentially no rotation is attempted during registration). You can probably use “General Registration (BRAINS)” module for this.</p>
<p>Once you have a working script, you can convert it to a module as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" rel="nofollow noopener">Slicer programming tutorials</a>.</p>

---

## Post #5 by @redsoxfan4 (2019-06-10 23:37 UTC)

<p>Thank you for that, very helpful.</p>

---

## Post #6 by @lxedk (2024-07-10 15:14 UTC)

<p>Sorry for hijacking old thread, but are there modules for registration of a donut shaped embedded marker? Thank you!</p>

---
