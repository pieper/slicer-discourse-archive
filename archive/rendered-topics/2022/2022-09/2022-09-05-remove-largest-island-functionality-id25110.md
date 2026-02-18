# Remove largest island functionality?

**Topic ID**: 25110
**Date**: 2022-09-05
**URL**: https://discourse.slicer.org/t/remove-largest-island-functionality/25110

---

## Post #1 by @Mike_Flanigan (2022-09-05 22:47 UTC)

<p>Hi there,</p>
<p>Currently I’ve been working on automating a work flow in python that goes like the following:</p>
<ol>
<li>Load CT scans (as .tiffs)</li>
<li>Create a segmentation and threshold to identify air in the scans</li>
<li>Automate a mouse click in a known location and use the “Remove selected island” feature</li>
<li>Apply the “Keep largest island” feature</li>
<li>Calculate and report statistics</li>
</ol>
<p>This process is functional and working currently, but requires my scripts to run with the slicer gui open (as opposed to running with “–no-splash --no-main-window”) because step 3 mimics a mouse click.</p>
<p>I’m realizing now that step 3 is actually always removing the largest island, which leads to my question.</p>
<p>Is there a “Remove largest island” functionality to accompany the “Keep largest island” function? (I haven’t been able to find one unfortunately).</p>
<p>If there isn’t, is there a way to programmatically sort the islands in python and then delete the biggest manually?</p>
<p>Thanks in advance for any help!</p>

---

## Post #2 by @laurabc (2023-01-23 10:25 UTC)

<p>Hello, have you found a solution for this? I also need it, if you know how to do it I would appreciate some help <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @cpinter (2023-01-23 10:55 UTC)

<p>Copy segment A to B → Keep largest in A → Subtract A from B ?</p>

---
