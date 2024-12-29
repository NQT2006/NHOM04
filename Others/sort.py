
def LimitSort(docs: list, limit: int, desc: bool, key = None):
    if (not limit) or len(docs) <= limit <= 30:
        docs.sort(key = key, reverse = desc)
        return docs
    elif key:
        test = (lambda a, b: a < b) if desc else (lambda a, b: a > b) 
        ordered = docs[:limit]
        for doc in docs[limit:]:
            for i in range(limit):
                if test(key(ordered[i]), key(doc)):
                    ordered[i] = doc
                    break
        ordered.sort(key = key, reverse = desc)
        return ordered

