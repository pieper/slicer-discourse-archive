---
topic_id: 36684
title: "Unicodedecodeerror When Running Dentalsegmentator"
date: 2024-06-09
url: https://discourse.slicer.org/t/36684
---

# UnicodeDecodeError when running DentalSegmentator

**Topic ID**: 36684
**Date**: 2024-06-09
**URL**: https://discourse.slicer.org/t/unicodedecodeerror-when-running-dentalsegmentator/36684

---

## Post #1 by @viet_duc_Vu (2024-06-09 08:30 UTC)

<p>Thank you. Recently I use this extension in other computer. But when running it I have a problem when the error was informed that <code>Check the inference folder content C:\Temp\Slicer-igReWK\output</code>  .This below is my python console. Hope you guys can help me to figure out<br>
Traceback (most recent call last):<br>
File “C:\Users\顎口腔変形\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-05\slicer.org\Extensions-32893\NNUNet\lib\Slicer-5.7\qt-scripted-modules\SlicerNNUNetLib\SegmentationLogic.py”, line 277, in _onReadyRead<br>
self._report(self.process.readAll(), self.readInfo)<br>
File “C:\Users\顎口腔変形\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-05\slicer.org\Extensions-32893\NNUNet\lib\Slicer-5.7\qt-scripted-modules\SlicerNNUNetLib\SegmentationLogic.py”, line 284, in _report<br>
info = bytes(stream.data()).decode()<br>
UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0x8a in position 53: invalid start byte<br>
Traceback (most recent call last):<br>
File “C:\Users\顎口腔変形\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-05\slicer.org\Extensions-32893\NNUNet\lib\Slicer-5.7\qt-scripted-modules\SlicerNNUNetLib\SegmentationLogic.py”, line 277, in _onReadyRead<br>
self._report(self.process.readAll(), self.readInfo)<br>
File “C:\Users\顎口腔変形\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-05\slicer.org\Extensions-32893\NNUNet\lib\Slicer-5.7\qt-scripted-modules\SlicerNNUNetLib\SegmentationLogic.py”, line 284, in _report<br>
info = bytes(stream.data()).decode()<br>
UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0x8a in position 65: invalid start byte<br>
Traceback (most recent call last):<br>
File “C:\Users\顎口腔変形\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-05\slicer.org\Extensions-32893\NNUNet\lib\Slicer-5.7\qt-scripted-modules\SlicerNNUNetLib\SegmentationLogic.py”, line 277, in _onReadyRead<br>
self._report(self.process.readAll(), self.readInfo)<br>
File “C:\Users\顎口腔変形\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-05\slicer.org\Extensions-32893\NNUNet\lib\Slicer-5.7\qt-scripted-modules\SlicerNNUNetLib\SegmentationLogic.py”, line 284, in _report<br>
info = bytes(stream.data()).decode()<br>
UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0x8a in position 87: invalid start byte<br>
[Python] Failed to load the segmentation.<br>
[Python] Check the inference folder content C:\Temp\Slicer-igReWK\output</p>

---
