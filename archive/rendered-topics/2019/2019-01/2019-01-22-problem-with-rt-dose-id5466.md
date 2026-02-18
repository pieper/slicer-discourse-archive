# Problem with RT dose

**Topic ID**: 5466
**Date**: 2019-01-22
**URL**: https://discourse.slicer.org/t/problem-with-rt-dose/5466

---

## Post #1 by @Malamente (2019-01-22 14:49 UTC)

<p>Hi, I’m starting to use Slicer RT. The problem is that I have not found a manual to handle it. I’m using it thanks to my knowledge with Eclipse of Varian Eclipse but I have a problem when calculating the dose, I get the following error: “No study currentNode for reference dose” I think it has to do with the “<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff367396d36e9c053e87b21fd48585819b30d642.png" data-download-href="/uploads/short-url/ApIpQd7urYuADSFOP0iYSwbr1ke.png?dl=1" title="Captura%20de%20pantalla%20de%202019-01-22%2015%3A45%3A12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff367396d36e9c053e87b21fd48585819b30d642_2_690x497.png" alt="Captura%20de%20pantalla%20de%202019-01-22%2015%3A45%3A12" data-base62-sha1="ApIpQd7urYuADSFOP0iYSwbr1ke" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff367396d36e9c053e87b21fd48585819b30d642_2_690x497.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff367396d36e9c053e87b21fd48585819b30d642.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff367396d36e9c053e87b21fd48585819b30d642.png 2x" data-dominant-color="B0DDA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura%20de%20pantalla%20de%202019-01-22%2015%3A45%3A12</span><span class="informations">971×700 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> output dose volume” but I don’t know exactly what to do to fix it.</p>
<p>My steps are:</p>
<p>1- I download a sample image.<br>
2- I paint the volumes with the segment editor.<br>
3- I go to external beam planning and configure the beams.</p>
<p>That I have to do?<br>
I upload a screenshot with the error</p>
<p>Many thanks.</p>

---

## Post #2 by @lassoan (2019-01-31 02:07 UTC)

<p><a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> <a class="mention" href="/u/gcsharp">@gcsharp</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #3 by @PaoloZaffino (2019-02-01 10:24 UTC)

<p>Hi,<br>
did you try to set a new volume for output dose volume?</p>
<p>Paolo</p>

---

## Post #4 by @Malamente (2019-02-05 08:37 UTC)

<p>I solved the problem. The issue was that sample images are not DICOM images. Once I loaded DICOM images, the sofware works.</p>

---

## Post #5 by @cpinter (2019-02-05 15:20 UTC)

<p>Sorry I missed this thread. The difference between DICOM and non-DICOM images are the subject hierarchy. In order to use dose volumes you need a subject and a study in which the anatomy image and the dose volume are. You can do it in the Data module.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data#How_to" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data#How_to</a></p>

---

## Post #6 by @gcsharp (2019-02-05 17:54 UTC)

<p>Should we be creating these automatically?</p>

---

## Post #7 by @cpinter (2019-02-05 22:23 UTC)

<p>That’s an option but I feel it wouldn’t help things much.</p>
<p>If we add only the volume nodes automatically under a dummy patient and study, then it would be inconsistent.<br>
On the other hand if we add all node types automatically then it would be the same problem as now, namely that there would be no meaningful grouping of all the different nodes, but a flat list under a study that is in reality meaningless. I think it would be more confusing as the user could feel that all the nodes belond to a study somehow.</p>
<p>From the RT point of view: if you have a dose volume under the dummy study, then the dummy study would contain the dose unit and the dose grid scaling, which, when exporting, will be needed to be moved under a different study (that has a name, contains just the nodes that are needed, etc.), and the new study won’t contain the same information unless explicitly specified. I think it is a greater hurdle than the current one; to create a real study and use that from the beginning.</p>
<p>Also not sure how it would conflict with the assignment of subjects when loading DICOM (there are multiple plugins implemented by different people), however, I think this issue could be avoided if we’re careful.</p>

---

## Post #8 by @lassoan (2019-02-05 23:16 UTC)

<p>It could be possible to add some heuristics that would try to build the study automatically (and/or may ask for essential information from the user). It could be launched when the user wants to start computation and it is detected that the data is not under a study.</p>

---

## Post #9 by @cpinter (2019-02-05 23:19 UTC)

<p>Yes, creating an operation-specific dummy study at the time of not finding a study might be a viable solution.</p>

---
