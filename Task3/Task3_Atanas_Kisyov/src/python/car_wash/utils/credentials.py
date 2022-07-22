def read_user_credentials(file_path: str) -> list:
    """
    Read the user credentials that are stored in the given file path and return a list with tuples 
    Example: [(user1, password1), (user2, password2), ...]
    """

    result = []

    with open(file_path, 'r') as file:
        current_user = file.readline()
        while current_user:
            hostname, user, password, database_name = current_user.split(',')
            result.append((hostname, user, password, database_name))
            current_user = file.readline()

    return result
