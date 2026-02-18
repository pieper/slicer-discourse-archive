# Transforming .json markups file

**Topic ID**: 30610
**Date**: 2023-07-14
**URL**: https://discourse.slicer.org/t/transforming-json-markups-file/30610

---

## Post #1 by @Sophrobs (2023-07-14 14:53 UTC)

<p>Operating system: MacOS Ventura 13.4.1<br>
Slicer version: 5.2.2<br>
Expected behavior: Save .json file with transform applied<br>
Actual behavior: Transform is not applied and markups are in the same position as the original file</p>
<p>I’m applying a transform in the ‘transforms’ module. Visually I can see that the markups move to the correct position. However, when I go to save or export the transformed file, the markups do not save in this transformed position. When I try to harden the transform it simply moves the markups back to the original spot.</p>

---

## Post #2 by @lassoan (2023-07-14 17:40 UTC)

<p>Two options to export markups with transformed coordinates:</p>
<ul>
<li>Option A: harden the transform on the markup (maybe you did not press the <code>harden</code> button but the green arrow button instead)</li>
<li>Option B: when you export the markup (by right-clicking on it in Data module) check the <code>Apply transforms</code> checkbox</li>
</ul>

---

## Post #3 by @Sophrobs (2023-07-16 03:15 UTC)

<p>Thank you for the prompt response Andras. I have tried both of your options but neither of them appear to work for me.<br>
Option A - when I click on the harden transform, the markups file moves from the ‘transformed’ section back into the ‘transformable’ section, as if I had clicked on the green arrow button.<br>
Option B - when I export the markup and select the apply transforms box it still saves in the original position…<br>
Can I provide you with any further information to help solve this issue?</p>

---

## Post #4 by @lassoan (2023-07-16 12:12 UTC)

<p>Please try with the latest Slicer Preview Release as well. If the behavior is still the same then share the scene (saved as a single .mrb file) so that we can investigate.</p>

---

## Post #5 by @Sophrobs (2023-07-16 23:10 UTC)

<p>Just tried the latest Slicer Preview Release and the behaviour is still the same.<br>
I can’t seem to attach the mrb file - what is the best way to send this to you?<br>
Once the matrix is applied, the markups should move closer to the model in the scene.</p>

---

## Post #6 by @muratmaga (2023-07-17 10:34 UTC)

<blockquote>
<p>Blockquote</p>
</blockquote>
<p>Not sure I understand this. If the points are under the transform and you hard it, you should see no displacement. They are already at the places that they are supposed to be and you are simply making this permanent by hardening the transform.</p>
<p>If you want to see the effect of the transform, take the points out of transform (which will bring them to their original positions they were created under) and the put them back in.</p>

---

## Post #7 by @Sophrobs (2023-07-17 13:57 UTC)

<p>Yes the transform function works correctly, but it seems I cannot harden the transform.<br>
When I try to harden the transform it does not work.</p>

---

## Post #8 by @muratmaga (2023-07-17 16:37 UTC)

<p>Sorry can’t replicate this on the preview on MacOS. See the screenshot, I created two points (red), cloned them (green), put the cloned ones under a transform that moved them some random place and then I hardened the transform. As you can see the points end it up in the modified spots. If the hardening didn’t work, they would have gone back on top of the red points.</p>
<p>So my guess you are either missing a step, or you have somewhat different expectation of what hardening does.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5949d169ae9088c1ad98f4ea01bb6a079299cbf8.png" data-download-href="/uploads/short-url/cJSEfHtCCLzvAsASGNHpPTXavIk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5949d169ae9088c1ad98f4ea01bb6a079299cbf8_2_690x411.png" alt="image" data-base62-sha1="cJSEfHtCCLzvAsASGNHpPTXavIk" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5949d169ae9088c1ad98f4ea01bb6a079299cbf8_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5949d169ae9088c1ad98f4ea01bb6a079299cbf8_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5949d169ae9088c1ad98f4ea01bb6a079299cbf8_2_1380x822.png 2x" data-dominant-color="C4C5DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1962×1170 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Sophrobs (2023-07-19 13:01 UTC)

<p>Thank you for your assistance.<br>
I have found a solution using the ‘split’ function on the transforms module.<br>
My .tfm file would apply the transform to the markups so that I could visualise the markups in the transformed orientation, but not export the .json file with the coordinates.<br>
After selecting the ‘split’ function and applying a single component of the transform (h5 file), the markups could be transformed, hardened and exported.</p>

---

## Post #10 by @lassoan (2023-07-19 15:56 UTC)

<p>It seems that something is wrong with the transform. Could you please share at least your transform file (but preferable the whole scene, saved as a single .mrb file)?</p>

---
