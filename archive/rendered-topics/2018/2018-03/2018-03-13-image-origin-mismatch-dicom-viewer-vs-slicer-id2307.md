# Image Origin mismatch: DICOM viewer vs. SLICER

**Topic ID**: 2307
**Date**: 2018-03-13
**URL**: https://discourse.slicer.org/t/image-origin-mismatch-dicom-viewer-vs-slicer/2307

---

## Post #1 by @dcantor (2018-03-13 21:34 UTC)

<p>Hi Slicers, I am writing a python script to convert from DICOM to NRRD so I am going through the different DICOM headers and I am calculating the Image Origin of my T2W volume.</p>
<p>After sorting the list of DICOM slices according to the projections in the slice direction (using ImageOrientationPatient and ImagePositionPatient) I get an order that I can verify with the SliceLocation header (So I know I have ordered them correctly to form a consistent volume).</p>
<p>So now, I take the ImagePositionPatient header of the first slice in the volume and I have<br>
[-57, -65, 24] which corresponds to the information I get for the first slice of the volume when I check with HOROS (So basically I confirm again that I have the correct order)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2163a151d6e28e5517cc85c5eead39f99eb1a3fe.jpeg" data-download-href="/uploads/short-url/4Lnddl12PljkCyltdpjrKBrWylw.jpg?dl=1" title="horos" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2163a151d6e28e5517cc85c5eead39f99eb1a3fe_2_690x298.jpg" alt="horos" data-base62-sha1="4Lnddl12PljkCyltdpjrKBrWylw" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2163a151d6e28e5517cc85c5eead39f99eb1a3fe_2_690x298.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2163a151d6e28e5517cc85c5eead39f99eb1a3fe_2_1035x447.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2163a151d6e28e5517cc85c5eead39f99eb1a3fe_2_1380x596.jpg 2x" data-dominant-color="9D9D9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">horos</span><span class="informations">1407×609 395 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However when I open the same DICOM volume in Slicer I get a slightly different Image Origin:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01a70935697a26373f7407da4a4d2e2aaeddc1b1.png" data-download-href="/uploads/short-url/eClITmdVVKzFU9BNqH5zNhPGed.png?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01a70935697a26373f7407da4a4d2e2aaeddc1b1_2_690x283.png" alt="slicer" data-base62-sha1="eClITmdVVKzFU9BNqH5zNhPGed" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01a70935697a26373f7407da4a4d2e2aaeddc1b1_2_690x283.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01a70935697a26373f7407da4a4d2e2aaeddc1b1_2_1035x424.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01a70935697a26373f7407da4a4d2e2aaeddc1b1_2_1380x566.png 2x" data-dominant-color="8D8C8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1392×571 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What is the reason for this?</p>
<p>I am not sure how slicer shows the Image Origin OR if I am correct in assuming it will coincide with the ImagePositionPatient of the “first” slice in the volume (as per the ordering method described here).</p>
<p>I appreciate any help!</p>
<p>Thanks,</p>
<p>Diego</p>
<p><strong>UPDATE</strong></p>
<p>I think I answered my own question. Notice the position of the sliders in the two tools. The first slide in HOURUS corresponds to the last slide in Slicer. I checked and the values actually match, so it is a matter of how I order the stack of slices. Horus orders the stack in the superior-&gt;inferior order where as slicer goes inferior-&gt;superior in the coronal slice.</p>
<p>Question 1: How is this decided?</p>
<p>Question 2: why do I get [57, 82, -27] in Slicer and I get  [<strong>-</strong> 57, <strong>-</strong> 82, 27] for the ImagePositionPatient header in the correct slice? (correct as in the matching the slice in both tools)</p>
<p>Is Slicer reporting the origin in RAS already?<br>
I would assume so but could anyone please confirm?</p>
<p>Thanks again,</p>
<p>Diego</p>

---

## Post #2 by @pieper (2018-03-14 19:54 UTC)

