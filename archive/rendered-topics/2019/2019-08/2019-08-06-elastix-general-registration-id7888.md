# Elastix general registration

**Topic ID**: 7888
**Date**: 2019-08-06
**URL**: https://discourse.slicer.org/t/elastix-general-registration/7888

---

## Post #1 by @Melanie (2019-08-06 02:22 UTC)

<p>Hi</p>
<p>In elastix general registration mask volume option doesn’t allow me to select anything. It jus give the option none.</p>
<p>I created a mask beforehand and then selected my fixed and moving volumes,</p>
<p>Can someone help please</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-08-06 03:07 UTC)

<p>Do you have labelmap volumes in the scene?</p>

---

## Post #3 by @Melanie (2019-08-06 03:29 UTC)

<p>Yes I do. I tried creating the mask with segment editor and then reading the clip with model module I did that also. So I had many label maps created but they don’t show up in the drop down. ( they do show up in data module)</p>
<p>Thanks a lot</p>

---

## Post #4 by @lassoan (2019-08-06 03:57 UTC)

<p>Have you chosen “Fill inside and outside” option and “(Create new labelmap volume)”<br>
output volume before clicking “Apply”? If you choose the mask volume in Volumes module, what is the value of “Volume type” in “Volume information” section?</p>

---

## Post #5 by @Melanie (2019-08-07 17:38 UTC)

<p>Thank you ever so much <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I had made the mask with clip volume with model; module. It did not work.</p>
<p>But when I did with segment editor it works.</p>
<p>Thanks a lot</p>

---
