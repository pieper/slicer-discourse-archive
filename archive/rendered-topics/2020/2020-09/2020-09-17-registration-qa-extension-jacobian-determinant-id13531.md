# Registration QA extension, jacobian determinant

**Topic ID**: 13531
**Date**: 2020-09-17
**URL**: https://discourse.slicer.org/t/registration-qa-extension-jacobian-determinant/13531

---

## Post #1 by @Ana1890 (2020-09-17 18:27 UTC)

<p>Hi everyone! I’m using Registration QA to calculate the Jacobian Determinant, but I want to calculate this with several regions of interest (ROI), individually. At this moment I’m creating several files to do that, and I have to load the files each time, but I wonder if there is a way to do that in the same file, withouth close slicer and create a new window, thanks!</p>

---

## Post #2 by @labixin (2020-10-12 14:54 UTC)

<p>Hi,</p>
<p>I want to calculate the Jacobian Determinant within specific segment too. Could you tell me how to implement this? Where could I modify the source code?</p>
<p>Thanks a lot. Your help is highly appreciated!</p>
<p>Crayon</p>

---

## Post #3 by @Ana1890 (2020-11-12 06:01 UTC)

<p>Hi! sorry for the late response. To calculate the Jacobian Determinant around a specific segment I created a ROI around the volume or the zone that I needed to analize, you can create this ROI and assign it the role as ROI in Registration Quality Assurance module. On the other hand you can press the button ‘create a ROI around  segments’ , and the calculate jacobian determinant. Previusly you have to assign the role ‘countors’ to your volume of interest. Let me know if I’ve been clear, I’m Argentinian and nowaday I’m learning english haha.</p>
<p>Ana</p>

---

## Post #4 by @Young_Wang (2022-02-22 20:44 UTC)

<p><a class="mention" href="/u/labixin">@labixin</a> <a class="mention" href="/u/ana1890">@Ana1890</a> hi there. I’m trying to use the QA module to calculate the inverse consistency error after assigning the role. I still can’t get anything. Could you provide some help?</p>

---
