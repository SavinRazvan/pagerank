# PageRank Project

This project implements the PageRank algorithm to rank web pages by importance using two approaches: a sampling method with the Markov Chain random surfer model and an iterative method with a recursive mathematical expression.

## Key Features

- **Transition Model**: Computes the probability distribution for the next page a random surfer visits.
- **Sampling PageRank**: Estimates PageRank by simulating random surfer behavior.
- **Iterative PageRank**: Calculates PageRank values through repeated application of the PageRank formula until convergence.

## Introduction

The PageRank algorithm revolutionized how search engines rank web pages by assigning a numerical weight to each page based on its link structure. This weight represents the importance of a page within the context of the entire web. The primary objective of this project is to implement and understand the iterative and sampling processes of the PageRank algorithm, providing insights into how search engines prioritize content.

## Project Goals

1. **Understand the Transition Model**: Learn how to compute the probability distribution for the next page a random surfer might visit, forming the basis of the PageRank algorithm.
2. **Implement Sampling PageRank**: Develop a method to estimate PageRank by simulating the random surfer's behavior over a large number of iterations.
3. **Implement Iterative PageRank**: Create an iterative process to calculate PageRank values through repeated application of the PageRank formula until convergence.
4. **Analyze Convergence**: Observe how PageRank values stabilize over iterations and understand the factors affecting convergence speed.
5. **Visualize Results**: Provide visual representations of the PageRank values and their convergence to facilitate a deeper understanding of the algorithm's behavior.

## Conclusion

The PageRank Project provides a comprehensive exploration of one of the fundamental algorithms that underpin modern search engines. By implementing both sampling and iterative approaches, this project highlights the versatility and robustness of the PageRank algorithm in determining the relative importance of web pages.

For more details and a visual representation of how the algorithm works, refer to the [CS50 AI course project on PageRank](https://cs50.harvard.edu/ai/2024/projects/2/pagerank/). Additionally, you can watch this [YouTube video](https://www.youtube.com/watch?v=JGQe4kiPnrU) (starting at minute 12:50) for an animation demonstrating the iterative process of the PageRank algorithm.