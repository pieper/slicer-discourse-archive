# mrc file- reading error 

**Topic ID**: 24952
**Date**: 2022-08-27
**URL**: https://discourse.slicer.org/t/mrc-file-reading-error/24952

---

## Post #1 by @deniseYR (2022-08-27 21:36 UTC)

<p>Hi all. I am trying to load 4 different volume files of some micro CT scans I did, but every time I try to open them in 3D slicer I get an error message that says the following:</p>
<p><strong>Error occurred while loading the selected files.</strong><br>
<strong>Click ‘Show details’ button and check the application log for more information</strong><br>
<strong>Error: Loading /Users/deniseyamhureramirez/Desktop/I2_Test_Tomo_AreaD_Recon.transformed.mrc - load failed.</strong></p>
<p>I have done this before with the same micro CT scanning and the files always work, but this last ones are not :(. The files were downloaded in the same way as the others from the box, and are saved as <strong>.transformed.mrc</strong> . They open fine in DragonFly, but not in Slicer, and I have tried in two different computers and the same error happens.<br>
Does anyone know what the problem may be?<br>
Thanks</p>

---

## Post #2 by @lassoan (2022-08-27 22:08 UTC)

<p>Please try to read the image using ITK-Python or SimpleITK. If loading fails then report the error to ITK developers on the <a href="https://discourse.itk.org/">ITK forum</a> (Slicer uses ITK for reading mrc files).</p>
<p>If ITK can read the file then please upload an example file somewhere (dropbox, onedrive, …) and post the link here so that we can have a look.</p>

---
