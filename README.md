## Overview

The plugins for managing passwords for posts on Wordpress are either too expensive or slowing down the system. This Python script provides a straightforward way to manage password protection for posts on a WordPress site. It offers functionalities to both check the current passwords of protected posts and update the password for posts using a specific old password. 

## Features

- **Check Post Passwords**: View a list of all currently password-protected posts along with their IDs, titles, and passwords.
- **Update Post Passwords**: Update the password for all posts currently protected by a specific old password after checking them through last feature.

## Requirements

- Python 3
- `mysql-connector-python`

You can install the required Python package using the following command:

```
pip install mysql-connector-python
```

## Usage

### Setup

Before using the script, ensure your local WordPress database is accessible and that you have the necessary credentials.

### Commands

- **To check the current post passwords**:

  ```
  python WP-PostPassManager.py <dbuser> <dbpass> --host <dbhost> --database <dbname> --check
  ```

  Replace `<dbuser>` and `<dbpass>` with your database username and password respectively.

  Enter host for `<dbhost>` (e.g. "127.0.0.1"), and the name of database for `<dbname>` (e.g. "mydb").

- **To update a password**:

  ```
  python WP-PostPassManager.py <dbuser> <dbpass> --host <dbhost> --database <dbname> --update <oldpassword> <newpassword>
  ```

  This command will replace `oldpassword` with `newpassword` for all posts currently using `oldpassword`, which we can check it out with last command.

## Configuration

If the WordPress database is hosted at `127.0.0.1` (localhost) and using a fixed database name. Simply modify the script directly with related variables and delete corresponding `argparse` vectors.
