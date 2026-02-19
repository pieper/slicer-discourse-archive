---
topic_id: 22769
title: "Where Did My Saved Segments Go"
date: 2022-03-30
url: https://discourse.slicer.org/t/22769
---

# Where did my saved Segments  go 

**Topic ID**: 22769
**Date**: 2022-03-30
**URL**: https://discourse.slicer.org/t/where-did-my-saved-segments-go/22769

---

## Post #1 by @tcboyer (2022-03-30 23:45 UTC)

<p>I am a new user.  I created a sucessful segment using seeds.  I saves the files and also created an .obj file to import into ZBrush.<br>
The import worked except that the file I imported was just the secondary segment that is used to limit the segment I was creating<br>
I would like to go back to the saved SLICER file but I can’t find it or how to reload it.</p>

---

## Post #2 by @rbumm (2022-03-31 11:46 UTC)

<p>If you saved them - I would recommend restarting Slicer and just pressing the “Save” button again</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10a7fe961a84999658c168f45ddc6ea4c36bfb71.png" alt="image" data-base62-sha1="2nlz5QfTJe9GV8kFRxcc2iYwRrj" width="154" height="86"></p>
<p>to see - in the following dialog box- where your scene files are saved by default.</p>

---

## Post #3 by @tcboyer (2022-03-31 17:25 UTC)

<p>Thanks Rudolf    While waiting I kept poking around until I did find out how to relaod my saved segmented files.  I reloaded them and attempted again to save as an .obj file but this time deleting the file that “fences” the segement that I want to import.  When I go to Zbrush, the segement I am interested in is empty.   So my problem is, I create 2 segments in SEEDS, one to identify the areas that I want to capture and another to identify areas that are “out of bounds”,  How do I export only the segment that I am interestedin and not the “out of bounds”</p>

---

## Post #4 by @rbumm (2022-03-31 17:46 UTC)

<p>Please use the technique described in <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">Save segmentation directly to STL/OBJ</a>.</p>
<p>The function is included in the “Segment Editor”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b9c1665dcfdad154c1e49f2244df5748b72b57.png" data-download-href="/uploads/short-url/sDHtlxnvg5ym8ZiY3tBXUIYPhZB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b9c1665dcfdad154c1e49f2244df5748b72b57_2_690x362.png" alt="image" data-base62-sha1="sDHtlxnvg5ym8ZiY3tBXUIYPhZB" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b9c1665dcfdad154c1e49f2244df5748b72b57_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b9c1665dcfdad154c1e49f2244df5748b72b57.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b9c1665dcfdad154c1e49f2244df5748b72b57.png 2x" data-dominant-color="D3D4D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">766×402 38.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and you include/exclude visible segmentations:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2e30bc4f1e7a2770144ff2e25078350f59f6543.png" alt="image" data-base62-sha1="u5AIb2ARNCBTOIbt8zsFH9PKJrB" width="298" height="334"></p>
<p>so it would be recommended to make your “out of bounds” segmentation invisible in Slicer before exporting with the above checkbox checked.</p>

---
