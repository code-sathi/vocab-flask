def get_top_n_from_list(list, n=3):
    newList = sorted(list, key=lambda syn: syn[1].min_depth())
    if len(newList) == 0:
        return None
    topNList = [syn[0] for syn in list[:3]]
    return topNList


def remove_duplicate_from_list(mList, word):
    newList = list(filter(lambda syn: syn[0] != word, mList))
    return newList
