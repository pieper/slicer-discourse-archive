# CLOSEDPLANAR_XOR visualization artefact with holes 2D

**Topic ID**: 43589
**Date**: 2025-07-03
**URL**: https://discourse.slicer.org/t/closedplanar-xor-visualization-artefact-with-holes-2d/43589

---

## Post #1 by @ferhue (2025-07-03 10:59 UTC)

<p>I have a 2D contour with a hole, that I am storing in an RTstruct as two contours of type CLOSEDPLANAR_XOR. The visualization looks weird in 3D Slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b34f20a5ced25d6ca7fbc66e1bb9ca2e50460a34.png" data-download-href="/uploads/short-url/pAeZP5wRBE5qdRRzotuOncZnyhS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b34f20a5ced25d6ca7fbc66e1bb9ca2e50460a34.png" alt="image" data-base62-sha1="pAeZP5wRBE5qdRRzotuOncZnyhS" width="481" height="317"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×423 33.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>whereas if I plot it in matplotlib, I do not see anything really weird with it. Contours are rather close, but not really touching.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/091c65739436ded73ee371dfbc3964448a6df263.png" data-download-href="/uploads/short-url/1iB8qQdJ3sMTYrIYHubYGX6fton.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/091c65739436ded73ee371dfbc3964448a6df263.png" alt="image" data-base62-sha1="1iB8qQdJ3sMTYrIYHubYGX6fton" width="414" height="306"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">552×409 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Question, is this a visualization bug in the 2D viewer? Or is something wrong with my pydicom script?</p>
<p>In particular:</p>
<pre><code class="lang-auto">[array([[253.625, 200.625],
        [254.125, 201.125],
        [257.   , 201.125],
        [257.75 , 201.125],
        [258.25 , 201.625],
        [258.25 , 202.5  ],
        [259.75 , 203.875],
        [260.25 , 204.375],
        [260.25 , 205.375],
        [260.75 , 205.75 ],
        [261.   , 206.25 ],
        [261.   , 207.25 ],
        [261.5  , 207.625],
        [262.   , 208.125],
        [262.   , 209.125],
        [262.   , 210.   ],
        [262.5  , 210.5  ],
        [263.   , 211.   ],
        [263.   , 211.875],
        [263.   , 212.875],
        [263.5  , 213.25 ],
        [264.   , 213.75 ],
        [264.   , 228.75 ],
        [264.   , 229.75 ],
        [263.5  , 230.125],
        [263.   , 230.625],
        [263.   , 232.5  ],
        [263.   , 233.5  ],
        [262.5  , 233.875],
        [262.   , 234.375],
        [262.   , 235.375],
        [262.   , 236.25 ],
        [261.5  , 236.75 ],
        [261.   , 237.25 ],
        [261.   , 238.125],
        [261.   , 239.125],
        [260.75 , 239.5  ],
        [260.25 , 240.   ],
        [260.25 , 241.   ],
        [259.75 , 241.375],
        [259.25 , 241.875],
        [259.25 , 242.875],
        [257.75 , 244.25 ],
        [257.25 , 244.75 ],
        [257.25 , 245.625],
        [256.   , 247.   ],
        [255.5  , 247.5  ],
        [255.5  , 248.5  ],
        [248.875, 255.   ],
        [248.5  , 255.5  ],
        [247.5  , 255.5  ],
        [246.125, 257.   ],
        [245.625, 257.25 ],
        [244.75 , 257.25 ],
        [243.25 , 258.75 ],
        [242.875, 259.25 ],
        [241.875, 259.25 ],
        [241.375, 259.75 ],
        [241.   , 260.25 ],
        [240.   , 260.25 ],
        [239.5  , 260.75 ],
        [239.125, 261.   ],
        [238.125, 261.   ],
        [237.25 , 261.   ],
        [236.75 , 261.5  ],
        [236.25 , 262.   ],
        [235.375, 262.   ],
        [234.375, 262.   ],
        [233.875, 262.5  ],
        [233.5  , 263.   ],
        [197.875, 263.   ],
        [196.875, 263.   ],
        [196.375, 262.5  ],
        [196.   , 262.   ],
        [195.   , 262.   ],
        [194.125, 262.   ],
        [193.625, 261.5  ],
        [193.125, 261.   ],
        [192.25 , 261.   ],
        [191.25 , 261.   ],
        [190.75 , 260.75 ],
        [190.375, 260.25 ],
        [189.375, 260.25 ],
        [188.5  , 260.25 ],
        [188.   , 259.75 ],
        [187.5  , 259.25 ],
        [186.625, 259.25 ],
        [186.125, 258.75 ],
        [185.625, 258.25 ],
        [184.75 , 258.25 ],
        [183.25 , 257.   ],
        [182.875, 256.5  ],
        [181.875, 256.5  ],
        [177.25 , 251.75 ],
        [176.75 , 251.25 ],
        [176.75 , 250.375],
        [175.375, 248.875],
        [174.875, 248.5  ],
        [174.875, 247.5  ],
        [174.375, 247.   ],
        [173.875, 246.625],
        [173.875, 245.625],
        [173.5  , 245.125],
        [173.   , 244.75 ],
        [173.   , 243.75 ],
        [173.   , 242.875],
        [172.5  , 242.375],
        [172.   , 241.875],
        [172.   , 241.   ],
        [172.   , 240.   ],
        [171.625, 239.5  ],
        [171.125, 239.125],
        [171.125, 228.75 ],
        [171.125, 227.875],
        [171.625, 227.375],
        [172.   , 226.875],
        [172.   , 226.   ],
        [172.   , 225.   ],
        [172.5  , 224.5  ],
        [173.   , 224.125],
        [173.   , 223.125],
        [173.   , 222.25 ],
        [173.5  , 221.75 ],
        [173.875, 221.25 ],
        [173.875, 220.375],
        [174.375, 219.875],
        [174.875, 219.375],
        [174.875, 218.5  ],
        [176.25 , 217.   ],
        [176.75 , 216.625],
        [176.75 , 215.625],
        [182.375, 210.   ],
        [182.875, 209.5  ],
        [183.75 , 209.5  ],
        [185.125, 208.125],
        [185.625, 207.625],
        [186.625, 207.625],
        [187.5  , 207.625],
        [188.   , 207.25 ],
        [188.5  , 206.75 ],
        [190.375, 206.75 ],
        [191.25 , 206.75 ],
        [191.75 , 206.25 ],
        [192.25 , 205.75 ],
        [194.125, 205.75 ],
        [195.   , 205.75 ],
        [195.5  , 205.375],
        [196.   , 204.875],
        [198.75 , 204.875],
        [199.75 , 204.875],
        [200.125, 204.375],
        [200.625, 203.875],
        [202.5  , 203.875],
        [203.5  , 203.875],
        [203.875, 203.5  ],
        [204.375, 203.   ],
        [207.25 , 203.   ],
        [208.125, 203.   ],
        [208.625, 202.5  ],
        [209.125, 202.   ],
        [211.875, 202.   ],
        [212.875, 202.   ],
        [213.25 , 201.625],
        [213.75 , 201.125],
        [218.5  , 201.125],
        [219.375, 201.125],
        [219.875, 200.625],
        [220.375, 200.125],
        [237.25 , 200.125],
        [238.125, 200.125],
        [238.625, 200.625],
        [239.125, 201.125],
        [241.   , 201.125],
        [241.875, 201.125],
        [242.375, 200.625],
        [242.875, 200.125],
        [252.25 , 200.125],
        [253.125, 200.125],
        [253.625, 200.625]], dtype=float32),
 array([[233.875, 202.5  ],
        [234.375, 203.   ],
        [237.25 , 203.   ],
        [238.125, 203.   ],
        [238.625, 203.5  ],
        [239.125, 203.875],
        [240.   , 203.875],
        [240.5  , 204.375],
        [241.   , 204.875],
        [241.875, 204.875],
        [247.5  , 210.5  ],
        [248.   , 211.   ],
        [248.   , 211.875],
        [248.5  , 212.375],
        [248.875, 212.875],
        [248.875, 213.75 ],
        [249.375, 214.25 ],
        [249.875, 214.75 ],
        [249.875, 217.5  ],
        [249.875, 218.5  ],
        [250.375, 218.875],
        [250.75 , 219.375],
        [250.75 , 223.125],
        [250.75 , 224.125],
        [250.375, 224.5  ],
        [249.875, 225.   ],
        [249.875, 227.875],
        [249.875, 228.75 ],
        [249.375, 229.25 ],
        [248.875, 229.75 ],
        [248.875, 231.625],
        [248.875, 232.5  ],
        [248.5  , 233.   ],
        [248.   , 233.5  ],
        [248.   , 234.375],
        [247.5  , 234.875],
        [247.   , 235.375],
        [247.   , 236.25 ],
        [236.75 , 246.625],
        [236.25 , 247.   ],
        [235.375, 247.   ],
        [234.875, 247.5  ],
        [234.375, 248.   ],
        [233.5  , 248.   ],
        [233.   , 248.5  ],
        [232.5  , 248.875],
        [229.75 , 248.875],
        [228.75 , 248.875],
        [228.25 , 249.375],
        [227.875, 249.875],
        [203.5  , 249.875],
        [202.5  , 249.875],
        [202.   , 249.375],
        [201.625, 248.875],
        [198.75 , 248.875],
        [197.875, 248.875],
        [197.375, 248.5  ],
        [196.875, 248.   ],
        [196.   , 248.   ],
        [195.   , 248.   ],
        [194.5  , 247.5  ],
        [194.125, 247.   ],
        [193.125, 247.   ],
        [192.625, 246.625],
        [192.25 , 246.125],
        [191.25 , 246.125],
        [187.5  , 242.375],
        [187.   , 241.875],
        [187.   , 241.   ],
        [186.625, 240.5  ],
        [186.125, 240.   ],
        [186.125, 239.125],
        [185.625, 238.625],
        [185.125, 238.125],
        [185.125, 235.375],
        [185.125, 234.375],
        [184.75 , 233.875],
        [184.25 , 233.5  ],
        [184.75 , 233.   ],
        [185.125, 232.5  ],
        [185.125, 229.75 ],
        [185.125, 228.75 ],
        [185.625, 228.25 ],
        [186.125, 227.875],
        [186.125, 226.875],
        [186.625, 226.375],
        [187.   , 226.   ],
        [187.   , 225.   ],
        [191.75 , 220.375],
        [192.25 , 219.875],
        [193.125, 219.875],
        [193.625, 219.375],
        [194.125, 218.875],
        [195.   , 218.875],
        [195.5  , 218.5  ],
        [196.   , 218.   ],
        [197.875, 218.   ],
        [198.75 , 218.   ],
        [199.25 , 217.5  ],
        [199.75 , 217.   ],
        [200.625, 217.   ],
        [201.625, 217.   ],
        [202.   , 216.625],
        [202.5  , 216.125],
        [204.375, 216.125],
        [205.375, 216.125],
        [205.75 , 215.625],
        [206.25 , 215.125],
        [207.25 , 215.125],
        [207.625, 214.75 ],
        [208.125, 214.25 ],
        [209.125, 214.25 ],
        [211.375, 211.875],
        [211.875, 211.375],
        [212.875, 211.375],
        [213.25 , 211.   ],
        [213.75 , 210.5  ],
        [214.75 , 210.5  ],
        [217.   , 208.125],
        [217.5  , 207.625],
        [218.5  , 207.625],
        [219.875, 206.25 ],
        [220.375, 205.75 ],
        [221.25 , 205.75 ],
        [221.75 , 205.375],
        [222.25 , 204.875],
        [223.125, 204.875],
        [223.625, 204.375],
        [224.125, 203.875],
        [225.   , 203.875],
        [225.5  , 203.5  ],
        [226.   , 203.   ],
        [228.75 , 203.   ],
        [229.75 , 203.   ],
        [230.125, 202.5  ],
        [230.625, 202.   ],
        [232.5  , 202.   ],
        [233.5  , 202.   ],
        [233.875, 202.5  ]], dtype=float32)]
