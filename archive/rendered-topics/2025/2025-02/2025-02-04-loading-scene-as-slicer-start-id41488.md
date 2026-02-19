---
topic_id: 41488
title: "Loading Scene As Slicer Start"
date: 2025-02-04
url: https://discourse.slicer.org/t/41488
---

# Loading scene as slicer start

**Topic ID**: 41488
**Date**: 2025-02-04
**URL**: https://discourse.slicer.org/t/loading-scene-as-slicer-start/41488

---

## Post #1 by @Djonathan_Souza (2025-02-04 12:13 UTC)

<p>how to load an image as soon as it starts. I just do it but when i use “–python-script” he just ignore the path to load</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c316796cdae57cb60bef53aad5fcfdb7aa8b665.png" data-download-href="/uploads/short-url/1JRzSaFtY6wbO9YEykagwXYBs7b.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c316796cdae57cb60bef53aad5fcfdb7aa8b665_2_690x71.png" alt="image" data-base62-sha1="1JRzSaFtY6wbO9YEykagwXYBs7b" width="690" height="71" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c316796cdae57cb60bef53aad5fcfdb7aa8b665_2_690x71.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c316796cdae57cb60bef53aad5fcfdb7aa8b665_2_1035x106.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c316796cdae57cb60bef53aad5fcfdb7aa8b665.png 2x" data-dominant-color="363641"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1372×142 35.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @RafaelPalomar (2025-02-04 12:58 UTC)

<p>Hello <a class="mention" href="/u/djonathan_souza">@Djonathan_Souza</a>, please have a look at the following related post and see if it helps. It is not clear to me what your problem is.</p>
<aside class="quote quote-modified" data-post="1" data-topic="36718">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c37758/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/run-a-python-script-with-command-line-arguments/36718">Run a python script with command line arguments</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I am trying to run a python script that accepts command line arguments as follows. 
./Slicer --python-script /home/user/extract_centerlines_vmtk.py --data_dir /PATH/TO/DATA --end_points --network --network_curve --network_prop --centerline --centerline_curve --centerline_prop

and the python script looks as follows 
def extract_centerlines(args):
...

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract centerlines from a dataset")
    parser.add_argument('--…
  </blockquote>
</aside>


---

## Post #3 by @Djonathan_Souza (2025-02-04 13:12 UTC)

<p>Hi <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> this is exactly what I’m looking for!</p>

---
