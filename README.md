<div align="center">

![project logo](https://user-images.githubusercontent.com/76540311/225113830-89be0dce-3996-44e6-aa24-207a8086db95.png)


# ComputeGPT Evaluation



</div>

ComputeGPT is a <b>computational chat model</b> that provides real-time accurate answers to numerical problems. The chat model is able to answer SAT questions, GRE questions, all kinds of math and science questions, and homework problems with high accuracy.

Find the original ComputeGPT repository at https://github.com/urbaninfolab/ComputeGPT and ComputeGPT at https://computegpt.org.

## Evaluation

This repository provides an evaluation and comparison of ComputeGPT on numerical problems against GPT-4 with Internet (Bing AI), GPT-3.5 (ChatGPT), GPT-3 (Davinci-003), and Wolfram Alpha Natural Language.

<div align="center">

| Model           | ComputeGPT | Wolfram Alpha | Davinci-003 | ChatGPT | GPT-4  |
|-----------------|------------|---------------|-------------|---------|--------|
| Overall Accuracy (%)     | **98%**    | 56%          | 28%        | 48%     | 64%    |
| Word Problems (%)  | **95%**    | 15%          | 35%        | 50%     | 65%    |
| Straightforward (%) | **100%**   | 83.3%        | 23.3%      | 46.6%   | 63.3%  |

</div>

Overall, ComputeGPT demonstrates state-of-the-art performance on numerical problems when compared against other models, on both straightforward problems
and word problems that require more reasoning. See below for examples of each.
  
## Example Questions

(Straightforward) Example Question: **What is the derivative of 200x?** (Correct: 200)

| ComputeGPT | Wolfram Alpha | Davinci-003 | ChatGPT | GPT-4     |
|------------|---------------|-------------|---------|-----------|
| 200        | 200           | 200         | 200     | 200       |


(Straightforward) Example Question: **What is the integral of 200x from 0 to 5?** (Correct: 2500)

| ComputeGPT | Wolfram Alpha | Davinci-003 | ChatGPT | GPT-4     |
|------------|---------------|-------------|---------|-----------|
| 2500       | 2500          | 5000        | 5000    | 5000      |

(Straightforward) LaTeX Example Question: **∫₋₂₀⁵₀ 2x10²¹x³ + 200x² dx** (Correct: 9135000000000000000026600000/3)

| ComputeGPT       | Wolfram Alpha | Davinci-003         | ChatGPT          | GPT-4             |
|------------------|---------------|---------------------|------------------|-------------------|
| 9135000000000000000026600000/3 | 26600000/3     | 50,000,000,000,000,000,000 | 1.83333 x 10²⁴ | 1.66666666666667E+24 |

We show that ComputeGPT is efficient at LaTeX parsing, as well as the parsing of large integers, which other models fail to do.

(Word Problem) Example Question: **Kevin's age is 5 times the age of his son, plus twenty. His son is 10. How old is Kevin?** (Correct: 70)

| ComputeGPT | Wolfram Alpha | Davinci-003 | ChatGPT | GPT-4 |
|------------|---------------|-------------|---------|-------|
| 70         | NULL          | 50          | 50      | 70    |

(Word Problem) Example Question: **A new technique, called 'jamulti' is invented by multiplying a number by five and then adding 2 and dividing by 3. What's the jamulti of 7?** (Correct: 12.33333)

| ComputeGPT | Wolfram Alpha | Davinci-003 | ChatGPT | GPT-4    |
|------------|---------------|-------------|---------|----------|
| 12.33333   | NULL          | 5           | 5       | 12       |

(Word Problem) Example Question: **An alien needs $50 USD to buy a spaceship. He needs to convert from ASD, which is worth $1.352 USD. How much ASD does he need?** (Correct: 36.9822485)

| ComputeGPT  | Wolfram Alpha | Davinci-003 | ChatGPT | GPT-4  |
|-------------|---------------|-------------|---------|--------|
| 36.9822485  | 1.352         | 36.68       | 67.6    | 37.01  |

We show that GPT-4 is capable of hallucinating 'close' answers, which becomes even worse as numbers get larger, and the absolute error increases.

(Word Problem) Trick Example Question: **An ant travels at 3 m/s on a rubber band. The rubber band is stretched at 2 m/s. How fast is the ant moving relative to the ground?** (Correct: 1)

| ComputeGPT | Wolfram Alpha | Davinci-003 | ChatGPT | GPT-4 |
|------------|---------------|-------------|---------|-------|
| NULL       | 3             | 5           | 5       | 1     |

We showcase an example of a loss for ComputeGPT, where it fails to see past the trick question's simplicity in a subtraction of 3 - 2 = 1.

(Word Problem) Example Question: **Given the matrix [[1, 2, 9, 3, 3], [9, 0, 1, 2, 4], [0, 0, 0, 3, 9], [1, 1, 1, 1, 1], [3, 4484, 456, 9, 6]], what is the determinant multiplied by 5 and then divided by twenty-three?** (Correct: -285832.173913042)

| ComputeGPT        | Wolfram Alpha | Davinci-003 | ChatGPT | GPT-4         |
|-------------------|---------------|-------------|---------|--------------|
| -285832.173913042 | -1314828      | 24          | -9915   | -30247.652    |

We showcase an example of a clear win for ComputeGPT, where it excels in understanding and performing a complex computation on the user's machine.


# Getting Started with ComputeGPT

Just head over to https://computegpt.org and use the model to your desire! There are no limits on its use.

Feel free to come back here and report any issues or leave any feedback to help improve the model.

![image](https://user-images.githubusercontent.com/76540311/225113515-4f6791f5-093e-48d8-be0a-504695fc977e.png)






