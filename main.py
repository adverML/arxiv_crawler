"
author: Peter Lorenz
"
import logging
import arxiv # https://awesomeopensource.com/project/lukasschwab/arxiv.py?...
import pdb

# arxiv.Search(
#   query: str = "",
#   id_list: List[str] = [],
#   max_results: float = float('inf'),
#   sort_by: SortCriterion = SortCriterion.Relevanvce,
#   sort_order: SortOrder = SortOrder.Descending
# )



logging.basicConfig(level=logging.INFO)

search = arxiv.Search(
    query = "adversarial",
    max_results = float('inf'),
    sort_by = arxiv.SortCriterion.LastUpdatedDate
)

wanted_result = []

for result in search.results():

    set_wanted_cats = set(['cs.CV', 'cs.CR', 'cs.LG', 'cs.AI']) # https://arxiv.org/category_taxonomy
    intersect = set(result.categories).intersection(set_wanted_cats)
    
    if len(intersect) > 0:
        nr_papers = len(wanted_result)  

        if nr_papers > 10:
            break

        wanted_result.append(result)
        #pdb.set_trace()
        print(nr_papers , result.updated.year, result.updated.month, result.title )
    

        #result.download_pdf(dirpath="./pdfs")
