# Automate printing segmentation volumes?

**Topic ID**: 19043
**Date**: 2021-08-03
**URL**: https://discourse.slicer.org/t/automate-printing-segmentation-volumes/19043

---

## Post #1 by @J1234 (2021-08-03 15:37 UTC)

<p>Sorry if this is painfully obvious or already covered elsewhere - I’m fairly new to both python programming and 3D Slicer. I’ve been reading through the docs all morning but so far they’ve been more confusing than helpful.</p>
<p>I have a directory of ~700 images (.nii) and corresponding segmentations. I want to write a simple script that will load each segmentation and print the volumes of the two segments (each segmentation contains a “tissue” and a “blood” volume).</p>
<p>So far I have slicer.util.loadSegmentation(“image_number.seg.nrrd”), but I’m not sure from a python perspective how to get the output shown by the segment statistics module on the GUI interface. Can anyone point me in the right direction?</p>

---

## Post #2 by @lassoan (2021-08-03 16:19 UTC)

<p>You are doing good so far. After you loaded the segmentation, run the segment statistics to get the volumes (see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-of-each-segment">complete example in the script repository</a>), and write the results into any format you prefer (for example, you can write the values to a CSV file).</p>

---

## Post #3 by @J1234 (2021-08-03 18:18 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you so much! Turns out I wasn’t looking in the right spot. This is exactly what I needed <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>However - I’ve successfully done pip install slicerio and pip install pynrrd and reloaded jupyter labs, but whenever I try to import them into a script I still get the error: ModuleNotFoundError: No module named ‘nrrd’ or ModuleNotFoundError: No module named ‘slicerio’.</p>
<p>Did these get changed to something else with the newest release?</p>

---

## Post #4 by @lassoan (2021-08-03 18:21 UTC)

<aside class="quote no-group" data-username="J1234" data-post="3" data-topic="19043">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f08c70/48.png" class="avatar"> J1234:</div>
<blockquote>
<p>I’ve successfully done pip install slicerio and pip install pynrrd and reloaded jupyter labs, but whenever I try to import them into a script I still get the error: ModuleNotFoundError: No module named ‘nrrd’ or ModuleNotFoundError: No module named ‘slicerio’.</p>
</blockquote>
</aside>
<p>Probably you installed them in a different Python environment.</p>
<p>However, both slicerio and pynrrd are only needed when your code runs outside of Slicer’s Python environment, so you should not need them.</p>

---

## Post #6 by @J1234 (2021-08-04 04:33 UTC)

<p>I see, thank you again so much!!</p>

---
