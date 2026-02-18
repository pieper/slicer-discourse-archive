# CLI module output image segmentation

**Topic ID**: 35797
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/cli-module-output-image-segmentation/35797

---

## Post #1 by @Franciska (2024-04-29 13:54 UTC)

<p>Hi!</p>
<p>I would like to create a custom module, just like the <a href="https://github.com/lassoan/SlicerPythonCLIExample?tab=readme-ov-file" rel="noopener nofollow ugc">BlurImage</a> example.</p>
<p>I put mine under Segmentation modules.<br>
When using the module, under the IO parameters I can chose Output Volume as creating a new volume, or creating a new LabelmapVolume.(and these work properly)</p>
<p>How could I chose to create a new segmentation?  I tried to find it <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel" rel="noopener nofollow ugc">here</a> but I didn’t.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2024-04-29 14:27 UTC)

<p>It is a bit hidden in the documentation, but the relevant part is this:</p>
<p>&lt;image [type=“<em>scalar</em> |<em>label</em> |<em>tensor</em> |<em>diffusion-weighted</em> |<em>vector</em> |<em>model</em> “] [reference=”…”]&gt;</p>
<p>If you want to select a segmentation node as input or output, you can specify <code>type="label"</code> for your image element in the .xml file. See example <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/LabelMapSmoothing/LabelMapSmoothing.xml">here</a>.</p>

---
