# Exporting values of "angle between two lines" (Q3DC) doesn't work

**Topic ID**: 11694
**Date**: 2020-05-25
**URL**: https://discourse.slicer.org/t/exporting-values-of-angle-between-two-lines-q3dc-doesnt-work/11694

---

## Post #1 by @Joao_L (2020-05-25 14:10 UTC)

<p>Operating system:<br>
Slicer version: 5.0<br>
Expected behavior: Exporting values of “angle between two lines” (Q3DC)<br>
Actual behavior: Hello. Hope you are fine.<br>
Two weeks ago I did export the values that I found by calculating the angles between the lines on Q3DC tool - it worked normally, creating a doc named “angle” with the measures. Now I’m trying to do exatcly the same process, but when I click the “export” buttom - after choosing the directory - nothing happens. I’ve tried several times, with no success. Can anyone picture anything I must be doing wrong that explains this?</p>

---

## Post #3 by @lassoan (2020-05-25 14:15 UTC)

<p>I think <a class="mention" href="/u/james_hoctor">@James_Hoctor</a> has been working on Q3DC in the past few days. Which Slicer version are you using?</p>
<p>Do you see any errors in the Python console?</p>

---

## Post #4 by @Joao_L (2020-05-25 14:30 UTC)

<p>Yes. James gave me the instructions to export the values one or two weeks ago and it worked normally. That’s why now I’m trying to do the same process, but it’s not working anymore.<br>
I am using Slicer 4.5.0. Actually, I did all the process on Slicer 4.10.2 and moved to Slicer 4.5.0 just to use the Q3DC tool because it wasn’t working in the other version.</p>
<p>Sorry, what does “python console” mean?</p>

---

## Post #5 by @lassoan (2020-05-25 14:50 UTC)

<aside class="quote no-group" data-username="Joao_L" data-post="4" data-topic="11694">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joao_l/48/6737_2.png" class="avatar"> Joao_L:</div>
<blockquote>
<p>Sorry, what does “python console” mean?</p>
</blockquote>
</aside>
<p>It is window where you can enter Python scripting commands and see script outputs. Hit <kbd>Ctrl/Cmd</kbd>+<kbd>3</kbd> to show it.</p>

---

## Post #6 by @Joao_L (2020-05-25 14:55 UTC)

<p>Right. This window opens but I never used.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c80b16b1093c1da3e4c180b7866d2dbfae0c4388.png" data-download-href="/uploads/short-url/sxFfAl2dqXdXHT4BNWNMmo6IDe8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c80b16b1093c1da3e4c180b7866d2dbfae0c4388_2_690x310.png" alt="image" data-base62-sha1="sxFfAl2dqXdXHT4BNWNMmo6IDe8" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c80b16b1093c1da3e4c180b7866d2dbfae0c4388_2_690x310.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c80b16b1093c1da3e4c180b7866d2dbfae0c4388_2_1035x465.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c80b16b1093c1da3e4c180b7866d2dbfae0c4388_2_1380x620.png 2x" data-dominant-color="CDC9D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×719 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2020-05-25 15:01 UTC)

<p>If you copy the entire content of the window to here then it’ll help <a class="mention" href="/u/james_hoctor">@James_Hoctor</a> to fix the issue. Today is a holiday in the US, so probably he won’t respond today.</p>

---

## Post #8 by @Joao_L (2020-05-25 15:04 UTC)

