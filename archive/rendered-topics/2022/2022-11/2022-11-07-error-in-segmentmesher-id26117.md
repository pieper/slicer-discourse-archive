# Error in SegmentMesher

**Topic ID**: 26117
**Date**: 2022-11-07
**URL**: https://discourse.slicer.org/t/error-in-segmentmesher/26117

---

## Post #1 by @ZSoltani (2022-11-07 19:13 UTC)

<p>Hello all,</p>
<p>I get the following error when I try to use Cleaver method to mesh a vertebra.</p>
<p>“Command ‘cleaver-cli’ returned non-zero exit status 109.” (attached photo)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc4fbdc35d16b6784b3c36e54217444a3a4818af.png" data-download-href="/uploads/short-url/qRSBMbQsaEf72MysczZh74qXdkr.png?dl=1" title="Screenshot from 2022-11-07 13-58-33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc4fbdc35d16b6784b3c36e54217444a3a4818af_2_690x397.png" alt="Screenshot from 2022-11-07 13-58-33" data-base62-sha1="qRSBMbQsaEf72MysczZh74qXdkr" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc4fbdc35d16b6784b3c36e54217444a3a4818af_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc4fbdc35d16b6784b3c36e54217444a3a4818af_2_1035x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc4fbdc35d16b6784b3c36e54217444a3a4818af_2_1380x794.png 2x" data-dominant-color="727070"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-07 13-58-33</span><span class="informations">2163×1246 461 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you have any idea what does this error mean and how it can be solved?</p>
<p>Also, I am looking for some documents on using Cleaver method through programming Python intractor, which I guess it’s needed for adaptive mesh. I found some ideas in this <a href="https://discourse.slicer.org/t/get-cell-indices-in-exported-mesh-corresponding-to-each-segment/15437/7">post</a>, but it is comprehensive enough. Any suggestion is highly appreciated.</p>
<p>Thank you,<br>
Zahra</p>

---

## Post #2 by @lassoan (2022-11-07 19:47 UTC)

<p>The cleaver mesher CLI <a href="https://github.com/SCIInstitute/Cleaver2/blob/master/src/cli/mesher/main.cpp">never explicitly returns with error code 109</a>, so most likely this is generated at somewhere higher level and will not reveal anything specific about the problem. Maybe the process has ran out of memory. Monitor the memory usage and free memory while the mesher is running to confirm this.</p>
<p>You can also build Cleaver and run it in a debugger to understand what is happening, and if you don’t find a solution then report all your findings at <a href="https://github.com/SCIInstitute/Cleaver2/issues">Cleaver’s issue tracker</a>. While you are waiting for the answer, you can adjust the meshing parameters to avoid this error.</p>

---

## Post #3 by @ZSoltani (2022-11-07 20:08 UTC)

<p>Hi Andras,</p>
<p>Thanks for your reply. I tried to use the module on another disk and actually another operating system (from Linux to Windows), but I still get the same error. The mesher doesn’t run at all for monitoring the process and the error pops up immediately. Plus, the WorkStation has plenty of empty space available.</p>
<p>Attached you can also see the error message in Python interactor, if it helps any.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c306f6bd1e47c3f63e318d6501ff4d23cd8aee7.png" data-download-href="/uploads/short-url/fr5l0sws2BwiV39jvRzxBqEEJuL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c306f6bd1e47c3f63e318d6501ff4d23cd8aee7_2_690x123.png" alt="image" data-base62-sha1="fr5l0sws2BwiV39jvRzxBqEEJuL" width="690" height="123" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c306f6bd1e47c3f63e318d6501ff4d23cd8aee7_2_690x123.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c306f6bd1e47c3f63e318d6501ff4d23cd8aee7_2_1035x184.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c306f6bd1e47c3f63e318d6501ff4d23cd8aee7_2_1380x246.png 2x" data-dominant-color="FEF7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2544×454 33.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-11-07 20:22 UTC)

<p>What are the messages above <code>Run with --help for more information</code>?</p>

---

## Post #5 by @pieper (2022-11-07 20:26 UTC)

<p>Didn’t we have an issue lately where an extra space or empty string was being post-pended to a command line string leading to an error message like this?  The error message makes it look like the same issue.</p>

---

## Post #6 by @ZSoltani (2022-11-07 20:28 UTC)

<p>Here is the full message:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5d1dcf3f6f9364c0d7c009adc3f3af424707aa6.png" data-download-href="/uploads/short-url/sdZGRk6ewO4BBcJbg1NjeUJQeCa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5d1dcf3f6f9364c0d7c009adc3f3af424707aa6.png" alt="image" data-base62-sha1="sdZGRk6ewO4BBcJbg1NjeUJQeCa" width="690" height="450" data-dominant-color="F9F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1442×942 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(I played with meshing parameters a bit!)</p>

