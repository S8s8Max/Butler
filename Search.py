import arxiv
from googletrans import Translator


# Query = "cat:stat.ML+AND+cat:q-fin.EC"
# https://arxiv.org/help/api/user-manual#subject_classifications
def SearchArxiv(search_words: list) -> str:
    text = ""
    for i in search_words:
        text += f"{i} "
    # Japanese to English
    translator = Translator()
    trans_en = translator.translate(text)
    trans_text = trans_en.__dict__()["text"]
    # set the query.
    Query = f"ti:{trans_text}"

    # search in arxiv.
    search = arxiv.Search(
        query=Query,
        max_results=2,
    )

    data = f"Search Query : {Query}\n\n"

    for i, result in enumerate(search.get()):
        title = result.title
        url = result.pdf_url
        summary = result.summary
        pub_date = result.published

        message = f"""
            No.{i+1}\n
            TITLE : '{title}',\n
            DATE : {pub_date}\n
            SUMMARY : {summary}\n
            URL : [ {url} ]\n\n"""

        data += message

    return data

