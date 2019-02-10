user-homedir
=========

Create a user on the system complete with a nice set of bash dotfiles

Requirements
------------

None

Role Variables
--------------

```yaml
# Should we create the user account?  Defaults to true
create_account: true

# Setup basic user information
user:
  # Account name
  name: tryme
  # Encrypted account password
  password: '*'
  # Account default group
  group: tryme
  # account email, will be used in setting up .gitconfig
  email: tryme@example.com
  # account full name, will be used in setting up .gitconfig and GECOS field
  fullname: Your Name
  # the github account name to use (inside .gitconfig)
  gituser: tryme
  # Add the user to the system groups, so they can sudo and other system tasks
  systemgroups: true
  # only set this if you want a specific UID, defaults to adduser mechanism
  # uid:
  # Add user to the list of extra_groups.
  extra_groups: []

# name of location based bashrc file to source (home/work/cloud/etc)
location_bashrc: home

# Name of molecule image to use in molecule function so we can easily run
# molecule from the docker container without having a long complicated command
# line.
molecule_image: retr0h/molecule:latest
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - role: phreddrick.user-homedir
      create_account: true
      user:
        name: auser
        password: '$6$ie8socMmqj.VBolt$qAA6k.M5a4S.ngB47RzcrOLuJ/bT2R.pwK6zVsXS33lQ0/m5rQXyoVXfdwzysxJrRYJeNkKOvZcbWD0ROM0.31'
        group: staff
        email: auser@example.com
        fullname: "Ima User"
        gituser: imauser
        systemgroups: true
      location_bashrc: work
```

License
-------

BSD

Author Information
------------------

[Steven Jorgensen](mailto: phreddrick@gmail.com).
