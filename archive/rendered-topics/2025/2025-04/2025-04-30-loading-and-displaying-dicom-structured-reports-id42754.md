# Loading and displaying DICOM Structured Reports

**Topic ID**: 42754
**Date**: 2025-04-30
**URL**: https://discourse.slicer.org/t/loading-and-displaying-dicom-structured-reports/42754

---

## Post #1 by @DeepaKrishnaswamy (2025-04-30 23:52 UTC)

<p>Hi,</p>
<p>I have been working on some changes to the QuantitativeReporting plugin for loading DICOM Structured Reports. Currently, the extension supports the loading of measurements. Now, we can load and display bounding boxes, lines, and points. It would be great to get feedback on how I can improve the UI. For instance, I could include automatic jumping to a slice when a markup is clicked, or when an entry in the table is selected.</p>
<p>Here is a gif for loading and displaying a bounding box:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67eef1ccba6a0ed7e27d942b015354a0374f61ad.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c64358c7e6760f5b4d910a26249a00faa0aea396.jpeg" data-video-base62-sha1="ePr7aWITiuU7E3yD6jhcn2Lktml.mp4">
  </div><p></p>
<p>One for a point:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f27426cc91e126f8acec3b2b78a9faded328681e.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71da6cbe29ad3b861c804a663e33bc9a67d551c5.jpeg" data-video-base62-sha1="yAQoT2HcGDSNWA1SW8tSq747hxQ.mp4">
  </div><p></p>
<p>And another for lines:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e070ab3174d0bd5124719a403f221af24636b08.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/803786ba34598359fad3cc332c6703613cf5d040.jpeg" data-video-base62-sha1="b8gkrfZCOQ3LLpuwJqjKAs0uKUM.mp4">
  </div><p></p>
<p>Thank you!</p>
<p>Deepa</p>

---

## Post #2 by @pieper (2025-05-01 11:11 UTC)

<p>Hi Deepa - it’s great you are working on this.  My thought would be to have a custom module that’s specific to the concept of a report.  It looks like now the SR is being parsed and the data is extracted into markups and tables, but other than having them in the same subject hierachy study, the idea that they all came from the same report is somehow lost.  It’s possible in the markups module to jump the slices to markup control points, but it would be nice to centralize this for the specific task of reviewing a report or comparing multiple reports.</p>
<p>It would be intestesting to look as some of the use cases where there is a clinical intent behind the SRs, like in the older QIICR datasets where there were lesion annotations from multiple raters and you’d want ways to load multiple SRs and easily compare the data across raters (e.g. turn all markups for one rater on/off or make the markups from one report yellow and all the ones from a second report blue).</p>

---

## Post #3 by @fedorov (2025-05-09 15:54 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="2" data-topic="42754">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>other than having them in the same subject hierarchy study, the idea that they all came from the same report is somehow lost</p>
</blockquote>
</aside>
<p>Steve, I had similar thoughts when we reviewed this with Deepa, but how can this be remedied? Is there a concept in the subject hierarchy that would map to an SR series and could have those measurements as children? Or do we need to introduce a new node?</p>

---

## Post #4 by @pieper (2025-05-09 18:05 UTC)

<p>I think you can easily create a folder in the subject hiearchy that corresponds to a report (even named by SeriesDescription or other attributes) and put all the extracted markups inside that folder inside the dicom study.</p>

---

## Post #5 by @DeepaKrishnaswamy (2025-05-12 20:16 UTC)

<p>How about this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6823d9db64aae360ff1c1893691a63d1664762d7.png" data-download-href="/uploads/short-url/eRgsYuctdJTdSz0GwY8QGsocAh9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6823d9db64aae360ff1c1893691a63d1664762d7.png" alt="image" data-base62-sha1="eRgsYuctdJTdSz0GwY8QGsocAh9" width="523" height="302"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">523×302 20.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @fedorov (2025-05-12 20:21 UTC)

<p>For the actual implementation, we should probably use SeriesDescription content for the name of that folder.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> you are saying we should not create a dedicated MRML node that would correspond to the SR series containing those measurements, and folder is sufficient?</p>

---

## Post #7 by @pieper (2025-05-13 12:28 UTC)

<p><a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a> yes, that looks like what I had in mind.  I agree the name should come from the SeriesDescription.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> I think it depends on how sophisticated you intend to be.  The folder seems like enough just to keep things organized.  I think you should check if it handles things like hierarchical visibility control (can you click the <code>eye</code> on the folder and turn on/off all the markups in the folder? Maybe that needs to be explicitly programmed.). Also can you drag the folder to a view and have the markups show up only in that view?  I.e. so you can compare two SRs side by side.  These features would make them act more like segmentations.</p>
<p>Also do you want to create this kind of SR in Slicer or just consume existing ones?  If you want to create them then a custom module with custom nodes (probably scripted) would make sense.</p>

---

## Post #8 by @fedorov (2025-05-13 13:11 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="42754">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Also do you want to create this kind of SR in Slicer or just consume existing ones? If you want to create them then a custom module with custom nodes (probably scripted) would make sense.</p>
</blockquote>
</aside>
<p>At the moment, the only need we have is consuming existing ones.</p>

---

## Post #9 by @DeepaKrishnaswamy (2025-05-20 22:14 UTC)

<p>Here is a sample of what I have for the subject hierarchy:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04de92d28f5b026f4e78ca4c2b4bfb238bdb7638.png" data-download-href="/uploads/short-url/H4LPuGgl8fqLehIsbiXlcl63MI.png?dl=1" title="Screenshot 2025-05-20 at 6.11.36 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04de92d28f5b026f4e78ca4c2b4bfb238bdb7638.png" alt="Screenshot 2025-05-20 at 6.11.36 PM" data-base62-sha1="H4LPuGgl8fqLehIsbiXlcl63MI" width="571" height="339"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-05-20 at 6.11.36 PM</span><span class="informations">571×339 22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This approach works well if the SR has a referenced series. However, in the case of a SCOORD3D point where a FrameOfReferenceUID is used, I would need to come up with a nice way to name the folder.</p>

---

## Post #10 by @fedorov (2025-05-21 18:50 UTC)

<p>I would use SeriesDescription (or SeriesNumber:SeriesDescription) as the name for the folder - I believe this is what is done for other items in the hierarchy that match DICOM series.</p>

---
