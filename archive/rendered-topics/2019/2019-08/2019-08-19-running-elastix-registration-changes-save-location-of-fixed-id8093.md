# Running Elastix registration changes save location of "fixed" and "moving" volumes

**Topic ID**: 8093
**Date**: 2019-08-19
**URL**: https://discourse.slicer.org/t/running-elastix-registration-changes-save-location-of-fixed-and-moving-volumes/8093

---

## Post #1 by @hbraunDSP (2019-08-19 16:25 UTC)

<p>Hi everyone,<br>
I’ve been using the Elastix extension for some registrations, and it’s been working great. However, after running Elastix the volumes I selected for the “fixed” and “moving” volumes are by default saved as metaImage (<code>*.mha</code>) files in the <code>[home]/AppData/Local/Temp/Slicer/Elastix/[datetime]/input/</code> directory. This behavior is unexpected and annoying: my data and slicer scene files are stored on a network drive in Nifti format, and I want to keep it that way.  The <code>...elastix/.../input/</code> directory is on my local machine, as it should be for speed. If I forget to change the volumes back to the original location, the MRML scene is broken when opening from any computer other than the one used to run the registration. On top of this, I don’t want to just overwrite the original Nifti files in case Slicer changed something (e.g. losing track of header data), so I have to re-add the files after completing registration.</p>
<p>Is this behavior necessary for some reason I haven’t thought of? Should I open an issue on <a href="https://github.com/lassoan/SlicerElastix/issues" rel="nofollow noopener">https://github.com/lassoan/SlicerElastix/issues</a> ? Is there a way to tell Slicer to keep the original image locations?</p>

---

## Post #2 by @lassoan (2019-08-21 16:40 UTC)

<p>Good point, we should indeed not change the default save location (it is an unintended side effect). Please enter a bug report in SlicerElastix issue tracker.</p>

---
