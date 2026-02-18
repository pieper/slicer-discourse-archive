# ROI registration not working

**Topic ID**: 10791
**Date**: 2020-03-23
**URL**: https://discourse.slicer.org/t/roi-registration-not-working/10791

---

## Post #1 by @wfurquim (2020-03-23 14:23 UTC)

<p>It is not possible to perform ROI registration since selection of landmarks does not work.<br>
Did anyone find a solution to this issue?</p>

---

## Post #2 by @lassoan (2020-03-23 14:39 UTC)

<p>There are several landmark registration modules available and you can also register segments (maybe you refer to that by ROI?). What would you like to achieve?</p>

---

## Post #3 by @wfurquim (2020-03-25 11:07 UTC)

<p>I need to superimpose two dental digital models by selecting landmarks in the palate and also including Regions of Interest around them. But as the “select landmark” tool does not work, applying radius and thus include ROI in the registration is not possible.<br>
I am using the extension CMF and Surface registration to do that.<br>
Is there another way?</p>

---

## Post #4 by @lassoan (2020-03-25 16:25 UTC)

<p>I don’t know CMF registration features - maybe <a class="mention" href="/u/bpaniagua">@bpaniagua</a> can help you with these.</p>
<p>However, you can use simple landmark registration using “Fiducial registration wizard” module in SlicerIGT extensions.</p>

---

## Post #5 by @wfurquim (2020-03-25 17:11 UTC)

<p>Yes, i have actually downloaded this extension as well. However, it does not allow us to perform ROI registration, which would add regions of interest to the desired landmarks.<br>
Thanks for all the help you can give.</p>

---

## Post #6 by @lassoan (2020-03-25 17:52 UTC)

<p>Yes, “Fiducial registration wizard” module only uses the landmark point positions.</p>

---

## Post #7 by @wfurquim (2020-03-25 18:17 UTC)

<p>Can <a class="mention" href="/u/bpaniagua">@bpaniagua</a> please help then?</p>

---

## Post #8 by @wfurquim (2020-03-26 10:39 UTC)

<p>Is it possible to download an older version of the software?<br>
Many published dental research mention the version 3.1 and the use of ROI registration.<br>
Maybe the tool “select landmark” worked just fine back then.<br>
Tks.</p>

---

## Post #9 by @lassoan (2020-03-26 13:37 UTC)

<p>You can download older releases from <a href="https://download.slicer.org/">https://download.slicer.org/</a>. Check out the “access older releases” and “Slicer3 download” links.</p>
<p>What is the name of the registration module that you have trouble with?</p>

---

## Post #10 by @wfurquim (2020-03-26 13:49 UTC)

<p>It has actually worked!!!<br>
The registration module is from extension “CMFreg”. Surface Registration - ROI registration.<br>
In version 5.0 the selection of landmarks works properly and thus ROI registration.</p>

---

## Post #11 by @wfurquim (2020-04-01 14:34 UTC)

<p>Hi.<br>
Do you know if there is a way a can get fiducials to follow a model when registration is performed? There are some landmarks that i need to place before performing the registration and these are both on the moving and the fixed model. But after registration the landmarks on the moving model do not follow it. Do you know if there is a way to fix that?<br>
Sincerely,<br>
Waleska</p>

---

## Post #12 by @muratmaga (2020-04-01 14:49 UTC)

<p>You may have to manually assign the landmarks to the resultant transform from the registration. You can use the <code>Transforms</code> module to do that.</p>

---

## Post #13 by @wfurquim (2020-04-02 12:26 UTC)

<p>That solved the problem. Thank you very much.</p>

---
