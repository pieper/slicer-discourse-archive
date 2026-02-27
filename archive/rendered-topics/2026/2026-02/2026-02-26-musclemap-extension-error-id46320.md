---
topic_id: 46320
title: "Musclemap Extension Error"
date: 2026-02-26
url: https://discourse.slicer.org/t/46320
---

# MuscleMap Extension Error

**Topic ID**: 46320
**Date**: 2026-02-26
**URL**: https://discourse.slicer.org/t/musclemap-extension-error/46320

---

## Post #1 by @MaxVs (2026-02-26 22:12 UTC)

<p>Hi Guys!<br>
I’ve recently downloaded a new extension built to segment muscles from multiple types of data. Unfortunatelly I haven’t managed to run it succesfully with GPU. CPU works perfectly fine. The authors can’t repeat this error to make some investigation, whats the cause of this issue.<br>
And the issue is:<br>
“Segmentation completed” but model is not rendered.</p>
<p>Bug details below:</p>
<p><a href="https://github.com/user-attachments/files/25457652/Slicer_5.11.0-2026-02-04_34418_20260215_190811_656.1.log" rel="noopener nofollow ugc">Slicer_5.11.0-2026-02-04_34418_20260215_190811_656 (1).log</a></p>
<p><a href="https://private-user-images.githubusercontent.com/200133193/553005200-5c137100-5766-4bff-b702-15c01685f51b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIxNDM4NzYsIm5iZiI6MTc3MjE0MzU3NiwicGF0aCI6Ii8yMDAxMzMxOTMvNTUzMDA1MjAwLTVjMTM3MTAwLTU3NjYtNGJmZi1iNzAyLTE1YzAxNjg1ZjUxYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyNlQyMjA2MTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zNjY5MTY3MzAxMGU2NzVjNDMyMTRkZjYyMzZjZTU0MzZmMzA2MmRiNzRjMDIyYTI5ZGNlOTQ4NWY2NTZmYzRiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.iXerZAFJ1U0oafk9r75qqI-VQpbiknZ5bA7uOjPErgY" rel="noopener nofollow ugc"><img src="https://private-user-images.githubusercontent.com/200133193/553005200-5c137100-5766-4bff-b702-15c01685f51b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIxNDM4NzYsIm5iZiI6MTc3MjE0MzU3NiwicGF0aCI6Ii8yMDAxMzMxOTMvNTUzMDA1MjAwLTVjMTM3MTAwLTU3NjYtNGJmZi1iNzAyLTE1YzAxNjg1ZjUxYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyNlQyMjA2MTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zNjY5MTY3MzAxMGU2NzVjNDMyMTRkZjYyMzZjZTU0MzZmMzA2MmRiNzRjMDIyYTI5ZGNlOTQ4NWY2NTZmYzRiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.iXerZAFJ1U0oafk9r75qqI-VQpbiknZ5bA7uOjPErgY" alt="Image" width="690" height="407"></a></p>
<p>More details:<br>
[Python] get_frame_offsets is deprecated and will be removed in v4.0<br>
[VTK] Warning: In vtkSlicerTerminologiesModuleLogic.cxx, line 3370<br>
[VTK] vtkSlicerTerminologiesModuleLogic (000001F3E0BDDDF0): LoadAnatomicContextFromFile is deprecated. Use LoadRegionContextFromFile instead.<br>
[Qt] QPixmap::scaleWidth: Pixmap is a null pixmap<br>
[Python] [MuscleMap] Could not apply JSON-based ColorTable: ‘MRMLCorePython.vtkMRMLLabelMapVolumeDisplayNode’ object has no attribute ‘SetInterpolate’<br>
[VTK] GetColor: requested color entry -1039 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] Warning: In vtkSlicerSegmentationsModuleLogic.cxx, line 1519<br>
[VTK] vtkMRMLSegmentationNode (000001F3E34612F0): vtkSlicerSegmentationsModuleLogic::ImportLabelmapToSegmentationNode: Segmentation is a floating point scalar type and will be cast to an integer type. Voxel values may be truncated<br>
[VTK] GetColor: requested color entry -1037 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1036 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1034 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1033 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1032 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1030 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1029 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1027 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1026 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1024 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.<br>
[VTK] GetColor: requested color entry -1023 is out of table range: 0 - 8162, call SetNumberOfColors to change the color table size.</p>
<p>It seems like something crash during interpolate, maybe there is some “CUDA OUT OF MEMORY” error because I can see how GPU rises to 100% memory for a while during processing and then drops down to 0%. A few seconds later segmentation appears but in this pixel-thing form.<br>
I’ve restarted multiple times multiple versions of Slicer starting from 5.4.0 to the newest. None of them are willing to work on GPU.</p>
<p>Does anyone have the same problem, or had and got up with the solution ??</p>
<p>Best regards<br>
Bartek</p>

---
