ansible-cis_rhel7-role
=========

Check hardening status of a target server. 

[ Modificar con la version real para rhel 7 ]This playbook is based on the official CIS Red Hat Enterprise Linux 8 Benchmark v1.0.0.1 : [https://workbench.cisecurity.org/benchmarks/4359](https://workbench.cisecurity.org/benchmarks/4359)  
Published on Dec 16th 2019

python3 spreadsheetconv.py --input defaults/main.yml -o rules.csv

all check are configured in the "rules" variable, a huge dictionary stored on "defaults/main.yml" file.

```yaml
audit_rules:
  rule_1_2_2:
    description: 1.2.2 Ensure GPG keys are configured (Not Scored)
    enabled: true
    scored: false
    severity: "critical"
    status: ''
```

# Known issues



Requirements
------------

root credentials, Ansible 2.9

Role Variables
--------------

Except for the "rules" variable (describe above), also these are included:

```yaml
_permitted_sudo_nopassword: [] # list of users granted to escalate to sudo without password
_sshd_access_limited: {} # dictionary of users and groups to manage during task 5.3.20
```


Dependencies
------------

NA

Example Playbook
----------------

```yaml
- hosts: all
  gather_facts: false
  become: true
  roles:
    - ansible-cis_rhel7-role

```

License
-------

BSD

Author Information
------------------

BBVA Infrastructure Enterprise Security - Security Architecture  
2020  
