---
topic_id: 15860
title: "Error When Importing Matplotlib"
date: 2021-02-05
url: https://discourse.slicer.org/t/15860
---

# Error when importing Matplotlib

**Topic ID**: 15860
**Date**: 2021-02-05
**URL**: https://discourse.slicer.org/t/error-when-importing-matplotlib/15860

---

## Post #1 by @11141 (2021-02-05 04:50 UTC)

<p>Hi.<br>
I created a extension, but the following error occurred.</p>
<blockquote>
<p>Blockquote<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\20200\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/20200/Desktop/Daehyeon/VXMController/VXMController.py”, line 18, in <br>
import matplotlib.pyplot as plt<br>
File “C:/Users/20200/anaconda3/envs/vxm/Lib/site-packages\matplotlib\pyplot.py”, line 36, in <br>
import matplotlib.colorbar<br>
File “C:/Users/20200/anaconda3/envs/vxm/Lib/site-packages\matplotlib\colorbar.py”, line 40, in <br>
import matplotlib.artist as martist<br>
File “C:/Users/20200/anaconda3/envs/vxm/Lib/site-packages\matplotlib\artist.py”, line 13, in <br>
from .path import Path<br>
File “C:/Users/20200/anaconda3/envs/vxm/Lib/site-packages\matplotlib\path.py”, line 18, in <br>
from . import _path, cbook<br>
ImportError: cannot import name ‘_path’</p>
</blockquote>
<p>I think it can’t import the <strong>.pyd</strong> file when importing matplotlib.<br>
I’d really appreciate if you could help me solve this problem.</p>
<p>I use windows 10, 64bits OS , intel i9 CPU, 32GB RAM.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05a29da4eed3d2dba6f720cda03e8ae0b8820aae.png" data-download-href="/uploads/short-url/NQMZ7a3xK5dMjA8sKKamv2rVwy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05a29da4eed3d2dba6f720cda03e8ae0b8820aae_2_690x309.png" alt="image" data-base62-sha1="NQMZ7a3xK5dMjA8sKKamv2rVwy" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05a29da4eed3d2dba6f720cda03e8ae0b8820aae_2_690x309.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05a29da4eed3d2dba6f720cda03e8ae0b8820aae.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05a29da4eed3d2dba6f720cda03e8ae0b8820aae.png 2x" data-dominant-color="141720"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">749×336 26.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pll_llq (2021-02-06 05:43 UTC)

<p>Why do you append the anaconda packages folded to sys.path?<br>
Are you sure that this anaconda environment is compatible with slicer?</p>

---
