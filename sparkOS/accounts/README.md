# SparkOS accounts

Local account records are stored in /var/lib/sparkos/accounts.json with salted PBKDF2-HMAC-SHA256 password hashes.

The graphical login manager creates a user session only after authentication. Guest Mode is a restricted session and cannot access other users' private data.

The prototype's blank-password idea is represented only as an explicit guest-like account; it must never bypass another user's password.
