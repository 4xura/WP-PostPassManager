# pip install mysql-connector-python
import argparse
import mysql.connector

def connect_database(username, password, host, database):
    """Connect to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print(f"[+] Successfully connected to database.")
        return connection
    except mysql.connector.Error as err:
        print(f"[!] Database connection Error: {err}")
        exit(1)

def check_post_passwords(connection):
    """Retrieve and print current post passwords."""
    query = """
    SELECT ID, post_title, post_password FROM wp_posts
    WHERE post_password <> ''
    ORDER BY post_date DESC;
    """
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Title: {row[1]}, Password: {row[2]}")
    cursor.close()

def replace_post_password(connection, old_password, new_password):
    """Update posts with a specific old password to a new password."""
    query = """
    UPDATE wp_posts
    SET post_password = %s
    WHERE post_password = %s;
    """
    cursor = connection.cursor()
    cursor.execute(query, (new_password, old_password))
    connection.commit()
    print(f"[*] Replacing old password {old_password}...")
    print(f"[!] Update successfully for {cursor.rowcount} posts.")
    print(f"[!] New password for the posts is {new_password}")
    cursor.close()

def update_password_by_title(connection, title, new_password):
    """Update the password of a post specified by its title."""
    query = """
    UPDATE wp_posts
    SET post_password = %s
    WHERE post_title = %s;
    """
    cursor = connection.cursor()
    cursor.execute(query, (new_password, title))
    connection.commit()
    print(f"[!] Password updated for post titled '{title}' as {new_password}.")
    cursor.close()

def main():
    parser = argparse.ArgumentParser(description="Manage WordPress post passwords.")
    parser.add_argument("username", help="Database username")
    parser.add_argument("password", help="Database password")
    parser.add_argument("--host", default="localhost", help="Database host")
    parser.add_argument("--database", default="wordpress", help="Database name")
    parser.add_argument("--check", action="store_true", help="Check current post passwords")
    parser.add_argument("--replace", nargs=2, metavar=("OLD_PASSWORD", "NEW_PASSWORD"), help="Replace a specific old password to a new password")
    parser.add_argument("--update", nargs=2, metavar=("POST_TITLE", "NEW_PASSWORD"), help="Update the password for a post by title")

    args = parser.parse_args()

    # Connect to the database
    connection = connect_database(args.username, args.password, args.host, args.database)

    if args.check:
        check_post_passwords(connection)

    if args.replace:
        replace_post_password(connection, args.replace[0], args.replace[1])

    if args.update:
        update_password_by_title(connection, args.update[0], args.update[1])

    connection.close()

if __name__ == "__main__":
    main()
