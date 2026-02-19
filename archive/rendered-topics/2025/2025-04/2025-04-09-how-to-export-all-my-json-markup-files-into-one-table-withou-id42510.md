---
topic_id: 42510
title: "How To Export All My Json Markup Files Into One Table Withou"
date: 2025-04-09
url: https://discourse.slicer.org/t/42510
---

# How to export all my JSON markup files into one table without running a GPA on it

**Topic ID**: 42510
**Date**: 2025-04-09
**URL**: https://discourse.slicer.org/t/how-to-export-all-my-json-markup-files-into-one-table-without-running-a-gpa-on-it/42510

---

## Post #1 by @grega (2025-04-09 23:10 UTC)

<p>I need to get a CSV table that includes the coordinates for all my landmarks in one CSV file. I have about 150 JSON files that all have 32 landmark coordinates in them, and normally I would do this by running a GPA through Slicer, which would give me all my landmark data with GPA applied to it, but I need to get the raw coordinate data without the any GPA done to it, and I am having trouble figuring out exactly how to do that</p>

---

## Post #2 by @muratmaga (2025-04-09 23:15 UTC)

<p>You can use MergeMarkups to merge your individual markup pointlist object into a single file. You want to use the <code>Merge All Markups</code> option. But it might be a bit slow.</p>

---

## Post #3 by @muratmaga (2025-04-09 23:28 UTC)

<p><a class="mention" href="/u/grega">@grega</a> you can also use chatgpt or other copilots to create simple python script that you can run inside the Slicer python console.</p>
<p>I gave this prompt to the bing copilot and took me about 3 tries to get the following script, which seems to work perfectly fine. I simply copy and pasted the errors from the python console until it self-corrected. Prompt was:</p>
<p><code>I have many markup pointlist that I generated in 3D Slicer. Each pointlist is in Slicer's mrk.json format and contains 32 control points. Create a python script that will read these files from the disk and turn it into CSV file in which each row is the coordinates from one of these markup files.</code></p>
<p>Functional script, which took about 5 minutes to generate, is:</p>
<pre data-code-wrap="python"><code class="lang-python">import os
import json
import csv

# Input directory containing JSON files
input_directory = '/Users/amaga/Desktop/Mouse_Models-main/LMs/'

# Output CSV file path
output_csv = '/Users/amaga/Desktop/flat.csv'

# Get a list of JSON files in the directory
json_files = [f for f in os.listdir(input_directory) if f.endswith('.json')]

# Open the CSV file for writing
with open(output_csv, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Header row
    header = ['File Name']
    for i in range(32):  # Assuming up to 32 control points
        header.extend([f'Point_{i+1}_X', f'Point_{i+1}_Y', f'Point_{i+1}_Z'])
    csv_writer.writerow(header)

    # Process each JSON file
    for json_file in json_files:
        file_path = os.path.join(input_directory, json_file)
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
                print(f"Processing file: {json_file}")

                # Check and parse the 3D Slicer `mrk.json` schema
                if 'markups' in data and 'controlPoints' in data['markups'][0]:
                    control_points = data['markups'][0]['controlPoints']
                    row = [json_file]  # Start the row with the file name

                    # Add coordinates for each control point
                    for point in control_points:
                        if 'position' in point and len(point['position']) == 3:
                            row.extend(point['position'])  # Add x, y, z
                        else:
                            row.extend([None, None, None])

                    # Ensure the row has exactly 32 points (96 values)
                    while len(row) &lt; (1 + 96):  # 1 for the file name, 96 for coordinates
                        row.extend([None, None, None])

                    csv_writer.writerow(row)
                else:
                    print(f"'markups' or 'controlPoints' key not found in {json_file}")
            except json.JSONDecodeError:
                print(f"Invalid JSON format in {json_file}")
            except KeyError:
                print(f"Missing expected keys in {json_file}")

</code></pre>

---

## Post #4 by @grega (2025-04-10 14:26 UTC)

<p>Hey Murat,</p>
<p>I tried doing the merge markups method, but I couldn’t find the “merge all markups” function so I tried importing all of my data into the scene and merging via the “merge landmark sets” function, but that just created a monster file that had all of my landmark points in it with very little organization. I tried transferring your lines of code to an R script via chatgpt as I am unfamiliar with python, but I’ve had little success doing that as well. I’ll keep working with chat to try to figure out the code you sent me though!</p>
<p>Out of curiosity, why does slicer not have a function to append JSON files together without running a GPA? It clearly has the capacity to do that as the GPA output is a file that is in the exact format I need, just with a GPA applied to it, so why isn’t there a function for making that output file without the GPA?</p>
<p>Thanks for your help</p>

---

## Post #5 by @muratmaga (2025-04-10 14:55 UTC)

<aside class="quote no-group" data-username="grega" data-post="4" data-topic="42510">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/96bed5/48.png" class="avatar"> grega:</div>
<blockquote>
<p>ut I couldn’t find the “merge all markups” function</p>
</blockquote>
</aside>
<p>Please update your SlicerMorph extension (you need to be running 5.8.1 to be able to do that).</p>
<aside class="quote no-group" data-username="grega" data-post="4" data-topic="42510">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/96bed5/48.png" class="avatar"> grega:</div>
<blockquote>
<p>I tried transferring your lines of code to an R script via chatgpt as I am unfamiliar with python,</p>
</blockquote>
</aside>
<p>All you had to do is to replace the paths. and then copy and paste it into the Slicer’s python console. But R should work too. But if you are going to use R, what don’t you use <a href="https://github.com/SlicerMorph/SlicerMorphR" rel="noopener nofollow ugc">SlicerMorphR</a> then? You can loop over all the files (as this python script was doing), and write a CSV file in whichever format you want.</p>
<aside class="quote no-group" data-username="grega" data-post="4" data-topic="42510">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/96bed5/48.png" class="avatar"> grega:</div>
<blockquote>
<p>why does slicer not have a function to append JSON files together without running a GPA?</p>
</blockquote>
</aside>
<p>That’s because, everybody’s use case, format requirements, workflows, etc are different. Slicer provides all the functionality to do what you want to do You can copy and paste control points from one pointList to the other. I just assumed you already knew that and don’t want to do that 132 times (that’s why scripting is easier).</p>
<p>I</p>

---