</code></pre>
<p>See full files here, look at slice 26 and select just last ROI:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://consigna.uv.es/consigna/pub/Consigna?recoge:ca:5266_8206_2288_7250">
  <header class="source">
      <img src="https://consigna.uv.es/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://consigna.uv.es/consigna/pub/Consigna?recoge:ca:5266_8206_2288_7250" target="_blank" rel="noopener nofollow ugc">consigna.uv.es</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://consigna.uv.es/consigna/pub/Consigna?recoge:ca:5266_8206_2288_7250" target="_blank" rel="noopener nofollow ugc">Consigna UV - Arreplegant fitxer</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @ferhue (2025-07-03 11:09 UTC)

<p>I see an additional problem in the following slice (27). It seems it does not like a U shape and draw a line inbetween:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa5c594c65c2a48bb2ece446d6a928869cc27187.png" data-download-href="/uploads/short-url/zINdTfALt1pE1hgnmb06mhoH9IP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa5c594c65c2a48bb2ece446d6a928869cc27187.png" alt="image" data-base62-sha1="zINdTfALt1pE1hgnmb06mhoH9IP" width="448" height="320"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">598×427 30.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>fyi <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #3 by @ferhue (2025-07-03 12:11 UTC)

<p>I just checked, and there is no difference if I use CLOSED_PLANAR with the keyhole technique by hand, or CLOSEDPLANAR_XOR with different contours. Visualization artefact is the same.</p>

