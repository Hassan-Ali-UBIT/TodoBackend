from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name="TODO_Todos"):
    client = get_client()
    index = client.init_index(index_name)
    return index
    
def perform_search(query, **kwargs):

    index = get_index()

    tags = ""
    params = {}

    print(query)

    if "tags" in kwargs:
        print(kwargs)
        tags = kwargs.pop("tags") or []

        if len(tags) != 0:
            params['tagFilters'] = tags

        index_filters = [f"{k}:{v}" for k,v in kwargs.items()]
        print(index_filters)

        if len(index_filters) != 0:
            params['facetFilters'] = index_filters

        result = index.search(query, params)
        return result