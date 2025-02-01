def paginate(data, page_num, per_page):
    start = (page_num - 1) * per_page
    end = start + per_page
    return data[start:end]