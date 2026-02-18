# How to load AIM annotations on top of the scans?

**Topic ID**: 37361
**Date**: 2024-07-13
**URL**: https://discourse.slicer.org/t/how-to-load-aim-annotations-on-top-of-the-scans/37361

---

## Post #1 by @Neermita_B (2024-07-13 20:06 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.6.2<br>
Expected behavior: Quantitative Reporting should allow me to import AIM xml files<br>
Actual behavior: It does not allow me to do that.</p>

---

## Post #2 by @lassoan (2024-07-13 20:11 UTC)

<p>It would probably very easy to write an importer (a short Python script). What would you like to import and what would you like to generate from it?</p>

---

## Post #3 by @Neermita_B (2024-07-14 05:17 UTC)

<p>So, I have tumor segmentations of a patient saved as XML files. I also have the complete PET/CT scans of the same patient. I want to load them both together to see the mask created. I’m just not able to do that.<br>
I just started to use 3D Slicer, so I’m a complete beginner. I was watching some videos on how to load data, and I saw that you can load any data using the ADD DATA and ADD DICOM DATA too. If I select the directory(with all scans of a patient) using ADD DATA, all my file names are lost.<br>
Now concerning the annotations, I try to load the xml file and place it under the patient itself. There is an option to ‘export to dicom’ and when i do that, this comes up.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43c0de24782036f591cbc1c7eb2233b67746b619.png" data-download-href="/uploads/short-url/9FncSC1MwNgltwIWztJv627GtjH.png?dl=1" title="Screenshot (651)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43c0de24782036f591cbc1c7eb2233b67746b619_2_690x388.png" alt="Screenshot (651)" data-base62-sha1="9FncSC1MwNgltwIWztJv627GtjH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43c0de24782036f591cbc1c7eb2233b67746b619_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43c0de24782036f591cbc1c7eb2233b67746b619_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43c0de24782036f591cbc1c7eb2233b67746b619_2_1380x776.png 2x" data-dominant-color="9D9DAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (651)</span><span class="informations">1920×1080 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Question is, how do I view the file on the scans themselves?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ac1450363b4be1f2984734ace5447dce246d92a.jpeg" data-download-href="/uploads/short-url/hvWkqQWDK8AM8oHujyj6hWOQy0y.jpeg?dl=1" title="Screenshot (652)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ac1450363b4be1f2984734ace5447dce246d92a_2_690x388.jpeg" alt="Screenshot (652)" data-base62-sha1="hvWkqQWDK8AM8oHujyj6hWOQy0y" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ac1450363b4be1f2984734ace5447dce246d92a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ac1450363b4be1f2984734ace5447dce246d92a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ac1450363b4be1f2984734ace5447dce246d92a_2_1380x776.jpeg 2x" data-dominant-color="8C8C91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (652)</span><span class="informations">1920×1080 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Want to view AMC-003 (xml file)</p>
<p>Thank you for any help.</p>

---

## Post #4 by @lassoan (2024-07-14 13:54 UTC)

<p>AIM format has not been adopted by the medical imaging community. I am not aware of any software that supports it.</p>
<p>That said, since it is an XML-based format, which is human-readable, and it may still be possible to find some specifications online, it would be fairly straightforward to write an importer. If you have Python scripting experience (or willing to learn) then you can do it. You can use <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py">OsiriX ROI file importer</a> as an example, which creates a segmentation from a set of parallel contours.</p>
<p>If you don’t have Python scripting experience or you would rather not spend time with this then you can contact <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-partners">Slicer Commercial Partners</a> to develop it for you or you can try to hire a student or find someone in the Slicer community (by posting in the <a href="https://discourse.slicer.org/c/announcements/jobs/22">Jobs category</a>) to help.</p>

---

## Post #5 by @Neermita_B (2024-07-14 16:49 UTC)

<p>Hello. Thank you for the reply. I do have python experience. Seems like i’d have to work with a script then. The example is informative; I’ll try using it.<br>
Thanks once again!</p>

---

## Post #6 by @Neermita_B (2024-07-17 07:47 UTC)

