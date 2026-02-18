# "Adding data failed" Files edited with "Segment Editor" cannot be reopened

**Topic ID**: 37058
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/adding-data-failed-files-edited-with-segment-editor-cannot-be-reopened/37058

---

## Post #1 by @JSteinJ (2024-06-26 20:37 UTC)

<p>using slicer 5.6.2 on win11</p>
<p>we are segmenting a few hundred mri brain images.<br>
we have mri scans stored in .nii.gz format.<br>
we have segmentations stored in the same .nii.gz format.</p>
<p>now we are adding new features so we have to edit the segmentations.<br>
opening scans &amp; segmentations via drag and drop…<br>
scans as VOLUMES<br>
segmentations as SEGMENTATION</p>
<p>after editing (it is really cumbersome that Slicer doesn’t  remember the settings ;( )<br>
we save the new segmentation as .nrrd segmentations.</p>
<p>NOW! We reopen this .nrrd segmentations as VOLUMES and save the segmentations as .nii.gz again.<br>
That works in many cases, BUT there are lots of cases where we get an error:</p>
<p>Adding data failed<br>
Error occurred while loading the selected file<br>
Click “Show details” button to…</p>
<p>End the info of the “Show details” button is:<br>
Error: …file… - load failed.</p>
<p>Any idea how we can solve this problem???<br>
Thanks for your help.</p>

---

## Post #2 by @muratmaga (2024-06-26 22:02 UTC)

<p>Please use seg.nrrd format to keep your segmentations, if you want to avoid issues like this.</p>

---

## Post #3 by @lassoan (2024-06-27 03:23 UTC)

<aside class="quote no-group" data-username="JSteinJ" data-post="1" data-topic="37058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/779978/48.png" class="avatar"> JSteinJ:</div>
<blockquote>
<p>after editing (it is really cumbersome that Slicer doesn’t remember the settings</p>
</blockquote>
</aside>
<p>Slicer remembers the settings. If you can give more details about what details are not preserved then let us know.</p>
<aside class="quote no-group" data-username="JSteinJ" data-post="1" data-topic="37058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/779978/48.png" class="avatar"> JSteinJ:</div>
<blockquote>
<p>End the info of the “Show details” button is:<br>
Error: …file… - load failed.</p>
</blockquote>
</aside>
<p>If you provide more information (for example, an image that cannot be opened) then we can have a look. However, I agere with <a class="mention" href="/u/muratmaga">@muratmaga</a> - there is a good chance that the issues are due to that you are using NIFTI file format. NIFTI is not a general-purpose 3D image file format and it suffers from ambiguities and has serious limitations.</p>

---

## Post #4 by @JSteinJ (2024-06-27 05:16 UTC)

<p>thank you for your help…<br>
can you give me an address where I can show such files?<br>
This is multi-center machine learning data. So there are no .nrrd files.</p>
<p>Oh really?<br>
What I mean:<br>
when I do the next segmentation and I open the segmentation in the segment editor, for example the 3d view is inactive at the start… I would like to have it active…<br>
e.g. Paint tool:<br>
Diameter of paint tool is 3% I need 1%<br>
Sphere brush is inactive, I need it active…<br>
Editable intensity range is inactive… need it active…<br>
and so on… other tools as well.<br>
that would be really nice to have…</p>

---

## Post #5 by @muratmaga (2024-06-27 06:12 UTC)

<aside class="quote no-group" data-username="JSteinJ" data-post="4" data-topic="37058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/779978/48.png" class="avatar"> JSteinJ:</div>
<blockquote>
<p>can you give me an address where I can show such files?</p>
</blockquote>
</aside>
<p>You can post it on dropbox, google drive, onedrive publicly and share the link:</p>

---

## Post #6 by @JSteinJ (2024-06-28 08:23 UTC)

<p>here are links to 2 .nrrd files…<br>
in this case the files can be opened as .nrrd but not as volume<br>
 → cannot be stored as nifi then…</p>
<p>have to look for those that cannot be reopened in both ways… (perhaps they are redone meanwhile…)</p>

---

## Post #7 by @JSteinJ (2024-06-28 08:58 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1csCuW1BxtYbCovv3vTIABSkNJmwzcPwO%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1csCuW1BxtYbCovv3vTIABSkNJmwzcPwO%2Fview%3Fusp%3Ddrive_link&amp;ifkv=AS5LTAQewgpUtU9Msog0MQmbS7_RQJLYxoey8tJGFOdiAOomIjBA2CsA0fAtmEIPyVOZCmuiUugeiQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1963631806%3A1719565120926863&amp;ddm=0">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1csCuW1BxtYbCovv3vTIABSkNJmwzcPwO%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1csCuW1BxtYbCovv3vTIABSkNJmwzcPwO%2Fview%3Fusp%3Ddrive_link&amp;ifkv=AS5LTAQewgpUtU9Msog0MQmbS7_RQJLYxoey8tJGFOdiAOomIjBA2CsA0fAtmEIPyVOZCmuiUugeiQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1963631806%3A1719565120926863&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1csCuW1BxtYbCovv3vTIABSkNJmwzcPwO%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1csCuW1BxtYbCovv3vTIABSkNJmwzcPwO%2Fview%3Fusp%3Ddrive_link&amp;ifkv=AS5LTAQewgpUtU9Msog0MQmbS7_RQJLYxoey8tJGFOdiAOomIjBA2CsA0fAtmEIPyVOZCmuiUugeiQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S1963631806%3A1719565120926863&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1HySw-z6pydKf3aWcUer1KnA6nQIbpKZY%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1HySw-z6pydKf3aWcUer1KnA6nQIbpKZY%2Fview%3Fusp%3Ddrive_link&amp;ifkv=AS5LTAQoDlNOWTNgwOIL0oRQbhxmBod46P5fvaqxJKEMRzDCz0jOCkeFRJ4RSJpiO3RjgRpk_700vw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-2029062529%3A1719565124505591&amp;ddm=0">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1HySw-z6pydKf3aWcUer1KnA6nQIbpKZY%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1HySw-z6pydKf3aWcUer1KnA6nQIbpKZY%2Fview%3Fusp%3Ddrive_link&amp;ifkv=AS5LTAQoDlNOWTNgwOIL0oRQbhxmBod46P5fvaqxJKEMRzDCz0jOCkeFRJ4RSJpiO3RjgRpk_700vw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-2029062529%3A1719565124505591&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1HySw-z6pydKf3aWcUer1KnA6nQIbpKZY%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1HySw-z6pydKf3aWcUer1KnA6nQIbpKZY%2Fview%3Fusp%3Ddrive_link&amp;ifkv=AS5LTAQoDlNOWTNgwOIL0oRQbhxmBod46P5fvaqxJKEMRzDCz0jOCkeFRJ4RSJpiO3RjgRpk_700vw&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-2029062529%3A1719565124505591&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @JSteinJ (2024-06-28 09:00 UTC)

<p>?? no idea if it works…</p>

---

## Post #9 by @muratmaga (2024-06-28 14:06 UTC)

<aside class="quote no-group" data-username="JSteinJ" data-post="8" data-topic="37058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/779978/48.png" class="avatar"> JSteinJ:</div>
<blockquote>
<p>??</p>
</blockquote>
</aside>
<p>You did not publicly share.</p>

---

## Post #10 by @JSteinJ (2024-07-01 09:45 UTC)

<p><a href="https://drive.google.com/file/d/1HySw-z6pydKf3aWcUer1KnA6nQIbpKZY/view?usp=drive_link" class="inline-onebox" rel="noopener nofollow ugc">Training_226_seg.nii.nrrd - Google Drive</a>, <a href="https://drive.google.com/file/d/1csCuW1BxtYbCovv3vTIABSkNJmwzcPwO/view?usp=drive_link" class="inline-onebox" rel="noopener nofollow ugc">Training_201_seg.nii.gz.nrrd - Google Drive</a></p>
<p>so hope it works now…</p>

---

## Post #11 by @muratmaga (2024-07-01 14:54 UTC)

<p>I was able to open both files and load them as segmentations without any problem or error messages. I didn’t have to change anything or set any option. I can edit them as well.</p>
<p>What is the specific problem you are facing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe27825282240619cb76ee0ae1b6cb7b72fefcf7.jpeg" data-download-href="/uploads/short-url/AglVmOlJ1pqYI5KStfuqsfhhjNB.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe27825282240619cb76ee0ae1b6cb7b72fefcf7_2_690x345.jpeg" alt="image" data-base62-sha1="AglVmOlJ1pqYI5KStfuqsfhhjNB" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe27825282240619cb76ee0ae1b6cb7b72fefcf7_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe27825282240619cb76ee0ae1b6cb7b72fefcf7_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe27825282240619cb76ee0ae1b6cb7b72fefcf7_2_1380x690.jpeg 2x" data-dominant-color="A8A7AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×960 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @JSteinJ (2024-07-02 05:11 UTC)

<p>yes that is correct.<br>
the problem is: how to convert it into niftis again?<br>
when I want to store it as nifti, I have to open it as VOLUME and that doesn t work…<br>
is there a workaround?<br>
thanks…</p>
<p>(there just one or two that don t open as segmentation &amp; volume but thats not a problem to segment this number again… )</p>

---

## Post #13 by @muratmaga (2024-07-02 05:30 UTC)

<p>As we me</p>
<aside class="quote no-group" data-username="JSteinJ" data-post="12" data-topic="37058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/779978/48.png" class="avatar"> JSteinJ:</div>
<blockquote>
<p>when I want to store it as nifti,</p>
</blockquote>
</aside>
<p>As we mentioned before, you will run into issues if you try to save a segmentation file as a nifti and try to load it as a segmentation into Slicer. NIFTI format will not store all the necessary information (like segment names, colors etc), and Slicer will have trouble reading back as a segmentation.</p>
<p>If you <strong>must</strong> save a nifti for some reason, then first export your segmentaiton as a labelmap, then you can save it as nifti. However, you will loose things like segment names and colors. To avoid that you can also look into creating a custom color table.</p>

---

## Post #14 by @JSteinJ (2024-07-02 09:16 UTC)

<p>brilliant! segment names &amp; colors don t matter…<br>
thank you!</p>

---