---

## Post #7 by @pieper (2022-11-07 20:30 UTC)

<p>Yes, that last <code>''</code> in the argument list looks like the issue I mentioned.  Maybe you can try editing the python code to remove it before running the command.</p>

---

## Post #8 by @ZSoltani (2022-11-07 20:32 UTC)

<p>Thanks Steve for the reply. Can you explain a bit more on the source of the error, so I can find a clue where should I edit in the code?<br>
​​<br>
​​​​​​​​​​​</p>

---

## Post #9 by @lassoan (2022-11-07 20:33 UTC)

<p>I’ve pushed a fix:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/lassoan/SlicerSegmentMesher/commit/444adc113a63533a433b7f15706555bcc33f31f3">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentMesher/commit/444adc113a63533a433b7f15706555bcc33f31f3" target="_blank" rel="noopener">github.com/lassoan/SlicerSegmentMesher</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerSegmentMesher/commit/444adc113a63533a433b7f15706555bcc33f31f3" target="_blank" rel="noopener">Fix Command 'cleaver-cli.exe' returned non-zero exit status 109.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-11-07" data-time="20:32:51" data-timezone="UTC">08:32PM - 07 Nov 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 2 additions and 1 deletions">
        <a href="https://github.com/lassoan/SlicerSegmentMesher/commit/444adc113a63533a433b7f15706555bcc33f31f3" target="_blank" rel="noopener">
          <span class="added">+2</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">There was an extra empty command-line parameter and the new, more strict parser <span class="show-more-container"><a href="https://github.com/lassoan/SlicerSegmentMesher/commit/444adc113a63533a433b7f15706555bcc33f31f3" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">of Cleaver2 returned with failure due to the unexpected argument.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can make the change in the script on your computer right now or update the extension from the extensions manager tomorrow.</p>

---

## Post #10 by @ZSoltani (2022-11-07 20:34 UTC)

<p>Thank you Andras, I’ll do that.</p>

---

## Post #11 by @pieper (2022-11-07 20:35 UTC)

<p>Yes, that’s the fix I would have expected.  Will be great if you can try it out and report back <a class="mention" href="/u/zsoltani">@ZSoltani</a></p>

---

## Post #12 by @ZSoltani (2022-11-07 20:36 UTC)

<p>Sure, I will try it and report back. Thank you <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a> for your great support.</p>

---

## Post #13 by @ZSoltani (2022-11-08 16:40 UTC)

<p>HI,</p>
<p>As a report: With the updated version of the Segment Mesher, it can complete the mesh generation using Cleaver method. Thank you for that.</p>
<p>However, at the end of the process, Python interactor shows a message that .vtk and .info files are written in a subfolder in SegmentMesher folder. But the folder is empty and no file is there (I checked view the hidden option too). Please see the attached image.</p>
<p>Thanks,<br>
Zahra</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee129f943994822070e94fc1c8ac5836d13af16c.png" data-download-href="/uploads/short-url/xY5xnjcqiesEahKn1PSfwUleRSA.png?dl=1" title="Screenshot from 2022-11-08 09-28-21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee129f943994822070e94fc1c8ac5836d13af16c_2_570x500.png" alt="Screenshot from 2022-11-08 09-28-21" data-base62-sha1="xY5xnjcqiesEahKn1PSfwUleRSA" width="570" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee129f943994822070e94fc1c8ac5836d13af16c_2_570x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee129f943994822070e94fc1c8ac5836d13af16c_2_855x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee129f943994822070e94fc1c8ac5836d13af16c_2_1140x1000.png 2x" data-dominant-color="7A7879"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-08 09-28-21</span><span class="informations">2163×1897 548 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @pieper (2022-11-08 19:00 UTC)

