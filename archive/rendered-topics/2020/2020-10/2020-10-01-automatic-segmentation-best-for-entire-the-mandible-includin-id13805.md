# Automatic segmentation best for entire the mandible including dentition, trabecular and cortical bone

**Topic ID**: 13805
**Date**: 2020-10-01
**URL**: https://discourse.slicer.org/t/automatic-segmentation-best-for-entire-the-mandible-including-dentition-trabecular-and-cortical-bone/13805

---

## Post #1 by @Lexus_H (2020-10-01 23:03 UTC)

<ol>
<li>How do I automatically segment all of the teeth, cortical and trabecular bone in the mandible?  Is it better to use ITK-SNAP or Slicer?</li>
<li>Is colorbar in an increment of 1cmm?  I mean for a range</li>
<li>Is there a way to crop colormap cross-sectionally?  Will it show anything since colormap is only applicable to surfaces?</li>
</ol>
<p>thanks,</p>

---

## Post #2 by @manjula (2020-10-02 08:48 UTC)

<ol>
<li>Please look here for teeth segmentation.</li>
</ol>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/teeth-segmentation/9775/9">Teeth Segmentation</a></div>
<blockquote>
<p>I’ve checked this and found that all teeth can be quite quickly and accurately segmented at once by the following steps:</p>
<ol>
<li>Set editable intensity range from about 1880 to maximum using Threshold effect, “Use for masking”</li>
</ol>
</blockquote>
</aside>
<ol start="2">
<li>
<p>Far as  I   understand if you are referring to the model to model distance colour map it is in the what ever the units that your data is originally in.</p>
</li>
<li>
<p>I do not really understand. If the way i understand is correct, if you crop the models and then run the colour map you will see the colours in the exact area you want</p>
</li>
</ol>

---
