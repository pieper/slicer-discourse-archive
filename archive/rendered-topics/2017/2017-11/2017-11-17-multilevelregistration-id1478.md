# MultiLevelRegistration

**Topic ID**: 1478
**Date**: 2017-11-17
**URL**: https://discourse.slicer.org/t/multilevelregistration/1478

---

## Post #1 by @Marta_Pais (2017-11-17 02:52 UTC)

<p>Hi all,</p>
<p>I need to get Jaccard coefient between some structure sets and the only way i found out, using slicer, is using the MultiLevelRegistration  extension, but i can’t seem to find it on the Extension Manager.</p>
<p>I event tried to build slicer from source and then build the extension but i couldn’t get it going.</p>
<p>any help would be welcome.</p>

---

## Post #2 by @gcsharp (2017-11-17 13:56 UTC)

<p>Hi Marta,</p>
<p>The SlicerRT extension has a “Segment Comparison” tool.  Although this does not give Jaccard at this time, it does display True/False Positive/Negative fractions.  Jaccard can be computed from these.</p>
<p>Greg</p>

---
