

def get_db_search_or_empty(db, query_vector, k, alternative=[]):
    """get search results in db or alternative string.
    """
    try:
        results = db.search(query_vector, k)
    except IndexError:
        results = alternative
    return results
