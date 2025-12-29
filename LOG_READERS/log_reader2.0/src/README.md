# Error Counting Script Roadmap

This is a clear roadmap for writing a Python script to summarize errors in a log file.

## Steps

1. **Open the log file for reading.**

2. **Create a storage structure**
   Use a dictionary to keep track of error types and their counts.

3. **Iterate through each line in the file.**

4. **Check for errors**
   Determine if `"ERROR"` is present in the line.

5. **Extract the error description**
   Capture everything after `"ERROR"` in the line.

6. **Update the error count**
   Increment the count for that specific error in the storage dictionary.

7. **Print the results**
   After processing all lines, print each error type with its total count.

## Outcome

        Database connection failed: 2
        File not found: 2
        Timeout while reading response: 1

By following these steps, the script will generate a summary of all unique errors in the log and show how often each one occurred.


    Total ERROR lines: 5
