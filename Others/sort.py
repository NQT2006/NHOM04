
def LimitSort(docs: list, limit: int, di: int, key = None):
    if (not limit) or len(docs) <= limit <= 30:
        docs.sort(key = key, reverse = di < 0)
        return docs
    elif key:
        test = (lambda a, b: a < b) if di < 0 else (lambda a, b: a > b) 
        ordered = docs[:limit]
        for doc in docs[limit:]:
            for i in range(limit):
                if test(key(ordered[i]), key(doc)):
                    ordered[i] = doc
                    break
        ordered.sort(key = key, reverse = di < 0)
        return ordered


