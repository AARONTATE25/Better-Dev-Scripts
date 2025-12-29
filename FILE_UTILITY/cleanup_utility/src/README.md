
# CleanUP Utility: 


# Steps

1. **Open Target Directory**
   Define the path to the specific folder you want to scan.

2. **Set Stale Threshold**
   Decide the age limit (e.g., 30 days) that classifies a file as "stale."

3. **Get Current Date**
   Retrieve the current system date and time to calculate the elapsed time.

4. **Iterate Through Items**
   Loop through every item contained within the chosen directory.

5. **Filter for Files**
   Check if the item is a regular file. Skip any sub-folders or directories.

6. **Retrieve Modification Time**
   Access the file's metadata get the "Last Modified" timestamp.

7. **Calculate File Age**
   Subtract the modification date from the current date to get the total days passed.

8. **Identify Stale Files**
   If the file's age is greater than the threshold, store its name and age.

9. **Output Results**
   Display the list of stale files and their ages to the user.

10. **Handle No Matches**
    If no files meet the criteria, output a message stating that nothing is stale.


# Example Output 

    Stale Files Report
    ------------------
    old_log.txt           — 45 days old
    backup_archive.zip    — 120 days old
    unused_config.ini     — 32 days old
    
    Total stale files: 3
    
If no files egfxceeded the threshold:

    Stale Files Report
    ------------------
    No stale files found. All files are within the age limit.
