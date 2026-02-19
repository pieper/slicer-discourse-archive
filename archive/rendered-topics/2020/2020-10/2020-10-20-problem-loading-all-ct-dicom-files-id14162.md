---
topic_id: 14162
title: "Problem Loading All Ct Dicom Files"
date: 2020-10-20
url: https://discourse.slicer.org/t/14162
---

# Problem loading ALL CT DICOM files

**Topic ID**: 14162
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/problem-loading-all-ct-dicom-files/14162

---

## Post #1 by @jonne (2020-10-20 14:12 UTC)

<p>I have a problem loading all DICOM files. My folder consist of MRI and CT images. Right now mainly interested in the CT images. The folder contains 205 CT images.<br>
In the DICOM database only 3 CT images are found. All the MRI images are found.<br>
What could be the problem? Thank you in advance!</p>

---

## Post #2 by @pieper (2020-10-20 14:47 UTC)

<p>Hi -</p>
<p>Can you try the steps described in the FAQ?<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" target="_blank" rel="noopener">Documentation/4.10/FAQ/DICOM - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jonne (2020-10-20 16:02 UTC)

<p>Hi Pieper,<br>
Thanks for responding. Right now it says the following:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64abaed0509b8d9dc448c4eba5271d0799804649.png" data-download-href="/uploads/short-url/emzzHIw74x5btUoMF8FRXpyFKn7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64abaed0509b8d9dc448c4eba5271d0799804649.png" alt="image" data-base62-sha1="emzzHIw74x5btUoMF8FRXpyFKn7" width="424" height="500" data-dominant-color="FDFDFD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">661×779 4.29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
So now nothing is importing… Instead of only a part. Not sure what happened. Happened after I used the drag and drop instead of loading via ‘Import DICOM files’, although I doubt that would be the problem.<br>
Can easily open/view the dicom files in Matlab or MicroDicom.</p>

---

## Post #4 by @lassoan (2020-10-20 16:14 UTC)

<p>Most likely the files cannot be accessed because they are in a special folder (e.g., network mapped or google cloud folder). There used to be issues with having international characters in the filenames, but that should not be a problem anymore (unless you are on an older Windows version). If you move it to a regular local folder then it should all work well.</p>
<p>If import still does not work then check if you see any error messages in the application log (menu: Help / Report a bug).</p>

---

## Post #6 by @jonne (2020-10-21 12:00 UTC)

<p>I found the problem. The folder consist of images 1 to 255 and 560 to 596, when I import it tries to read 256, 257 and so on and then crashes. I have now imported images 1 to 255 separately successfully. No idea how this problem could be solved without separating the data, but at least I can import my data separately now.</p>

---
