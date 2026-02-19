---
topic_id: 28942
title: "Printing Dicom Files"
date: 2023-04-16
url: https://discourse.slicer.org/t/28942
---

# Printing dicom files

**Topic ID**: 28942
**Date**: 2023-04-16
**URL**: https://discourse.slicer.org/t/printing-dicom-files/28942

---

## Post #1 by @mmasoudsf (2023-04-16 18:36 UTC)

<p>I think printing dicom files on radiology films and normal paper would be a big advantageous for Slicer3D.</p>

---

## Post #2 by @lassoan (2023-04-16 20:42 UTC)

<p>Printing, transferring, archiving of films is so much more expensive, slower, and less convenient than fully digital solutions that I would find it hard to justify investing any efforts into it.</p>
<p>Can you write a bit more about your workflow - what kind of images are still printed and for what purpose?</p>

---

## Post #3 by @mmasoudsf (2023-04-17 05:08 UTC)

<p>I think all the regions in the world do not use digital solutions of medical imaging yet for some reasons such as the low-speed Internet connection. Hence, despite the great advantages of digital imaging and sharing, printing on a radiology film or even on a normal paper is still a widely used way to share the images.</p>

---

## Post #4 by @pieper (2023-04-17 16:18 UTC)

<p>That’s a good observation and it sounds good to support it somehow.  I haven’t worked with medical film printers in a very long time. In your experience do people use dicom printing?  If so perhaps this tool is helpful and someone might make a hook to use it from Slicer:</p>
<p><a href="https://support.dcmtk.org/docs-products/tcpprt.html" class="onebox" target="_blank" rel="noopener">https://support.dcmtk.org/docs-products/tcpprt.html</a></p>
<p>Or if it’s paper I guess someone could add something to print using these services.</p>
<p><a href="https://doc.qt.io/qt-5/qtprintsupport-index.html" class="onebox" target="_blank" rel="noopener">https://doc.qt.io/qt-5/qtprintsupport-index.html</a></p>
<p>Of course you can also do a screen capture into a document or right click on a view and select Copy image from the context menu and paste in a document.</p>

---

## Post #5 by @mmasoudsf (2023-04-17 19:19 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I checked the links and there are seemingly some codes available here and there for dicom printing. Hence, if someone knows the back-end code of slicer3d, this might not be so time-consuming. According to my experience, dicom printing on radiology films is still used (mainly in dental imaging). But paper printing is more common in radiology of other organs.</p>

---

## Post #6 by @pieper (2023-04-17 19:24 UTC)

<p>Thanks for the extra info.  I agree that it shouldn’t be a huge task, so maybe a student could take it on as a project.  Ideally it would be done in collaboration with clinical users who have a specific need in mind and could test it out.</p>

---

## Post #7 by @pearsonm (2023-04-18 23:02 UTC)

<p>The free PACS <a href="https://ingenium.home.xs4all.nl/dicom.html" rel="noopener nofollow ugc">Conquest</a> is able to print to both DICOM and paper printers so you could process the files in Slicer and then send as DICOM to Conquest for printing. There are many options in Conquest for automatic processing of incoming files.</p>

---

## Post #8 by @lassoan (2023-04-20 01:51 UTC)

<p>Good point, you can just right-click on a patient/study/series and send it to conquest for automatic printing.</p>
<p>However, I’m wondering if printing images might be just an old habit. A good quality print costs much more than a CD or DVD (and even a USB stick) and a printer (even just a regular printer) costs much more than a DVD writer, and a printout only captures a small fraction of the information content. All you need is any Windows computer (even a 10-year-old laptop should suffice) because a DICOM viewer is always included on the DICOM CD/DVD. Cost of such a computer is maybe $200-300 which should be a negligible cost for a medical practice.</p>
<p>We need more information about why people still consider medical image printing as a need and see if those needs can be satisfied with more modern solutions.</p>

---

## Post #9 by @mmasoudsf (2023-04-20 04:12 UTC)

<p><a class="mention" href="/u/pearsonm">@pearsonm</a> Thanks for the suggestion. I’ve never worked with this PACS before but will try it.</p>

---
