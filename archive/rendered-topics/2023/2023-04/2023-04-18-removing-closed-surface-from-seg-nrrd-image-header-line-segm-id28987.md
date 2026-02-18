# Removing "Closed Surface" from seg.nrrd image header Line: Segmentation_ContainedRepresentationNames

**Topic ID**: 28987
**Date**: 2023-04-18
**URL**: https://discourse.slicer.org/t/removing-closed-surface-from-seg-nrrd-image-header-line-segmentation-containedrepresentationnames/28987

---

## Post #1 by @Joshua_Binswanger (2023-04-18 15:56 UTC)

<p>Removing or giving the option to bypass “Closed Surface” Representation of Segmentations in the image header of seg.nrrd files on the line “Segmentation_ContainedRepresentationNames”</p>
<p>The Corresponding Line in the Header is:<br>
Segmentation_ContainedRepresentationNames:=Binary labelmap|Closed surface|</p>
<p>Like this if you save a file with Closed Surface Representation active, you can bypass them on loading it a new. If you can’t somtimes the file is impossible to load or takes a long time. this would allow for a workaround.</p>

---

## Post #2 by @pieper (2023-06-09 22:51 UTC)

<p>This has really bothered me too.  In fact, in my local build I have changed the code so that this flag is ignored.  We have discussed it at developer meetings but haven’t reached agreement yet on the best behavior.  I would prefer to disable this feature completely, but another option would be to provide a UI option to disable. it   Yet another option would be to put building of surface models in a separate, cancelable thread, like the legacy Model Maker so that the model building time won’t make the application hang.  Putting the lablemap to surface model converter in a separate thread (basically into a CLI) would also help the workflow for people who leave 3D on when editing in the Segment Editor and then get slow update times.</p>

---