<p>Nice. I wait for his response. Thank you very much!<br>
Here it is:</p>
<p>Python 2.7.10 (default, Nov 12 2015, 13:07:50) [MSC v.1500 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote>
<p>-------Surface Registration Widget SetUp--------<br>
-------Fixed Model Change--------<br>
Model Radio change<br>
---------Moving Model Change----------<br>
Model Radio change<br>
Model Radio change<br>
------------Landmark scaled change-----------<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/CMFreg/lib/Slicer-4.5/qt-scripted-modules/SurfaceRegistration.py”, line 451, in onFixedLandmarksChanged<br>
self.onFixedModelRadio()<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/CMFreg/lib/Slicer-4.5/qt-scripted-modules/SurfaceRegistration.py”, line 475, in onFixedModelRadio<br>
self.UpdateInterface()<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/CMFreg/lib/Slicer-4.5/qt-scripted-modules/SurfaceRegistration.py”, line 265, in UpdateInterface<br>
self.logic.UpdateThreeDView(self.landmarkComboBox.currentText)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/CMFreg/lib/Slicer-4.5/qt-scripted-modules/SurfaceRegistration.py”, line 650, in UpdateThreeDView<br>
for key in landmarkDescription.iterkeys():<br>
AttributeError: ‘NoneType’ object has no attribute ‘iterkeys’<br>
Model Radio change<br>
adding observers removed!<br>
moving observers removed!<br>
moving observers removed!<br>
Model Radio change<br>
------------Landmark scaled change-----------<br>
Model Radio change<br>
------------Landmark scaled change-----------<br>
------------Landmark scaled change-----------<br>
-------Q3DC Widget Setup------<br>
enter Q3DC<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’<br>
Traceback (most recent call last):<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 477, in onExportAngleButton<br>
self.logic.exportationFunction(self.directoryExportAngle, self.computedAnglesList, ‘angle’)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1498, in exportationFunction<br>
self.exportAsCSV(fileName, listToExport, typeCalculation)<br>
File “C:/Users/u119987/AppData/Roaming/NA-MIC/Extensions-24735/Q3DC/lib/Slicer-4.5/qt-scripted-modules/Q3DC.py”, line 1504, in exportAsCSV<br>
file = open(filename, ‘w’)<br>
IOError: [Errno 2] No such file or directory: ‘C:/Users/u119987/STG-Business/Waleska Furquim - Pacientes Pesquisa Clear/Pesquisa Clear Final/Erro do M\xc3\xa9todo Final/Angular/A/angle.csv’</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #9 by @lassoan (2020-05-25 15:13 UTC)

<p>By the way, have you tried if Q3DC works in latest (today’s) Slicer Preview Release?</p>

---

## Post #10 by @Joao_L (2020-05-25 15:29 UTC)

<p>No. Wich version is this?<br>
I only worked with 4.5.0 and 4.10.2.</p>

---

## Post #11 by @lassoan (2020-05-25 15:32 UTC)

<p>Preview Release that you can download from <a href="https://download.slicer.org/">https://download.slicer.org/</a></p>

---

## Post #12 by @Joao_L (2020-05-25 15:34 UTC)

<p>No, I haven’t use it yet.<br>
I’ll check if our TI crew can install this in our system so I can try.</p>

---

## Post #13 by @lassoan (2020-05-25 15:56 UTC)

<p>Installation of Slicer-4.11 does not require administrator access. You can install it as a regular user.</p>

---

## Post #14 by @Joao_L (2020-05-25 19:29 UTC)

<p>Ok. I just installed the new version. Is the process to open a stl. archive different now? Because I click the archive but it doesn’t open.</p>

---

## Post #15 by @lassoan (2020-05-25 19:44 UTC)

<p>What do you mean by “stl. archive”? Model files stored as STL should open the same way as before. Make sure the folder you are trying to load from does not contain special characters (or you are running a recent version of Windows 10).</p>

---

## Post #16 by @Joao_L (2020-05-25 20:05 UTC)

<p>Actually I’m trying to open the exact same archives I’ve openned in the other versions - and from the same Windows PC (10).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87ae0e14002f84e0a3448b784821377da759e3a9.png" data-download-href="/uploads/short-url/jmhmUN23CviZJ8c6Zga4y2TAFD3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87ae0e14002f84e0a3448b784821377da759e3a9.png" alt="image" data-base62-sha1="jmhmUN23CviZJ8c6Zga4y2TAFD3" width="690" height="479" data-dominant-color="F5F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">696×484 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @lassoan (2020-05-25 20:14 UTC)

<p>Slicer-4.11 is updated to support international characters in file and folder names, but this requires recent Windows10 version. I’ve noticed that you have special character in your name and if you use it in your username on your computer (or you use other special characters in any of the parent folder or filenames) and your Windows10 is not recent enough then the file will not load.</p>
<p>You can find detailed explanation of why the file did not load in application log (menu: Help / Report a bug).</p>

---

## Post #18 by @Joao_L (2020-05-26 12:46 UTC)

<p>Good morning.<br>
Our Windows is the most actual.<br>
The error described in “python” was “the specified module could not be found”.<br>
Now I got it to load the file - after pasting it on desktop and trying to open it from there.</p>

---

## Post #19 by @James_Hoctor (2020-05-28 00:35 UTC)

<p>Hi <a class="mention" href="/u/joao_l">@Joao_L</a> ,</p>
<p>I apologize that I only got a chance to look at the error logs you posted today. Based on the logs you posted (thank you), and the fact that moving your issue was resolved by moving your data to your desktop, I believe that <a class="mention" href="/u/lassoan">@lassoan</a> is correct in identifying special characters as the issue. The latest Slicer (4.11) is the solution here, as he says.</p>

---

## Post #20 by @Joao_L (2020-05-28 13:38 UTC)

<p>Hi <a class="mention" href="/u/james_hoctor">@James_Hoctor</a>.<br>
No problem. Thank you very much for the support.</p>

---
