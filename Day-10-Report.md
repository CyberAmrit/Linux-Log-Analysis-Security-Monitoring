Day 10 Report – MITRE ATT&CK Mapping

Project: Linux Log Analysis and Security Monitoring
Day: 10
Platform: Kali Linux
Python Version: 3.13.12

1. Objective

The objective of Day 10 was to connect security events identified during Linux log analysis with the MITRE ATT&CK framework.

2. Activities Performed

- Reviewed previously identified authentication events.
- Mapped failed login attempts to MITRE ATT&CK.
- Reviewed invalid username attempts.
- Analysed successful login events.
- Mapped sudo-related activity.
- Documented security recommendations and investigation limitations.

3. MITRE ATT&CK Mapping

Technique ID| Technique| Relevance
T1110| Brute Force| Repeated failed login attempts
T1087| Account Discovery| Potential relevance to invalid usernames
T1078| Valid Accounts| Potential relevance to successful authentication
T1548.003| Sudo and Sudo Caching| Linux privilege-related activity

These mappings indicate possible behavioural relevance and do not confirm actual attacks.

4. Technical Validation

A Python-based validation command was executed to verify the evidence file.

Validation results:

- T1110: PASS
- T1087: PASS
- T1078: PASS
- T1548.003: PASS
- Security Recommendations: PASS
- Important Limitations: PASS

Total checks passed: 6/6

5. Security Recommendations

- Monitor repeated authentication failures.
- Investigate unknown usernames.
- Review unexpected successful logins.
- Audit privileged sudo commands.
- Maintain accurate authentication logs.
- Improve account-specific monitoring.

6. Limitations

- Test logs are simulated.
- Successful authentication does not automatically indicate malicious activity.
- Sudo activity is not automatically suspicious.
- Technique mapping requires further investigation.
- The repeated-failure counter currently operates across the entire input file.

7. Conclusion

Day 10 successfully connected Linux authentication and privilege-related log analysis with the MITRE ATT&CK framework.

The evidence file was created and technically validated with six successful checks.

Status: Day 10 documentation and validation completed.
