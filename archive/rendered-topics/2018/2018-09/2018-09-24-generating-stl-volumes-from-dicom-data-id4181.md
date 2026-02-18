# Generating STL volumes from DICOM data

**Topic ID**: 4181
**Date**: 2018-09-24
**URL**: https://discourse.slicer.org/t/generating-stl-volumes-from-dicom-data/4181

---

## Post #1 by @Deyline (2018-09-24 17:45 UTC)

<p>Hello Slicer wizards,</p>
<p>I’ve been using Slicer for the past days and I’ve been having some problems with generating volumes from the DICOM data that I have. I’ve been mainly following tutorials on youtube, but I can’t seem to figure out what I’m doing wrong.</p>
<p>Basically, I’m trying to generate a volume of an artery from an Angiography. However, every time I try generating the volume, I just get a “mess” with a lot of noise. The artery becomes sort of a “flat” thing, instead of a cylinder as it should be.</p>
<p>I’ll share a screenshot of what I’ve done (Yes, there are a lot of problems with what I’m doing, I’ve just done something quickly to illustrate the problem):</p>
            <div class="onebox imgur-album">
              <a href="https://imgur.com/a/5DODYGy" target="_blank" rel="noopener nofollow ugc">
                <span class="outer-box" style="width:600px">
                  <span class="inner-box">
                    <span class="album-title">[Album] imgur.com</span>
                  </span>
                </span>
                <img src="https://i.imgur.com/u5Kzs7g.png?fb" title="imgur.com" height="315" width="600">
              </a>
            </div>

<p>What I’ve noticed is that the Y and G views are just a “small window”, rather than a “full window” like the R view. In the tutorials that I’ve been watching, all the 3 views have full windows, like the R view in this case. Does this has anything to do with the problem that I’m having?</p>

---

## Post #2 by @lassoan (2018-09-24 18:11 UTC)

<p>The DICOM series that you loaded contained a secondary capture (screenshot) image, not a 3D volume. You cannot create 3D models from such series.</p>
<p>It is possible that the series also has volumetric data stored in private tags, but those fields may not be accessible to third-party software, such as Slicer.</p>
<p>What device did you use to acquire the data?<br>
Did you tried to load the rotational angio series (sequence of 2D frames) or the reconstructed 3D volume?<br>
Do you have an option to export the 3D volume as a series of CT modality?</p>

---

## Post #3 by @Deyline (2018-09-26 01:55 UTC)

<p>Thanks for the reply!</p>
<p>As for the questions you’ve made, I’m not really sure how to answer, since I’m not from a medical field<br>
<img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"><br>
All that I know is that I got the images directly from a physician, who did the CT scans. From all the images I have available, I have two modalities - OT and XA (not even sure what is the difference). I’m not sure what kind of different data I could have from the scan, that I would be able to generate the volumes in Slicer.<br>
Long story short, I’m very lost not only with Slicer, but also with the medical data, as I’m from an engineering field. What kind of data should I be looking for?</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2018-09-26 05:20 UTC)

<p>XA modality refers to X-ray angiography image sequence. It consists of a series of 2D projection images. If images are acquired while the gantry was rotating then you can probably use the vendor’s software to reconstruct a 3D volume and save it as DICOM. This reconstructed volume may be loadable into Slicer.</p>
<p>OT means other, non-imaging data (maybe dose report?), probably not relevant for you.</p>

---

## Post #5 by @Deyline (2018-09-27 11:14 UTC)

<p>I see, thanks for the info!</p>

---
