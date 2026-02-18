# Add unit to the fcsv header

**Topic ID**: 13716
**Date**: 2020-09-27
**URL**: https://discourse.slicer.org/t/add-unit-to-the-fcsv-header/13716

---

## Post #1 by @muratmaga (2020-09-27 04:13 UTC)

<p>While we complain that formats like OBJ and STL suffers from lack of explicit unit size description, a similar problem exists for fcsv and as mrk.json as far as I can tell. There is no field which tells what the reported units are in. It appears that changing the default unit to something like micron doesn’t seem to have an effect on the output. Is it always assumed that the values will be written as millimeters? Is this going to cause precision issues when units are more widely supported and used?</p>
<p>Should we consider adding a unit tag to outputs of markups for the sake of completeness?</p>

---

## Post #2 by @lassoan (2020-09-27 14:21 UTC)

<p>I agree, length unit must be saved into markups file.</p>
<p>I guess it is not as a big problem for markups as for images and meshes, because markups rarely interpreted on their own and so the unit can be taken from the associated input data.</p>
<p>I will add this to the json format, but I would not touch the fcsv export, as it could break existing parsers that just ignore the first N lines of the file.</p>

---

## Post #3 by @muratmaga (2020-09-27 16:11 UTC)

<p>Yes, I was worried about breaking the existing parsers, but we have done quite a bit of breaking free from previous versions (such as coordinate changes for models etc). Can’t we find a solution that will support the units in fcsv, at least going forward?</p>
<p>In my field it is actually the landmarks that will get published and distributed as part of the results. So the dependency of needing to have the original data to figure out the unit would be concerning…</p>

---

## Post #4 by @lassoan (2020-10-23 15:51 UTC)

<p>Added a ticket to make sure saving of “length” unit will get implemented: <a href="https://github.com/Slicer/Slicer/issues/5261">https://github.com/Slicer/Slicer/issues/5261</a></p>

---
