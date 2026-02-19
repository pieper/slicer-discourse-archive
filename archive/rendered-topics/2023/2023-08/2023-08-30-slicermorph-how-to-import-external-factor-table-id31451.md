---
topic_id: 31451
title: "Slicermorph How To Import External Factor Table"
date: 2023-08-30
url: https://discourse.slicer.org/t/31451
---

# Slicermorph - How to import external factor table

**Topic ID**: 31451
**Date**: 2023-08-30
**URL**: https://discourse.slicer.org/t/slicermorph-how-to-import-external-factor-table/31451

---

## Post #1 by @Ale (2023-08-30 18:49 UTC)

<p>Hi all, I’m using the GPA module of Slicermorph to visualize shape change in a PCA plot. Is the a way to build externally and import a table with different factors for use with the GPA plot options? I imported a tsv table into Slicer but I cant make GPA use it for color the PCA points.<br>
Cheers,</p>
<p>Ale</p>

---

## Post #2 by @muratmaga (2023-08-30 19:52 UTC)

<p>No unfortunately, not at the moment. And that’s mostly due to the difficulty in making sure that IDs match (typos, missing characters, encoding, ordering sort of thing) correctly.</p>
<p>But you can go to the factors in GPA module, create a blank factor and copy and paste from the table to inserted into Slicer. Again be careful about that the ordering is the same.</p>

---
