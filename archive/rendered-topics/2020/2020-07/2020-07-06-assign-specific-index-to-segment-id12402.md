---
topic_id: 12402
title: "Assign Specific Index To Segment"
date: 2020-07-06
url: https://discourse.slicer.org/t/12402
---

# Assign specific index to segment

**Topic ID**: 12402
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/assign-specific-index-to-segment/12402

---

## Post #1 by @pieper (2020-07-06 19:05 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, do we have a way to set a specific labelmap index number to a segment?  That is, we are trying to pass nrrd files to another program and want to use a convention something like 1-10 are various specific structures, 101-110 are corresponding structures but with necrosis.  For our purposes it would be helpful to be able to designate a preferred index value for a terminology entry.</p>

---

## Post #2 by @Sunderlandkyl (2020-07-06 19:16 UTC)

<p>vtkSegment::SetLabelValue(int) can be used to set a specific label value, however if the labelmap layers get “collapsed”, that value could change.</p>
<p>The label values could be populated from terminology, but it hasn’t been implemented yet. “Labelmap layer collapse” should also be updated to ensure that the label value isn’t changed if it is paired with some corresponding terminology.</p>

---

## Post #3 by @pieper (2020-07-06 20:05 UTC)

<p>Thanks Kyle, that makes sense.  I’ll see if we can switch over to using the coded concepts to convey the meaning rather than relying on an numbering scheme.</p>

---