<p>Hi Zahra -</p>
<p>I think you are getting close - the files are usually deleted after they are re-loaded in Slicer (with the idea that you can save out your final version form Slicer).  But you can have them preserved if you check the box in the application settings:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f47e6320a9e820e5944ebe3447578a59ebdd23c8.png" alt="image" data-base62-sha1="ySThJYo8wP4IP2IWIWIm4DxyuSs" width="487" height="346"></p>
<p>For me the current nightly version of the Segment Mesher extension is working as expected in the 5.0.3 release.  Let us know if it works for you or you run into other issues.  Here the source segmentation is shown semi-transparent over the meshed result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb3ea233edf02c385351527afeb061902de063c8.jpeg" data-download-href="/uploads/short-url/sZZ7l3rpqudO2gHh0uGHqVgjnSg.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb3ea233edf02c385351527afeb061902de063c8_2_690x324.jpeg" alt="image" data-base62-sha1="sZZ7l3rpqudO2gHh0uGHqVgjnSg" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb3ea233edf02c385351527afeb061902de063c8_2_690x324.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb3ea233edf02c385351527afeb061902de063c8_2_1035x486.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb3ea233edf02c385351527afeb061902de063c8.jpeg 2x" data-dominant-color="81848C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1241×584 48.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @ZSoltani (2022-11-08 19:28 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a>, that default setting makes a real sense.</p>
<p>I was also wondering if there is a way to improve the mesh quality in a few local areas manually? In the attached image, I want to have some control in the two specified areas.</p>
<p>Thanks,<br>
Zahra</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c34abd9100103a35551f16502289300cb17fe77.png" data-download-href="/uploads/short-url/6j3R5ZKNNqtCtfmtucxc76PyJYr.png?dl=1" title="Screenshot from 2022-11-08 13-13-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c34abd9100103a35551f16502289300cb17fe77_2_690x397.png" alt="Screenshot from 2022-11-08 13-13-46" data-base62-sha1="6j3R5ZKNNqtCtfmtucxc76PyJYr" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c34abd9100103a35551f16502289300cb17fe77_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c34abd9100103a35551f16502289300cb17fe77_2_1035x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c34abd9100103a35551f16502289300cb17fe77_2_1380x794.png 2x" data-dominant-color="88878A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-08 13-13-46</span><span class="informations">2163×1246 537 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @ZSoltani (2022-11-08 20:23 UTC)

<p>With changing the mesh parameters, I could get rid of those areas and have a nice mesh generated as below. But still I am wondering about possibility to control mesh in local areas?</p>
<p>Thank you,<br>
Zahra</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c90c5db31b1d1327e493d55b6b03f7f6afa88a3.png" data-download-href="/uploads/short-url/8DMP0ooKiCDfb9418fuVtannsRB.png?dl=1" title="Screenshot from 2022-11-08 14-19-10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c90c5db31b1d1327e493d55b6b03f7f6afa88a3_2_690x397.png" alt="Screenshot from 2022-11-08 14-19-10" data-base62-sha1="8DMP0ooKiCDfb9418fuVtannsRB" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c90c5db31b1d1327e493d55b6b03f7f6afa88a3_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c90c5db31b1d1327e493d55b6b03f7f6afa88a3_2_1035x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c90c5db31b1d1327e493d55b6b03f7f6afa88a3_2_1380x794.png 2x" data-dominant-color="838385"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-08 14-19-10</span><span class="informations">2163×1246 459 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @pieper (2022-11-08 20:31 UTC)

<p>Great <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=12" title=":tada:" class="emoji" alt=":tada:" loading="lazy" width="20" height="20"> Glad it’s working for you.</p>

---

## Post #18 by @ZSoltani (2022-11-08 20:36 UTC)

<p>Thanks Steve indeed for the great support!</p>
<p>I have another question though. The mesh generated is 4-node linear tetrahedral element (C3D4), by default. How can I change the element type to 10-node quadratic tetrahedral element (C3D10)?</p>
<p>Thanks,<br>
Zahra</p>

---

## Post #19 by @pieper (2022-11-08 20:42 UTC)

<p>That’s a great question but I don’t know enough about Cleaver to answer.  If nobody here knows you could follow up at the cleaver github.</p>

---

## Post #20 by @ZSoltani (2022-11-09 15:04 UTC)

<p>Just as an update, I asked people in the Cleaver github and based on their reply, higher order elements aren’t supported in Cleaver at this time. But still, C3D4 can be converted to C3D10 by adding nodes at the midpoints of the edges.</p>
<p>Best,<br>
Zahra</p>

---

## Post #21 by @pieper (2022-11-09 16:05 UTC)

<p>Thanks for reporting back.  Yes, adding nodes on the edges could be done with a script in Slicer, but probably there are FEM tools that do this sort of thing.</p>

---

## Post #22 by @ZSoltani (2022-11-09 16:09 UTC)

<p>Sure, I’m looking around to assess alternatives.</p>
<p>Thanks,<br>
Zahra</p>

---

## Post #23 by @ZSoltani (2022-11-09 23:02 UTC)

<p>Update: Gmsh can do that in the .vtk file, without need to change the mesh format.</p>

---