<p>Hello. So i tried doing what you said. I wrote a script to extract the segmentations and converted them to nrrd format. One problem though which I tried solving using your answer here - <a href="https://discourse.slicer.org/t/how-to-find-the-image-match-between-the-external-reference-with-the-annotations-and-the-sequence-in-3dslicer/18145/4" class="inline-onebox">How to find the image match between the external reference with the annotations and the sequence in 3DSlicer? - #4 by lassoan</a><br>
The segmentation is in 2D (since I have only one AIM annotation XML file for a patient). So the doctor must’ve made a segmentation on one of the slices (123 here) and exported it if im not wrong. Now, I’m able to display the 2D segmentation on 3D slicer but the location is off. I tried using the header of just one dicom file (1-123 only) and this is what it gives</p>
<p>OrderedDict([(‘type’, ‘short’),<br>
(‘dimension’, 3),<br>
(‘space’, ‘left-posterior-superior’),<br>
(‘sizes’, array([512, 512,   1])),<br>
(‘space directions’,<br>
array([[0.53320312, 0.        , 0.        ],<br>
[0.        , 0.53320312, 0.        ],<br>
[0.        , 0.        , 1.        ]])),<br>
(‘kinds’, [‘domain’, ‘domain’, ‘domain’]),<br>
(‘endian’, ‘little’),<br>
(‘encoding’, ‘gzip’),<br>
(‘space origin’,<br>
array([-131.23339844, -274.73339844, -140.        ]))])<br>
when I try to enter these values as the header for the 2D image, it obviously throws an error. Could you please tell me how to fix this? what space variables should I put for the 2d segmentation so that it loads in the correct position? When I plot it using plt.imshow() over the scan, it is fine.<br>
Thank you.</p>

---

## Post #7 by @lassoan (2024-07-17 11:50 UTC)

<p>Do you know which slice was annotated?</p>
<p>How did you compute directions and origin from the DICOM file?</p>
<p>Did you compute the nrrd file voxels from polygon points?</p>

---

## Post #8 by @Neermita_B (2024-07-17 11:58 UTC)

<p>Yes, I know which slice was annotated. It was slice 123 (given in the AIM file).<br>
I made a new folder with only that dcm slice and loaded it in 3D Slicer. Downloaded that nrrd file and got the header.<br>
As for your last point, I didnt understand what you mean. Could you please explain what you mean by finding voxels from polygon points?<br>
Also the segmentation is just a 2D circle, not a polygon.</p>
<p>If i simply save the label maps file as nrrd, it doesn’t have any space or space direction keys from inspection. Thats why I tried using the same slice’s header to make it work.</p>
<p>Thank you.</p>

---

## Post #9 by @Neermita_B (2024-07-17 12:10 UTC)

<p>this was the function i created:</p>
<pre><code class="lang-auto">def create_label_map(annotations, image_shape):
    label_map = np.zeros(image_shape, dtype=np.short)
    label_value = 1  
    for center, radius in annotations:
        rr, cc = np.ogrid[:image_shape[0], :image_shape[1]]
        circle_mask = (rr - center[1]) ** 2 + (cc - center[0]) ** 2 &lt;= radius ** 2
        label_map[circle_mask] = label_value
        label_value += 1  
    return label_map
</code></pre>
<p>Center and radius are manually calculated. I have x1,y1, x2,y2 values.</p>

---

## Post #10 by @lassoan (2024-07-17 13:20 UTC)

<aside class="quote no-group" data-username="Neermita_B" data-post="8" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neermita_b/48/77307_2.png" class="avatar"> Neermita_B:</div>
<blockquote>
<p>I know which slice was annotated. It was slice 123 (given in the AIM file)</p>
</blockquote>
</aside>
<p>Slices are uniquely identified by SOPInstanceUID. Do you have that information? Relying on some index like <code>123</code> would be error-prone (it may look like an <code>Instance number (0020,0013)</code>, but it may be some index into an array, but we don’t know the frame order in that array).</p>
<p>Can you look up the SOPInstanceUID in your annotation file?</p>
<p>If yes, then you can find the corresponding frame and use the ImagePositionPatient, ImageOrientationPatient, PixelSpacing attribute to get the position and orientation of the slice.</p>
<p>To get the slice spacing (third spacing value), you need to find the two closest slices (based on analysis of ImagePositionPatient, ImageOrientationPatient tags in all frames). Alternatively, you can create a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-json-file-format-mrk-json">markups json file</a> that define the markups (ROI, plane, closed curve, …) in physical space.</p>

---

## Post #11 by @Neermita_B (2024-07-17 13:40 UTC)

