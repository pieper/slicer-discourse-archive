# Determining Modifier labels and what gets a unique identifier

**Topic ID**: 29192
**Date**: 2023-04-28
**URL**: https://discourse.slicer.org/t/determining-modifier-labels-and-what-gets-a-unique-identifier/29192

---

## Post #1 by @egrace479 (2023-04-28 17:21 UTC)

<p>Background: I’m following the segment-context-schema.json (as demonstrated in the slicer docs on GitHub) to programmatically generate new JSON files from CSVs following that schema so we can import them into slicer (specifically to use with SlicerMorph).<br>
My question pertains to the “Modifier” of a “Type”. I see “CodeMeaning”: “Right”, “Left”, and “Right and Left” as per the “SCT” designator, but there’s some inconsistency with how that’s applied in generating a “3dSlicerIntegerLabel”. For some Types, all three modifiers are generated, but the unique identifier remains with the Type. However, it is mostly both the “Right” and “Left” that each get a “3dSlicerIntegerLabel” (while the parent Type does not). I did not see any cases in the example where the “Right and Left” modifier had a unique ID. How is this determined? My assumption would be that the “Right and Left” modifier would apply to a fused bone, in which case, why is it listed under all “paired” Types, even when they cannot be fused (as with the right and left scapula)?<br>
To the point of determining the Modifier labels, what is the distinction between “paired”: “U” and “N”? I see “paired”: “U” appear, but if not paired, the term doesn’t appear.<br>
Thanks!</p>

---

## Post #2 by @lassoan (2023-05-10 05:01 UTC)

<p>3dSlicerIntegerLabel is only informational (not used by the software), for cross-referencing the terms with Slicer GenericAnatomyColors table. It is not used by the software, you can ignore it.</p>
<p>The terms were specified as part of the QIICR project by <a class="mention" href="/u/fedorov">@fedorov</a> et al., maybe he can explain some of these nuances around modifiers.</p>

---
