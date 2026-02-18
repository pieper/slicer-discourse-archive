# File export / saving trouble 

**Topic ID**: 11184
**Date**: 2020-04-19
**URL**: https://discourse.slicer.org/t/file-export-saving-trouble/11184

---

## Post #1 by @Allison_Brea (2020-04-19 02:27 UTC)

<p>Hi all,<br>
I have an annotated CT scan data set that I am having trouble saving on my Mac Book Pro laptop. I have tried to save the set several times changing the file format and saving it in many places on the computer but I keep getting the same error message that says: “Cannot write data file.” Does anyone have any suggestions as to how I can solve this issue?</p>

---

## Post #2 by @timeanddoctor (2020-04-19 05:45 UTC)

<p>Can you uploard the data and we could save in our computer to find whether the problems…</p>

---

## Post #3 by @Allison_Brea (2020-04-19 19:11 UTC)

<p>The files cannot be exported and uploaded because the computer “cannot write the data file.”</p>

---

## Post #4 by @lassoan (2020-04-19 20:39 UTC)

<p>Check that your Slicer temporary folder is writeable and has enough space. You can find the folder location in application settings (menu: Edit / Application settings).</p>

---

## Post #5 by @Allison_Brea (2020-04-19 23:07 UTC)

<p>Under application settings I only see temporary directory. I tried changing that to an empty folder on the computer as well as a flash drive but neither worked. I am still getting the same error message when I try to save. Is this what you mean by temporary folder?</p>

---

## Post #6 by @lassoan (2020-04-19 23:48 UTC)

<p>Do you have the problem with latest Slicer Preview Release as well? Can you copy her the complete path (folder and filename) of the file that you have set? Can you attach a screenshot?</p>

---

## Post #7 by @Allison_Brea (2020-04-20 15:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/824dab7c21f12be0d8fac2121286702de29874ee.png" data-download-href="/uploads/short-url/iAItDHXZ8Dh0RvPNVvAF9G6aCEm.png?dl=1" title="Screen Shot 2020-04-20 at 11.10.22 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824dab7c21f12be0d8fac2121286702de29874ee_2_690x152.png" alt="Screen Shot 2020-04-20 at 11.10.22 AM" data-base62-sha1="iAItDHXZ8Dh0RvPNVvAF9G6aCEm" width="690" height="152" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824dab7c21f12be0d8fac2121286702de29874ee_2_690x152.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824dab7c21f12be0d8fac2121286702de29874ee_2_1035x228.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824dab7c21f12be0d8fac2121286702de29874ee_2_1380x304.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-04-20 at 11.10.22 AM</span><span class="informations">2582×570 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Allison_Brea (2020-04-20 15:12 UTC)

<p>I am using slicer 4.10.2.  The file name it cannot read is in the screenshot above.</p>

---

## Post #9 by @lassoan (2020-04-20 15:21 UTC)

<p>How did you create “6th segmet” node? Maybe it cannot be saved because it is empty. Could you go to Volumes module, select this node, open the “Information” section and take a screeenshot? Is there any details about the error displayed in the application log (menu: Help / Report a bug)?</p>

---

## Post #10 by @Allison_Brea (2020-04-20 21:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35358d617e2568caa385bc467006ee7150639ba7.png" data-download-href="/uploads/short-url/7AI2y8YRrkouHt5FeLQCF04uLdR.png?dl=1" title="Screen Shot 2020-04-20 at 5.36.49 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35358d617e2568caa385bc467006ee7150639ba7_2_441x500.png" alt="Screen Shot 2020-04-20 at 5.36.49 PM" data-base62-sha1="7AI2y8YRrkouHt5FeLQCF04uLdR" width="441" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35358d617e2568caa385bc467006ee7150639ba7_2_441x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35358d617e2568caa385bc467006ee7150639ba7_2_661x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35358d617e2568caa385bc467006ee7150639ba7_2_882x1000.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-04-20 at 5.36.49 PM</span><span class="informations">1270×1438 94.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @Allison_Brea (2020-04-20 21:41 UTC)

<p>I do not know how to access the application log. What do I click to get there?</p>

---

## Post #12 by @lassoan (2020-04-21 00:27 UTC)

<p>The volume looks valid. Application log is available in menu: Help / Report a bug.</p>

---
