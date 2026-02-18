# Maxilla segmentation - Ai driven?

**Topic ID**: 28556
**Date**: 2023-03-24
**URL**: https://discourse.slicer.org/t/maxilla-segmentation-ai-driven/28556

---

## Post #1 by @Gergo_Dr_Balazs (2023-03-24 09:52 UTC)

<p>Dear 3D Slicer Community,</p>
<p>I am writing to you with great admiration and respect for your hard work in creating such an amazing platform. I am a second-year orthodontic resident from Hungary with a strong interest in 3D planning.</p>
<p>As a part of my work, I spend a lot of time manually segmenting our CBCTs. Recently, I had the opportunity to try the trial version of Diagnocat’s AI segmentator system, and I was impressed with its efficiency. This experience has sparked my curiosity about AI-driven segmentation and deep learning machines.</p>
<p>Given the expertise of the 3D Slicer Community, I am reaching out to you for recommendations on dental CBCT segmentation, specifically for the maxilla and upper teeth. Our CBCTs are performed in a closed position, which makes it challenging - or rather time consuming - to separate the upper teeth from the lower ones.<br>
AMASSS seems to be a great tool in Slicer, but unfortunately, the prediction calculation is stuck at 0%. So my question would be:</p>
<p>-Could AMASSS get the job done?<br>
-If not, what alternative(s) would you recommend?</p>
<p>I appreciate your time and knowledge and look forward to your insights.</p>
<p>Best regards,<br>
Gergő Balázs</p>

---

## Post #2 by @Gergo_Dr_Balazs (2023-03-24 10:11 UTC)

<p>error message:<br>
Traceback (most recent call last):<br>
File “C:/Users/Gergő/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerAutomatedDentalTools/lib/Slicer-5.2/qt-scripted-modules/AMASSS.py”, line 827, in onProcessUpdate<br>
print(“CLI execution failed: \n \n” + errorText)<br>
TypeError: can only concatenate str (not “bytes”) to str</p>
<p>Laptop specifications:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Name</th>
<th>DESKTOP-11VTOLS</th>
</tr>
</thead>
<tbody>
<tr>
<td>Processor (CPU)</td>
<td>Intel(R) Core™ i7-9750H CPU @ 2.60GHz   2.59 GHz</td>
</tr>
<tr>
<td>Memory</td>
<td>16,0 GB</td>
</tr>
<tr>
<td>Storage</td>
<td>465 GB</td>
</tr>
<tr>
<td>Operating System</td>
<td>Microsoft Windows 11 Pro x64</td>
</tr>
</tbody>
</table>
</div><p>Slicer 5.2.2.</p>

---

## Post #3 by @lassoan (2023-03-27 03:05 UTC)

<p>We fixed most issues related to special characters but maybe some remained, so your username (“Gergő”) in the path might cause issues. I would recommend to try to install Slicer into a folder that only has ASCII characters in its name (e.g., “C:/tmp”). Maybe it will not solve the issue but at least we’ll see the actual error message.</p>
<p>Check if the error that you get is already reported (someone has problems with special characters, too) and add your comments/questions if you find a related report; or create a new issue if your problem seems different from all the other open issues.</p>
<p>Daniel Palkovics and Csaba Pinter are also working on dental segmentation tools - see their <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/TeethSegmentation/">project page</a> from the last project week. You may contact them for more information about their progress and if you can get access to their module.</p>

---

## Post #4 by @Gergo_Dr_Balazs (2023-03-29 08:24 UTC)

<p>Thank you for the fast response.<br>
After reinstalling Slicer in “C:\temp”, this is the error message that I encounter.</p>
<p>========= ERROR =========</p>
<p>CLI execution failed:</p>
<p>AMASSS_CLI standard error:</p>
<p>Traceback (most recent call last):<br>
File “C:\temp\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerAutomatedDentalTools\lib\Slicer-5.2\cli-modules\AMASSS_CLI.py”, line 1220, in <br>
main(args)<br>
File “C:\temp\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerAutomatedDentalTools\lib\Slicer-5.2\cli-modules\AMASSS_CLI.py”, line 801, in main<br>
convertdicom2nifti(args[‘input’])<br>
File “C:\temp\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerAutomatedDentalTools\lib\Slicer-5.2\cli-modules\AMASSS_CLI.py”, line 731, in convertdicom2nifti<br>
nifti_file = search(current_directory,‘nii.gz’)[‘nii.gz’][0]<br>
IndexError: list index out of range</p>

---

## Post #5 by @PalkoD (2023-03-30 15:36 UTC)

<p>Dear Gergő,</p>
<p>We are sort of in the same boat here. We have experience with a lot of different segmentation methods for teeth and maxilla, semi-automatic and AI as well.</p>
<p>In the segment editor region growing works very for bone and watershed works very well for teeth.</p>
<p>If you would like to discuss this more just PM me.<br>
Or come to the perio department at Semmelweis <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20">.</p>
<p>Cheers</p>
<p>Daniel Palkovics</p>

---

## Post #6 by @ladamus (2023-04-20 20:14 UTC)

<p>Dear Young Friends,</p>
<p>I have been segmenting both maxillae and mandibles for quite a few years. My personal experience is, that mandibles are easy due to their density and structure. Maxillae are tough because CBCT imaging tends to yield fairly low quality images, mostly due to the low doses that we use, but also due to the various artefact reduction algorithms used by the CBCT machines as well as the complex anatomy. So, basically, you get a good segmentation of a maxilla if you have very few artefacts and used a relatively higher dose for image acquisition. This unfortunately is not really ALARA, but will look a lot better. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>It is not really surprising that most tutorials and wonderful presentations show the mandible and not the maxilla.</p>
<p>As Dani mentioned, teeth are relatively easy with watershed…</p>
<p>I would be really interested in the project mentioned by Andris.</p>
<p>Best of luck,</p>
<p>Kind regards,</p>
<p>Adam</p>

---
