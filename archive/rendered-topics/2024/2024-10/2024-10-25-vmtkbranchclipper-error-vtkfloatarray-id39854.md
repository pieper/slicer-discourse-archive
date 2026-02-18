# vmtkbranchclipper error:vtkFloatArray

**Topic ID**: 39854
**Date**: 2024-10-25
**URL**: https://discourse.slicer.org/t/vmtkbranchclipper-error-vtkfloatarray/39854

---

## Post #1 by @SARA_DOSSENA (2024-10-25 03:28 UTC)

<p>Hi!<br>
I’m trying to follow the guide ‘Mapping and Patching’  on vmtk (<a href="http://www.vmtk.org/tutorials/MappingAndPatching.html" class="inline-onebox" rel="noopener nofollow ugc">Mapping and Patching | vmtk - the Vascular Modelling Toolkit</a>).<br>
When I run the the code 'vmtkbranchclipper -ifile aorta.vtp -centerlinesfile aorta_cl.vtp -groupidsarray GroupIds -radiusarray MaximumInscribedSphereRadius -blankingarray Blanking -ofile aorta_clipped.vtp` I recive this error<br>
‘ERROR: In …/Common/Core/vtkAOSDataArrayTemplate.txx, line 333<br>
vtkFloatArray (0x600002d9e3a0): Source array too small, requested tuple at index 96107, but there are only 96107 tuples in the array.’<br>
The command gives back a result, but I’m not sure that this problem doesn’t affect the next steps.<br>
I tried to ignore it but I couldn’t get results in the next steps.</p>
<p>Has anyone had the same problem? Thank you in advance<br>
Sara</p>

---