<aside class="quote no-group" data-username="dcantor" data-post="1" data-topic="2307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dcantor/48/782_2.png" class="avatar"> dcantor:</div>
<blockquote>
<p>Question 1: How is this decided?</p>
</blockquote>
</aside>
<p>Slicer delegates this to ITK.  As I recall depending on the method used to read it may enforce a right-handed orientation matrix so it may reorder the data to match.</p>
<aside class="quote no-group" data-username="dcantor" data-post="1" data-topic="2307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dcantor/48/782_2.png" class="avatar"> dcantor:</div>
<blockquote>
<p>Is Slicer reporting the origin in RAS already?</p>
</blockquote>
</aside>
<p>Yes, see: <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox">Coordinate systems - Slicer Wiki</a></p>

---

## Post #3 by @dcantor (2018-03-15 17:32 UTC)

<p>Hi Steve, there is a problem with the wiki page, cheers, Diego.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7763d1e3ac57bb56c019d1b97cfd45123005d688.png" data-download-href="/uploads/short-url/h2aGhXhENz7zqknfKblNVhFvfxm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7763d1e3ac57bb56c019d1b97cfd45123005d688_2_690x432.png" alt="image" data-base62-sha1="h2aGhXhENz7zqknfKblNVhFvfxm" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7763d1e3ac57bb56c019d1b97cfd45123005d688_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7763d1e3ac57bb56c019d1b97cfd45123005d688_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7763d1e3ac57bb56c019d1b97cfd45123005d688.png 2x" data-dominant-color="F3D5D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1047×657 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2018-03-15 20:38 UTC)

<p>Hi Diego - maybe try reloading?  It looks fine to me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36f7f1ab2a275343183841d026903ba174c74d3a.png" data-download-href="/uploads/short-url/7Qh03ToUQb7oit551441h5PfRHA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f7f1ab2a275343183841d026903ba174c74d3a_2_690x408.png" alt="image" data-base62-sha1="7Qh03ToUQb7oit551441h5PfRHA" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f7f1ab2a275343183841d026903ba174c74d3a_2_690x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f7f1ab2a275343183841d026903ba174c74d3a_2_1035x612.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36f7f1ab2a275343183841d026903ba174c74d3a.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1254×742 90.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2018-03-15 20:53 UTC)

<p>In general, slice indexes do not matter and may be quite random for certain imaging modalities and 4D sequences. So, most 3D software (which operates on reconstructed 3D volumes instead of just showing 2D image slices) do not keep track of which pixel generated from which combination of slices. If you need to find slice index corresponding to a coordinate then you have to go back to the Slicer DICOM database and search the slice based on image position patient and image orientation tags.</p>

---

## Post #6 by @dcantor (2018-03-15 21:30 UTC)

<p>Hi Steve, I checked again and it does work on Chrome but it shows those error messages on Firefox and Safari. My browsers are up to date (latest versions on OS X High Sierra).</p>

---

## Post #7 by @dcantor (2018-03-15 21:39 UTC)

<p>Hi Andras,</p>
<p>I am writing my own code to convert DICOM to NRRD, the question I have at hand right now is to generate the appropriate <strong>space dimensions</strong> tag in the NRRD header from the information contained in the <strong>Image OrientationPatient</strong> and <strong>ImagePositionPatient</strong> in DICOM.</p>
<p>I think I am almost done with this problem. I need to know what was the <em>first slice</em> in the DICOM series (and yes I can see that they are not ordered and the lexicographic order of the series does not guarantee the order in the volume). So I think I already solved it: I take the <strong>ImagePositionPatient</strong> of the <em>first slice</em> (after ordering the slices in space) as the value for the <strong>space dimensions</strong> NRRD header.</p>
<p>The second part of the question (which I believed Steve addressed) was the conversion from LPS to RAS, So I basically need to change the signs appropriately to reflect the origin in RAS coordinates.</p>
<p>I hope this makes sense. Is there anyone here with experience in this type of code? Who wrote it in ITK?</p>
<p>Thanks,</p>
<p>Diego</p>

---

## Post #8 by @lassoan (2018-03-15 21:57 UTC)

<aside class="quote no-group" data-username="dcantor" data-post="7" data-topic="2307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dcantor/48/782_2.png" class="avatar"> dcantor:</div>
<blockquote>
<p>I am writing my own code to convert DICOM to NRRD</p>
</blockquote>
</aside>
<p>Oh, no… Why would you even consider doing this? This is so much more complicated than you would think. So many people have spent years implementing the current DICOM image readers (ITK, vtkDICOM, GDCM, etc) and you can see that the results are still so much limited. Instead of starting from scratch with a DICOM image reader, it would make much more sense if you contributed to existing implementations with bugfixes or improvements.</p>

