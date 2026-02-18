# Run a python script with command line arguments

**Topic ID**: 36718
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/run-a-python-script-with-command-line-arguments/36718

---

## Post #1 by @RomanStriker (2024-06-12 11:25 UTC)

<p>Hi,</p>
<p>I am trying to run a python script that accepts command line arguments as follows.</p>
<pre><code class="lang-auto">./Slicer --python-script /home/user/extract_centerlines_vmtk.py --data_dir /PATH/TO/DATA --end_points --network --network_curve --network_prop --centerline --centerline_curve --centerline_prop
</code></pre>
<p>and the python script looks as follows</p>
<pre><code class="lang-auto">def extract_centerlines(args):
...

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract centerlines from a dataset")
    parser.add_argument('--data_dir', type=str, help='Path to the dataset directory')
    parser.add_argument('--end_points', action='store_true', default=False, help='Save the endpoints')
    parser.add_argument('--network', action='store_true', default=False, help='Save the network model')
    parser.add_argument('--network_curve', action='store_true', default=False, help='Save the network curve')
    parser.add_argument('--network_prop', action='store_true', default=False, help='Save the network properties')
    parser.add_argument('--centerline', action='store_true', default=False, help='Save the centerline model')
    parser.add_argument('--centerline_curve', action='store_true', default=False, help='Save the centerline curve')
    parser.add_argument('--centerline_prop', action='store_true', default=False, help='Save the centerline properties')
    args = parser.parse_args()
    
    extract_centerlines(args)
</code></pre>
<p>when I run this script using the command above, I get</p>
<pre><code class="lang-auto">./Slicer --python-script /home/user/extract_centerlines_vmtk.py --data_dir /PATH/TO/DATA --end_points --network --network_curve --network_prop --centerline --centerline_curve --centerline_prop
&gt;
</code></pre>
<p>guessing that it’s expecting something more. I also tried</p>
<pre><code class="lang-auto">./Slicer --python-script "/home/user/extract_centerlines_vmtk.py --data_dir /PATH/TO/DATA --end_points --network --network_curve --network_prop --centerline --centerline_curve --centerline_prop"
</code></pre>
<p>but I get the error</p>
<pre><code class="lang-auto">./Slicer --no-splash --no-main-window --python-script "/home/user/extract_centerlines_vmtk.py --data_dir /PATH/TO/DATA --end_points --network --network_curve --network_prop --centerline --centerline_curve --centerline_prop"
</code></pre>
<p>How to run this script with the arguments?</p>

---

## Post #2 by @RafaelPalomar (2024-06-12 11:31 UTC)

<p><a class="mention" href="/u/romanstriker">@RomanStriker</a>, check this post and see if it helps:</p>
<aside class="quote" data-post="1" data-topic="33390">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/derekcbr/48/18793_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-parameters-conflicts-when-adding-load-file-and-python-script/33390">Slicer parameters conflicts when adding "--load-file" and "--python-script"</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Slicer.exe, “–python-code”, “print(‘Start Slicer from Blender!’)”, “–python-script”, startup_slice_script_file 
When adding both “–load-file” and “–python-script”, “–load-file” will not be executed to load .mrb file, and it only executes “–python-script”. Is there a way of adding both parameters and make it working? Thanks.
  </blockquote>
</aside>


---

## Post #3 by @RomanStriker (2024-06-12 12:07 UTC)

<p>Thanks. I can use the sys.argv as follows</p>
<pre data-code-wrap="bash"><code class="lang-bash">./Slicer --python-script /home/user/extract_centerlines_vmtk.py "/home/user/data" end_points network network_curve network_prop centerline centerline_curve centerline_prop
</code></pre>
<p>and in the script</p>
<pre data-code-wrap="py"><code class="lang-py">def extract_centerlines(args):
...

if __name__ == '__main__':
    # create args object
    args = argparse.Namespace(
        dataset_dir=sys.argv[1],
        end_points=True if 'end_points' in sys.argv else False,
        network=True if 'network' in sys.argv else False,
        network_curve=True if 'network_curve' in sys.argv else False,
        network_prop=True if 'network_prop' in sys.argv else False,
        centerline=True if 'centerline' in sys.argv else False,
        centerline_curve=True if 'centerline_curve' in sys.argv else False,
        centerline_prop=True if 'centerline_prop' in sys.argv else False,
    )
    
    extract_centerlines(args)
</code></pre>

---
