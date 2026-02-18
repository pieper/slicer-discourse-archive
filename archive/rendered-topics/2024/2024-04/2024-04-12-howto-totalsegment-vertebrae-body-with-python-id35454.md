# Howto `totalSegment` vertebrae_body with python?

**Topic ID**: 35454
**Date**: 2024-04-12
**URL**: https://discourse.slicer.org/t/howto-totalsegment-vertebrae-body-with-python/35454

---

## Post #1 by @jumbojing (2024-04-12 08:50 UTC)

<p>From <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/TotalSegmentator/TotalSegmentator.py#L488" rel="noopener nofollow ugc">SlicerTotalSegmentator</a>, I extract a function (see <img src="https://emoji.discourse-cdn.com/twitter/point_down/2.png?v=12" title=":point_down:t2:" class="emoji" alt=":point_down:t2:" loading="lazy" width="20" height="20">) for segment the vertebrae.</p>
<pre data-code-wrap="python"><code class="lang-python">_subset = ['vertebrae_S1', 'vertebrae_L5', 'vertebrae_L4', 
           'vertebrae_L3', 'vertebrae_L2', 'vertebrae_L1', 
           'vertebrae_T12', 'vertebrae_T11', 'vertebrae_T10', 
           'vertebrae_T9', 'vertebrae_T8', 'vertebrae_T7', 
           'spinal_cord']
def ttSegVert(inputFile, mNam,  taSb=_subset):
#   if isinstance(taSb, list):
  outFile = rf'output/{mNam}.nii.gz'
#   else:
#     outFile = rf'{TMP}/{mNam}'
  import shutil
  ttSegCode = [shutil.which('PythonSlicer'),]
  import sysconfig
  ttSegCode += [os.path.join(sysconfig.get_path('scripts'),
                             "TotalSegmentator")]
  ttSegCode += ['-i', f'{inputFile}', 
                '-o', f'{outFile}', 
                '--fast',
                '--device', 'cpu',]
  if isinstance(taSb, list):
    ttSegCode += ['--ml', '--roi_subset', *taSb]
  else: # [TODO]: 无法完成`taSb='vertebrae_body'`
    ttSegCode += ["--task", taSb]
  print(ttSegCode)
  pros = ut.launchConsoleProcess(ttSegCode).wait()
  print(pros)
  return
</code></pre>
<p>Well, run <code>ttSegVert(input, 'ttSegVert', _subset)</code> , got <img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20"> a good result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c125d1125120c739d3ea4384a86333baf2f1fbf.jpeg" data-download-href="/uploads/short-url/8zpZv08CvJI12hmtM4gZeAb49eD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c125d1125120c739d3ea4384a86333baf2f1fbf_2_437x500.jpeg" alt="image" data-base62-sha1="8zpZv08CvJI12hmtM4gZeAb49eD" width="437" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c125d1125120c739d3ea4384a86333baf2f1fbf_2_437x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c125d1125120c739d3ea4384a86333baf2f1fbf_2_655x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c125d1125120c739d3ea4384a86333baf2f1fbf_2_874x1000.jpeg 2x" data-dominant-color="585B5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1122×1282 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, run<code>ttSegVert(inputFile, 'ttSegVert</code>, ‘vertebrae_body’)`, got None…</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/vertebra">@vertebra</a></p>
<p>Howto <code>totalsegment</code> vertebrae_body? Or <img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"> what’s wrong?</p>

---

## Post #2 by @jumbojing (2024-04-12 09:05 UTC)

<p>Also, I made some modifications to <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/7aa1ca252261a2b6d026cf58d662286aac904fa3/TotalSegmentator/TotalSegmentator.py#L1169" rel="noopener nofollow ugc">this code</a> as <img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20">:</p>
<pre><code class="lang-auto">            # SampleData.downloadSample('CTLiver')
            logic.process(inputVolume, outputSegmentation, cpu=True, fast = True, task="vertebrae_body")
</code></pre>
<p>I can get a good result too! <img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e2bb442fb01a3acb3191ad67350a373815e925f.jpeg" data-download-href="/uploads/short-url/fIC9LfmlJ6AfB1EP7tCxTB4szjV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2bb442fb01a3acb3191ad67350a373815e925f_2_465x500.jpeg" alt="image" data-base62-sha1="fIC9LfmlJ6AfB1EP7tCxTB4szjV" width="465" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2bb442fb01a3acb3191ad67350a373815e925f_2_465x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2bb442fb01a3acb3191ad67350a373815e925f_2_697x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2bb442fb01a3acb3191ad67350a373815e925f_2_930x1000.jpeg 2x" data-dominant-color="5F626A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1180×1268 97.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
