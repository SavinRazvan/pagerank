import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a set of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probability_distribution = {}
    page_links = list(corpus[page])
    pages = list(corpus.keys())

    # Initialize probabilities for all pages to 0
    for i in corpus:
        probability_distribution[i] = 0

    if page_links:
        # Assign probability to pages linked from the current page
        for link in page_links:
            probability_distribution[link] = damping_factor * (1 / len(page_links))

        # Assign probability to all pages in the corpus
        for page in pages:
            probability_distribution[page] += (1 - damping_factor) * (1 / len(pages))
    else:
        # If the page has no outgoing links, assign equal probability to all pages
        for page in pages:
            probability_distribution[page] = 1 / len(pages)

    return probability_distribution

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to the transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    original_pages = list(corpus.keys())
    samples_pages = {}
    random_sample_page = random.choice(original_pages)

    # Initialize sample pages with probability 0
    for page in original_pages:
        samples_pages[page] = 0

    # Select the first random sample page and assign it a probability of 1/n
    samples_pages[random_sample_page] = 1 / n

    # Calculate the probability distribution for the current page
    prob_dist_current_page = transition_model(corpus, random_sample_page, damping_factor)

    # Generate the remaining n-1 samples
    for i in range(1, n):
        # Select a new sample page based on the probability distribution
        new_sample = random.choices(
            list(prob_dist_current_page.keys()),
            list(prob_dist_current_page.values()),
            k=1
        )[0]

        # Update the probability of the new sample page
        samples_pages[new_sample] += 1 / n

        # Update the probability distribution for the current page based on the new sample
        prob_dist_current_page = transition_model(corpus, new_sample, damping_factor)

    return samples_pages

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N = len(corpus)
    old_values = {}
    new_value = {}
    convergence_threshold = 0.001

    # Initialize the PageRank values with an equal probability of 1/N for each page
    for page in corpus:
        old_values[page] = 1 / N

    # Iteratively update PageRank values until convergence
    while True:
        for page in corpus:
            page_rank = 0
            for link in corpus:
                # Check if the current page is linked to by other pages
                if page in corpus[link]:
                    page_rank += old_values[link] / len(corpus[link])
                # If the current page has no links, interpret it as having one link for every other page
                if len(corpus[link]) == 0:
                    page_rank += old_values[link] / len(corpus)

            # Update the PageRank value for the current page using the damping factor
            page_rank *= damping_factor
            page_rank += (1 - damping_factor) / N

            # Update the new PageRank value
            new_value[page] = page_rank

        # Calculate the maximum change (difference) in PageRank values
        difference = max([abs(new_value[val] - old_values[val]) for val in old_values])

        # Check for convergence by comparing the maximum change with the convergence threshold 
        if difference < ((1 / SAMPLES) * convergence_threshold):
            break
        else:
            old_values = new_value.copy()

    return old_values

if __name__ == "__main__":
    main()



# Usage example:

# (base) razvansavin@AEGIS:~/ProiecteVechi/CS50AI/pagerank$ python pagerank.py corpus0
# PageRank Results from Sampling (n = 10000)
#   1.html: 0.2208
#   2.html: 0.4293
#   3.html: 0.2216
#   4.html: 0.1283
# PageRank Results from Iteration
#   1.html: 0.2199
#   2.html: 0.4292
#   3.html: 0.2199
#   4.html: 0.1310