---

## Post #4 by @lassoan (2025-07-09 00:45 UTC)

<p>CLOSEDPLANAR_XOR was added to the standard very late (years after SlicerRT importer was developed), to deal with the issue that some software created self-intersecting or overlapping contours instead of following the DICOM standard. Primary goal of adding this option was to allow radiotherapy software to <em>reject</em> RTSTRUCT that used this non-conform interpretation. In SlicerRT we have not implemented this rejection of CLOSEDPLANAR_XOR contours yet.</p>
<p>Of course the alternative of rejection would be to implement support for it, for example by using <a href="https://github.com/AngusJohnson/Clipper2">Clipper2</a> to split the contours to a set of non-intersecting polygons before further processing.</p>
<p>However, I’m not sure if this is worth the effort. The entire idea of using planar contour sets for representing 3D shapes was not a good one even at the time of manual contouring, because this representation makes it very difficult to reconstruct a solid 3D shape. Nowadays most segmentations are done with AI (or at least AI support) and AI models create segmentations as binary labelmaps, which makes planar contour representation for storage an even worse idea, because it adds two complex, error-prone, lossy conversions (binary labalmap to planar contours + planar contours to binary labelmap) to the data flow.</p>

---

## Post #5 by @ferhue (2025-07-09 06:17 UTC)

<p>Thanks for the feedback.<br>
In this case the input data are closed contours from an already published dataset, which I cannot change.</p>
<p>Could you clarify what is the failure mechanism for slice 27 (the second picture with the U shape? Because in this case, the contour is simply closed, a U shape. Is it because first ot tries to reconstruct 3d, then gets confused because neighbor slices are non standard, and then backprojects to 2d with those issues? (Rather than just representing the original input 2d data in the 2d view, which would be faster and wouldn’t suffer from this artefact?</p>
<p>(I would be ok with the 3d view showing artefacts as long as the 2d view shows the original data without artefacts.)</p>

---

## Post #6 by @lassoan (2025-07-09 11:03 UTC)

<p>You can see the original planar contours if in Segmentations module you choose to display the planar contour or ribbon representation.</p>

---