<p>This is what I found</p>
<pre><code class="lang-auto">&lt;sopInstanceUid root="1.3.6.1.4.1.14519.5.2.1.4334.1501.553921625749272741224744327937"/&gt;
</code></pre>
<p>I theorised that this would likely be the slice number from here.</p>
<pre><code class="lang-auto">&lt;ImageAnnotation&gt;
&lt;uniqueIdentifier root="bh5cfg5vqmerg4db8coxnyhr05od845fsltt3gzb"/&gt;
&lt;typeCode code="LT1" codeSystem="Lung Template" codeSystemName="Lung Template"/&gt;
&lt;dateTime value="2014-09-03T18:07:05"/&gt;
&lt;name value="Lesion1"/&gt;
&lt;comment value="CT / THORAX LUNG 1MM / 123"/&gt;
</code></pre>
<p>and here</p>
<pre><code class="lang-auto">&lt;referencedFrameNumber value="123"/&gt;
</code></pre>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To get the slice spacing (third spacing value), you need to find the two closest slices (based on analysis of ImagePositionPatient, ImageOrientationPatient tags in all frames).</p>
</blockquote>
</aside>
<p>What would you mean by “closest?” Do you mean closest by value of both these parameters?<br>
And what should I do after finding them exactly?  Am I supposed to stack them and make a 3D volume nrrd file?</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Alternatively, you can create a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-json-file-format-mrk-json" rel="noopener nofollow ugc">markups json file</a> that define the markups (ROI, plane, closed curve, …) in physical space.</p>
</blockquote>
</aside>
<p>Okay, I shall try this out too!</p>
<p>Thank you.</p>

---

## Post #12 by @lassoan (2024-07-17 14:22 UTC)

<aside class="quote no-group" data-username="Neermita_B" data-post="11" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neermita_b/48/77307_2.png" class="avatar"> Neermita_B:</div>
<blockquote>
<p>This is what I found</p>
<pre><code class="lang-auto">&lt;sopInstanceUid root="1.3.6.1.4.1.14519.5.2.1.4334.1501.553921625749272741224744327937"/&gt;
</code></pre>
</blockquote>
</aside>
<p>This looks good, use this UID then. This uniquely identifies the frame.</p>
<aside class="quote no-group" data-username="Neermita_B" data-post="11" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neermita_b/48/77307_2.png" class="avatar"> Neermita_B:</div>
<blockquote>
<p>What would you mean by “closest?” Do you mean closest by value of both these parameters?<br>
And what should I do after finding them exactly? Am I supposed to stack them and make a 3D volume nrrd file?</p>
</blockquote>
</aside>
<p>Going from 2D to 3D in general is a very complex task, as it requires 3D reconstruction of a 3D image from 2D slices, when spacing between slices may be varying, slices may not even be parallel, and you can have many slices for the same position, potentially at multiple time points. However, if you only need to work with a specific data set and you know that slices are parallel and equally spaced throghout the entire series then it may be enough to find the slice in the image series that has the closest ImageOrientationPatient value, and use that distance as slice spacing.</p>
<p>You can also let Slicer do the 3D reconstruction and then create a segment using cylinder sources in physical space.</p>
<aside class="quote no-group" data-username="Neermita_B" data-post="9" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neermita_b/48/77307_2.png" class="avatar"> Neermita_B:</div>
<blockquote>
<p>this was the function i created:</p>
<pre><code class="lang-auto">def create_label_map(annotations, image_shape):
    label_map = np.zeros(image_shape, dtype=np.short)
    label_value = 1  
    for center, radius in annotations:
        rr, cc = np.ogrid[:image_shape[0], :image_shape[1]]
        circle_mask = (rr - center[1]) ** 2 + (cc - center[0]) ** 2 &lt;= radius ** 2
        label_map[circle_mask] = label_value
        label_value += 1  
    return label_map
</code></pre>
</blockquote>
</aside>
<p>This looks OK, if <code>center</code> and <code>radius</code> are specified in pixels and pixel spacing is the same along both axes.</p>

---

## Post #13 by @Neermita_B (2024-07-22 04:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This looks good, use this UID then. This uniquely identifies the frame.</p>
</blockquote>
</aside>
<p>Okay. I will.</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Going from 2D to 3D in general is a very complex task, as it requires 3D reconstruction of a 3D image from 2D slices, when spacing between slices may be varying, slices may not even be parallel, and you can have many slices for the same position, potentially at multiple time points. However, if you only need to work with a specific data set and you know that slices are parallel and equally spaced throghout the entire series then it may be enough to find the slice in the image series that has the closest ImageOrientationPatient value, and use that distance as slice spacing.</p>
</blockquote>
</aside>
<p>Ahh, I understand. I’ll try this. Hopefully it works!</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="37361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also let Slicer do the 3D reconstruction and then create a segment using cylinder sources in physical space.</p>
</blockquote>
</aside>
<p>My professor requires me to visualise already segmented lung areas so I don’t have to create one as of now.</p>
<p>Thank you so much for your time. Very grateful.</p>

---