---

## Post #9 by @dcantor (2018-03-15 22:14 UTC)

<p>I am realizing that now. I don’t think it is complex <em>per se</em> but the problem is the many possible combinations and making sure your reader handles all the possible cases correctly. So it is <em>laborious</em> and you could say it’s almost <em>combinatorics</em> problem. <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=5" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>
<p>I wanted to avoid ITK compilation but I think it’s currently available as any other pip package in Python? so that would solve my problem.</p>

---

## Post #10 by @pieper (2018-03-15 22:27 UTC)

<p>Hi Diego -</p>
<p>Concerning the coordinate system web site, can you test again - I tried chrome, safari, firefox, (all on mac) and edge on windows and it looks fine.  There was a mathml problem a couple weeks ago but it should be fixed now.</p>
<p>Also following up on the ITK/Slicer etc DICOM reading, since there are so many possible ways to map DICOM data to things of interest in Slicer (not just image data, but reports, segmentations, transforms, etc) we have a Plugin mechanism were different readers can take responsibility for different data.</p>
<p>Within the ScalarVolume reader, we first use this consistency check code linked below and then provide the files to ITK pre-sorted (I don’t know if it is still the case but at one point ITK got the image origin from the first file in the list we provided).</p>
<p>-Steve</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/12806744fdf549f46b15be8d945f03cd06e7a580/Modules/Scripted/DICOMLib/DICOMUtils.py#L394-L496" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/12806744fdf549f46b15be8d945f03cd06e7a580/Modules/Scripted/DICOMLib/DICOMUtils.py#L394-L496" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/12806744fdf549f46b15be8d945f03cd06e7a580/Modules/Scripted/DICOMLib/DICOMUtils.py#L394-L496</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="394" style="counter-reset: li-counter 393 ;">
<li>def getSortedImageFiles(filePaths, epsilon=0.01):</li>
<li>""" Sort DICOM image files in increasing slice order (IS direction) corresponding to a series</li>
<li>
</li>
<li>    Use the first file to get the ImageOrientationPatient for the</li>
<li>    series and calculate the scan direction (assumed to be perpendicular</li>
<li>    to the acquisition plane)</li>
<li>
</li>
<li>    epsilon: Maximum difference in distance between slices to consider spacing uniform</li>
<li>"""</li>
<li>warningText = ''</li>
<li>if len(filePaths) == 0:</li>
<li>  return filePaths, [], warningText</li>
<li>
</li>
<li># Define DICOM tags used in this function</li>
<li>tags = {}</li>
<li>tags['position'] = "0020,0032"</li>
<li>tags['orientation'] = "0020,0037"</li>
<li>tags['numberOfFrames'] = "0028,0008"</li>
<li>tags['seriesUID'] = "0020,000E"</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/12806744fdf549f46b15be8d945f03cd06e7a580/Modules/Scripted/DICOMLib/DICOMUtils.py#L394-L496" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #11 by @dcantor (2018-03-15 22:31 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="2307">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>n the ScalarVolume reader, we first use this consistency check code linked below and then provide the files to ITK pre-sorted (I don’t know if it is still the case but at one point ITK got the image origin from the first file in the list we provided)</p>
</blockquote>
</aside>
<p>Thank you for the information Steve. I think I am going to try and read my DICOM series with ITK and save them as NRRD in ITK. I haven’t done it but I imagine this is pretty straightforward with an image reader and an image writer. Also, can you confirm that I don’t need to compile ITK with CMake as in preivous years but now I can just download the python wrapper as a pip package?</p>
<p>Thanks,</p>
<p>Diego</p>

---

## Post #12 by @pieper (2018-03-15 22:45 UTC)

<p>Yes, I believe now you can just use the pip installed ITK as in the example linked below.</p>
<p><a href="https://itk.org/ITKExamples/src/IO/GDCM/ReadDICOMSeriesAndWrite3DImage/Documentation.html" class="onebox" target="_blank">https://itk.org/ITKExamples/src/IO/GDCM/ReadDICOMSeriesAndWrite3DImage/Documentation.html</a></p>

---
