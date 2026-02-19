---
topic_id: 13567
title: "Problems With Load Data From A Directory"
date: 2020-09-19
url: https://discourse.slicer.org/t/13567
---

# Problems with Load Data from a directory

**Topic ID**: 13567
**Date**: 2020-09-19
**URL**: https://discourse.slicer.org/t/problems-with-load-data-from-a-directory/13567

---

## Post #1 by @lars12345 (2020-09-19 14:46 UTC)

<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.10.2<br>
Expected behavior:The red slider scrolls through the images<br>
Actual behavior: Adjusting the red slider does nothing</p>
<p>First of all thank you for your help, I am probably missing something basic. Here are the steps I am following:</p>
<ol>
<li>Open up 3D slicer.</li>
<li>Click on the Load Data button.</li>
<li>Click on the Choose Directory to Add button.</li>
<li>Browse out to my directory and click on the Choose button.</li>
<li>Click Ok on the Add data into the scene dialog. I then temporarily see a Loading progress bar.</li>
<li>I then see an overlay with the name of the 10th image file, along with with part of the 10th image in the red slider panel.</li>
<li>If I drag the red slider, the image draws centered once and then nothing changes no matter how much I drag the slider.</li>
</ol>
<p>Additional note: The png files are 14 bits deep and of size 1104 x 1104. They open normally in Windows Paint. The associated calibration factor (sCAL) is 0.37u/p. The images were captured by a Cellomics CX7.</p>
<p>Thanks,</p>
<p>Lars</p>

---

## Post #2 by @lassoan (2020-09-19 14:51 UTC)

<p>If you uncheck “Single file” option and file names are similar then Slicer will load the entire image stack. See detailed instructions here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-a-series-of-png-jpeg-or-tiff-images-as-volume">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-a-series-of-png-jpeg-or-tiff-images-as-volume</a></p>

---

## Post #3 by @pieper (2020-09-19 14:55 UTC)

<p>You might also want to try the ImageStacks module from SlicerMorph:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/ImageStacks/ImageStacks.md" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/ImageStacks/ImageStacks.md" target="_blank" rel="noopener">SlicerMorph/S_2020/blob/master/Day_1/ImageStacks/ImageStacks.md</a></h4>
<pre><code class="lang-md">## ImageStacks
This is a SlicerMorph specific utility to import non-DICOM image sequences (TIF/PNG/JPG/BMP) into 3D Slicer. It provides additional features such as only loading a subset of the data, downsampling (by factor of 2), skipping slice(s) along the Z plane, and reverse the stack order. You can also specify the voxel spacing for your dataset at the import time. `ImageStacks` always produces a ScalarVolume (single channel), so that volumes can be immediately visualized or can be processed with `Segment Editor`.

To use the `ImageStacks`, first download &lt;a href="https://app.box.com/s/zvs162oja7tzszesmygnqs15t631y15m/file/701646040827" target="_blank"&gt; Sample_microCT_stack.zip&lt;/A&gt;, and unzip to a location. 

Then find the `ImageStacks` under SlicerMorph menu folder and:

1. Click the **Browse Files** button and select all *PNG* files in the folder you just unzipped.

&lt;img src="ImageStacks1.png"&gt;

2. Image spacing in this dataset is provided in the accompanying left_side_damaged__rec.log file as 35.28 micron. Enter this value in millimeters as 0.03528 for all three axes
3. You leave the **Output Volume** blank, which will use the filename prefix. Or you can choose to create a new volume name. 
4. Click **Load Files** and see that all three slices viewers contain our data.
5. To visualize what the specimen looks like, go to `Data` module and right-click just to the right of the eye button and then choose 'Show 3D views as Volume Rendering'. (Note: We will cover `Volume Rendering` module in great detail tomorrow. For the time being, this is all you need)

&lt;img src="Data_Volume_Rendering.png"&gt;

Notice that the resultant rendering show the damage to the zygomatic arch in the **right side** of the specimen. Curiously, the specimen is named **Left side damaged**. 

</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/ImageStacks/ImageStacks.md" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2020-09-19 14:57 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> could you add a note about imagestacks module to the readthedocs page?</p>

---

## Post #5 by @pieper (2020-09-19 15:07 UTC)

<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5191/files" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5191" target="_blank" rel="noopener">DOC: add ImageStacks information to volume docs</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>Slicer:add-imagestacks-doc</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-09-19" data-time="15:07:07" data-timezone="UTC">03:07PM - 19 Sep 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars0.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 3 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5191/files" target="_blank" rel="noopener">
          <span class="added">+3</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @muratmaga (2020-09-19 18:46 UTC)

<p><a class="mention" href="/u/lars12345">@lars12345</a> just keep in mind the SlicerMorph is only available for v4.11 but not for stable.  So you will need to use a preview version.</p>

---

## Post #7 by @lars12345 (2020-09-21 18:31 UTC)

<p>I was able to import my images with SlicerMorph &gt; ImageStacks after updating to the 4.11 pre-release. Thank you very much for the help.</p>

---
