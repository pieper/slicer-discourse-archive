# Can't load one of volumes into neither elastic nor BRAINS registration

**Topic ID**: 14417
**Date**: 2020-11-04
**URL**: https://discourse.slicer.org/t/cant-load-one-of-volumes-into-neither-elastic-nor-brains-registration/14417

---

## Post #1 by @l.znaniecki (2020-11-04 05:55 UTC)

<p>HI,</p>
<p>Slicer 4.11.0 form 12.9.2020</p>
<p>Module: elastics / BRAINS registration.</p>
<p>I have two series from the same examination (contrast &amp; non-contrast) as two volumes.<br>
The problem is - in both registration modules the non-contrast serie doesn’t show up on the list of volumes.<br>
What do I do wrong?</p>
<p>Regards &amp; thank you for help.<br>
Łukasz</p>

---

## Post #2 by @l.znaniecki (2020-11-04 06:27 UTC)

<p>I have also updated to the latest Slicer 4.11 30.9.2020, no success.</p>
<p>Please help.</p>
<p>Lukasz</p>

---

## Post #3 by @lassoan (2020-11-04 14:39 UTC)

<p>Most likely it is a vector volume (either it is a time sequence or an RGB volume).</p>
<p>Does it show up in Volumes module? In Volume information section, what are the values of “Volume type” and “Number of Scalars”?</p>
<p>Where does that series come from? Did you import it from DICOM?</p>

---
