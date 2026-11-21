Day 7 – Sudo Authentication Log Analysis & Security Verification

1. Objective

The objective of Day 7 was to analyze sudo authentication logs, review privileged command activity, and check for failed sudo authentication or unauthorized privilege access attempts.

2. Log Source

- Log File: "data/sudo-authentication.txt"
- Analysis Directory: "Project-1-Log-Analysis"
- Evidence Directory: "evidence/"

3. Sudo Command Summary

The sudo authentication logs were analyzed to identify recorded privileged command activity.

The following command entries were found:

Command| Count
journalctl -b --no-pager| 7
journalctl -b -u ssh.service --no-pager| 1
systemctl -b -u ssh.service --no-pager| 1
systemctl status ssh| 1
systemctl status ssh --no-pager| 2

These entries represent the commands recorded in the analyzed sudo log data.

4. Failed Sudo / Unauthorized Access Check

The log file was searched for the following patterns:

- Authentication failure
- Incorrect password
- NOT in sudoers

Result: No matching failed sudo authentication or unauthorized sudo access events were found for the checked patterns.

5. Actual Security Verification

An additional verification check was performed against the sudo authentication log data.

Output: No matching events found for the checked patterns.

This indicates that the selected search patterns did not match any entries in the analyzed log file.

6. Evidence Collected

The following evidence files were saved:

1. "day-7-sudo-command-summary.txt"
2. "day-7-security-check.txt"
3. "day-7-actual-security-verification.txt"

Additional screenshots were captured to document the command outputs and evidence file verification.

7. Findings

- Sudo command activity was identified in the analyzed logs.
- Journalctl and systemctl commands were recorded.
- No matching failed sudo authentication events were found for the selected search patterns.
- No matching unauthorized sudo access events were found for the selected search patterns.
- The additional security verification returned no matching events.

8. Conclusion

Day 7 successfully completed the sudo authentication log analysis and basic security verification.

The analyzed log data did not contain entries matching the selected failed authentication and unauthorized access patterns.

This result is limited to the available log data and the patterns checked. It does not establish that the entire system is free from suspicious activity.

Status: Day 7 Analysis Completed.
